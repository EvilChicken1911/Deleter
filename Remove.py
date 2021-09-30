import os
import shutil
import time 

#source = input("File name to delete:")
def main():
    deletedFolderCount = 0
    filesCount = 0
    days = 10
    path = "/PATH_TO_DELETE"
    seconds = time.time() - (days*24*60*60)
    if os.path.exists(path):
        for rootFolder, folders, files in os.walk(path):
            if seconds >= getFileRFolderAge(rootFolder):
                removeFolder(rootFolder)
                deletedFolderCount += 1
                break
            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolder, folder)
                     if seconds >= getFileRFolderAge(folderPath):
                        removeFolder(folderPath)
                        deletedFolderCount += 1
                for file in files:
                    filePath = os.path.join(rootFolder, file)
                     if seconds >= getFileRFolderAge(filePath):
                        removeFiles(filePath)
                        deletedFilesCount += 1
        else:
            if seconds > getFileRFolderAge(path):
                removeFiles(path)
                filesCount += 1
    else:
        print("File or Folder does not exist")
        filesCount += 1
    print("Deleted Files: ", deletedFolderCount)
    print("Deleted Folders: ", FilesCount)

def removeFolders(path):
    if not shutil.rmtree(path):
        print("Folder removed succesfully")
    else:
        print("Unable to delete folder")

def removeFiles(path):
    if not os.remove(path):
        print("File removed succesfully")
    else:
        print("Unable to delete file")

def getFileOrFolderAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == "__main__":
    main()