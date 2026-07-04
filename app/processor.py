from PIL import Image

class ImageProcessor:

    def resize_image(self, input_path, output_path, width, height):
        image = Image.open(input_path)
        image = image.resize((width, height))
        image.save(output_path)

    def grayscale_image(self, input_path, output_path):
        image = Image.open(input_path)
        gray = image.convert("L")
        gray.save(output_path)

    def rotate_image(self, input_path, output_path, angle):
        image = Image.open(input_path)
        rotated = image.rotate(angle, expand=True)
        rotated.save(output_path)

    def compress_image(self, input_path, output_path, quality):
        if quality < 1 or quality > 100:
            raise ValueError("Quality must be between 1 and 100")

        image = Image.open(input_path)
        image.save(output_path, optimize=True, quality=quality)