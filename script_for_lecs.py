import subprocess
from bs4 import BeautifulSoup

# URL of the page to crawl
url = "https://www.iitg.ac.in/physics/fac/padmakumarp/Courses/"

# Use curl to get the page content
result = subprocess.run(['curl', '-s', url], stdout=subprocess.PIPE)
page_content = result.stdout

# Parse the page content
soup = BeautifulSoup(page_content, "html.parser")

# Find all links on the page
links = soup.find_all("a")

# Print all found links for debugging
print("All found links:")
for link in links:
    print(link.get("href"))

# Filter links that look like course directories
course_links = []
for link in links:
    href = link.get("href")
    if href and href.endswith('/'):
        course_links.append(href)

# Print the list of courses
print("\nFiltered course links:")
for course in course_links:
    print(course)

