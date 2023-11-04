from PIL import Image, ImageDraw, ImageFont

# get an image
with Image.open(r'source\市府班AI大頭貼\12鄭楷諭.jpg').convert("RGBA") as base:

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

    # get a font
    fnt = ImageFont.truetype(r"C:\Windows\Fonts\msjhbd.ttc", 180)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    d.rectangle([250, 170, 850, 950], fill=None, outline=(0, 0, 255), width=10)
    d.rectangle([250, 950, 850, 1200], fill=(0, 0, 255), outline=None , width=10)

    # draw text, with opacity
    d.text((270, 950), "鄭楷諭", font=fnt, fill=(255, 255, 255, 128))

    out = Image.alpha_composite(base, txt)

    out.show()