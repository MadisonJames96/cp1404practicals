import shutil
import os

def main():

    # Change to desired directory
    os.chdir('FilesToSort')

    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass



        os.rename(filename, "{}/{}".format(extension, filename))

main()