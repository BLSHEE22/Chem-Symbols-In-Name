import sys

def main():
    symbs = {"h","he","li","be","b","c","n","o","f","ne",
             "na","mg","al","si","p","s","cl","ar","k","ca",
             "sc","ti","v","cr","mn","fe","co","ni","cu","zn",
             "ga","ge","as","se","br","kr","rb","sr","y","zr",
             "nb","mo","tc","ru","rh","pd","ag","cd","in","sn",
             "sb","te","i","xe","cs","ba","hf","ta","w","re",
             "os","ir","pt","au","hg","tl","pb","bi","po","at",
             "rn","fr","ra","rf","db","sg","bh","hs","mt","ds",
             "rg","cn","uut","uuq","uup","uuh","uus","uuo","la","ce",
             "pr","nd","pm","sm","eu","gd","tb","dy","ho","er",
             "tm","yb","lu","ac","th","pa","u","np","pu","am",
             "cm","bk","cf","es","fm","md","no","lr"}

    name0 = ""

    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            if i == len(sys.argv)-1:
                name0 += sys.argv[i]
            else:
                name0 += sys.argv[i] + " "
    else:
        name0 = sys.argv[1]

    name = name0.lower()
    output = name
    finds = []
    earliest = 100000
    for x in symbs:
        if x in name:
            if len(x) == 1:
                finds.append(x.upper())
            else:
                finds.append(x[0].upper()+x[1:])
            if name.index(x[0]) < earliest:
                if len(x) == 1:
                    output = name0[0:name.index(x)] + '\033[1;32m' + name0[name.index(x[0])].upper() + '\033[m' + name0[name.index(x[-1])+1:]
                else:
                    output = name0[0:name.index(x)] + '\033[1;32m' + name0[name.index(x[0])].upper() + name0[name.index(x[1]):name.index(x[-1])+1] + '\033[m' + name0[name.index(x[-1])+1:]
                earliest = name.index(x[0])

    print

    if len(finds) == 0:
        print("Sorry, there's no chemical symbol contained within " + name + ".")
    elif len(finds) == 1:
        print("There's only one chemical symbol contained in " + name0 + "!")
        print(output)
    else:
        print("There are " + str(len(finds)) + " different chemical symbols contained in " + name0 + ".\n")
        print(str(finds) + "\n")
        print("The earliest occuring one is shown below:\n")
        print(output)

    print

if __name__ == "__main__":
    main()
