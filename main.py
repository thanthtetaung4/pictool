import sys
import os
from PIL import Image
from PIC import PIC

def whichMode(flag: str) -> int:
    print(flag == "-f")
    if (flag == "-r"):
        return (1)
    elif (flag == "-f"):
        return (2)
    return (-1)

def changeExtension(image: PIC):
    if (os.path.exists(image.infile) and os.path.isdir(image.outfile) and len(image.format) > 0):
        outfile, e = os.path.splitext(image.infile)
        outfile += f".{image.format}"
        if (outfile != image.infile):
            try:
                with Image.open(image.infile) as im:
                    im.save(outfile)
            except OSError:
                print("err: cannot conver", image.infile)
        else:
            print("err: same format as the input aborted")

def changeSize(image: PIC):
    pass

def printHelp():
    print("Help") # will improve later

def pic(*argv):
    data = argv[0]
    if (len(data) == 2):
        if (data[1] == "-h" or data[1] == "-help"):
            printHelp()
    elif (4 >= len(data) <= 5):
        print(data)
        mode: int = whichMode(data[1])
        try :
            image = PIC(mode, data)
            print(image)
            if (image.mode == 1):
                print("resize")
            elif (image.mode == 2):
                print("format")
                changeExtension(image)
        except Exception as e:
            print("fatal err:", e)
    else:
        print("<image_path> -[option] <save_path> <new_format>")

if __name__ == "__main__":
    del sys.argv[0]
    print(sys.argv)
    pic(sys.argv)