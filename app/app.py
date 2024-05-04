from tkinter import *
from components import *
import tkinter as tk
import os
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def main():
    root = tk.Tk()
    root.title("Weather Checker")

    # Set the full path to the icon
    dir_path = os.path.dirname(os.path.realpath(__file__))  # Gets the directory of the current script
    icon_path = os.path.join(dir_path, 'assets', 'icon.png')

    # Load the icon image
    icon_image = PhotoImage(file=icon_path)
    root.iconphoto(False, icon_image)

    search_bar = SearchBar(root)
    search_bar.pack(pady=0)

    root.mainloop()

if __name__ == "__main__":
    main()