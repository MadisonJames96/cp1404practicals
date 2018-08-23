OUTPUT_FILE = "name.txt"
out_file = open(OUTPUT_FILE, 'r')
name = out_file.read()

print("Your name is {}".format(name))

out_file.close()