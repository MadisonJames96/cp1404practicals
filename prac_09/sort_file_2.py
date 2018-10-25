import shutil
import os

def main():
    extensions_to_directories = {}
    os.chdir("FilesToSort")
    for file in os.listdir('.'):
        if os.path.isdir(file):
            continue

        extension = file.split('.')[-1]
        if extension not in extensions_to_directories:
            new_directory = input("What category would you like to sort {} files into?".format(extension))
            extensions_to_directories[extension] = new_directory

            try:
                os.mkdir(new_directory)
            except FileExistsError:
                pass

        shutil.move(file, new_directory + "/" + file)

main()