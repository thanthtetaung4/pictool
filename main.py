import sys
import os
from PIL import Image
from PIC import PIC

def whichMode(flag: str) -> int:
    if (flag == "-r"):
        return (1)
    elif (flag == "-f"):
        return (2)
    return (-1)

def changeExtension(image: PIC):
    if (os.path.exists(image.infile)):
        if (os.path.exists(image.outfile)):
            print(f"file {image.outfile} already exist")
            return
        if (image.outfile != image.infile):
            try:
                with Image.open(image.infile) as im:
                    im.save(image.outfile)
                    print(f"new image is saved as {image.outfile}")
            except OSError as e:
                print(f"err: {e} cannot convert {image.infile}")
        else:
            print("err: same format as the input aborted")
    else:
        print("err: broken path")

def changeSize(image: PIC):
    if (os.path.exists(image.infile)):
        if (os.path.exists(image.outfile)):
            print(f"file {image.outfile} already exist")
            return
        if (image.outfile != image.infile):
            try:
                with Image.open(image.infile) as im:
                    im = im.resize([image.width, image.height])
                    im.save(image.outfile)
                    print(f"new image is saved as {image.outfile}")
            except OSError as e:
                print(f"err: {e} cannot convert {image.infile}")
        else:
            print("err: same format as the input aborted")
    else:
        print("err: broken path")

def printHelp():
    print("Help") # will improve later

def pic(*argv):
    data = argv[0]
    if (len(data) == 2):
        if (data[1] == "-h" or data[1] == "-help"):
            printHelp()
    elif (5 >= len(data) <= 6):
        mode: int = whichMode(data[1])
        try :
            image = PIC(mode, data)
            if (image.mode == 1):
                changeSize(image)
            elif (image.mode == 2):
                changeExtension(image)
        except Exception as e:
            print("fatal err:", e, "aborting")
    else:
        print("<image_path> -[option] <new_image_path>")

if __name__ == "__main__":
    del sys.argv[0]
    pic(sys.argv)