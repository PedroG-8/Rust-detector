#
# Deteção de corrosão em superfícies metálicas
#
# 88859 - Pedro Gonçalves
# 89228 - Pedro Silva
#
# Referências
# https://answers.opencv.org/question/178394/detection-of-rust-with-opencv-python/?fbclid=IwAR1Lztp2SBI73kiGvkekMHdWPXO16HbhvNjWfhdgQh7T5gCs1v2mXA8Bp_Q
#

import cv2
import imutils
import numpy as np

# Ver no_3, no_5 e no_7
# Ver 1, 3, 4, 5, 11, 21
# Melhores 7, 8, 10, 12, 13, 14, 16, 17, 18, 20, 22
img = cv2.imread('imgs/no_1.jpg', 1)
height, width, channels = img.shape

# Diferentes cores de ferrugem
# rust = [(min[B, G, R], max[B, G, R])]

# Low Red
rust1 = [([30, 30, 60], [50, 40, 70])]
rust2 = [([25, 30, 70], [40, 45, 80])]
rust3 = [([40, 60, 90], [60, 65, 110])]
# Mid Red
rust4 = [([70, 57, 115], [83, 90, 130])]
rust5 = [([80, 100, 145], [90, 110, 180])]
rust6 = [([35, 65, 115], [45, 90, 145])]
rust7 = [([20, 45, 140], [40, 65, 165])]
rust8 = [([40, 85, 170], [50, 100, 185])]
rust9 = [([5, 25, 115], [25, 45, 130])]
# High Red
rust10 = [([95, 125, 200], [100, 140, 205])]
rust11 = [([115, 150, 220], [120, 160, 225])]

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

for (lower7, upper7) in rust7:
    lower7 = np.array(lower7, dtype = "uint8")
    upper7 = np.array(upper7, dtype = "uint8")
    mask = cv2.inRange(img, lower7, upper7)
    output7 = cv2.bitwise_and(img, img, mask=mask)

for (lower8, upper8) in rust8:
    lower8 = np.array(lower8, dtype = "uint8")
    upper8 = np.array(upper8, dtype = "uint8")
    mask = cv2.inRange(img, lower8, upper8)
    output8 = cv2.bitwise_and(img, img, mask=mask)

for (lower9, upper9) in rust9:
    lower9 = np.array(lower9, dtype = "uint8")
    upper9 = np.array(upper9, dtype = "uint8")
    mask = cv2.inRange(img, lower9, upper9)
    output9 = cv2.bitwise_and(img, img, mask=mask)

for (lower10, upper10) in rust10:
    lower10 = np.array(lower10, dtype = "uint8")
    upper10 = np.array(upper10, dtype = "uint8")
    mask = cv2.inRange(img, lower10, upper10)
    output10 = cv2.bitwise_and(img, img, mask=mask)

# Combinar os diferentes tipos de ferugem num ficheiro só
final = cv2.bitwise_or(output1, output2)
final = cv2.bitwise_or(final, output3)
final = cv2.bitwise_or(final, output4)
final = cv2.bitwise_or(final, output5)
final = cv2.bitwise_or(final, output6)
final = cv2.bitwise_or(final, output7)
final = cv2.bitwise_or(final, output8)
final = cv2.bitwise_or(final, output9)
final = cv2.bitwise_or(final, output10)

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
