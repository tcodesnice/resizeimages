from PIL import Image

def resize_image(input_image_path, output_image_path, target_width, target_height):
    # Open the input image
    image = Image.open(input_image_path)

    # Calculate the aspect ratio of the input image
    aspect_ratio = image.width / image.height

    # Calculate the new dimensions while maintaining the aspect ratio
    if aspect_ratio > target_width / target_height:
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    else:
        new_width = int(target_height * aspect_ratio)
        new_height = target_height

    # Resize the image while maintaining the aspect ratio
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)

    # Create a new blank canvas of the target size
    canvas = Image.new('RGB', (target_width, target_height), (255, 255, 255))

    # Calculate the center position to paste the resized image on the canvas
    paste_x = (target_width - new_width) // 2
    paste_y = (target_height - new_height) // 2

    # Paste the resized image onto the canvas
    canvas.paste(resized_image, (paste_x, paste_y))

    # Save the final resized image
    canvas.save(output_image_path)

# Provide the input and output image paths
input_image_path = 'input.jpg'
output_image_path = 'output.jpg'

# Set the target dimensions for resizing
target_width = 688
target_height = 459

# Call the function to resize the image
resize_image(input_image_path, output_image_path, target_width, target_height)