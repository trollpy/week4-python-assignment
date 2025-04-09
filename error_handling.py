def read_file_safely():
    while True:
        filename = input("Please enter the filename you'd like to read: ")
        try:
            with open(filename, 'r') as file:
                contents = file.read()
                print("\nFile contents:")
                print(contents)
                return contents
                
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist. Please try again.")
        except PermissionError:
            print(f"Error: You don't have permission to read '{filename}'. Please try another file.")
        except IsADirectoryError:
            print(f"Error: '{filename}' is a directory, not a file. Please provide a filename.")
        except UnicodeDecodeError:
            print(f"Error: Could not decode the contents of '{filename}'. It may be a binary file.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}. Please try again.")

if __name__ == "__main__":
    print("File Reader with Error Handling")
    print("--------------------------------")
    read_file_safely()