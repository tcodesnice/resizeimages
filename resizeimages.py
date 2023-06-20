#make it so it takes a file path to the photo as an input
#add function that resizes to 320x320
#add an option to resize the photo to 688x459, 320x320 or both

from PIL import Image

def crop_and_resize_image(input_image_path, output_image_path, target_width, target_height):
    # Open the input image
    image = Image.open(input_image_path)

    # Calculate the aspect ratio of the input image
    aspect_ratio = image.width / image.height

    # Calculate the proportional width and height for cropping
    if aspect_ratio > target_width / target_height:
        crop_width = target_width
        crop_height = int(target_width / aspect_ratio)
    else:
        crop_width = int(target_height * aspect_ratio)
        crop_height = target_height

    # Calculate the coordinates for cropping
    left = (image.width - crop_width) // 2
    top = (image.height - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height

    # Crop the image
    cropped_image = image.crop((left, top, right, bottom))

    # Resize the cropped image
    resized_image = cropped_image.resize((target_width, target_height), Image.ANTIALIAS)

    # Save the resized image
    resized_image.save(output_image_path)

# Provide the input and output image paths
input_image_path = 'input.jpg'
output_image_path = 'output.jpg'

# Set the target dimensions for cropping and resizing
target_width = 688
target_height = 459

# Call the function to perform cropping and resizing
crop_and_resize_image(input_image_path, output_image_path, target_width, target_height)

#add more to above function