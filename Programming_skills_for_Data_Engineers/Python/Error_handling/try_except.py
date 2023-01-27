import os

try:
    f = open("demofile.txt") # File does not exist
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when opening the file")
finally:
    print("Process has ended!")