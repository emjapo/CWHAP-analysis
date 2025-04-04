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
                z_coords = []

                for i in experiment_limit:

                    row = rows[i]
                    # Assign the string value and convert to floating point
                    value = row[column_index]
                    coords = value.strip("() ").split(";")
                    coords = [float(x.strip()) for x in coords]

                    # Append with appropriate coordinate system
                    x_coords.append(coords[0])
                    y_coords.append(coords[2])
                    z_coords.append(-coords[1])

                # Append to the overall array
                position_arrays.append(np.array([x_coords, y_coords, z_coords]))

        # Returns arrays of shape (length_of_rows) and (3, length_of_rows)
        return time, *position_arrays
    
    # Exception catch statements
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit()
    except Exception as e:
        print(f"An error occured: {e}")
        exit()


def calculate_derivative(position, time):
    # Calculate the velocity through broadcasting
    velocity = np.diff(position, axis=1) / np.diff(time)[:, np.newaxis].T

    # Calculate the magnitude
    magnitude = np.sqrt(np.sum(velocity**2, axis=0))

    return velocity, magnitude

def plot_position(hand_l, hand_r, head):
    
    # Creates the 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Concatenate all the information to set the bounds
    all_x = np.concatenate([hand_l[0], hand_r[0], head[0]])
    all_y = np.concatenate([hand_l[1], hand_r[1], head[1]])
    all_z = np.concatenate([hand_l[2], hand_r[2], head[2]])

    # Set the axis limits for the graph
    ax.set_xlim([np.min(all_x) - 1, np.max(all_x) + 1])
    ax.set_ylim([np.min(all_y) - 1, np.max(all_y) + 1])
    ax.set_zlim([np.min(all_z) - 1, np.max(all_z) + 1])

    # Plot the data points
    ax.plot(hand_l[0], hand_l[1], hand_l[2], c='r', label='Left Hand', linewidth=.25)
    ax.plot(hand_r[0], hand_r[1], hand_r[2], c='g', label='Right Hand', linewidth=.25)
    ax.plot(head[0], head[1], head[2], c='b', label='Head', linewidth=.25)

    # # Set appropriate axis labels
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Z-axis')
    ax.set_zlabel('Y-axis')

    # Add the title to the plot
    ax.set_title('VR Player Positional Data')

    ax.legend(loc='upper left', bbox_to_anchor=(-0.35, 0.6))
    plt.show()

def plot_magnitude(time, hand_l_mag, hand_r_mag, head_mag):

    # Creates the 2D plot
    fig, axes = plt.subplots(3, 1, figsize=(8, 6))
    
    # Format for Axes (10 minute experiment)
    time /= 60.0

    axes[0].plot(time[:-1], hand_l_mag, color='red', label='Left Hand Magnitude')
    axes[0].set_title('Left Hand Magnitude')
    axes[0].set_xlabel('Time Elapsed (m)')
    axes[0].set_ylabel('Magnitude (N)')

    axes[1].plot(time[:-1], hand_r_mag, color='green', label='Right Hand Magnitude')
    axes[1].set_title('Right Hand Magnitude')
    axes[1].set_xlabel('Time Elapsed')
    axes[1].set_ylabel('Magnitude (N)')

    axes[2].plot(time[:-1], head_mag, color='blue', label='Head Magnitude')
    axes[2].set_title('Head Magnitude')
    axes[2].set_xlabel('Time Elapsed')
    axes[2].set_ylabel('Magnitude (N)')

    plt.tight_layout()
    plt.show()

def write_csv_file(file_path, experiment_row, left_avg, right_avg, head_avg):
    try:

        # Read the CSV file from path
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        if 1 <= experiment_row < len(rows):
            rows[experiment_row][1] = f"{left_avg:.6f}"
            rows[experiment_row][2] = f"{right_avg:.6f}"
            rows[experiment_row][3] = f"{head_avg:.6f}"
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
    file_path = input("Enter the input file name: ")

    # Get the time array as well as positions for hands/head
    time, hand_l, hand_r, head = read_csv_file(file_path, 3, 4, 5)

    # Calculate the velocity and magnitude of each body part
    hand_l_vel, hand_l_mag = calculate_derivative(hand_l, time)
    hand_r_vel, hand_r_mag = calculate_derivative(hand_r, time)
    head_vel, head_mag = calculate_derivative(head, time)

    # Calculate the average magnitudes of each body part
    hand_l_mag_avg = np.mean(hand_l_mag)
    hand_r_mag_avg = np.mean(hand_r_mag)
    head_mag_avg = np.mean(head_mag)

    # Plot the three dimensional graph of positional data
    plot_position(hand_l, hand_r, head)

    # Plot the magnitude over time
    plot_magnitude(time, hand_l_mag, hand_r_mag, head_mag)

    # Calculate the acceleration
    hand_l_accel, _ = calculate_derivative(hand_l_vel, time[:-1])

    # Calculate the jerk
    hand_l_jerk, _ = calculate_derivative(hand_l_accel, time[:-2])

    experiment_row = int(input("Enter the experiment number to save data: "))
    file_path = input("Enter the output file name: ")
    write_csv_file(file_path, experiment_row, hand_l_mag_avg, hand_r_mag_avg, head_mag_avg)
    

if __name__ == "__main__":
    main()