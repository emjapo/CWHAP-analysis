import csv
import numpy as np

def read_csv_file(file_path, *column_indices, mode):
   
    """
    Function:
    Reads the CSV file give through the file path and places data into usable arrays.
    
    Parameters:
    - file path: The file path of the CSV file
    - column indicies: What columns of the CSV file do you want to be read
    - mode: Whether you are passing in "VR" data or "PC" data

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


def write_csv_file(*data, file_path, experiment_row):

    """
    Function:
    Reads the data given and writes it to the file path under the row specified

    Parameters:
    - data: The data you would like to enter into the CSV file (This can only be length of 2 or 6)
    - file_path: The path of the CSV file you would like to write out to
    - experiment_row: The row of which experiment you are analyzing

    """

    try:

        num_data = len(data)

        if(num_data != 2 and num_data != 6):
            print("Error: Insufficient input data")
            return
        

        # Read the CSV file from path
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        if 1 <= experiment_row < len(rows):
            if(num_data == 2):
                m_avg, mj_avg = data
                rows[experiment_row][4] = f"{m_avg:.6f}"
                rows[experiment_row][8] = f"{mj_avg:.6f}"
            elif(num_data == 6):
                l_avg, r_avg, h_avg, lj_avg, rj_avg, hj_avg = data
                rows[experiment_row][1] = f"{l_avg:.6f}"
                rows[experiment_row][2] = f"{r_avg:.6f}"
                rows[experiment_row][3] = f"{h_avg:.6f}"
                rows[experiment_row][5] = f"{lj_avg:.6f}"
                rows[experiment_row][6] = f"{rj_avg:.6f}"
                rows[experiment_row][7] = f"{hj_avg:.6f}"

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