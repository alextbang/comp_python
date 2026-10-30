# Appendto an existing file called newfile.txt
with open("newfile.txt", "a") as f:
 
    string = '''Adding more text to the file to demonstrate appending...'''
    f.write("\n")  # add a newline character at the end of the line
    f.write(string)
    f.write("\n")  # add a newline character at the end of the line

    f.close()  # explicitly close the file after writing
    print("--- File writing completed. ---")

# print the content of the file to verify it was written correctly
with open("newfile.txt", "r") as f:
    content = f.read()
    print(content)
    f.close()  # explicitly close the file after reading
    print("--- File reading completed. ---")

    