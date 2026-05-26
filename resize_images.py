from PIL import Image

def resize_image(file_path, width, height):
    # Open image
    img = Image.open(file_path)

    # Resize image
    resized_img = img.resize((width, height), Image.LANCZOS)

    # Save back to the same file path
    resized_img.save(file_path)

    print(f"Image resized and saved at: {file_path}")


# Example usage
resize_image(r"C:\Users\97433\Portfolio\src\png\stryker.png",
            2975, 2996)