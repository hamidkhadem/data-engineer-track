import sys

print("\nInside python file")

file_to_write = "output_data/output_data.txt"
with open(file_to_write, "a") as file:
    file.write("\n")
    file.write(f"\nFile name: {sys.argv[0]}")  # print file name
    file.write(f"\nFirst argument: {sys.argv[1]}")  # print first command line argument
    file.write(f"\nSecond argument: {sys.argv[2]}")  # print second command line argument

print("\nDone with Python file")