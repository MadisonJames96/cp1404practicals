import os


def main():
    os.chdir('FilesToSort')

    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    for file in os.listdir('.'):
        if os.path.isdir(file):
            continue

        extension = file.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

        os.rename(file,  extension)


main()
