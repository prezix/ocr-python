import easyocr


def recognize_text(image_path):
    """
    Function to recognize text from an image using EasyOCR.
    Args:
        image_path (str): Path to the image file.
    Returns:
        str: Recognized text from the image.
    """
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])  # Specify language(s) for text recognition

    # Read text from the image
    result = reader.readtext(image_path)

    # Extract text from the result
    text = ' '.join([text_result[1] for text_result in result])

    return text


def save_text_to_file(text, output_file):
    """
    Function to save recognized text to a text file.
    Args:
        text (str): Recognized text to be saved.
        output_file (str): Path to the output text file.
    """
    with open(output_file, 'w') as file:
        file.write(text)


def main():
    image_path = "g6DFDCAxu-8.jpg"  # Path to your image
    output_file = "recognized_text.txt"  # Path to the output text file

    # Recognize text from the image
    recognized_text = recognize_text(image_path)

    # Save recognized text to a text file
    save_text_to_file(recognized_text, output_file)

    print("Text recognition completed. Result saved to:", output_file)


if __name__ == "__main__":
    main()
