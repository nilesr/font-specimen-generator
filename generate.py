from PIL import Image, ImageDraw, ImageFont
import subprocess, os, random
def getFontName(font, extra = False):
    result = font.split("/")[-2]
    if result == "tmp":
        return font.split("/")[-1]
    if extra:
        result += "-" + font.split("/")[-1]
    return result
i=0
word = "The brown fox jumps over the lazy red dog or something"
wordlist = "/usr/share/dict/american-english"
null = open("/dev/null", "w")
print(" ".join(["find", "/home/niles/Documents/fonts", "-type", "f", "-iregex", ".*\\.ttf|.*\\.otf"]))
fonts = subprocess.check_output(["find", "/home/niles/Documents/fonts", "-type", "f", "-iregex", ".*\\.\(ttf\|otf\)"]).decode("utf-8").split("\n")[:-1]
i = 0
for font in fonts:
    i+=1
    idx = str(i).zfill(len(str(len(fonts))))
    print("Generating " + idx + getFontName(font, True))
    try:
        if os.path.exists(wordlist):
            word = ""
            while len(word) < 8:
                wllen = subprocess.check_output(["wc", "-l", wordlist]).decode("utf-8").strip().split()[0]
                newword = subprocess.check_output(["bash", "-c", "head -n " + str(random.randint(0,int(wllen))) + " " + wordlist + "|tail -n 1"]).decode("utf-8").strip()
                newword = newword[0].upper() + newword[1:]
                if '\'' in newword:
                    continue
                word = word + " " + newword
            print(word)
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
        d.text((100,1200), word, font=fnt, fill=(0,0,0,255))
        fnt = ImageFont.truetype(font, 180)
        d.text((100,1700), "abcdefghijklm", font=fnt, fill=(0,0,0,255))
        d.text((100,1900), "nopqrstuvwxyz", font=fnt, fill=(0,0,0,255))
        fnt = ImageFont.truetype(font, 250)
        d.text((450,2100), "0123456789", font=fnt, fill=(255,255,255,255))
        out = txt#Image.alpha_composite(base, txt)
        out.save("out/" + idx + "-" + getFontName(font, True) + ".png")
    except:
        import traceback
        print(traceback.format_exc())
