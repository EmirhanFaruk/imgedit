
# Modification date: Wed Dec 29 12:54:28 2021

# Production date: Sun Sep  3 15:43:47 2023

import os
from PIL import Image


arr = os.listdir(r"C:\Users\emirh\OneDrive\Bureau\My_World_Dont_Change\dosyalar\Kodlarim\Python\imgedit\imgedit2")

for i in range(len(arr)):
    image = Image.open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\imgedit\\imgedit2\\{arr[i]}")
    image = image.resize((640, 480))
    image.save(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\imgedit\\imgedit2\\resized_to_480p_{arr[i]}", "png")
    image.close()