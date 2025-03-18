import csv

def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for column in csv_reader:
                print(colum)

    except FileNotFoundError:
        print(f"Error: The file '{file_path} was not found.")
    except Exception as e:
        print(f"An error occured: {e}")

file_path = "03-06-2025_12-17-49.csv"
read_csv_file(file_path)