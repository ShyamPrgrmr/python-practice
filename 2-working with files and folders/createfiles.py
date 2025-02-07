import random
from pathlib import Path
import sys
import time

def createFolder(path):
    try:
        path.mkdir()
    except FileExistsError:
        print("Folder already exists")


def createFiles(foldername, noOfFiles, toBeDeleted):

    path = Path(foldername)
    no_of_files = noOfFiles
    files_to_be_deleted = toBeDeleted

    createFolder(path)

    for i in range(0, no_of_files):
        file_name = str(random.getrandbits(40))
        file_path = Path("./"+foldername+"/"+file_name)
        if not file_path.exists():
            file_path.touch()
            with open(file_path.absolute(),"w") as file:
                try:
                    if(random.choice(["yes", "no"])=="yes"):
                        file.write(str(random.getrandbits(40)))
                except:
                    print("Error in writing file")

    if files_to_be_deleted:
        time.sleep(3)
        for file in path.iterdir():
            if file.exists() and file.is_file():
                file.unlink()



if __name__ == "__main__":
    createFiles("./random-folders", 2, False)

        






