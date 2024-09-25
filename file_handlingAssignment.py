
# File Creation: Writing initial content to the file
try:
    # Create a new file in write mode ('w')
    with open("my_file.txt", "w") as file:
        file.write("Line 1: Hello, this is a test file.\n")
        file.write("Line 2: The year is 2024.\n")
        file.write("Line 3: Python is awesome!\n")
    print("File 'my_file.txt' created and written successfully.")
except PermissionError:
    print("Permission Error: Unable to write to the file.")
except Exception as e:
    print(f"An error occurred: {e}")

# File Reading and Display: Reading the contents of the file
try:
    with open("my_file.txt", "r") as file:
        print("\nReading from 'my_file.txt':")
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File Not Found: The file does not exist.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending: Appending additional lines to the file
try:
    with open("my_file.txt", "a") as file:
        file.write("Line 4: Appending more content.\n")
        file.write("Line 5: Learning file handling in Python.\n")
        file.write("Line 6: Task completed successfully.\n")
    print("Content appended to 'my_file.txt'.")
except PermissionError:
    print("Permission Error: Unable to append to the file.")
except Exception as e:
    print(f"An error occurred: {e}")

# File Reading again after appending
try:
    with open("my_file.txt", "r") as file:
        print("\nReading the updated content from 'my_file.txt':")
        updated_content = file.read()
        print(updated_content)
except FileNotFoundError:
    print("File Not Found: The file does not exist.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

finally:
    print("File handling process completed.")
