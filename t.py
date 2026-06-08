from PIL import Image

image = Image.open("/home/yacine/Bureau/test/pexels-jan-van-der-wolf-11680885-15367720.webp")

new_width = 800

ratio = new_width / image.width
new_height = int(image.height * ratio)

image_resized = image.resize((new_width, new_height))

image_resized.save("image_resize.webp")