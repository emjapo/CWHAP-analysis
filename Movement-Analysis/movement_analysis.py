import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def read_csv_file(file_path, column_index):
    try:
        with open(file_path, 'r') as file:
            
            # Create an object for the csv file
            csv_reader = csv.reader(file)
            
            # Skip the string header file
            next(csv_reader)

            # Create the coordinate arrays
            x, y, z = [], [], []

            # Sample every 10th datapoint
            for i, row in enumerate(csv_reader):
                #if i % 30 == 0:

                    # Reformat the data
                    value = row[column_index]
                    coords = value.strip("() ").split(";")
                    coords = [float(x.strip()) for x in coords]

                    # Append the new coordinate
                    x.append(coords[0])
                    y.append(coords[2])
                    z.append(-coords[1])

    except FileNotFoundError:
        print(f"Error: The file '{file_path} was not found.")
    except Exception as e:
        print(f"An error occured: {e}")
    
    return x, y, z

# Asks for input on which file needs to be analyzed
file_path = input("Enter the file name: ")

# Captures the data for each hand and the head
x1, y1, z1 = read_csv_file(file_path, 3)
x2, y2, z2 = read_csv_file(file_path, 4)
x3, y3, z3 = read_csv_file(file_path, 5)

# Creates the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set custom axis limits
ax.set_xlim([min(x1)-1, max(x1)+1])
ax.set_ylim([min(x1)-1, max(y1)+1]) 
ax.set_zlim([0, max(z3)+1]) 


ax.plot(x1, y1, z1, c='r', label='Left Hand', linewidth=.1)
ax.plot(x2, y2, z2, c='g', label='Right Hand', linewidth=.1)
ax.plot(x3, y3, z3, c='b', label='Head', linewidth=.1)

# Set appropriate axis labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Z-axis')
ax.set_zlabel('Y-axis')

plt.show()