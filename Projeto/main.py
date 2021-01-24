# Original
# boundaries = [ ([58, 57, 101], [76, 95, 162]) ]


import cv2
import imutils
import numpy as np

#Read the Rust Photograph
img = cv2.imread('no_1.jpg', 1)
height, width, channels = img.shape

#Set different boundaries for different shades of rust
# boundaries = [B, G, R] em vez de RGB
rust1 = [([70, 57, 110], [83, 95, 130])]
rust2 = [([80, 100, 140], [90, 110, 180])]
rust3 = [([95, 125, 200], [100, 140, 205])]
# ferrugem laranja
rust4 = [([35, 65, 115], [45, 90, 145])]


rust5 = [([30, 30, 60], [50, 40, 70])]

rust6 = [([115, 150, 220], [120, 160, 225])]

# no = [([30, 40, 60], [50, 55, 70])]

# no = [([100, 140, 205], [115, 150, 220])]


#Highlight out the shades of rust
for (lower1, upper1) in rust1:
    lower1 = np.array(lower1, dtype = "uint8")
    upper1 = np.array(upper1, dtype = "uint8")
    mask = cv2.inRange(img, lower1, upper1)
    output1 = cv2.bitwise_and(img, img, mask=mask)

for (lower2, upper2) in rust2:
    lower2 = np.array(lower2, dtype = "uint8")
    upper2 = np.array(upper2, dtype = "uint8")
    mask = cv2.inRange(img, lower2, upper2)
    output2 = cv2.bitwise_and(img, img, mask=mask)

for (lower3, upper3) in rust3:
    lower3 = np.array(lower3, dtype = "uint8")
    upper3 = np.array(upper3, dtype = "uint8")
    mask = cv2.inRange(img, lower3, upper3)
    output3 = cv2.bitwise_and(img, img, mask=mask)

for (lower4, upper4) in rust4:
    lower4 = np.array(lower4, dtype = "uint8")
    upper4 = np.array(upper4, dtype = "uint8")
    mask = cv2.inRange(img, lower4, upper4)
    output4 = cv2.bitwise_and(img, img, mask=mask)

for (lower5, upper5) in rust5:
    lower5 = np.array(lower5, dtype = "uint8")
    upper5 = np.array(upper5, dtype = "uint8")
    mask = cv2.inRange(img, lower5, upper5)
    output5 = cv2.bitwise_and(img, img, mask=mask)

for (lower6, upper6) in rust6:
    lower6 = np.array(lower6, dtype = "uint8")
    upper6 = np.array(upper6, dtype = "uint8")
    mask = cv2.inRange(img, lower6, upper6)
    output6 = cv2.bitwise_and(img, img, mask=mask)

#Combine the 3 different masks with the different shades into 1 image file
final = cv2.bitwise_or(output1, output2)
final = cv2.bitwise_or(final, output3)
final = cv2.bitwise_or(final, output4)
final = cv2.bitwise_or(final, output5)
final = cv2.bitwise_or(final, output6)

# Limitar a largura da imagem a 1280,
# mas manter a largura se a original for menor que 1280
max_width = 1280
if width > max_width:
    n_width = max_width
else:
    n_width = width

# Imagem original
img = imutils.resize(img, width=n_width)
cv2.imshow("original", img)
# Imagem que indica onde há ferrugem
final = imutils.resize(final, width=n_width)
cv2.imshow("final", final)

cv2.waitKey(0)
