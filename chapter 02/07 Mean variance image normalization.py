import cv2
import numpy as np

image = cv2.imread('../data/Lena.png').astype(np.float32) / 255

image -= image.mean()
image /= image.std()