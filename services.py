import os
from pydub import AudioSegment
import tkinter as tk
from tkinter import filedialog
import re
from pathlib import Path
from app import app
 
# TODO: Add try catch here
def convert_files():
    folder_path=app.config["LOCAL_DIR"]
    convert_path = folder_path+"/output/"
    Path(convert_path).mkdir(parents=True, exist_ok=True)
    
    # rename files first
    for item_name in os.listdir(folder_path):
        rename_file_and_remove_whitespace(folder_path+"/"+item_name)
       
    #convert files 
    for item_name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item_name)
        if os.path.isfile(full_path):
            new_name = re.sub(r'\.[^.]*$', '', item_name)
            convert_mp4_to_mp3(folder_path+"/"+item_name, convert_path+new_name+".mp3")
    
def convert_mp4_to_mp3(input_file_path, output_file_path):
    try:
        # Load the MP4 audio file
        audio = AudioSegment.from_file(input_file_path, format="mp4")

        # Export the audio to MP3 format
        audio.export(output_file_path, format="mp3")
        print(f"Successfully converted '{input_file_path}' to '{output_file_path}'")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

def rename_file_and_remove_whitespace(old_filename):
    if not os.path.exists(old_filename):
        print(f"Error: File '{old_filename}' does not exist.")
        return

    # Remove all whitespace characters from the filename
    new_filename = old_filename.replace(" ", "")  # Removes all spaces
    new_filename = new_filename.replace("\t", "") # Removes all tabs
    new_filename = new_filename.replace("\n", "") # Removes all newlines

    if old_filename == new_filename:
        print(f"No whitespace found in '{old_filename}', no rename needed.")
        return

    try:
        os.rename(old_filename, new_filename)
        print(f"File '{old_filename}' renamed to '{new_filename}'.")
    except OSError as e:
        print(f"Error renaming file: {e}")