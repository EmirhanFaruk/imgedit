
# Modification date: Wed Dec 29 12:50:30 2021

# Production date: Sun Sep  3 15:43:47 2023

from PIL import Image
import os
import csv


try:
    ground = open("ground_training.csv", "w", encoding = "utf-8")
    gwriter = csv.writer(ground)
    gtableau = []
    water = open("water_training.csv", "w", encoding = "utf-8")
    wwriter = csv.writer(water)
    wtableau = []

    #writer.writerow(row)

    originals = os.listdir("C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\imgedit\\imgedit_training\\originals\\")
    edited = os.listdir("C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\imgedit\\imgedit_training\\edited\\")

    print(edited)
    print(originals)

    for i in range(len(originals)):
        eimg = Image.open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\imgedit\\imgedit_training\\edited\\{edited[i]}")
        oimg = Image.open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\imgedit\\imgedit_training\\originals\\{originals[i]}")
        width, height = eimg.size
        for w in range(width):
            for h in range(height):
                rgb = eimg.getpixel((w, h))
                rgbo = oimg.getpixel((w, h))
                if rgb[1] == 255 and rgb[0] == 0 and rgb[2] == 0:
                    gtableau.append(rgbo)
                if rgb[2] == 255 and rgb[0] == 0 and rgb[1] == 0:
                    wtableau.append(rgbo)
        print(edited[i])
        print(originals[i])
        print(len(gtableau))
        print(len(wtableau))
        oimg.close()
        eimg.close()

    print("\n\n\n\n\n\n")
    print(gtableau)
    print("-------------------------------------------------------------")
    print(wtableau)

    def f(seq): # Order preserving
        ''' Modified version of Dave Kirby solution '''
        seen = set()
        return [x for x in seq if x not in seen and not seen.add(x)]

    gtableau = f(gtableau)
    wtableau = f(wtableau)


    print("\n\n\n\n\n\n")
    print(gtableau)
    print("-------------------------------------------------------------")
    print(wtableau)

    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


    print(len(wtableau))
    print(len(gtableau))

    """
    if len(wtableau) > len(gtableau):
        wtableau = wtableau[0:len(gtableau)]
    if len(wtableau) < len(gtableau):
        gtableau = gtableau[0:len(wtableau)]

    print(len(wtableau))
    print(len(gtableau))
    """
    """
    def ayıklama(t1, t2, n, n2):
        if n < 900:
            print(f"\ndeleted {n} items(total {n2}), t1 lenght: {len(t1)}, t2 lenght: {len(t2)}")
            for i in t2:
                if i in t1:
                    t2.remove(i)
                    t1.remove(i)
                    n += 1
                    n2 += 1
                    return ayıklama(t1, t2, n, n2)
            print("All done. WOHOOOOOOOO!!!!!")
            n = 0
            return t1, t2, n, n2
        n = 1
        return t1, t2, n, n2

    

    n = 1
    n2 = 0
    while n != 0:
        if len(wtableau) >= len(gtableau):
            wtableau, gtableau, n, n2 =  ayıklama(wtableau, gtableau, n, n2)
        if len(wtableau) < len(gtableau):
            gtableau, wtableau, n, n2 =  ayıklama(gtableau, wtableau, n, n2)

    #wtableau, gtableau, n, n2 =  ayıklama(wtableau, gtableau, n, n2)
    """
    print("\n\n\n\n\n\n")
    print(gtableau)
    print("-------------------------------------------------------------")
    print(wtableau)
    print("\n\n\n")
    print(len(gtableau))
    print(len(wtableau))
    #print(f"{n2} duplicate items were deleted.")

    input("Last checkpoint. Press enter to continue...")
    for i in range(len(gtableau)):
        gwriter.writerow(gtableau[i])
    for i in range(len(wtableau)):
        wwriter.writerow(wtableau[i])


    print(len(gtableau))
    print(len(wtableau))
    input("All done. Press enter to continue...")
except Exception as exception:
    print(exception)
    input("\nPress enter to continue...")




