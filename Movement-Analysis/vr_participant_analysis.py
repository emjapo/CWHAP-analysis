from file_handler import *
from math_helper import *
from plot_manager import *

from met_brewer import met_brew
import numpy as np

def main():

    # Input the colors you want for the graph through MetBrewer library
    colors = met_brew(name="Archambault")

    # Asks for input on which file needs to be analyzed
    file_path = input("Enter the input file name: ")

    # Get the time array as well as positions for hands/head
    time, hand_l, hand_r, head = read_csv_file(file_path, 3, 4, 5, mode="vr")

    # Downsample the time and data to one entry per second
    ds_time, ds_hand_l, ds_hand_r, ds_head = downsample_data(time, hand_l, hand_r, head, target_rate=1.0)

    # Calculate the velocity of each each body part
    hand_l_vel = calculate_derivative(ds_hand_l, ds_time)
    hand_r_vel = calculate_derivative(ds_hand_r, ds_time)
    head_vel = calculate_derivative(ds_head, ds_time)

    # Calculate the magnitudes of each body
    hand_l_mag = calculate_magnitude(hand_l_vel)
    hand_r_mag = calculate_magnitude(hand_r_vel)
    head_mag = calculate_magnitude(head_vel)

    # Calculate the average magnitudes of each body part
    hand_l_mag_avg = np.mean(hand_l_mag)
    hand_r_mag_avg = np.mean(hand_r_mag)
    head_mag_avg = np.mean(head_mag)

    # Plot the three dimensional graph of positional data
    plot_position(hand_l, hand_r, head, colors)

    # Plot the magnitude over time
    labels = ["Left Hand Magnitude", "Right Hand Magnitude", "Head Magnitude"]
    plot_magnitude(ds_time, hand_l_mag, hand_r_mag, head_mag, labels=labels, colors=colors, ylim=(0, 1.5))

    # Calculate the acceleration
    hand_l_accel = calculate_derivative(hand_l_vel, ds_time[:-1])
    hand_r_accel = calculate_derivative(hand_r_vel, ds_time[:-1])
    head_accel = calculate_derivative(head_vel, ds_time[:-1])

    # Calculate the jerk
    hand_l_jerk = calculate_derivative(hand_l_accel, ds_time[:-2])
    hand_r_jerk = calculate_derivative(hand_r_accel, ds_time[:-2])
    head_jerk = calculate_derivative(head_accel, ds_time[:-2])

    # Calculate the average jerk magnitude
    hand_l_jerk_mag_avg = np.mean(calculate_magnitude(hand_l_jerk))
    hand_r_jerk_mag_avg = np.mean(calculate_magnitude(hand_r_jerk))
    head_jerk_mag_avg = np.mean(calculate_magnitude(head_jerk))

    capture_data = input("Do you need to save data? y/N ")
    if(capture_data == "y"):
        experiment_row = int(input("Enter the experiment number to save data: "))
        file_path = input("Enter the output file name: ")
        write_csv_file(hand_l_mag_avg, hand_r_mag_avg, head_mag_avg, hand_l_jerk_mag_avg, hand_r_jerk_mag_avg, head_jerk_mag_avg, file_path=file_path, experiment_row=experiment_row)
    elif(capture_data == "N" or capture_data == "n"):
        exit()
    else:
        print("Error: Input not recognized...exiting program")
        exit()

if __name__ == "__main__":
    main()