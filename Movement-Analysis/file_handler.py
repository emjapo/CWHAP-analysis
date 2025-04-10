import csv
import numpy as np

def read_csv_file(file_path, *column_indices, mode):
    """
    Function:
    Reads the CSV file give through the file path and places data into usable arrays.
    
    Parameters:
    - file path: The file path of the CSV file
    - column indicies: What columns of the CSV file do you want to be read

    Returns:
    - time: Array of timestamps
    - position arrays: List of positional data [3 x length of time]
    """

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
                coords_list = []

                for i in experiment_limit:

                    # Assign the string value and convert to floating point
                    value = rows[i][column_index]
                    coords = value.strip("() ").split(";")
                    coords = [float(x.strip()) for x in coords]

                    # Append with appropriate coordinate system
                    if mode == "vr":
                        coords_list.append([coords[0], coords[2], -coords[1]])
                    
                    elif mode == "pc":
                        coords_list.append([coords[0], coords[1]])
                    
                    else:
                        raise ValueError(f"Unknown mode '{mode}'. Use 'vr' or 'pc'.")

                # Append to the overall array
                position_array = np.array(coords_list).T
                position_arrays.append(position_array)

        # Returns arrays of shape (length_of_rows) and (3, length_of_rows)
        return time, *position_arrays
    
    # Exception catch statements
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit()
    except Exception as e:
        print(f"An error occured: {e}")
        exit()


def write_csv_file(file_path, experiment_row, left_avg, right_avg, head_avg, left_j_avg, right_j_avg, head_j_avg):
    try:
        # Read the CSV file from path
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Ensure the row has at least 7 columns
        while len(rows[experiment_row]) < 9:
            rows[experiment_row].append("")

        
        if 1 <= experiment_row < len(rows):
            rows[experiment_row][1] = f"{left_avg:.6f}"
            rows[experiment_row][2] = f"{right_avg:.6f}"
            rows[experiment_row][3] = f"{head_avg:.6f}"
            rows[experiment_row][5] = f"{left_j_avg:.6f}"
            rows[experiment_row][6] = f"{right_j_avg:.6f}"
            rows[experiment_row][7] = f"{head_j_avg:.6f}"

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