import argparse
import os

from PIL import Image, ImageDraw, ImageFont


def main(width, height):
    text = f"{width} x {height}"

    # Create a new image with blue background
    image = Image.new("RGB", (width, height), color="blue")
    draw = ImageDraw.Draw(image)
    font_size = min(width, height)
    font_path = os.path.join("fonts", "ttf", "Hack-Bold.ttf")
    font = ImageFont.truetype(font_path, font_size)

    # Calculate the bounding box of the text to be drawn
    while True:
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        if text_width <= width and text_height <= height:
            break
        font_size -= 1
        font = ImageFont.truetype(font_path, font_size)

    # Calculate X, Y position of the text
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Add text to image
    draw.text((x, y), text, fill="white", font=font)

    # Save the image
    os.makedirs("output", exist_ok=True)
    image.save(os.path.join("output", f"image_{width}x{height}.jpg"))

    print("Images have been generated.")

def parse_args():
    parser = argparse.ArgumentParser(description='Generate images of various dimensions.')
    parser.add_argument('width', type=int, help='Width of the image')
    parser.add_argument('height', type=int, help='Height of the image')
    args = parser.parse_args()

    width = args.width
    height = args.height
    return width, height

if __name__ == "__main__":
    width, height = parse_args()
    main(width, height)