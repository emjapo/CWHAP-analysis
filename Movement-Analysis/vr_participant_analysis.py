from file_handler import *
from math_helper import *
from plot_manager import *

from met_brewer import met_brew
import numpy as np

def main():
    
    colors = met_brew(name="Archambault")

    # Asks for input on which file needs to be analyzed
    file_path = input("Enter the input file name: ")

    # Get the time array as well as positions for hands/head
    time, hand_l, hand_r, head = read_csv_file(file_path, 3, 4, 5, mode="vr")

    ds_time, ds_hand_l, ds_hand_r, ds_head = downsample_data(time, hand_l, hand_r, head, target_rate=1.0)

    # Calculate the velocity and magnitude of each body part
    hand_l_vel, hand_l_mag = calculate_derivative(ds_hand_l, ds_time)
    hand_r_vel, hand_r_mag = calculate_derivative(ds_hand_r, ds_time)
    head_vel, head_mag = calculate_derivative(ds_head, ds_time)

    # Calculate the average magnitudes of each body part
    hand_l_mag_avg = np.mean(hand_l_mag)
    hand_r_mag_avg = np.mean(hand_r_mag)
    head_mag_avg = np.mean(head_mag)

    # Plot the three dimensional graph of positional data
    plot_position(hand_l, hand_r, head, colors)

    # Plot the magnitude over time
    labels = ["Left Hand", "Right Hand", "Head"]
    colors = ["red", "blue", "green"]
    plot_magnitude(time, hand_l_mag, hand_r_mag, head_mag, labels=labels, colors=colors, ylim=(0, 1.5))


    # Calculate the acceleration
    hand_l_accel, hand_l_accel_mag = calculate_derivative(hand_l_vel, ds_time[:-1])
    hand_r_accel, hand_r_accel_mag = calculate_derivative(hand_r_vel, ds_time[:-1])
    head_accel, head_accel_mag = calculate_derivative(head_vel, ds_time[:-1])

    # Calculate the jerk
    hand_l_jerk, hand_l_jerk_mag = calculate_derivative(hand_l_accel, ds_time[:-2])
    hand_r_jerk, hand_r_jerk_mag = calculate_derivative(hand_r_accel, ds_time[:-2])
    head_jerk, head_jerk_mag = calculate_derivative(head_accel, ds_time[:-2])

    hand_l_jerk_mag_avg = np.mean(hand_l_jerk_mag)
    hand_r_jerk_mag_avg = np.mean(hand_r_jerk_mag)
    head_jerk_mag_avg = np.mean(head_jerk_mag)
    

    experiment_row = int(input("Enter the experiment number to save data: "))
    file_path = input("Enter the output file name: ")
    write_csv_file(file_path, experiment_row, hand_l_mag_avg, hand_r_mag_avg, head_mag_avg, hand_l_jerk_mag_avg, hand_r_jerk_mag_avg, head_jerk_mag_avg)
    

if __name__ == "__main__":
    main()