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
fonts = subprocess.check_output(["find", "/home/niles/Downloads/fonts", "-type", "f", "-iname", "*.ttf"]).decode("utf-8").split("\n")[:-1]
for font in subprocess.check_output(["find", "/home/niles/Downloads/fonts", "-type", "f", "-iname", "*.otf"]).decode("utf-8").split("\n")[:-1]:
    #prettyname = "-".join(font.split("/")[-2:]).replace(".otf", ".ttf")
    prettyname = getFontName(font, True).replace(".otf", ".ttf")
    print("Converting " + str(i) + " " + prettyname)
    i += 1
    subprocess.call(["fontforge", "-script", "convert_script.sh", font, prettyname], stderr=null, stdout=null)
    fonts.append("/tmp/" + prettyname)
i = 0
for font in fonts:
    i+=1
    print("Generating " + str(i) + getFontName(font, True))
    try:
        txt = Image.new('RGBA', (2000, 400), (29,204,32, 255))
        fnt = ImageFont.truetype(font, 150)
        d = ImageDraw.Draw(txt)
        d.text((10,10), getFontName(font, True), font=fnt, fill=(0,0,0,255))
        d.text((10,10 + 150), "The brown fox jumps over the lazy red dog or something", font=fnt, fill=(0,0,0,255))
        out = txt#Image.alpha_composite(base, txt)
        out.save("out/" + str(i) + "-" + getFontName(font, True) + ".png")
    except:
        continue
