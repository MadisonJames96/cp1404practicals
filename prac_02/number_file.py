
OUTPUT_FILE = "number.txt"
out_file = open(OUTPUT_FILE,'r')
first_number = int(out_file.readline())
second_number = int(out_file.readline())
result = second_number + first_number
print(result)

out_file.close()