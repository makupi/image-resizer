from PIL import Image
from PIL import ImageFilter
import glob, os, json


default_config = {
        "config": {
            "filter": 0,
            "experimental": {
                "sharper": False,
                "smoother": False,
                "edgeEnhance": False,
                "detail": False
            }
        },
        "twitchEmotes": {
            "sizes": [112, 56, 28],
            "inputFolder": "in_emotes", 
            "outputFolder": "out_emotes"
        },
        "subBadges": {
            "sizes": [72, 36, 18],
            "inputFolder": "in_badges",
            "outputFolder": "out_badges"
            }    
        }
try:
    with open('config.json') as config_file:
        config = json.load(config_file)
except:  # fallback default config
    config = default_config

linebreaker = "-----------------------------------------------"
print(linebreaker)
print("## Running resize tool by maku :3")
print("## For issues/feedback contact me via discord maku#0001")
print(linebreaker)

cfg = config.get('config')
filt = cfg.get('filter', None)
if not filt:
    filt = Image.ANTIALIAS
else:
    filt = filt.lower()
    if filt == 'bicubic':
        filt = Image.BICUBIC
    elif filt == 'bilinear':
        filt = Image.BILINEAR
    elif filt == 'lanczos':
        filt = Image.ANTIALIAS
exp = cfg.get('experimental', None)
sharper = False
smoother = False
edge = False
detail = False
if exp:
    sharper = exp.get('sharper', False)
    smoother = exp.get('smoother', False)
    edge = exp.get('edgeEnhance', False)
    detail = exp.get('detail', False)

for key, value in config.items():
    if key == "config":
        continue
    sizes = value['sizes']
    in_folder = value.get('inputFolder', 'input')
    out_folder = value.get('outputFolder', 'output')
    files = glob.glob(in_folder + "/*.png")

    print("Output sizes: " + str(sizes))
    print("Number of input files found: " + str(len(files)))
    print("Starting resize " + key + "..")
    print(linebreaker)

    for infile in files:
        file, ext = os.path.splitext(os.path.basename(infile))
        print("Resizing " + file + ".. ", end='')
        im = Image.open(infile)
        for size in sizes:
            res = im.resize((size, size), filt)

            if sharper:
                res = res.filter(ImageFilter.SHARPEN)
                print("using sharper.. ")
            if smoother:
                res = res.filter(ImageFilter.SMOOTH)
                print("using smoother.. ")
            if edge:
                res = res.filter(ImageFilter.EDGE_ENHANCE)
                print("using edge enhance.. ")
            if detail:
                res = res.filter(ImageFilter.DETAIL)
                print("using detail.. ")

            filename = out_folder + "/" + file + "_" + str(size) + ".png"
            res.save(filename, "PNG", quality=95)
        print("done.")
    print(key + " done.")
    print(linebreaker)


print("All files processed and saved to output folder.")

input("Press ENTER to exit..")
