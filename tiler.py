from PIL import Image
import os
import glob

def pad_image_to_tile_height(image, tile_height=1024):
    image_width, image_height = image.size
    if image_height != tile_height:
        padded_image = Image.new("RGBA", (image_width, tile_height), (0, 0, 0, 0))
        padded_image.paste(image, (0, 0))
        padding_info = {
            "top": 0,
            "bottom": tile_height - image_height
        }
        return padded_image, padding_info
    else:
        return image, {"top": 0, "bottom": 0}

def split_image(image, output_folder, tile_size, image_name, log_file):
    image_width, image_height = image.size

    for y in range(0, image_height, tile_size):
        for x in range(0, image_width, tile_size):
            box = (x, y, x + tile_size, y + tile_size)
            tile = image.crop(box)

            tile_filename = os.path.join(output_folder, f'{image_name}_tile_{x}_{y}.png')
            tile.save(tile_filename)
            log_file.write(f'{image_name}_tile_{x}_{y}.png: position=({x}, {y})\n')

def process_images(input_folder, output_folder, tile_size=1024):
    os.makedirs(output_folder, exist_ok=True)
    log_file_path = os.path.join(output_folder, 'log.txt')

    with open(log_file_path, 'w') as log_file:
        for image_path in glob.glob(os.path.join(input_folder, "layer*.png")):
            image = Image.open(image_path)
            image_width, image_height = image.size

            # Pad vertically to ensure height is 1024
            padded_image, padding_info = pad_image_to_tile_height(image, tile_size)
            log_file.write(f'{os.path.basename(image_path)}: padded to ({image_width}, {tile_size}) '
                           f'with vertical padding (top: {padding_info["top"]}, bottom: {padding_info["bottom"]})\n')

            # Split the image into tiles
            image_name = os.path.splitext(os.path.basename(image_path))[0]
            split_image(padded_image, output_folder, tile_size, image_name, log_file)

    print(f"Processing complete. Log file created at {log_file_path}")

# Example usage
input_folder = 'C:\\XAMPP\\htdocs\\Phaser\\l15'  # Replace with your input folder path
output_folder = 'C:\\XAMPP\\htdocs\\Phaser\\l15'  # Replace with your output folder path
process_images(input_folder, output_folder)
