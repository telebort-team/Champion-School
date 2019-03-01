## Import all necessary packages
from picamera import PiCamera
from time import sleep
import numpy as np
from PIL import Image
from PIL import ImageColor
import matplotlib.pyplot as plt

## File name for save capture and read image
filename = 'image.jpg'

##camera = PiCamera()
##camera.start_preview(fullscreen=False, window=(800,330,400,400))
##sleep(5)
##camera.capture(filename)
##camera.stop_preview()
##camera.close()

## Blindness matrix
blind = {
    'Normal': [
        1, 0, 0,
        0, 1, 0,
        0, 0, 1
    ],
    'Protanopia': [
        0.567, 0.433, 0,
        0.558, 0.442, 0,
        0, 0.242, 0.758
    ],
    'Protanomaly': [
        0.817, 0.183, 0,
        0.333, 0.667, 0,
        0, 0.125, 0.875
    ],
    'Deuteranopia': [
        0.625, 0.375, 0,
        0.70, 0.30, 0,
        0, 0.30, 0.70
    ],
    'Deuteranomaly': [
        0.80, 0.20, 0,
        0.258, 0.742, 0,
        0, 0.142, 0.858
    ],
    'Tritanopia': [
        0.95, 0.05, 0,
        0, 0.433, 0.567,
        0, 0.475, 0.525
    ],
    'Tritanomaly': [
        0.967, 0.033, 0,
        0, 0.733, 0.267,
        0, 0.183, 0.817
    ],
    'Achromatopsia': [
        0.299, 0.587, 0.114,
        0.299, 0.587, 0.114,
        0.299, 0.587, 0.114
    ],
    'Achromatomaly': [
        0.618, 0.32, 0.062,
        0.163, 0.775, 0.062,
        0.163, 0.320, 0.516
    ]
}

## Function definition to filter image
def filterC(img, kernel=blind['Normal']):
    imR = np.asarray(img.getchannel("R"))
    imG = np.asarray(img.getchannel("G"))
    imB = np.asarray(img.getchannel("B"))
    
    red = Image.fromarray(np.uint8(imR * kernel[0] + imG * kernel[1] + imB * kernel[2]))
    green = Image.fromarray(np.uint8(imR * kernel[3] + imG * kernel[4] + imB * kernel[5]))
    blue = Image.fromarray(np.uint8(imR * kernel[6] + imG * kernel[7] + imB * kernel[8]))
    
    blind_img = Image.merge('RGB', [red, green, blue])
    return blind_img

## Read and resize image
im = Image.open(filename).resize((600, 600))

## Apply filter on different color blind
Pro1 = filterC(im, blind['Protanopia'])
Pro2 = filterC(im, blind['Protanomaly'])
Deu1 = filterC(im, blind['Deuteranopia'])
Deu2 = filterC(im, blind['Deuteranomaly'])
Tri1 = filterC(im, blind['Tritanopia'])
Tri2 = filterC(im, blind['Tritanomaly'])
Ach1 = filterC(im, blind['Achromatopsia'])
Ach2 = filterC(im, blind['Achromatomaly'])

## Plot images
plt.figure()
plt.subplot(3,3,1), plt.imshow(Pro1), plt.title('Protanopia'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,2), plt.imshow(Ach1), plt.title('Achromatopsia'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,3), plt.imshow(Pro2), plt.title('Protanomaly'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,4), plt.imshow(Deu1), plt.title('Deuteranopia'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,5), plt.imshow(im), plt.title('Normal'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,6), plt.imshow(Deu2), plt.title('Deuteranomaly'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,7), plt.imshow(Tri1), plt.title('Tritanopia'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,8), plt.imshow(Ach2), plt.title('Achromatomaly'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,9), plt.imshow(Tri2), plt.title('Tritanomaly'), plt.xticks([]), plt.yticks([])

## Put everyone into 1 image
x = 0
y = 0
box = (x,y,x+200,y+200)
im.paste(Pro1.crop(box), (x,y))
x = 200
y = 0
box = (x,y,x+200,y+200)
im.paste(Ach1.crop(box), (x,y))
x = 400
y = 0
box = (x,y,x+200,y+200)
im.paste(Pro2.crop(box), (x,y))
x = 0
y = 200
box = (x,y,x+200,y+200)
im.paste(Deu1.crop(box), (x,y))
x = 400
y = 200
box = (x,y,x+200,y+200)
im.paste(Deu2.crop(box), (x,y))
x = 0
y = 400
box = (x,y,x+200,y+200)
im.paste(Tri1.crop(box), (x,y))
x = 200
y = 400
box = (x,y,x+200,y+200)
im.paste(Ach2.crop(box), (x,y))
x = 400
y = 400
box = (x,y,x+200,y+200)
im.paste(Tri2.crop(box), (x,y))

## Draw border line
x = 200
y = 0
box = (x,y,x+1,y+600)
im.paste(ImageColor.getrgb('black'), box)
x = 400
y = 0
box = (x,y,x+2,y+600) ## Cannot draw line on 400
im.paste(ImageColor.getrgb('black'), box)
x = 0
y = 200
box = (x,y,x+600,y+1)
im.paste(ImageColor.getrgb('black'), box)
x = 0
y = 400
box = (x,y,x+600,y+2) ## Cannot draw line on 400
im.paste(ImageColor.getrgb('black'), box)

plt.figure(), plt.xticks([]), plt.yticks([])
plt.imshow(im)
plt.show()