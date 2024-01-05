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
    time.sleep(2)
except ImportError:
    print(Fore.RED + "Colorama has not been installed. Installing it...")
    subprocess.run(["pip", "install", "colorama"], check=True)
    from colorama import init, Fore
    print(Fore.LIGHTMAGENTA_EX + "Done, Colorama has been installed.")
    time.sleep(2)

# Initialize colorama
init(autoreset=True)

# Check if emoji has been already installed or not
try:
    import emoji
except ImportError:
    print(Fore.LIGHTRED_EX+ "Emoji not found! Installing it...")
    subprocess.run(["pip", "install", "emoji"], check=True)
    import emoji
    print(Fore.LIGHTCYAN_EX + "Done, Emoji has been installed.")
    time.sleep(2)

# Clear the terminal screen
os.system("clear")
time.sleep(1)

# Create 3D banner for showcase
def create_3d_banner():
    # Banner text
    banner_text = "  IMG2EMOJI"

    try:
        # Use figlet to create ASCII art with mono9 font
        figlet_process = subprocess.Popen(
            ["figlet", "-w", "100", "-f", "mono9", banner_text],
            stdout=subprocess.PIPE
        )
        figlet_output, _ = figlet_process.communicate()

        # Use lolcat to add color to the ASCII art
        lolcat_process = subprocess.Popen(["lolcat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        banner_output, _ = lolcat_process.communicate(input=figlet_output)

        # Print the result
        print(banner_output.decode("utf-8"))

    except FileNotFoundError:
        print(Fore.LIGHTRED_EX + "Error: Make sure 'figlet' and 'lolcat' are installed on your system.")

if __name__ == "__main__":
    create_3d_banner()

# Create a function to prompt the path of the image file which user wants to convert into an emoji
def input_path():
    return input(Fore.LIGHTYELLOW_EX + "Enter the path of the image file e.g., /path/to/image.png: ")

# Create a function to prompt the size of the emoji user wants
def output_size():
    return input(Fore.LIGHTGREEN_EX + "Enter the size of the emoji in format of (width, height) e.g., 32, 28: ")

# Create a function to prompt the user to input the path to save the converted image
def output_path():
    return input(Fore.CYAN + "Enter the path of output file along with the output file name e.g., /path/to/save/file.jpg: ")

# Create function to convert the image into emoji
def convert_to_emoji(input_path, output_path, output_size):
    try:
        # Open the image file
        img = Image.open(input_path)

        # Validate and parse the output size
        try:
            width, height = map(int, output_size().split(','))
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

    convert_to_emoji(input_image_path, output_emoji_path, output_size)