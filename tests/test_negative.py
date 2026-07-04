from app.processor import ImageProcessor
import pytest

processor = ImageProcessor()


def test_resize_image_file_not_found():
    with pytest.raises(FileNotFoundError):
        processor.resize_image(
            "image/not_found.jpg",
            "output/error.jpg",
            300,
            300
        )


def test_grayscale_image_file_not_found():
    with pytest.raises(FileNotFoundError):
        processor.grayscale_image(
            "image/not_found.jpg",
            "output/error.jpg"
        )


def test_rotate_image_file_not_found():
    with pytest.raises(FileNotFoundError):
        processor.rotate_image(
            "image/not_found.jpg",
            "output/error.jpg",
            90
        )


def test_compress_image_file_not_found():
    with pytest.raises(FileNotFoundError):
        processor.compress_image(
            "image/not_found.jpg",
            "output/error.jpg",
            60
        )