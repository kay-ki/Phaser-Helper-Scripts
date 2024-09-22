import os
from PIL import Image

def convert_png_to_webp(folder_path, quality=50):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.png'):
                png_path = os.path.join(root, file)
                webp_path = os.path.splitext(png_path)[0] + '.webp'
                
                try:
                    with Image.open(png_path) as img:
                        img.save(webp_path, 'webp', quality=quality)
                    os.remove(png_path)
                    print(f"Converted and removed {png_path}")
                except Exception as e:
                    print(f"Error converting {png_path}: {e}")

# Replace 'your_folder_path' with the path to your folder
convert_png_to_webp('C:\\XAMPP\\htdocs\\Phaser\\l15')