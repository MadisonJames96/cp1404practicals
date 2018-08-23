
name = input("Enter name: ")
OUTPUT_FILE = "name.txt"
out_file = open(OUTPUT_FILE, 'w')
print("{}".format(name), file=out_file)

out_file.close()