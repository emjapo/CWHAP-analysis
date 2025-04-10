import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

from math_helper import * 
from file_handler import *

def plot_magnitude(time, mouse):

    # Format for Axes (10 minute experiment)
    time /= 60.0
    
    # Creates the 2D plot
    fix, ax = plt.subplots()

    plt.plot(time, mouse, color='purple')
    ax.set_title("Mouse Magnitude")
    ax.set_xlabel("Time Elapsed (m)")
    ax.set_ylabel("Magnitude (N)")

    plt.show()

def write_csv_file(file_path, experiment_row, mouse_avg, mouse_j_avg):
    try:

        # Read the CSV file from path
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        if 1 <= experiment_row < len(rows):
            rows[experiment_row][4] = f"{mouse_avg:.6f}"
            rows[experiment_row][8] = f"{mouse_j_avg:.6f}"
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
    time , mouse = read_csv_file(file_path, 2, mode="pc")

    ds_time, ds_mouse = downsample_data(time, mouse)

    # Get the magnitudes
    mouse_mag = calculate_magnitude(ds_mouse)

    mouse_accel, mouse_accel_mag = calculate_derivative(ds_mouse, ds_time)

    mouse_jerk, mouse_jerk_mag = calculate_derivative(mouse_accel, ds_time[:-1])

    mouse_jerk_mag = calculate_magnitude(mouse_jerk)
    
    # Plot the magnitude over time
    plot_magnitude(ds_time, mouse_mag)

    # Calculate the average mouse magnitude
    mouse_mag_avg = np.mean(mouse_mag)
    mouse_jerk_mag_avg = np.mean(mouse_jerk_mag)

    experiment_row = int(input("Enter the experiment number to save data: "))
    file_path = input("Enter the output file name: ")
    write_csv_file(file_path, experiment_row, mouse_mag_avg, mouse_jerk_mag_avg)
    
    

if __name__ == "__main__":
    main()