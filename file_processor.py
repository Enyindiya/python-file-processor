import os

def process_file():
    """
    Reads a file provided by the user, reverses the text on each line,
    and writes the modified content to a new file.
    Includes robust error handling for file-related issues.
    """
    print("--- Welcome to the File Reverser ---")
    
    # Prompt the user for the name of the file to read.
    input_filename = input("Enter the name of the file to read (e.g., original.txt): ")
    
    # Create the output filename automatically.
    # It will add '_reversed' to the original filename.
    name, extension = os.path.splitext(input_filename)
    output_filename = f"{name}_reversed{extension}"
    
    try:
        # Open the input file for reading and the output file for writing.
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            print(f"Reading from '{input_filename}' and writing to '{output_filename}'...")
            
            # Read the file line by line.
            for line in infile:
                # Remove leading/trailing whitespace and reverse the line.
                reversed_line = line.strip()[::-1]
                # Write the reversed line to the output file, followed by a newline.
                outfile.write(reversed_line + '\n')
            
            print("Success! The file has been processed and saved.")

    except FileNotFoundError:
        # Handle the case where the input file does not exist.
        print(f"\nError: The file '{input_filename}' was not found.")
        print("Please make sure the file is in the same directory as this script.")
    
    except Exception as e:
        # Handle any other potential errors, such as permission issues.
        print(f"\nAn unexpected error occurred: {e}")

# This is the entry point of the script.
if __name__ == "__main__":
    process_file()
