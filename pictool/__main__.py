#!/usr/bin/env python3
import sys
import os
from PIL import Image
from pictool.pic_class import PIC

def whichMode(flag: str) -> int:
    if flag == "-r":
        return 1
    elif flag == "-f":
        return 2
    return -1

def changeExtension(image: PIC):
    if os.path.exists(image.infile):
        if os.path.exists(image.outfile):
            print(f"file {image.outfile} already exists")
            return
        if image.outfile != image.infile:
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
    if os.path.exists(image.infile):
        if os.path.exists(image.outfile):
            print(f"file {image.outfile} already exists")
            return
        if image.outfile != image.infile:
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
    print("Usage:")
    print("  pictool <image_path> -r <width> <height> <new_image_path>")
    print("  pictool <image_path> -f <new_image_path>")
    print("Options:")
    print("  -r     Resize image")
    print("  -f     Change image format")
    print("  -h     Show this help message")

def pic(*argv):
    data = argv[0]
    if not data:
        print("<image_path> -[option] <new_image_path>")
        return

    if len(data) == 1 and (data[0] in ("-h", "-help")):
        printHelp()
        return

    if len(data) in (3, 5):
        mode = whichMode(data[1]) if len(data) > 1 else -1
        try:
            image = PIC(mode, data)
            if image.mode == 1:
                changeSize(image)
            elif image.mode == 2:
                changeExtension(image)
            else:
                print("err: invalid flag, use -r or -f")
        except Exception as e:
            print("fatal err:", e, "aborting")
    else:
        print("<image_path> -[option] <new_image_path>")

def main():
    del sys.argv[0]
    pic(sys.argv)

if __name__ == "__main__":
    main()
