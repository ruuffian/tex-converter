import re
import urllib.parse

print("Welcome to ruuffian's tex-converter! Hopefully,"
      " this will allow you to host your obsidian notes "
      "on github and not lose the power that latex brings!")
param = r'\$[^\$]+\$'
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


def applyregex(regex, filestring):
    match = re.search(regex, filestring)
    while match:
        raw = match.group().strip("$")
        encoded = urllib.parse.quote(raw)
        url = urlhead + encoded + urltail
        filestring = re.sub(regex, url, filestring, 1)
        match = re.search(regex, filestring)
    return filestring


def writefile(modifiedstring):
    f = open("git.md", "w")
    f.write(modifiedstring)
    f.close()


string = readfile("test.md")
gitfile = applyregex(param, string)
writefile(gitfile)
