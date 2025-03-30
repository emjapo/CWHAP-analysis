import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def read_csv_file(file_path, *column_indices):
    try:
        with open(file_path, 'r') as file:
            
            # Create an object for the csv file
            csv_reader = csv.reader(file)
            
            # Skip the string header file
            next(csv_reader)

            # Read all the data
            rows = list(csv_reader)

            # Create the time array
            time = np.array([float(row[1]) for row in rows])

            # Initialize the positional array
            position_arrays = []

            for column_index in column_indices:
                # Initialize coordinate lists
                x_coords = []
                y_coords = []

                for row in rows:
                    # Assign the string value and convert to floating point
                    value = row[column_index]
                    coords = value.strip("() ").split(";")
                    coords = [float(x.strip()) for x in coords]

                    # Append with appropriate coordinate system
                    x_coords.append(coords[0])
                    y_coords.append(coords[1])

                # Append to the overall array
                position_arrays.append(np.array([x_coords, y_coords]))

        # Returns arrays of shape (length_of_rows) and (3, length_of_rows)
        return time, *position_arrays
    
    # Exception catch statements
    except FileNotFoundError:
        print(f"Error: The file '{file_path} was not found.")
        return None, *[None] * len(column_indices)
    except Exception as e:
        print(f"An error occured: {e}")
        return None, *[None] * len(column_indices)



def calculate_magnitude(velocity):
    # Calculate the magnitude
    magnitude = np.sqrt(np.sum(velocity**2, axis=0))
    return magnitude

def plot_magnitude(time, mouse):

    # Creates the 2D plot
    plt.plot(time, mouse)
    plt.show()


def main():

    # Asks for input on which file needs to be analyzed
    file_path = input("Enter the file name: ")

    # Get the time array as well as positions for hands/head
    time , mouse = read_csv_file(file_path, 2)

    # Get the magnitudes
    mouse_mag = calculate_magnitude(mouse)

    # Plot the magnitude over time
    plot_magnitude(time, mouse_mag)

    # Print the average for the magnitude
    print(f"Average Mouse Magnitude: {np.mean(mouse_mag)}" )
    

if __name__ == "__main__":
    main()