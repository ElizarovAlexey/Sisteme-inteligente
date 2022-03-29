import numpy as np
import os

pathToImages = './images/'

imagesPath = os.listdir(pathToImages)

images = []

# a. Citiți imaginile din aceste fișiere și salvați-le într-un np.array (va avea dimensiunea 9x400x600).

for path in imagesPath:
    images.append(np.load(pathToImages + path))

images = np.array(images)

# b. Calculați suma valorilor pixelilor tuturor imaginilor.

sumPixels = np.sum(images)

print(sumPixels)

# c. Calculați suma valorilor pixelilor pentru fiecare imagine în parte.

sumPixelsImage = np.sum(images, axis = (1, 2))
print(sumPixelsImage)

# d. Afișați indexul imaginii cu suma maximă.

sumPixelsImageMaxPosition = np.argmax(sumPixelsImage)
print(sumPixelsImageMaxPosition)

# e. Calculați imaginea medie și afișati-o.

averageImage = np.mean(images, axis = 0)
io.imshow(averageImage.astype(np.uint8))
io.show()

# f. Cu ajutorul funcției np.std(images_array), calculați deviația standard a imaginilor.

imageStandartDeviation  = np.std(images)
print(imageStandartDeviation)

# g. Normalizați imaginile. (se scade imaginea medie și se împarte rezultatul la deviația standard)

normalizedImages = (images - averageImage) / np.std(images)
print(normalizedImages)

# h. Decupați fiecare imagine, afișând numai liniile cuprinse între 200 și 300, respectiv coloanele cuprinse între 280 și 400.

cropImage = images[:, 200:301, 290:401]
plt.imshow(images[4].astype(np.uint), cmap = 'gray')
plt.imshow(cropImage[4].astype(np.uint), cmap = 'gray')