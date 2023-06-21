#make it so it takes a file path to the photo as an input
#add function that resizes to 320x320
#add an option to resize the photo to 688x459, 320x320 or both

## updated as of 6/20 342pm
##code intakes file path and outputs two photos, 320x320 and 688x459
##BUT the square photo is coming out no nicely cropped and is pixelated 


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
    resized_image = cropped_image.resize((target_size, target_size), Image.LANCZOS)
    
    # Save the final resized image
    resized_image.save(output_image_path)


# Provide the input and output image paths
input_image_path = input('Enter the file path: ')
output_image_pathsquare = '/Users/tomascontreras/Desktop/320output.jpg'
output_image_path = '/Users/tomascontreras/Desktop/688output.jpg'
input_size = input('do you want this image to be 320x320, 688x459 or both?: ')

# Set the target size for resizing (in pixels)
target_size = 320

# Set the target dimensions for resizing
notsquare_target_width = 688
notsquare_target_height = 459


# Call the function to resize the image 688x320
if input_size == '688':
    resize_image(input_image_path, output_image_path, notsquare_target_width, notsquare_target_height)
# Call the function to resize the image 320x320
elif input_size == 320:
    square_resize_image(input_image_path, output_image_pathsquare, target_size)
else:
    resize_image(input_image_path, output_image_path, notsquare_target_width, notsquare_target_height)
    square_resize_image(input_image_path, output_image_pathsquare, target_size)