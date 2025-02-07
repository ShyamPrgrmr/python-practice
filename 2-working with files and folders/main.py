
import createfiles
import removefiles
import zipfiles


folderpath = str(input("Enter folder path : "))
nof = int(input("Enter no of files to create : "))
createfiles.createFiles(folderpath,nof,False)
removefiles.removeFiles(folderpath)
zipfiles.createZip(folderpath)





