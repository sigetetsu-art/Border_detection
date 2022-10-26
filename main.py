from inspect import BoundArguments
import numpy as np
from PIL import Image
import sys

def mirror_padding(image, PADDING_SIZE):
    image_pixels = np.array(image)
    padding_image = np.pad(image_pixels, ((PADDING_SIZE, PADDING_SIZE), (PADDING_SIZE, PADDING_SIZE)), "edge")
    return padding_image

def Border_detection(degraded_image):
    h, w = degraded_image.shape
    binary_image = np.zeros(degraded_image.shape)
    
    for i in range(h):
        for j in range(w):
            if(i % 7 == 0 or j % 7 == 0):
                binary_image[i][j] = 255
    return binary_image

def main():
    param = sys.argv
    
    original_image = Image.open(param[1])
    original_image = np.array(original_image, dtype = "float64")
    degraded_image = Image.open(param[2])
    degraded_image = np.array(degraded_image, dtype = "float64")

    binary_image = Border_detection(degraded_image)
    binary_image = Image.fromarray(binary_image.astype("uint8"))
    binary_image.save("binary.jpg")
    binary_image.show()
    
    
if __name__ == "__main__":
    main()
