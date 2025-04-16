import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from met_brewer import met_brew

from math_helper import * 
from file_handler import *
from plot_manager import *


def main():

    # Color palatte provided be MetBrewer
    colors = met_brew(name="Archambault")

    # Asks for input on which file needs to be analyzed
    file_path = input("Enter the file name: ")

    # Get the time array as well as positions for hands/head
    time , mouse = read_csv_file(file_path, 2, mode="pc")

    ds_time, ds_mouse = downsample_data(time, mouse)

    # Get the magnitude of velocity
    mouse_mag = calculate_magnitude(ds_mouse)

    # Calculate the acceleration
    mouse_accel = calculate_derivative(ds_mouse, ds_time)

    # Calculate the jerk
    mouse_jerk = calculate_derivative(mouse_accel, ds_time[:-1])

    # Calculate the magnitude of the jerk 
    mouse_jerk_mag = calculate_magnitude(mouse_jerk)
    
    # Plot the magnitude over time
    plot_magnitude(ds_time, mouse_mag, labels="Mouse Magnitude", colors=colors, ylim=(0, 80))

    # Calculate the average mouse magnitude
    mouse_mag_avg = np.mean(mouse_mag)
    mouse_jerk_mag_avg = np.mean(mouse_jerk_mag)

    capture_data = input("Do you need to save data? y/N ")
    if(capture_data == "y"):
        experiment_row = int(input("Enter the experiment number to save data: "))
        file_path = input("Enter the output file name: ")
        write_csv_file(mouse_mag_avg, mouse_jerk_mag_avg, file_path=file_path, experiment_row=experiment_row)
    elif(capture_data == "N" or capture_data == "n"):
        exit()
    else:
        print("Error: Input not recognized...exiting program")
        exit()

if __name__ == "__main__":
    main()