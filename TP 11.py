
# Modification date: Thu Dec 10 09:54:18 2020

# Production date: Sun Sep  3 15:43:47 2023

from PIL import Image
"""

#ex 2)

img = Image.open("Engineer.png")


for i in range(184):
    for j in range(184):
        RVB = img.getpixel((i, j))
        R00 = (RVB[0], 0, 0)
        img.putpixel((i, j), R00)

img.save("EngiFEAR.png", "png")

img.show()




#ex 3)


#Bleu

img = Image.open("Engineer.png")


for i in range(184):
    for j in range(184):
        RVB = img.getpixel((i, j))
        _00B = (0, 0, RVB[2])
        img.putpixel((i, j), _00B)

img.save("BLUEngie.png", "png")

img.show()

#Vert

img = Image.open("Engineer.png")


for i in range(184):
    for j in range(184):
        RVB = img.getpixel((i, j))
        _0V0 = (0, RVB[1], 0)
        img.putpixel((i, j), _0V0)

img.save("GREEngie.png", "png")

img.show()



#Noir et Blanc

img = Image.open("Engineer.png")

for i in range(184):
  for j in range(184):
    RVB = img.getpixel((i, j))
    if RVB[0] + RVB[1] + RVB[2] < 255:
      img.putpixel ((i, j) ,(255, 255, 255))
    else:
      img.putpixel ((i, j) ,(0, 0, 0))


img.save("WhiteBlackEngie.png","png")


img.show()


#Blanc et Noir

img = Image.open("Engineer.png")

for i in range(184):
  for j in range(184):
    RVB = img.getpixel((i, j))
    if RVB[0] + RVB[1] + RVB[2] < 255:
      img.putpixel ((i, j) ,(0, 0, 0))
    else:
      img.putpixel ((i, j) ,(255, 255, 255))


img.save("BlackWhiteEngie.png","png")


img.show()



#rotation de 180 degré 

img = Image.open("Engineer.png")

img = img.rotate(180)

img.save("180degrEngie.png","png")


img.show()


#rotation de 90 degré 

img = Image.open("Engineer.png")

img = img.rotate(90)

img.save("90degrEngie.png","png")


img.show()


#Pixelisation

img = Image.open("Engineer.png")

imgS = img.resize((23, 23),resample=Image.BILINEAR)

img = imgS.resize(img.size,Image.NEAREST)

img.save("PixEngie.png","png")


img.show()


#Combination de deux images

img = Image.open("Engineer.png")

image = Image.open("Ubered_Engineer.png")

for i in range(0, 184, 2):
    for j in range(0, 184, 2):
        imagepixel = image.getpixel((i, j))
        img.putpixel ((i, j), imagepixel)

for i in range(1, 183, 2):
    for j in range(1, 183, 2):
        imagepixel = image.getpixel((i, j))
        img.putpixel ((i, j), imagepixel)
        

img.save("RagEngie.png","png")


img.show()




#Combination à l'aide d'un fond vert

img = Image.open("Engineer.png")

image = Image.open("UseMoreGun.png")

for i in range(184):
    for j in range(184):
        px = image.getpixel((i, j))
        if not(px[1] >= 252):
            img.putpixel ((i, j), px)


img.save("GiveMeTheMoney.png","png")


img.show()

"""




img = Image.open("lennaSP25.gif")#256x256



img.save("photo.png", "png")














