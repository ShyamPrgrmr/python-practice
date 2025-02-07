from pathlib import Path


def removeFiles(foldername):
    path = Path(foldername)
    total_file = 0
    empty_file_count = 0 
    for file in path.iterdir():
        if file.is_file():
            total_file = total_file + 1
            file_path = Path(file.absolute())
            if file_path.stat().st_size > 0:
                if file_path.name[len(file_path.name)-4:]!=".log" and file_path.name[len(file_path.name)-4:]!=".zip":
                    file_path.rename(str(path)+"/"+file_path.name+".log")
            else:
                empty_file_count = empty_file_count+1
                file_path.unlink()
    print(f"""total files {total_file} : , empty_file : {empty_file_count}""")

if __name__=="__main__":
    removeFiles("./random-folders")