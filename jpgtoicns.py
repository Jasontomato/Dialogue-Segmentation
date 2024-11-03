import os
from PIL import Image

# Paths to input and output files
input_image_path = "./scissors.jpg"   # Replace with your JPG file
output_icns_path = "output_icon.icns" # Replace with desired output file

def create_iconset(input_image_path, output_icns_path):
    # Standard macOS icon sizes
    icon_sizes = [
        (16, "icon_16x16"),
        (32, "icon_16x16@2x"),
        (32, "icon_32x32"),
        (64, "icon_32x32@2x"),
        (128, "icon_128x128"),
        (256, "icon_128x128@2x"),
        (256, "icon_256x256"),
        (512, "icon_256x256@2x"),
        (512, "icon_512x512"),
        (1024, "icon_512x512@2x")
    ]

    # Create the .iconset folder
    iconset_folder = "temp.iconset"
    if not os.path.exists(iconset_folder):
        os.makedirs(iconset_folder)

    # Open the input image
    with Image.open(input_image_path) as img:
        for size, filename in icon_sizes:
            img_resized = img.resize((size, size), Image.LANCZOS)
            img_resized.save(os.path.join(iconset_folder, f"{filename}.png"))

    # Use iconutil to convert to .icns
    os.system(f"iconutil -c icns {iconset_folder} -o {output_icns_path}")

    # Clean up temporary .iconset folder
    for file in os.listdir(iconset_folder):
        os.remove(os.path.join(iconset_folder, file))
    os.rmdir(iconset_folder)

    print(f"Conversion complete. Saved as {output_icns_path}")

# Call the function directly
create_iconset(input_image_path, output_icns_path)
