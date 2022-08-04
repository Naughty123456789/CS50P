import sys
from os.path import splitext
from PIL import Image,ImageOps


def main():
    checking_command_line()

    try:
        Image_file=Image.open(sys.argv[1])
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)
    shirt_file=Image.open("shirt.png")
    size= shirt_file.size
    picture=ImageOps.fit(Image_file,size)

    picture.paste(shirt_file,shirt_file)
    picture.save(sys.argv[2])


def checking_command_line():
    if len(sys.argv)<3:
        print("Too few command-line arguement")
        sys.exit(1)

    if len(sys.argv)>3:
        print("Too many command-line arguement")
        sys.exit(1)
    file1=splitext(sys.argv[1])
    file2=splitext(sys.argv[2])

    if check_extend(file1[1])==False or check_extend(file2[1])==False:
        print("Wrong extension")
        sys.exit(1)

    if file1[1].lower() != file2[1].lower():
        print("Different extension")
        sys.exit(1)



def check_extend(file):
    if file in [".jpg",".jpeg",".png"]:
        return True


if __name__ == "__main__":
    main()

