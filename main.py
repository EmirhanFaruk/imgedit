
# Modification date: Wed Dec 29 16:44:10 2021

# Production date: Sun Sep  3 15:43:47 2023

"""import sqlite
from flask import Flask, request, g, redirect, url_for, render_template, abort, jsonify
here lie my hope and dreams"""

import os
from PIL import Image
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from clear_screen import clear#clear()
from datetime import datetime
import csv


def main():
    def enter():
        input("Press enter to continue...")

    def Convert(string):
        try:
            the_list = list(string.split(","))
            the_tuple = (int(the_list[0]), int(the_list[1]), int(the_list[2]))
            return the_tuple
        except:
            return "bruh"

    start = time.time()
    # datetime object containing current date and time
    now = datetime.now()



    arr = os.listdir(r"C:\Users\emirh\OneDrive\Bureau\My_World_Dont_Change\dosyalar\Kodlarim\Python\imgedit\imgedit2")
    #arr.pop(0)
    """
    print(arr)

    for i in range(len(arr)):
        arr[i] = "C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\imgedit\\imgedit2\\" + arr[i]
        os.rename(arr[i], f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\imgedit\\imgedit2\\sc_{i + 1}.png")

    print(arr)
    """

    water = list()
    grass = list()
    wandg = list()
    soarr = len(arr)
    other = list()

    p1soar = soarr / 50
    
    print(p1soar)
    print(soarr)
    


    wcsv = open("water_training2.csv", "r", encoding = "utf-8")
    lecteurCSV = csv.reader(wcsv, delimiter = ' ')
    wtt = []
    for row in lecteurCSV:
        if row != ['']:
            row = str(row)
            row = row[2:-2]
            row = Convert(row)
            if row != "bruh":
                wtt.append(row)

    gcsv = open("ground_training2.csv", "r", encoding = "utf-8")
    lecteurCSV = csv.reader(gcsv, delimiter = ' ')
    gtt = []
    for row in lecteurCSV:
        if row != "":
            row = str(row)
            row = row[2:-2]
            row = Convert(row)
            if row != "bruh":
                gtt.append(row)

    print("-----------------------------------")
    print(wtt)
    print("-----------------------------------")
    print(gtt)
    print("-----------------------------------")


    print(len(gtt))
    print(len(wtt))

    gtt = gtt[0:10000]
    wtt = wtt[0:10000]

    print(len(gtt))
    print(len(wtt))
    print((len(wtt) + len(gtt)) * 640 * 480)

    print(arr)

    input("Press enter to start...")

    f = open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\imgedit\\water_grass_sc.txt", "a")
    f.write(f"\n\n\n---------------------------------------------------------------------\n\n\nStarted at {now}\n\n\n")
    f.close()

    now_for_imgs = datetime.now()
    the_delta_image_time = [0, 0, 0]
    for i in range(len(arr)):
        now_for_imgs = datetime.now()
        dt_string1 = now_for_imgs.strftime("%d/%m/%Y %H:%M:%S")
        image = Image.open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\imgedit\\imgedit2\\{arr[i]}")
        width, height = image.size
        waterp = 0
        grassp = 0
        gwp = 0
        clear()
        print(f"Last image done in {the_delta_image_time[0]} hours, {the_delta_image_time[1]} minutes and {the_delta_image_time[2]} seconds.")
        print(f"Started/started from the last image: {dt_string1}")
        print(f"Image {i + 1}")
        print(f"Water screenshots: {len(water)}")
        print(f"Grass screenshots: {len(grass)}")
        print(f"Water and grass screenshots: {len(wandg)}")
        print(f"Other screenshots: {len(other)}")
        green_bars_num = int((((len(water) + len(grass) + len(other)) / len(arr)) * 100))
        green_bars = " " * green_bars_num
        white_bars = " " * (100 - green_bars_num)
        print(Back.GREEN + green_bars + Back.RED + white_bars)
        the_image_time = datetime.now()
        the_image_time = [the_image_time.hour, the_image_time.minute, the_image_time.second]
        for w in range(width):
            for h in range(height):
                rgb = image.getpixel((w, h))

                #time things
                now_for_imgs2 = datetime.now()
                dt_string2 = now_for_imgs2.strftime("%d/%m/%Y %H:%M:%S")
                img_break_time = time.time()
                current_running_time = int(img_break_time - start)
                
                if rgb in gtt and rgb in wtt:
                    gwp += 1
                    image.putpixel((w, h), (0, 255, 255))
                    print(f"ground and water found {i} {w} {h} g: {grassp} w: {waterp} gw: {gwp}| Current time: {dt_string2}, the program has been running for {current_running_time// 60} minutes {current_running_time - (current_running_time // 60 * 60)} seconds.         ", end = "\r")
                elif rgb in wtt:
                    waterp += 1
                    image.putpixel((w, h), (0, 0, 255))
                    print(f"water found {i} {w} {h} g: {grassp} w: {waterp} gw: {gwp}| Current time: {dt_string2}, the program has been running for {current_running_time// 60} minutes {current_running_time - (current_running_time // 60 * 60)} seconds.         ", end = "\r")
                elif rgb in gtt:
                    grassp += 1
                    image.putpixel((w, h), (0, 255, 0))
                    print(f"ground found {i} {w} {h} g: {grassp} w: {waterp} gw: {gwp}| Current time: {dt_string2}, the program has been running for {current_running_time// 60} minutes {current_running_time - (current_running_time // 60 * 60)} seconds.         ", end = "\r")
                else:
                    print(f"nothing found {i} {w} {h} g: {grassp} w: {waterp} gw: {gwp}| Current time: {dt_string2}, the program has been running for {current_running_time// 60} minutes {current_running_time - (current_running_time // 60 * 60)} seconds.         ", end = "\r")
        loc = ""
        if waterp + gwp > (width * height) // 3 and grassp + gwp > (width * height) // 3:
            wandg.append(arr[i])
            loc = "wandg"
        elif waterp > (width * height) // 3:
            water.append(arr[i])
            loc = "water"
        elif grassp > (width * height) // 3:
            grass.append(arr[i])
            loc = "grass"
        else:
            other.append(arr[i])
            loc = "other"
        next_path = f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\imgedit\\{loc}\\{loc}_sc_{i + 1}.png"
        image.save(next_path, "png")
        clear()
        print(f"Image {i + 1}")
        print(f"Water screenshots: {len(water)}")
        print(f"Grass screenshots: {len(grass)}")
        print(f"Water and grass screenshots: {len(wandg)}")
        print(f"Other screenshots: {len(other)}")
        green_bars_num = int((((len(water) + len(grass) + len(other)) / len(arr)) * 100))
        green_bars = " " * green_bars_num
        white_bars = " " * (100 - green_bars_num)
        print(Back.GREEN + green_bars + Back.RED + white_bars)
        image.close()
        f = open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\imgedit\\water_grass_sc.txt", "a")
        the_image_time_end = datetime.now()
        the_image_time_end = [the_image_time_end.hour, the_image_time_end.minute, the_image_time_end.second]
        the_delta_image_time = [the_image_time_end[0] - the_image_time[0], the_image_time_end[1] - the_image_time[1], the_image_time_end[2] - the_image_time[2]]
        if the_delta_image_time[2] < 0:
            the_delta_image_time[2] = the_delta_image_time[2] + 60
            the_delta_image_time[1] -= 1
        if the_delta_image_time[1] < 0:
            the_delta_image_time[1] = the_delta_image_time[1] + 60
            the_delta_image_time[0] -= 1
        f.write(f"\nImage {i + 1} has been done in {the_delta_image_time[0]} hours, {the_delta_image_time[1]} minutes and {the_delta_image_time[2]} seconds.")
        f.close()

    print(f"\n\n\n\n\nWater screenshots: {len(water)}")
    print(f"Grass screenshots: {len(grass)}")
    print(f"Water and grass screenshots: {len(wandg)}")
    print(f"Other screenshots: {len(other)}")

    print(f"\n\n\nWater screenshots: {water}")
    print(f"\n\n\nGrass screenshots: {grass}")
    print(f"Water and grass screenshots: {wandg}")
    print(f"\n\n\nOther screenshots: {other}")

    finish = time.time()

    total_time = finish - start

    f = open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\imgedit\\water_grass_sc.txt", "a")

    f.write(f"\n\n--------------------------------------------------------------------------------------------------\n\n\n\n\nAll done in {total_time}\n\nWater screenshots: {len(water)}\n{water}\n\n\nGrass screenshots: {len(grass)}\n{grass}\n\n\n\Water and grass screenshots: {len(wandg)}\n{wandg}n\n\nOther screenshots: {len(other)}\n{other}")

    f.close()


    now2 = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Started at ", dt_string)	
    # dd/mm/YY H:M:S
    dt_string = now2.strftime("%d/%m/%Y %H:%M:%S")
    print("Ended at ", dt_string)	
    print(f"All done in {total_time}")

    enter()
main()
