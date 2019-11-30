from win32api import GetFileVersionInfo
import shutil
import os

Source_directory = 'C:/Users/Xizor/Desktop/dll_nowe1'
Select_directory = 'C:/Users/Xizor/Desktop/dll_nowe/'
Destination_directory = 'C:/Users/Xizor/Desktop/test/'
Select = ['amqmdnet','AutoMapper.Net4.dll','AutoMapper.dll']
Directory = []


def file_list_directory(source):
    for root, dirs, files in os.walk(source):
        for filename in files:
            Directory.append(filename)

def file_list_selective(source):
    for root, dirs, files in os.walk(source):
        for filename in files:
            for file in Select:
                if file == filename:
                    Directory.append(filename)




def copy_selective(source,destination, symlinks=False, ignore=None):
    for item in os.listdir(Select_directory):
        for file in Select:
            if file == item:
                if os.path.isdir(item):
                    shutil.copytree(os.path.join(source, item), os.path.join(destination, item), symlinks, ignore)
                else:
                    shutil.copy2(os.path.join(source, item), os.path.join(destination, item))


def copy_directory(source,destination, symlinks=False, ignore=None):
    for item in os.listdir(Select_directory):
        for file in Select:
            if file == item:
                if os.path.isdir(item):
                    shutil.copytree(os.path.join(source, item), os.path.join(destination, item), symlinks, ignore)
                else:
                    shutil.copy2(os.path.join(source, item), os.path.join(destination, item))

def test_version(source, destination):
    mismatch_files = 0
    for file in Directory:
        source_version = GetFileVersionInfo(os.path.join(destination, file), "\\")
        destination_version = GetFileVersionInfo(os.path.join(source, file), "\\")
        if source_version != destination_version:
            mismatch_files += 1
    if mismatch_files > 0:
        print("Test nie zaliczony, wersje plików się nie zgadzają")
        print("Liczba niezgodnych plików"+str(mismatch_files))
    else:
        print("Test zaliczony, wersje plików się zgadzają")



copy_directory(Source_directory,Destination_directory)
copy_selective(Select_directory,Destination_directory)
file_list_directory(Source_directory)
test_version(Source_directory,Destination_directory)
Directory = []
file_list_selective(Select_directory)
test_version(Select_directory,Destination_directory)