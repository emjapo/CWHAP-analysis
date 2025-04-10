import numpy as np

def calculate_derivative(position, time):
    """
    Function:
    Calculates the derivative using broadcasting

    Parameters:
    - position: The data you want derived
    - time: The time you want to derive the data with

    Returns:
    - derivative: The new derived data
    - magnitude: The magnitudes of each of the derived vectors
    """

    # Calculate time differences
    dt = np.diff(time)
    
    # Calculate the position differences
    dp = np.diff(position, axis=1)
    
    # Calculate the derivative (velocity, acceleration, or jerk)
    derivative = np.zeros_like(dp)
    for i in range(dp.shape[1]):
        derivative[:, i] = dp[:, i] / dt[i]
    
    # Calculate the magnitude
    magnitude = np.sqrt(np.sum(derivative**2, axis=0))
    
    return derivative, magnitude

def calculate_magnitude(velocity):
    # Calculate the magnitude
    magnitude = np.sqrt(np.sum(velocity**2, axis=0))
    return magnitude


def downsample_data(time, *position_arrays, target_rate=1.0):
    """
    Downsample position data to approximately 1 sample per second.
    
    Parameters:
    - time: Array of timestamps
    - position_arrays: Arrays of position data with shape (3, n_samples)
    - target_rate: Target sample rate in Hz (default: 1.0 Hz = 1 sample per second)
    
    Returns:
    - downsampled_time: Array of downsampled timestamps
    - downsampled_positions: List of downsampled position arrays
    """
    # Calculate the time span of the original data
    time_span = time[-1] - time[0]
    
    # Calculate how many samples we want (roughly 1 per second)
    target_samples = int(time_span * target_rate) + 1
    
    # Create indices for uniform sampling
    indices = np.linspace(0, len(time) - 1, target_samples, dtype=int)
    
    # Extract the downsampled time points
    downsampled_time = time[indices]
    
    # Downsample each position array
    downsampled_positions = []
    for pos in position_arrays:
        downsampled_pos = pos[:, indices]
        downsampled_positions.append(downsampled_pos)
    
    return downsampled_time, *downsampled_positions