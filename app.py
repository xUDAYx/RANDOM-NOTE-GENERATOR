import os
import random
import cv2
import gradio as gr
from PIL import Image
import numpy as np

def generate_and_delete_word_image(word):
    """Generates a combined image, displays it, and deletes it afterward.

    Args:
        word: The user-provided word (uppercase).

    Returns:
        The image data for displaying.
    """

    dataset_path = "C:\DYPIU\___________________CODE___________________\Random Word Genrator\dataset"  # Adjust for your dataset path
    sample = "C:\DYPIU\___________________CODE___________________\Random Word Genrator\dataset\samples.jpg"
    resized_images = []
    for letter in word:
        letter_folder_path = os.path.join(dataset_path, letter)

        # Check if the folder exists
        if not os.path.isdir(letter_folder_path):
            print("Folder not found for the letter:", letter)
            continue

        images_in_folder = [img for img in os.listdir(letter_folder_path)
                            if img.endswith(".jpg") or img.endswith(".png")]

        if not images_in_folder:
            print("No images found for the letter:", letter)
            continue

        # Randomly select an image from the folder
        random_image_name = random.choice(images_in_folder)
        image_path = os.path.join(letter_folder_path, random_image_name)

        try:
            # Load image using PIL, ensuring RGB mode
            image = Image.open(image_path).convert("RGB")
            # Convert to NumPy array for OpenCV
            resized_image = np.array(image.resize((250, 250)))
        except Exception as e:
            print(f"Error loading image: {e}")
            continue

        resized_images.append(resized_image)

    if not resized_images:
        print("No images found for the input word.")
        return None

    sample_img = sample
    concatenated_image = cv2.hconcat(resized_images)

    # Display the concatenated image
    # cv2.imshow("Concatenated Image", concatenated_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Return the image data
    return concatenated_image

# Gradio interface with clear explanations
interface = gr.Interface(
    fn=generate_and_delete_word_image,
    inputs="text",  # User input for the word
    outputs="image",  # Output as an image
    title="POCKET RANDOM NOTE GENERATOR", # Title
    description="Randsomator allows you to generate random ranson with one click.",
    
    css="""
      botton {
      background: green;
      color: #32B531
      }
      body {
        background-color: black;
        font-family: Arial, sans-serif;
      }
      .gr-interactive-component h1 {
        font-size: 20px;
        margin-bottom: 10px;
      }
    """,
    
)


interface.launch(share=True)  # Launch the Gradio interface and share it publicly
