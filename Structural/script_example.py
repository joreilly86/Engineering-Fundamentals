import matplotlib.pyplot as plt

# Introduction 
"""
Exploring Newton's Second Law: F = m * a

We calculate force (F) as mass (m) in kilograms times acceleration (a) in meters per second squared. 
The result is in Newtons.
"""

# Define Variables & Function
m = 5  # mass in kilograms
a = 2  # acceleration in meters per second squared

def calculate_force(mass, acceleration):
    return mass * acceleration

# Calculate & Print
force = calculate_force(m, a)
print(f"The resulting force is: {force} Newtons")

# Visualization 1: Bar Chart
categories = ['Mass', 'Acceleration', 'Force']
values = [m, a, force]

plt.figure(figsize=(10, 6))
plt.bar(categories, values, color=['blue', 'orange', 'green'])
plt.title('Force Calculation')
plt.ylabel('Values')
plt.show()

# Visualization 2: Line Plot (Mass vs. Force)
a_values = [1, 2.5, 4, 5.5]
forces = [calculate_force(m, a_val) for a_val in a_values]

plt.figure(figsize=(10, 6))
plt.plot(a_values, forces, marker='o')
plt.title('Force vs. Acceleration')
plt.xlabel('Acceleration (m/s^2)')
plt.ylabel('Force (Newtons)')
plt.grid(True)
plt.show()
