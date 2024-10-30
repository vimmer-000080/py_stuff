import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# URL of the website to scrape
start_url = "https://www.kicad.org/"  # Replace with the target website

# Directory to save downloaded PDFs
download_directory = "downloaded_pdfs"
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Set of visited URLs to avoid revisiting the same pages
visited_urls = set()

# Function to download PDFs
def download_pdf(pdf_url):
    response = requests.get(pdf_url)
    filename = pdf_url.split('/')[-1]
    file_path = os.path.join(download_directory, filename)

    with open(file_path, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded: {filename}")

# Function to recursively scrape website for PDFs
def scrape_and_download_pdfs(url):
    # If the URL has been visited, skip it
    if url in visited_urls:
        return

    # Add the URL to the set of visited URLs
    visited_urls.add(url)

    # Send a GET request to the website
    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException as e:
        print(f"Failed to retrieve {url}: {e}")
        return

    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve {url}. Status code: {response.status_code}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Define the case-insensitive regex pattern for matching PDF links
    pdf_pattern = re.compile(r'.*\.pdf', re.IGNORECASE)

    # List to store all found PDF links
    pdf_links = []

    # Check for <a> tags with href containing .pdf anywhere in the link
    for link in soup.find_all('a', href=True):
        href = link['href']
        if '.pdf' in href.lower():
            pdf_links.append(href)

    # Remove duplicates
    pdf_links = list(set(pdf_links))

    # Download PDFs that match the regex pattern
    for pdf_link in pdf_links:
        if pdf_pattern.search(pdf_link):
            # Make sure the link is absolute, not relative
            pdf_url = urljoin(url, pdf_link)
            download_pdf(pdf_url)

    # Recursively follow all internal links (on the same domain)
    for link in soup.find_all('a', href=True):
        href = link['href']
        full_url = urljoin(url, href)
        parsed_url = urlparse(full_url)

        # Ensure we only follow internal links (same domain)
        if parsed_url.netloc == urlparse(start_url).netloc:
            scrape_and_download_pdfs(full_url)

# Start the recursive scraping
scrape_and_download_pdfs(start_url)
