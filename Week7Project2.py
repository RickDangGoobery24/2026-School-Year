def main():
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    total_lines = len(lines)

    while True:
        print("\nNumber of lines:", total_lines)
        number = int(input("Enter a line number (0 to quit): "))

        if number == 0:
            break
        elif 1 <= number <= total_lines:
            print(lines[number - 1], end="")
        else:
            print("Invalid line number.")


if __name__ == "__main__":
    main()
