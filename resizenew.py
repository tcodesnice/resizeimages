from PIL import Image
import os

def resize_images(folder_path):
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Get the full file path
        file_path = os.path.join(folder_path, filename)

        # Check if the file is a .jpeg image
        if os.path.isfile(file_path) and filename.lower().endswith('.jpeg'):
            # Open the image file
            image = Image.open(file_path)

            # Calculate the aspect ratio
            aspect_ratio = image.width / image.height

            # Determine the new width and height
            if aspect_ratio > 688 / 459:
                new_width = 688
                new_height = int(688 / aspect_ratio)
            else:
                new_width = int(459 * aspect_ratio)
                new_height = 459

            # Resize the image while maintaining aspect ratio
            resized_image = image.resize((new_width, new_height))

            # Create a blank white canvas with the target size
            canvas = Image.new('RGB', (688, 459), (255, 255, 255))

            # Calculate the position to paste the resized image
            x_offset = (688 - new_width) // 2
            y_offset = (459 - new_height) // 2

            # Paste the resized image onto the canvas
            canvas.paste(resized_image, (x_offset, y_offset))

            # Get the output file path by replacing the file extension with .png
            output_file_path = os.path.splitext(file_path)[0] + '.png'

            # Save the resized image as a .png file
            canvas.save(output_file_path, format="PNG")

            print(f"Resized {filename} and saved as {output_file_path}")

# Provide the folder path as input
folder_path = input("Enter the folder path: ")

# Call the function to resize the images
resize_images(folder_path)
