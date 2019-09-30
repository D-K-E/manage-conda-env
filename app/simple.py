# author: Kaan Eraslan
# purpose: simple application for displaying image

from PIL import Image

if __name__ == "__main__":
    img = Image.open("mexica.jpg")
    img.resize((640, 480)).show()
