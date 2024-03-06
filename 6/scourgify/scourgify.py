import sys
import csv

def scourgify(file_input, file_output):
    try:
        with open(file_input) as file:
            reader = csv.DictReader(file, fieldnames=["name", "house"])
            newfile = []
            for row in reader:
                newfile.append({'name': row['name'], 'house': row['house']})

            newfile2 = []
            for n in range(len(newfile)):
                fname = newfile[n]['name']
                if ',' in fname:
                    lastname, firstname = fname.split(', ')
                else:
                    continue
                newfile2.append({'firstname': firstname, 'lastname': lastname, 'house': newfile[n]['house']})

        with open(file_output, 'w') as file2:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(file2, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(newfile2)):
                writer.writerow({
                    'first': newfile2[i]['firstname'],
                    'last': newfile2[i]['lastname'],
                    'house': newfile2[i]['house']
                })

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
    else:
        file_input = sys.argv[1]
        file_output = sys.argv[2]
        if not file_input.endswith('.csv'):
            print("Not a CSV file")
            sys.exit(1)
        else:
            scourgify(file_input, file_output)
