import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# function definition
def filter(img, kernel):
    imR = np.asarray(im.getchannel("R"))
    imG = np.asarray(im.getchannel("G"))
    imB = np.asarray(im.getchannel("B"))
    

# Read image
im = Image.open('raspberry.jpeg').resize((256, 256))
plt.figure()
plt.imshow(im)

# Dealing RGB layers
imR = im.getchannel("R")
imG = im.getchannel("G")
imB = im.getchannel("B")

plt.figure()
plt.set_cmap('gray')
plt.xticks([]), plt.yticks([])

plt.subplot(1,3,1), plt.imshow(imR)
plt.title('Red layer')

plt.subplot(1,3,2), plt.imshow(imG)
plt.title('Green layer')

plt.subplot(1,3,3), plt.imshow(imB)
plt.title('Blue layer')

# Combine layers back to RGB
imRGB = Image.merge('RGB', [imR, imG, imB])
plt.figure()
plt.imshow(imRGB)

# Dealing with grayscale
imgray = im.convert("L")

plt.figure()
plt.imshow(imgray)

# Show all plots
plt.show()