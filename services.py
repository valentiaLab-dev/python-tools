import os
from pydub import AudioSegment
import tkinter as tk
from tkinter import filedialog

def get_path():
    root = tk.Tk()
    root.withdraw() # Hide the main tkinter window
    folder_selected = filedialog.askdirectory()
    return folder_selected


def test2():
    print(f"TEST@")
    
    
def convert_m4a_to_mp3(input_file_path, output_file_path):
    """
    Converts an M4A audio file to MP3 format.

    Args:
        input_file_path (str): The path to the input M4A file.
        output_file_path (str): The path where the output MP3 file will be saved.
    """
    try:
        # Load the M4A audio file
        audio = AudioSegment.from_file(input_file_path, format="mp4")

        # Export the audio to MP3 format
        audio.export(output_file_path, format="mp3")
        print(f"Successfully converted '{input_file_path}' to '{output_file_path}'")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        
    return
