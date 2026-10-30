
# using 'with open' is best practice because it automatically closes the file after reading, even if an error occurs.
# with open("textfile.txt", "r") as f:
#     content = f.read()  # read the entire content of the file into a single string
#     print(content)  # print the content of the file 
#     f.close()  # explicitly close the file after reading   
#     print("--- File reading completed. ---")


# this is an alternative way to read a file without using 'with open', but it requires manually closing the file, which is more error-prone.
f = open("textfile.txt", "r")
content = f.read()  # read the entire content of the file into a single string
print(content)  # print the content of the file 
f.close()  # explicitly close the file after reading   
print("--- File reading completed. ---")

