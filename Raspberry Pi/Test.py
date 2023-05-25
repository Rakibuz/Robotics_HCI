import os
from PIL import Image
import time

directory = '/Users/rakib/OneDrive/Desktop/Optoshi/12 Feet/contrast'


def get_files_in_directory(directory):
        return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

print(get_files_in_directory(directory))
