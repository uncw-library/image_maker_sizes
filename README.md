# Image Maker Sizes

This Python script generates images of various dimensions with the dimensions written in the center of each image. The generated images are saved in the "output" directory.

Useful when testing how an image appears on a display.

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Create a virtual environment:

    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

- On macOS and Linux:
    ```sh
    source venv/bin/activate
    ```

- On Windows:
    ```sh
    .\venv\Scripts\activate

    (or Git Bash)
     
    ./venv/Scripts/activate

    ```

4. Install the dependencies using pip:

    ```sh
    pip install -r requirements.txt
    ```

## Usage
Save the script as image_maker_sizes.py.
Run the script using the following command:

```sh
python image_maker_sizes.py {width} {height}

(or)

python image_maker_sizes.py -h       **for help message**
```

## Output
The generated images will be saved in the "output" directory with filenames in the format 
"image_{WIDTH}x{HEIGHT}.jpg".
