import sys
import csv
import tabulate

def Tabulate(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            table_data = [row for row in reader]

        headers = table_data[0]
        data = table_data[1:]

        tabulated_data = tabulate.tabulate(data, headers=headers, tablefmt='grid')
        return tabulated_data

    except FileNotFoundError:
        print(f"File does not exist")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    file_name = sys.argv[1]
    if not file_name.endswith('.csv'):
        print("Not a CSV file")
        sys.exit(1)

    Tabulated_file = Tabulate(file_name)
    print(f"{Tabulated_file}")
