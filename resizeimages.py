##6/22/23 1:19PM 
##reverting back to this branch because sharpening fucked it up
##version sharpening function is in Attempt2sharpening branch


import os
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
    canvas = Image.new('RGB', (new_width, new_height), (255, 255, 255))

    # Calculate the center position to paste the resized image on the canvas
    paste_x = (new_width - resized_image.width) // 2
    paste_y = (new_height - resized_image.height) // 2

    # Paste the resized image onto the canvas
    canvas.paste(resized_image, (paste_x, paste_y))

    final_image = canvas.resize((target_width, target_height), Image.LANCZOS)

    # Save the final resized image
    final_image.save(output_image_path)


def square_resize_image(input_image_path, output_image_path, target_size):
    image = Image.open(input_image_path)
    width, height = image.size
    
    # Calculate the new dimensions while maintaining the aspect ratio
    if width > height:
        new_width = height
        new_height = height
    else:
        new_width = width
        new_height = width
    
    # Calculate the coordinates to crop the image
    left = (width - new_width) // 2
    top = (height - new_height) // 2
    right = left + new_width
    bottom = top + new_height
    
    # Crop the image to a square
    cropped_image = image.crop((left, top, right, bottom))
    
    # Resize the cropped image to the target size
    resized_image = cropped_image.resize((target_size, target_size), Image.BICUBIC) #Image.LANCZOS
    
    # Save the final resized image
    resized_image.save(output_image_path)


# Provide the input and output image paths
input_folder_path = input('Enter the file path: ')
output_folder_path = '/Users/tomascontreras/Desktop/resizedimages'
input_size = input('do you want this image to be 320x320, 688x459 or both?: ')

# Set the target size for resizing (in pixels)
target_size = 320
notsquare_target_width = 688
notsquare_target_height = 459

# Create the output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

for filename in os.listdir(input_folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):  # Add more file extensions if needed
        input_image_path = os.path.join(input_folder_path, filename)
        
        # Create the corresponding output file paths
        output_image_path_square = os.path.join(output_folder_path, '320_' + os.path.basename(filename))
        output_image_path_notsquare = os.path.join(output_folder_path, '688_' + os.path.basename(filename))

        # Call the function to resize the image to the user-specified size
        if input_size in ['320', 'both']:
            square_resize_image(input_image_path, output_image_path_square, target_size)

        # Call the function to resize the image 688x459 if desired
        if input_size in ['688', 'both']:
            resize_image(input_image_path, output_image_path_notsquare, notsquare_target_width, notsquare_target_height)



###old language below - just creates two new images based on file path. Redid code above to create a new folder with both or just one pixel density

# # Call the function to resize the image 688x320
# if input_size == '688':
#     resize_image(input_image_path, output_image_path, notsquare_target_width, notsquare_target_height)
# # Call the function to resize the image 320x320
# elif input_size == '320':
#     square_resize_image(input_image_path, output_image_pathsquare, target_size)
# else:
#     resize_image(input_image_path, output_image_path, notsquare_target_width, notsquare_target_height)
#     square_resize_image(input_image_path, output_image_pathsquare, target_size)