from PIL import Image
from pathlib import Path

def convert_to_webp(input_path, quality=100):
    input_path = Path(input_path)

    with Image.open(input_path) as img:
        output_path = input_path.with_suffix(".webp")
        img.save(output_path, "WEBP", quality=quality)

    print(f"Converti : {output_path}")

# Exemple
convert_to_webp("/home/yacine/Bureau/test/pexels-jan-van-der-wolf-11680885-15367720.jpg")