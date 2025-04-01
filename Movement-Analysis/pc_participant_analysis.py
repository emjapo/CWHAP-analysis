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
            experiment_limit = np.where(time <= 600.0)[0]
            time = time[experiment_limit]

            # Initialize the positional array
            position_arrays = []

            for column_index in column_indices:
                # Initialize coordinate lists
                x_coords = []
                y_coords = []

                for i in experiment_limit:

                    row = rows[i]
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
        exit()
    except Exception as e:
        print(f"An error occured: {e}")
        exit()



def calculate_magnitude(velocity):
    # Calculate the magnitude
    magnitude = np.sqrt(np.sum(velocity**2, axis=0))
    return magnitude

def plot_magnitude(time, mouse):

    # Format for Axes (10 minute experiment)
    time /= 60.0
    
    # Creates the 2D plot
    fix, ax = plt.subplots()

    plt.plot(time, mouse, color='black')
    ax.set_title("Mouse Magnitude")
    ax.set_xlabel("Time Elapsed (m)")
    ax.set_ylabel("Magnitude (N)")

    plt.show()

def write_csv_file(file_path, experiment_row, mouse_avg):
    try:

        # Read the CSV file from path
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        if 1 <= experiment_row < len(rows):
            rows[experiment_row][4] = f"{mouse_avg:.6f}"
        else:
            print("Invalid Experiment Row")
            return
        
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    
    # Exception catch statements
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit()
    except Exception as e:
        print(f"An error occured: {e}")
        exit()


def main():

    # Asks for input on which file needs to be analyzed
    file_path = input("Enter the file name: ")

    # Get the time array as well as positions for hands/head
    time , mouse = read_csv_file(file_path, 2)

    # Get the magnitudes
    mouse_mag = calculate_magnitude(mouse)

    # Plot the magnitude over time
    plot_magnitude(time, mouse_mag)

    # Calculate the average mouse magnitude
    mouse_mag_avg = np.mean(mouse_mag)

    experiment_row = int(input("Enter the experiment number to save data: "))
    file_path = input("Enter the output file name: ")
    write_csv_file(file_path, experiment_row, mouse_mag_avg)
    
    

if __name__ == "__main__":
    main()