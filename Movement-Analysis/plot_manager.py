import matplotlib.pyplot as plt
import numpy as np

def plot_position(hand_l, hand_r, head, colors):

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
    ax.plot(hand_l[0], hand_l[1], hand_l[2], c=colors[0], label='Left Hand', linewidth=.25)
    ax.plot(hand_r[0], hand_r[1], hand_r[2], c=colors[1], label='Right Hand', linewidth=.25)
    ax.plot(head[0], head[1], head[2], c=colors[2], label='Head', linewidth=.25)

    # # Set appropriate axis labels
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Z-axis')
    ax.set_zlabel('Y-axis')

    # Add the title to the plot
    ax.set_title('Low Movement VR Player Positional Data')

    ax.legend(loc='upper left', bbox_to_anchor=(-0.35, 0.6))
    plt.show()


def plot_magnitude(time, *magnitudes, labels=None, colors=None, title_prefix="Magnitude", ylim=None):
    
    # Format for Axes (10 minute experiment)
    time /= 60.0

    # Get the length of magnitudes to determine how much to write
    num_plots = len(magnitudes)

    # If the arguments are empty, then we exit the program because this is incorrect
    if labels is None or colors is None or ylim is None:
        print("Error: insufficient data entered.")
        exit()

    # If we are just plotting the mouse magnitude
    if num_plots == 1:
        plt.figure(figsize=(8,4))
        plt.plot(time, magnitudes[0], color=colors[3])
        plt.title(labels)
        plt.xlabel("Time Elapsed (min)")
        plt.ylabel("Magnitude (N)")

        if ylim[0]:
            plt.ylim(*ylim[0])
        plt.tight_layout
        plt.show()

    # If we are plotting the left/right hands and head magnitudes
    else:
        fig, axes = plt.subplots(num_plots, 1, figsize=(8, 2.5 * num_plots), sharex=True)
        for i in range(num_plots):
            ax = axes[i]
            ax.plot(time[:-1], magnitudes[i], color=colors[i])
            ax.set_title(labels[i])
            ax.set_ylabel("Magnitude (N)")
            ax.set_ylim(ylim)
        
        axes[-1].set_xlabel("Time Elapsed (min)")
        plt.tight_layout()
        plt.show()
