import os

# Creating a file to write some text into it
# Method 1: Using open() in write mode
file = open('test.txt', 'w')  # Opening the file in write mode
file.write("This is the write command.\n")
file.write("It allows us to write in a particular file.\n")
file.close()  # Closing the file

# Alternative method: Using with() statement
with open("test2.txt", "w") as f:
    f.write("Hello World!!!")

# Opening an existing file in reading mode
# Default is read and text mode
file1 = open('test.txt')  # This is equivalent to open('test.txt', 'rt')
file2 = open('test.txt', 'r')
file3 = open('test.txt', 'rt')

# Print each line in the file
print("\nReading the file using open():")
for each in file1:
    print(each, end='')  # Printing line by line

# Alternative Way 1: Using read() method to read all the content
print("\nReading the file using read() method:")
file = open("test.txt", "r")
print(file.read())  # Reads all the content at once
file.close()

# Alternative Way 2: Using append mode
print("\nAppending to the file:")
file = open('test.txt', 'a')  # Open file in append mode
file.write("This will add at the end of the file.\n")
file.close()

# Print the content again after appending
file1 = open('test.txt')
print("\nReading the file after appending:")
for each in file1:
    print(each, end='')

# Alternative Way 3: Using with-read() method to read content
print("\nReading the file using with-read():")
with open("test2.txt") as file:
    data = file.read()
    print(data)

# Alternative Way 4: Reading a set of characters of a given size
print("\nReading file content character by character (5 characters at a time):")
file = open("test.txt", "r")
print(file.read(5))  # Read the first 5 characters
file.close()

# Alternative Way 5: Read all words in a file using split()
print("\nReading words in the file:")
with open("test.txt", "r") as file:
    data = file.readlines()
    for line in data:
        words = line.split()
        print(words)

# File Handling Functions
def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello, world!\n')
        print(f"File {filename} created successfully.")
    except IOError:
        print(f"Error: could not create file {filename}")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
        print(contents)
    except IOError:
        print(f"Error: could not read file {filename}")

def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print(f"Text appended to file {filename} successfully.")
    except IOError:
        print(f"Error: could not append to file {filename}")

def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print(f"File {filename} renamed to {new_filename} successfully.")
    except IOError:
        print(f"Error: could not rename file {filename}")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File {filename} deleted successfully.")
    except IOError:
        print(f"Error: could not delete file {filename}")

# Running file handling functions
if __name__ == '__main__':
    filename = "example.txt"
    new_filename = "new_example.txt"
    
    create_file(filename)
    read_file(filename)
    append_file(filename, "This is some additional text.\n")
    read_file(filename)
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename)

# Using file methods for additional file handling operations
with open('test.txt', 'r') as file:
    # 1. close() - Close the file
    file.close()

    # 2. detach() - Returns the raw stream from the buffer (used for buffered IO)
    # (Not applicable to simple file objects)

    # 3. fileno() - Get the file descriptor number
    file_descriptor = file.fileno()
    print(f"File descriptor of 'test.txt': {file_descriptor}")

    # 4. flush() - Flushes the internal buffer
    file.flush()

    # 5. isatty() - Checks if the file is interactive (e.g., terminal)
    print(f"Is the file a terminal? {file.isatty()}")

    # 6. readable() - Checks if the file can be read
    print(f"Can the file be read? {file.readable()}")

    # 7. readline() - Reads one line from the file
    print(f"First line of the file: {file.readline()}")

    # 8. readlines() - Reads all lines from the file into a list
    file.seek(0)  # Reset file pointer to beginning
    print(f"All lines in the file: {file.readlines()}")

    # 9. seek() - Change the file position
    file.seek(10)  # Move file pointer to 10th byte
    print(f"File position after seek: {file.tell()}")

    # 10. seekable() - Checks if the file allows changing position
    print(f"Can the file's position be changed? {file.seekable()}")

    # 11. tell() - Returns the current position of the file pointer
    print(f"Current file position: {file.tell()}")

    # 12. truncate() - Resizes the file to a specified size
    file.truncate(20)  # Truncate file to 20 bytes
    print(f"File truncated to 20 bytes.")

    # 13. writable() - Checks if the file can be written to
    print(f"Can the file be written to? {file.writable()}")

    # 14. write() - Writes a specified string to the file
    file.write("Adding some more text.")
    
    # 15. writelines() - Writes a list of strings to the file
    lines = ["First line\n", "Second line\n", "Third line\n"]
    file.writelines(lines)
