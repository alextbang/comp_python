# read the file line by line to optimize memory usage
with open("newfile.txt", "r") as f:
    for line in f:
        print(line.strip()) #
    print("--- File reading line by line completed. ---")