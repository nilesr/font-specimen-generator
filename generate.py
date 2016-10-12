from PIL import Image, ImageDraw, ImageFont
import subprocess
def getFontName(font, extra = False):
    result = font.split("/")[-2]
    if result == "tmp":
        return font.split("/")[-1]
    if extra:
        result += "-" + font.split("/")[-1]
    return result
i=0
null = open("/dev/null", "w")
print(" ".join(["find", "/home/niles/Documents/fonts", "-type", "f", "-iregex", ".*\\.ttf|.*\\.otf"]))
fonts = subprocess.check_output(["find", "/home/niles/Documents/fonts", "-type", "f", "-iregex", ".*\\.\(ttf\|otf\)"]).decode("utf-8").split("\n")[:-1]
i = 0
for font in fonts:
    i+=1
    print("Generating " + str(i) + getFontName(font, True))
    try:
        txt = Image.new('RGBA', (2000, 2400), (211,141,95, 255))
        #txt.putpixel((x, y), (255, 127, 42, 255))
        d = ImageDraw.Draw(txt)
        d.rectangle([(0, 1600), (2000, 2400)], (255, 127, 42, 255))
        fnt = ImageFont.truetype(font, 200)
        d.text((100,110), getFontName(font, True), font=fnt, fill=(0,0,0,255))
        fnt = ImageFont.truetype(font, 300)
        d.text((50,450), "Aa Ee Rr", font=fnt, fill=(0,0,0,255))
        fnt = ImageFont.truetype(font, 300)
        d.text((50,750), "Aa Ee Rr", font=fnt, fill=(0,0,0,255))
        fnt = ImageFont.truetype(font, 800)
        d.text((1500,300), "a", font=fnt, fill=(255,255,255,255))
        fnt = ImageFont.truetype(font, 200)
        d.text((100,1200), "The brown fox jumps over the lazy red dog or something", font=fnt, fill=(0,0,0,255))
        fnt = ImageFont.truetype(font, 180)
        d.text((100,1700), "abcdefghijklm", font=fnt, fill=(0,0,0,255))
        d.text((100,1900), "nopqrstuvwxyz", font=fnt, fill=(0,0,0,255))
        fnt = ImageFont.truetype(font, 250)
        d.text((450,2100), "0123456789", font=fnt, fill=(255,255,255,255))
        out = txt#Image.alpha_composite(base, txt)
        out.save("out/" + str(i) + "-" + getFontName(font, True) + ".png")
    except:
        import traceback
        print(traceback.format_exc())
