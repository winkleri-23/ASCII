from PIL import Image

# ASCII characters used to represent pixel intensity
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """Resize image while maintaining aspect ratio."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  # Adjust for font height
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale(image):
    """Convert image to grayscale."""
    return image.convert("L")

def map_pixels_to_ascii(image, ascii_chars):
    """Map pixels to ASCII characters."""
    pixels = image.getdata()
    ascii_str = ''.join([ascii_chars[pixel // 25] for pixel in pixels])  # 0-255 mapped to 0-10
    return ascii_str

def generate_ascii_art(image_path, new_width=100):
    """Convert an image to ASCII art."""
    try:
        # Load and process the image
        image = Image.open(image_path)
        image = resize_image(image, new_width)
        image = grayscale(image)
        
        # Convert to ASCII
        ascii_str = map_pixels_to_ascii(image, ASCII_CHARS)
        img_width = image.width
        ascii_art = "\n".join([ascii_str[i:(i + img_width)] for i in range(0, len(ascii_str), img_width)])
        return ascii_art
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # User input for the image file and width
    input_path = input("Enter the path to the image: ").strip()
    width = int(input("Enter the desired width of ASCII art (e.g., 100): ").strip())

    # Generate ASCII art
    ascii_art = generate_ascii_art(input_path, width)
    
    # Display and save ASCII art
    print("\nGenerated ASCII Art:\n")
    print(ascii_art)
    
    with open("ascii_art.txt", "w") as f:
        f.write(ascii_art)
        print("\nASCII art saved to ascii_art.txt")
