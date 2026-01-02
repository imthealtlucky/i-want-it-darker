from PIL import Image, ImageEnhance
import PIL
import os

imagealist = "C:\\Users\\Moi\\Desktop\\cool python image shit\\image"



print("Images in directory:", os.listdir(imagealist))

cHosenfile = input("Enter the name of the image file (with extension): ")



for filename in os.listdir(imagealist):
    if filename == cHosenfile:
        img_path = os.path.join(imagealist, filename)
        print("Selected image path:", img_path)
        break


    
img_path = os.path.join(imagealist, cHosenfile)
    
def is_valid_threshold():
    
    while True:
        question = input("Enter darkening threshold (0-255): ")
        try:
            question = int(question)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        if -1 < question < 255:
            return question
        else:
            print("Invalid threshold. Please enter a value between 0 and 255.")



def is_valid_saturation():
    
    while True:
        question = input("Enter saturation value (0-10): ")
        try:
            question = int(question)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        if -1 < question < 10:
            return question
        else:
            print("Invalid threshold. Please enter a value between 0 and 10.")

darkene = is_valid_threshold()
saturation = is_valid_saturation()

img = Image.open(img_path)
img.show()

print("Image format:", img.format)
print("Image size:", img.size)

px = img.load()
print("Pixel data at (0,0):", px[0, 0])

# Ensure image is in RGB mode
if img.mode != "RGB":
    img = img.convert("RGB")
    px = img.load()
if darkene > 0:
    print("loading... (this may take a while depending on image size)")
    for x in range(img.width):
        for y in range(img.height):
            if px[x, y] < (darkene, darkene, darkene):
                px[x, y] = (0, 0, 0)



        
img = ImageEnhance.Color(img).enhance(saturation)
# Show and save the modified image
img.show()
img.filter

img.save("black_image.png")
print("Modified image saved as black_image.png")
