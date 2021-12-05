import re
import urllib.parse

print("Welcome to ruuffian's tex-converter! Hopefully,"
      " this will allow you to host your obsidian notes "
      "on github and not lose the power that latex brings!")
paramsingle = r'\$[^\$]+\$'
paramdouble = r'\${2}[^\$]+\${2}'

urlhead = r'<img src="https://render.githubusercontent.com/render/math?math='
urltail = r'">'


# Step 1: find latex in file
# Step 2: encode formula
# Step 3: plug it into github markdown img link
# Step 4: replace in filestring, then write to a new file


def readfile(filename):
    f = open(filename, "r")
    fstr = f.read()
    f.close()
    return fstr


def applyregex(regex, filestring, newline=''):
    match = re.search(regex, filestring)
    while match:
        raw = match.group().strip("$")
        encoded = urllib.parse.quote(raw)
        url = newline + urlhead + encoded + urltail + newline
        filestring = re.sub(regex, url, filestring, 1)
        match = re.search(regex, filestring)
    return filestring


def writefile(modifiedstring):
    f = open("git.md", "w")
    f.write(modifiedstring)
    f.close()


rawfile = readfile("test.md")
removedoubledollar = applyregex(paramdouble, rawfile, '\n')
removesingledollar = applyregex(paramsingle, removedoubledollar)
writefile(removesingledollar)
