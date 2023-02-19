import os
from PIL import Image
import time

directory = '/Users/rakib/OneDrive/Desktop/Optoshi/12 Feet/contrast'

while True:
    # Get a sorted list of JPEG image filenames in the directory
    filenames = sorted([f for f in os.listdir(directory) if f.endswith('.jpg')])
    print(type(filenames))
    
    # Loop through the sorted list of filenames
    for filename in filenames:
        # Open the image and show it
        image = Image.open(os.path.join(directory, filename))
        image.show()
        # Pause for 3 seconds before showing the next image
        time.sleep(3)
