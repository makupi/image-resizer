from PIL import Image
import glob, os
linebreaker = "-----------------------------------------------"
print(linebreaker)
print("## Running resize tool by maku :3")
print("## For issues/feedback contact me via discord maku#0001")
print(linebreaker)

sizes = [112, 56, 28]
files = glob.glob("input/*.png")

print("Output sizes: " + str(sizes))
print("Number of input files found: " + str(len(files)))
print("Starting resize..")
print(linebreaker)

for infile in files:
    file, ext = os.path.splitext(os.path.basename(infile))
    print("Resizing " + file + ".. ", end='')
    im = Image.open(infile)
    for size in sizes:
        res = im.resize((size, size), Image.ANTIALIAS)
        filename = "output/" + file + "_" + str(size) + ".png"
        res.save(filename, "PNG", quality=95)
    print("done.")

print(linebreaker)
print("All files processed and saved to output folder.")

input("Press ENTER to exit..")
