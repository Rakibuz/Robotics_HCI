import os
from PIL import Image

class ImageLoader:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.image_names = [name for name in os.listdir(folder_path) if name.endswith(".jpg") or name.endswith(".jpeg") or name.endswith(".png")]

    def open_image(self, index):
        try:
            image_name = self.image_names[index]
            image_path = os.path.join(self.folder_path, image_name)
            image = Image.open(image_path)
            return image
        except Exception as e:
            print(f"Error: {e}")

# create an instance of the ImageLoader class
image_loader = ImageLoader("C:/Users/rakib/OneDrive/Desktop/Pi Zero/cdr-dbus-ssh")

# open the first image from the folder
image = image_loader.open_image(0)

# show the image
image.show()