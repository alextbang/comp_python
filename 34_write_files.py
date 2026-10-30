# Write to a file called newfile.txt
with open("newfile.txt", "w") as f:
    f.write("Hello, this is a new file.")
    f.write("\n")  # add a newline character at the end of the line
    f.write("This is another line in the new file.")
    f.write("\n")  # add a newline character at the end of the line

    string = '''lorem ipsum dolor sit amet consectetur adipiscing elit iusto duis fuga excepturi nam voluptas ullamco et assumenda et incididunt est dolore est quidem et id quos provident culpa provident sunt occaecat possimus quo ea quibusdam voluptate harum autem dolores minus qui iusto ullamco omnis consectetur cumque et libero rerum dolor.'''
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

    