import zipfile
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import json

# Path: labgrader.py

def getFileName():
    '''Prompts user to select a file and returns the filename'''
    Tk().withdraw()
    filename = askopenfilename()
    return filename

def unzipCore(filename):
    '''Unzips the core ZyBooks file'''
    zip_ref = zipfile.ZipFile(filename, 'r')
    zip_ref.extractall()
    zip_ref.close()

def unzipStudent(file):
    '''Unzips the student files and renames the .py file to match the students last name'''
    zFile = zipfile.ZipFile(file, 'r')
    zFile.extractall()
    extracted = zFile.namelist()
    for pyfile in extracted:
        try:
            if pyfile.endswith(".py"):
                os.rename(pyfile, file.split("_")[0] + ".py")
                print("Renamed " + extracted[0] + " to " + file.split(".")[0] + ".py")
            else:
                os.remove(pyfile)
        except:
            print(f'{pyfile} - Does not Exist Error Manually Check')
    zFile.close()
    os.remove(file)


def comments(commentUsage):
    '''Returns a dictionary of the comments used in each file'''
    print(os.listdir())
    for file in os.listdir():
        if file != "labgrader.py":
            comments = []
            with open(file, "r") as f:
                for line in f:
                    if '#' in line:
                        comments.append('#' + line.split('#')[1])
                    else:
                        continue
            commentUsage[file] = comments
            os.remove(file)
    return commentUsage
 
            
def main():
    filename = getFileName()
    unzipCore(filename)
    for file in os.listdir():
        if file.endswith(".zip"):
            unzipStudent(file)
    commentUsage = {}
    comments(commentUsage)
    cleandata = json.dumps(commentUsage, indent=10)
    print(cleandata)
    print("Done!")

if __name__ == "__main__":
    main()