
# with open("textfile.txt", "r") as f:
#     content = f.read()  # read the entire content of the file into a single string
#     print(content)  # print the content of the file 
#     f.close()  # explicitly close the file after reading   
#     print("--- File reading completed. ---")


f = open("textfile.txt", "r")
content = f.read()  # read the entire content of the file into a single string
print(content)  # print the content of the file 
f.close()  # explicitly close the file after reading   
print("--- File reading completed. ---")

