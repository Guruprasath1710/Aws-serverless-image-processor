from app.processor import ImageProcessor
import pytest

processor = ImageProcessor()

INPUT_IMAGE = "image/sample.jpg"


def test_resize_zero_width():
    with pytest.raises(Exception):
        processor.resize_image(
            INPUT_IMAGE,
            "output/zero_width.jpg",
            0,
            300
        )


def test_resize_zero_height():
    with pytest.raises(Exception):
        processor.resize_image(
            INPUT_IMAGE,
            "output/zero_height.jpg",
            300,
            0
        )


def test_resize_negative_width():
    with pytest.raises(Exception):
        processor.resize_image(
            INPUT_IMAGE,
            "output/negative_width.jpg",
            -100,
            300
        )


def test_resize_negative_height():
    with pytest.raises(Exception):
        processor.resize_image(
            INPUT_IMAGE,
            "output/negative_height.jpg",
            300,
            -100
        )


def test_rotate_invalid_angle():
    with pytest.raises(Exception):
        processor.rotate_image(
            INPUT_IMAGE,
            "output/invalid_angle.jpg",
            "hello"
        )


def test_compress_invalid_quality_high():
    with pytest.raises(Exception):
        processor.compress_image(
            INPUT_IMAGE,
            "output/high_quality.jpg",
            150
        )


def test_compress_invalid_quality_low():
    with pytest.raises(Exception):
        processor.compress_image(
            INPUT_IMAGE,
            "output/low_quality.jpg",
            -5
        )