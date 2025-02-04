from PIL import Image, ImageDraw, ImageFont
import os

# List of dimensions for the images
dimensions = [(100, 100), (200, 150), (300, 200), (400, 300), (500, 400)]

# Loop through each dimension and create an image
for width, height in dimensions:
    # Create a new image with black background
    image = Image.new("RGB", (width, height), color="black")

    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # Define the text to be written on the image
    text = f"{width} x {height}"

    # Load a font
    font = ImageFont.load_default()

    # Calculate the bounding box of the text to be drawn
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Calculate X, Y position of the text
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Add text to image
    draw.text((x, y), text, fill="white", font=font)

    # Save the image
    os.makedirs("output", exist_ok=True)
    image.save(os.path.join("output", f"image_{width}x{height}.jpg"))

print("Images have been generated.")
