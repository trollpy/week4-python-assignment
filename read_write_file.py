input_file = "sample.txt"
output_file = "output.txt"

# Read the contents of the input file
with open(input_file, 'r') as file:
    content = file.read()
    # print(content)
    
# Write the contents to the output file
modified_content = content.upper()
with open(output_file, 'w') as file:
    file.write(modified_content)  # Changed from content to modified_content
    print(f"Content written to {output_file}")
    