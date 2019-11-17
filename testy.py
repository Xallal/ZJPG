from win32api import GetFileVersionInfo
import shutil
import os

src = 'C:/Users/Xizor/Desktop/dll_nowe'
dst = 'C:/Users/Xizor/Desktop/test'
list = []

#Funkcja kopiująca pliki
def copytree(source, destination, symlinks=False, ignore=None):
    for item in os.listdir(source):
        if os.path.isdir(s):
            shutil.copytree(os.path.join(source, item), os.path.join(destination, item), symlinks, ignore)
        else:
            shutil.copy2(os.path.join(source, item), os.path.join(destination, item))

#Funkcja pobierająca listę plików z folderu do sprawdzenia
def file_list(source):
    list = []
    for root, dirs, files in os.walk(source):
        for filename in files:
            list.append(filename)

#Funkcja porównująca biblioteki z dwóch folderów. Test czy wersje bibliotek się zgadzają.
def test_version(source, destination):
    mismatch_files = 0
    for file in list:
        source_version = GetFileVersionInfo(os.path.join(destination, file), "\\")
        destination_version = GetFileVersionInfo(os.path.join(source, file), "\\")
        if source_version != destination_version:
            mismatch_files += 1
    if mismatch_files > 0:
        print("Test nie zaliczony, wersje plików się nie zgadzają")
        print("Liczba niezgodnych plików"+str(mismatch_files))
    else:
        print("Test zaliczony, wersje plików się zgadzają")


# copytree('C:/Users/Xizor/Desktop/dll_nowe','C:/Users/Xizor/Desktop/test')
file_list('C:/Users/Xizor/Desktop/dll_nowe')
test_version('C:/Users/Xizor/Desktop/dll_nowe', 'C:/Users/Xizor/Desktop/test')
