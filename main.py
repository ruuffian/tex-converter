import re, sys, getopt
import urllib.parse


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["help="])
    except getopt.GetoptError:
        print(r'usage: main.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ["-h", "--help"]:
            print(r'usage: main.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt == "-i":
            inputfile = arg
        elif opt == "-o":
            outputfile = arg
    if outputfile == '':
        outputfile = inputfile
    print(f'File to be processed:: {inputfile}')

    paramsingle = r'\$[^\$]+\$'
    paramdouble = r'\${2}[^\$]+\${2}'

    rawinput = readfile(inputfile)
    doubledollarremoved = applyregex(paramdouble, rawinput, '\n')
    singledollarremoved = applyregex(paramsingle, doubledollarremoved)
    writefile(singledollarremoved, outputfile)


def readfile(filename):
    f = open(filename, "r")
    fstr = f.read()
    f.close()
    return fstr


def applyregex(regex, filestring, newline=''):
    urlhead = r'<img src="https://render.githubusercontent.com/render/math?math='
    urltail = r'">'
    match = re.search(regex, filestring)
    while match:
        raw = match.group().strip("$")
        encoded = urllib.parse.quote(raw)
        url = newline + urlhead + encoded + urltail + newline
        filestring = re.sub(regex, url, filestring, 1)
        match = re.search(regex, filestring)
    return filestring


def writefile(modifiedstring, outputfile):
    f = open(outputfile, "w")
    f.write(modifiedstring)
    f.close()


if __name__ == "__main__":
    main(sys.argv[1:])
