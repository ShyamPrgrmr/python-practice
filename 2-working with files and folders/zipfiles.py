import zipfile
from pathlib import Path


def createZip(foldername):
    path = Path(foldername)
    zipF = zipfile.ZipFile(str(path.absolute())+"/"+"archive.zip","w")
    for file in path.iterdir():
        if file.is_file():
            zipF.write(str(path)+"/"+file.name)

if __name__ == "__main__":
    createZip("./random-folders")








