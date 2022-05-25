# AMC's Breaking Bad does a very interesting thing in its credits, and I wanted to explore it further.

# Each name of the credits has a group of highlighted letters, and these letters make up a various chemical symbol.

# For a name to contain a chemical symbol, it must meet ANY of the following criteria:
# - Contain an "a" "b", "c", "f", "h", "i", "k", "n", "o", "p", "s", "u", "v", "w", or "y".
# - Contain an "er", "gd", "ge", "lr", "md", "mg", "mt", "re", "rg", "te", "tl", "tm", "xe", or "zr".

# So, a name containing no chemical symbols must consist of ONLY the letters:
# --> "d", "e", "g", "j", "l", "m", "q", "r", "t", "x", or "z".
# AND that name must not contain any of the above two-letter symbols.

# For example, "Gex" would not work because it contains symbol "Ge".
# Conversely, "Lex" or "Mel" would work.
# There are very few full names in existence that follow the specifications immediately above.
# (hence why Breaking Bad had no trouble with this process!)

# What if we wanted to know just how many chemical symbols existed within a name?

# The below program can be run with the following command:
# python brba.py name

# It will print a summary of the symbols found, and then print the name with the earliest symbol
# highlighted in green, as if the name were a cast/crew member of AMC's Breaking Bad.

# My challenge to you would be to find a legal full name that doesn't contain a chemical symbol.

# Good luck, and have fun!

import sys

def main():
    symbs = ["h","he","li","be","b","c","n","o","f","ne",
             "na","mg","al","si","p","s","cl","ar","k","ca",
             "sc","ti","v","cr","mn","fe","co","ni","cu","zn",
             "ga","ge","as","se","br","kr","rb","sr","y","zr",
             "nb","mo","tc","ru","rh","pd","ag","cd","in","sn",
             "sb","te","i","xe","cs","ba","la","hf","ta","w","re",
             "os","ir","pt","au","hg","tl","pb","bi","po","at",
             "rn","fr","ra","ac","rf","db","sg","bh","hs","mt","ds",
             "rg","cn","nh","fl","mc","lv","ts","og","ce",
             "pr","nd","pm","sm","eu","gd","tb","dy","ho","er",
             "tm","yb","lu","th","pa","u","np","pu","am",
             "cm","bk","cf","es","fm","md","no","lr"]

    elems = ["Hydrogen","Helium","Lithium","Beryllium","Boron","Carbon","Nitrogen","Oxygen","Flourine","Neon",
             "Sodium","Magnesium","Aluminum","Silicon","Phosphorus","Sulfur","Chlorine","Argon","Potassium","Calcium",
             "Scandium","Titanium","Vanadium","Chromium","Manganese","Iron","Cobalt","Nickel","Copper","Zinc",
             "Gallium","Germanium","Arsenic","Selenium","Bromine","Krypton","Rubidium","Strontium","Yttrium","Zirconium",
             "Niobium","Molybdenum","Technetium","Ruthenium","Rhodium","Palladium","Silver","Cadmium","Indium","Tin",
             "Antimony","Tellurium","Iodine","Xenon","Caesium","Barium", "Lanthanum", "Hafnium","Tantalum","Tungsten","Rhenium",
             "Osmium","Iridium","Platinum","Gold","Mercury","Thallium","Lead","Bismuth","Polonium","Astatine",
             "Radon","Francium","Radium","Actinium","Rutherfordium","Dubnium","Seaborgium","Bohrium","Hassium","Meitnerium","Darmstadtium",
             "Roentgenium","Copernicium", "Nihonium","Flerovium","Moscovium","Livermorium","Tennessine","Oganesson","Cerium",
             "Praseodymium","Neodymium","Promethium","Samarium","Europium","Gadolinium","Terbium","Dysprosium","Holmium","Erbium",
             "Thulium","Ytterbium","Lutetium","Thorium","Protactinium","Uranium","Neptunium","Plutonium","Americium",
             "Curium","Berkelium","Californium","Einsteinium","Fermium","Mendelevium","Nobelium","Lawrencium"]

    name0 = ""

    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            if i == len(sys.argv)-1:
                name0 += sys.argv[i]
            else:
                name0 += sys.argv[i] + " "
    else:
        print("\nSorry, you must run the program with a full name as an argument.\n")
        quit()

    name = name0.lower()
    output = name
    outputEl = ""
    finds = []
    earliest = 100000
    for x in symbs:
        if x in name:
            if len(x) == 1:
                finds.append((x.upper(), elems[symbs.index(x)]))
            else:
                finds.append((x[0].upper()+x[1:], elems[symbs.index(x)]))
            if name.index(x[0]) < earliest:
                outputEl = elems[symbs.index(x)]
                if len(x) == 1:
                    output = name0[0:name.index(x)] + '\033[1;32m' + name0[name.index(x[0])].upper() + '\033[m' + name0[name.index(x[-1])+1:]
                else:
                    output = name0[0:name.index(x)] + '\033[1;32m' + name0[name.index(x[0])].upper() + name0[name.index(x[1]):name.index(x[-1])+1] + '\033[m' + name0[name.index(x[-1])+1:]
                earliest = name.index(x[0])

    print

    if len(finds) == 0:
        print("Sorry, there's no chemical symbol contained within " + name0 + ".")
    elif len(finds) == 1:
        print("\nThere's only one chemical symbol contained in " + name0 + "!")
        print(output)
    else:
        print("\nThere are " + str(len(finds)) + " different chemical symbols contained in " + name0 + ".\n")
        print(str(finds) + "\n")
        print("The earliest occuring one is " + outputEl + "!\n")
        print(output)

    print()

if __name__ == "__main__":
    main()
