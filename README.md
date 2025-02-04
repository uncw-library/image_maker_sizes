# Image Maker Sizes

This Python script generates images of various dimensions with the dimensions written in the center of each image. The generated images are saved in the `output` directory.

Useful when testing how an image appears on a display.

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Create a virtual environment:

    ```sh
    python -m venv image_maker_sizes
    ```

3. Activate the virtual environment:

- On macOS and Linux:
    ```sh
    source venv/bin/activate
    ```

- On Windows:
    ```sh
    .\venv\Scripts\activate
    ```

4. Install the Pillow library using pip:

    ```sh
    pip install pillow
    ```

## Usage
Save the script as image_maker_sizes.py.
Run the script using the following command:

```sh
python image_maker_sizes.py
```

## Output
The script will generate images with the following dimensions:

- 100 x 100
- 200 x 150
- 300 x 200
- 400 x 300
- 500 x 400

The generated images will be saved in the output directory with filenames in the format 
"image_{WIDTH}x{HEIGHT}.jpg".

## Example
After running the script, you will find the generated images in the "output" directory:

    output/
    ├── image_100x100.jpg
    ├── image_200x150.jpg
    ├── image_300x200.jpg
    ├── image_400x300.jpg
    └── image_500x400.jpg