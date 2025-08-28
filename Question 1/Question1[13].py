# VIBGYOR Wavelength Ranges (in nanometers)
# Violet: 400–440 nm
# Indigo: 440–460 nm
# Blue:   460–500 nm
# Green:  500–570 nm
# Yellow: 565–590 nm
# Orange: 590–620 nm
# Red:    620–750 nm

wavelength = int(input("Enter the wavelength (in nm): "))

match wavelength:
    case w if 400 <= w <= 440:
        color = "Violet"
    case w if 441 <= w <= 460:
        color = "Indigo"
    case w if 461 <= w <= 500:
        color = "Blue"
    case w if 501 <= w <= 570:
        color = "Green"
    case w if 571 <= w <= 590:
        color = "Yellow"
    case w if 591 <= w <= 620:
        color = "Orange"
    case w if 621 <= w <= 720:
        color = "Red"
    case _:
        color = "Out of visible spectrum"

print(f"The color for wavelength {wavelength} nm is: {color}")


# Sample Input/Output
#Enter the wavelength (in nm): 22
#The color for wavelength 22 nm is: Out of visible spectrum

#Enter the wavelength (in nm): 457 
#The color for wavelength 457 nm is: Indigo