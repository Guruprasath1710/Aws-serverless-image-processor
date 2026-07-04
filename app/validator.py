from PIL import Image

class ImageValidator:

    def validate(self, image_path):
        try:
            with Image.open(image_path) as img:
                img.verify()
            return True
        except Exception:
            return False