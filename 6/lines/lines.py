import sys

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        count = 0
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                count += 1

        return count

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
    if not file_name.endswith('.py'):
        print("Not a Python file")
        sys.exit(1)

    lines_count = count_lines(file_name)
    print(f"{lines_count}")
