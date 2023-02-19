import os
from PIL import Image
import time
directory = '/Users/rakib/OneDrive/Desktop/Optoshi/12 Feet/contrast'
while True:
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            image = Image.open(directory + '/' + filename) 
            image.show()
            time.sleep(3)