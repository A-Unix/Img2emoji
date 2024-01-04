#!/usr/bin/python3

from PIL import Image
import sys
import os
import subprocess
import time

print("Checking if Colorama has been installed already or not!")

time.sleep(2)

# Check if Colorama has been already installed or not
try:
    from colorama import init, Fore
    print(Fore.LIGHTBLUE_EX + "Colorama has been already installed, We have initialized it for you :)")
except ImportError:
    print(Fore.RED + "Colorama has not been installed. Installing it...")
    subprocess.run(["pip", "install", "colorama"], check=True)
    from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Check if emoji has been already installed or not
try:
    import emoji
except ImportError:
    print(Fore.LIGHTRED_EX+ "Emoji not found! Installing it...")
    subprocess.run(["pip", "install", "emoji"], check=True)
    import emoji

# Clear the terminal screen
os.system("clear")
time.sleep(1)

# Get the terminal size
rows, columns = os.popen('stty size', 'r').read().split()

# Calculate the center position
center_row = int(rows) // 2
center_column = int(columns) // 2

# Set the font size
font_size = 6

# Print an empty line for top margin
print()

# Print empty lines for top margin
for _ in range(center_row - font_size):
    print()

# Print the welcome message at the center with bigger font size
print(" " * center_column + Fore.LIGHTMAGENTA_EX + "Welcome\n".center(font_size * 2))

# Print empty lines for bottom margin
for _ in range(center_row - font_size):
    print()

time.sleep(2)

# Create a function to prompt the path of the image file which user wants to convert into an emoji
def input_path():
    return input(Fore.LIGHTBLUE_EX + "Enter the path of the image file e.g., /path/to/image.png: ")

# Create a function to prompt the size of the emoji user wants
def output_size():
    return input(Fore.LIGHTGREEN_EX + "Enter the desired size of the emoji in format of (width, height) e.g., 32, 28: ")

# Create a function to prompt the user to input the path to save the converted image
def output_path():
    return input(Fore.CYAN + "Enter the path of the output file along with the desired output file name e.g., /path/to/save/file.jpg: ")

# Create function to convert the image into emoji
def convert_to_emoji(input_path, output_path, output_size):
    try:
        # Open the image file
        img = Image.open(input_path)

        # Validate and parse the output size
        try:
            width, height = map(int, output_size.split(','))
        except ValueError:
            print(Fore.LIGHTRED_EX + "Invalid output size format. Please use the format: width, height")
            return

        # Create the output directory if it doesn't exist(Error handling)
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Resize the image to the specified size
        img_resized = img.resize((width, height))

        # Save the processed image as an emoji file
        img_resized.save(output_path)

        print(Fore.GREEN + f"Emoji file saved at: {output_path}")

    except FileNotFoundError:
        print(Fore.LIGHTRED_EX + f"Error: Image file not found at {input_path}")
    except OSError as e:
        print(Fore.RED + f"Error: {e}")

# Run main function
if __name__ == "__main__":
    input_image_path = input_path()
    output_emoji_path = output_path()

    convert_to_emoji(input_image_path, output_emoji_path)