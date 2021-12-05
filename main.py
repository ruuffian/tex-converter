import re
import urllib.parse

print("Welcome to ruuffian's tex-converter! Hopefully,"
      " this will allow you to host your obsidian notes "
      "on github and not lose the power that latex brings!")


# plus signs need to be replaced by %2B

# Step 1: find latex in file
# Step 2: encode formula
# Step 3: plug it into github markdown img link
# Step 4: replace in filestring, then write to a new file

def readfile(filename):
    f = open(filename, "r")
    fstr = f.read()
    f.close()
    return fstr


param = "^\\$.*\\$$"
hack1 = "<img src=\"https://render.githubusercontent.com/render/math?math="
hack2 = "\">"


def applyregex(filestring, regex):
    match = re.search(regex, filestring)
    while match != "None":
        re.sub(match.string, hack1 + urllib.parse.quote(match.group()) + hack2, filestring)

# need to implement new file write

