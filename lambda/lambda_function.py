from app.processor import ImageProcessor
from app.validator import ImageValidator
from app.logger import logger
from app.config import *

def main():

    validator = ImageValidator()

    if not validator.validate(INPUT_IMAGE):
        logger.error("Invalid Image")
        return

    processor = ImageProcessor()

    processor.resize_image(
        INPUT_IMAGE,
        OUTPUT_RESIZE,
        WIDTH,
        HEIGHT
    )

    processor.grayscale_image(
        INPUT_IMAGE,
        OUTPUT_GRAY
    )

    processor.rotate_image(
        INPUT_IMAGE,
        OUTPUT_ROTATE,
        ROTATE_ANGLE
    )

    processor.compress_image(
        INPUT_IMAGE,
        OUTPUT_COMPRESS,
        JPEG_QUALITY
    )

    logger.info("All image operations completed successfully!")

if __name__ == "__main__":
    main()