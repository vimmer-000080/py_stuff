from vpython import *
import numpy as np

# VPython scene setup
scene1 = canvas(title="Original Function", width=500, height=300, background=color.white)
scene2 = canvas(title="Fourier Terms", width=500, height=300, background=color.white)
scene3 = canvas(title="Reconstructed Function", width=500, height=300, background=color.white)

# Define the time variable and step size
t_values = np.linspace(-np.pi, np.pi, 200)  # Time steps
dt = t_values[1] - t_values[0]

# Original square wave function
def square_wave(t):
    return np.sign(np.sin(t))

# Fourier series approximation for square wave
def fourier_series_square_wave(t, n_terms):
    approx = np.zeros_like(t)
    for n in range(1, n_terms + 1, 2):  # Only odd harmonics
        approx += (4 / (np.pi * n)) * np.sin(n * t)
    return approx

# Create spheres in VPython to represent the points of each function
def plot_function(canvas, t_values, y_values, color=color.red):
    points = []
    for t, y in zip(t_values, y_values):
        point = sphere(pos=vector(t, y, 0), radius=0.03, color=color)
        points.append(point)
    return points

# Update points with new y-values
def update_points(points, y_values):
    for point, y in zip(points, y_values):
        point.pos.y = y

# Main loop to update the Fourier series approximation
n_terms = 1
original_wave = square_wave(t_values)
fourier_approx = fourier_series_square_wave(t_values, n_terms)
reconstructed_wave = np.zeros_like(t_values)

# Plot the original function
original_points = plot_function(scene1, t_values, original_wave, color=color.red)

# Plot the Fourier term (initially the first term)
fourier_points = plot_function(scene2, t_values, fourier_approx, color=color.blue)

# Plot the reconstructed wave (initially the first Fourier term)
reconstructed_points = plot_function(scene3, t_values, fourier_approx, color=color.green)

# Update loop to add more Fourier terms progressively
while True:
    rate(1)  # Slow down the loop

    # Add more terms to the Fourier series (odd harmonics only)
    n_terms += 2
    new_fourier_term = (4 / (np.pi * n_terms)) * np.sin(n_terms * t_values)

    # Update the Fourier term points in scene2
    update_points(fourier_points, new_fourier_term)

    # Update the reconstructed wave by adding the new Fourier term
    reconstructed_wave += new_fourier_term
    update_points(reconstructed_points, reconstructed_wave)

    # Stop after 15 terms
    if n_terms > 15:
        break

