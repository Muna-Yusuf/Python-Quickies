def read_and_write_file():
    """
    Reads a file and writes a modified version to a new file.
    Handles errors if the file does not exist or cannot be read.
    """
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the file to write: ")
    
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            modified_content = content.upper()  # Example modification
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Successfully wrote to {output_filename}")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Could not read or write to file.")

# Run the function
read_and_write_file()
