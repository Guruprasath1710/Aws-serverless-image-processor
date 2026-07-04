from app.processor import ImageProcessor
from PIL import Image
import os

processor = ImageProcessor()

INPUT_IMAGE = "image/sample.jpg"


def test_resize_image():
    output_path = "output/test_resize.jpg"

    processor.resize_image(
        INPUT_IMAGE,
        output_path,
        300,
        300
    )

    assert os.path.exists(output_path)

    image = Image.open(output_path)
    assert image.size == (300, 300)


def test_grayscale_image():
    output_path = "output/test_grayscale.jpg"

    processor.grayscale_image(
        INPUT_IMAGE,
        output_path
    )

    assert os.path.exists(output_path)

    image = Image.open(output_path)
    assert image.mode == "L"


def test_rotate_image():
    output_path = "output/test_rotate.jpg"

    processor.rotate_image(
        INPUT_IMAGE,
        output_path,
        90
    )

    assert os.path.exists(output_path)

    image = Image.open(output_path)
    assert image.width > 0
    assert image.height > 0


def test_compress_image():
    output_path = "output/test_compress.jpg"

    processor.compress_image(
        INPUT_IMAGE,
        output_path,
        60
    )

    assert os.path.exists(output_path)

    original_size = os.path.getsize(INPUT_IMAGE)
    compressed_size = os.path.getsize(output_path)

    assert compressed_size < original_size