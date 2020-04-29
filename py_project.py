from tkinter import *
from datetime import *

now = datetime.now()
d = ('Date: {}/{}/{}'.format(now.day, now.month, now.year))
t = ('Time: {}:{}'.format(now.hour, now.minute))

def click(event):
    # to get text from the text entry box
    usertext = textentry.get()
    output.delete(0.0, END)
    # to check if element info is available, and display it
    try:
        info = pt_dictionary[usertext]
    except:
        info = "There is no such element present \nPlease try again"
    output.insert(END, info)

    # to save history in a txt file
    file1 = open("history.txt", "a")  # append mode, so file will show all inputs & outputs till now
    file1.writelines(usertext)
    file1.write("\n")
    file1.writelines(info)
    file1.write("\n\n")
    file1.close()

def close():
    # to indicate that the program was exit
    file1 = open("history.txt", "a")
    file1.write("===========================================================================================\n\n")
    file1.close()

    # to stop and close the 'main' window
    main.destroy()
    exit()


main = Tk()
main.title("Periodic Table Glossary")
main.geometry('1000x1000')
main.configure(background="black")

# to display today's date
ld = Label(main, text=d, bg="black", fg="white", font="none 11 italic")
ld.place(relx=0.07, anchor = N)

# to display current time
lt = Label(main, text=t, bg="black", fg="white", font="none 11 italic")
lt.place(relx=0.06, rely=0.03, anchor = N)

# image to be displayed
img = PhotoImage(file="img1.gif")
Label(main, image=img, bg="black").place(relx = 0.5, anchor = N)

# user input instructions
l1 = Label(main, text="Enter the symbol of the element you are searching for:", bg="black", fg="white", font="none 18 bold")
l1.place(relx = 0.5, rely=0.5, anchor = N)

l2 = Label(main, text="For example - Na, Hg, F etc.", bg="black", fg="white", font="none 14")
l2.place(relx = 0.5, rely=0.55, anchor = N)

# text entry box for user input
textentry = Entry(main, width=20,font="none 14", bg="white")
textentry.place(relx = 0.5, rely=0.6, anchor = N)

# submit button
b1 = Button(main, text="SUBMIT", width=7, height=1, bg='yellow', font="none 12 bold", fg='blue', activebackground='green', activeforeground='white', command=click)
b1.place(relx = 0.7, rely=0.6, anchor = N)

# label for output box
l3 = Label(main, text="Element Information:", bg="black", fg="white", font="none 18 bold italic")
l3.place(relx = 0.25, rely=0.7, anchor = N)

# creating output box
output = Text(main, width=30, height=5, wrap=WORD, font=("none 14 bold italic"), bg="white")
output.place(relx = 0.555, rely=0.7, anchor = N)

# to bind the Enter key with the click function
main.bind('<Return>', click)


# the periodic table dictionary, have made for around 64 elements
pt_dictionary = {
    'H': 'Hydrogen \nAtomic No.: 1 \nAtomic Mass: 1u', 'He': 'Helium \nAtomic No.: 2 \nAtomic Mass: 4u',
    'Li': 'Lithium \nAtomic No.: 3 \nAtomic Mass: 7u', 'Be': 'Beryllium \nAtomic No.: 4 \nAtomic Mass: 9u',
    'B': 'Boron \nAtomic No.: 5 \nAtomic Mass: 11u', 'C': 'Carbon \nAtomic No.: 6 \nAtomic Mass: 12u',
    'N': 'Nitrogen \nAtomic No.: 7 \nAtomic Mass: 14u', 'O': 'Oxygen \nAtomic No.: 8 \nAtomic Mass: 16u',
    'F': 'Fluorine \nAtomic No.: 9 \nAtomic Mass: 19u', 'Ne': 'Neon \nAtomic No.: 10 \nAtomic Mass: 20u',
    'Na': 'Sodium \nAtomic No.: 11 \nAtomic Mass: 23u', 'Mg': 'Magnesium \nAtomic No.: 12 \nAtomic Mass: 24u',
    'Al': 'Aluminium \nAtomic No.: 13 \nAtomic Mass: 27u', 'Si': 'Silicon \nAtomic No.: 14 \nAtomic Mass: 28u',
    'P': 'Phosphorus \nAtomic No.: 15 \nAtomic Mass: 31u', 'S': 'Sulphur \nAtomic No.: 16 \nAtomic Mass: 32u',
    'Cl': 'Chlorine \nAtomic No.: 17 \nAtomic Mass: 35u', 'Ar': 'Argon \nAtomic No.: 18 \nAtomic Mass: 39.95u',
    'K': 'Potassium \nAtomic No.: 19 \nAtomic Mass: 39u', 'Ca': 'Calcium \nAtomic No.: 20 \nAtomic Mass: 40u',
    'Sc': 'Scandium \nAtomic No.: 21 \nAtomic Mass: 45u', 'Ti': 'Titanium \nAtomic No.: 22 \nAtomic Mass: 48u',
    'V': 'Vanadium \nAtomic No.: 23 \nAtomic Mass: 51u', 'Cr': 'Chromium \nAtomic No.: 24 \nAtomic Mass: 52u',
    'Mn': 'Manganese \nAtomic No.: 25 \nAtomic Mass: 55u', 'Fe': 'Iron \nAtomic No.: 26 \nAtomic Mass: 56u',
    'Co': 'Cobalt \nAtomic No.: 27 \nAtomic Mass: 59u', 'Ni': 'Nickel \nAtomic No.: 28 \nAtomic Mass: 58u',
    'Cu': 'Copper \nAtomic No.: 29 \nAtomic Mass: 63u', 'Zn': 'Zinc \nAtomic No.: 30 \nAtomic Mass: 65u',
    'Ga': 'Galium \nAtomic No.: 31 \nAtomic Mass: 69u', 'Ge': 'Germanium \nAtomic No.: 32 \nAtomic Mass: 72.6u',
    'As': 'Arsenic \nAtomic No.: 33 \nAtomic Mass: 75u', 'Se': 'Selenium \nAtomic No.: 34 \nAtomic Mass: 79u',
    'Br': 'Bromine \nAtomic No.: 35 \nAtomic Mass: 79u', 'Kr': 'Krypton \nAtomic No.: 36 \nAtomic Mass: 83u',
    'Rb': 'Rubidium \nAtomic No.: 37 \nAtomic Mass: 85', 'Sr': 'Strontium \nAtomic No.: 38 \nAtomic Mass: 87u',
    'Y': 'Yttrium \nAtomic No.: 39 \nAtomic Mass: 89u', 'Zr': 'Zirconium \nAtomic No.: 40 \nAtomic Mass: 91u',
    'Cs': 'Caesium \nAtomic No.: 55 \nAtomic Mass: 133u', 'Ba': 'Barium \nAtomic No.: 56 \nAtomic Mass: 137u',
    'Fr': 'Francium \nAtomic No.: 87 \nAtomic Mass: 223u', 'Ra': 'Krypton \nAtomic No.: 88 \nAtomic Mass: 226u',
    'La': 'Lanthanum \nAtomic No.: 57 \nAtomic Mass: 139u', 'Hf': 'Hafnium \nAtomic No.: 72 \nAtomic Mass: 178u',
    'Ac': 'Actinium \nAtomic No.: 89 \nAtomic Mass: 227u', 'Rf': 'Rutherfordium \nAtomic No.: 104 \nAtomic Mass: 267u',
    'Nb': 'Niobium \nAtomic No.: 41 \nAtomic Mass: 93u', 'Mo': 'Molybdenum \nAtomic No.: 42 \nAtomic Mass: 96u',
    'Ta': 'Tantalium \nAtomic No.: 73 \nAtomic Mass: 181u', 'W': 'Tungsten \nAtomic No.: 74 \nAtomic Mass: 183.8u',
    'Db': 'Dubnium \nAtomic No.: 105 \nAtomic Mass: 268u', 'Sg': 'Seaborgium \nAtomic No.: 106 \nAtomic Mass: 269u',
    'Tc': 'Technetium \nAtomic No.: 43 \nAtomic Mass: 98u', 'Ru': 'Ruthenium \nAtomic No.: 44 \nAtomic Mass: 101u',
    'Re': 'Rhenium \nAtomic No.: 75 \nAtomic Mass: 186u', 'Os': 'Osmium \nAtomic No.: 76 \nAtomic Mass: 190u',
    'Hg': 'Mercury \nAtomic No.: 80 \nAtomic Mass: 200.6u', 'Au': 'Gold \nAtomic No.: 79 \nAtomic Mass: 197u',
    'Ag': 'Silver \nAtomic No.: 47 \nAtomic Mass: 108u', 'Pt': 'Platinum \nAtomic No.: 78 \nAtomic Mass: 195u',
    'Pb': 'Lead \nAtomic No.: 82 \nAtomic Mass: 207u', 'Bi': 'Bismuth \nAtomic No.: 83 \nAtomic Mass: 209u',
    'Bh': 'Bohrium \nAtomic No.: 107 \nAtomic Mass: 270u', 'Hs': 'Hassium \nAtomic No.: 108 \nAtomic Mass: 269u',

}

# exit button
b2 = Button(main, text="CLICK TO EXIT", width=15, height=1, font="none 10 bold", activebackground='white', activeforeground='black', command=close)
b2.place(relx = 0.5, rely=0.89, anchor = N)


main.mainloop()
