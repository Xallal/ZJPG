# coding=utf-8
from win32api import GetFileVersionInfo
import shutil
import os


# Funckja sterująca kopiowanie. Pozwala na kopiowanie selektywne
def Copy_main(source, destination, Switch=False, Select=[]):
    if Switch == True:
        for item in os.listdir(source):
            for file in Select:
                if file == item:
                    Copy_select(item, source, destination)
    else:
        for item in os.listdir(source):
            Copy_select(item, source, destination)


# Funkcja pomocnicza do Copy main (Tu odbywa się właściwe kopiowanie)
def Copy_select(item, source, destination, symlinks=False, ignore=None):
    if os.path.isdir(item):
        shutil.copytree(os.path.join(source, item), os.path.join(destination, item), symlinks, ignore)
    else:
        shutil.copy2(os.path.join(source, item), os.path.join(destination, item))


# Funkcja szykująca tablicę z nazwami plików do sprawdzenia
def File_list(source, Directory=[]):
    for root, dirs, files in os.walk(source):
        for filename in files:
            Directory.append(filename)
    return Directory


# Funckja sterująca testowaniem wersji plików. Pozwala na selektywne testowanie
def Test(source, destination, Directory=[], Switch=False, Select=[]):
    if Switch == True:
        for file in Directory:
            for item in Select:
                if file == item:
                    Check_version(source, destination, file)
    else:
        for file in Directory:
            Check_version(source, destination, file)


# Funckja pomocnicza do testów. Testowanie właściwe
def Check_version(source, destination, file):
    source_version = GetFileVersionInfo(os.path.join(destination, file), "\\")
    destination_version = GetFileVersionInfo(os.path.join(source, file), "\\")
    if source_version != destination_version:
        print("Test nie zaliczony, wersje plików się nie zgadzają")
        print(source_version)
        print(destination_version)


# Instruckja wywoływania:

# Dla kopiowania
# Copy_main('Ścieżka do folderu z plikami do kopiowania','Ścieżka do folderu do którego kopiujemy'
# ,Switch=True - Włącza kopiowanie selektywne,Select=[Nazwy plików które chcemy skopiować]

# Dla Testów
# Test('Ścieżka do folderu z plikami do testowania','Ścieżka do drugiego folderu'
# ,Directory=File_list('Ścieżka do pliku z plikami do testowania'),Switch=True - Włącza testowanie selektywne,
# Select=[Nazwy plików które chcemy testować]

# Dla File_list
# File_list('Ścieżka do pliku z plikami')

Copy_main('C:/Users/Xizor/Desktop/dll_nowe', 'C:/Users/Xizor/Desktop/test')

Copy_main('C:/Users/Xizor/Desktop/dll_nowe1', 'C:/Users/Xizor/Desktop/test', Switch=True,
          Select=['amqmdnet', 'AutoMapper.Net4.dll', 'AutoMapper.dll'])

Test('C:/Users/Xizor/Desktop/dll_nowe', 'C:/Users/Xizor/Desktop/test',
     Directory=File_list('C:/Users/Xizor/Desktop/test'))

Test('C:/Users/Xizor/Desktop/dll_nowe1', 'C:/Users/Xizor/Desktop/test',
     Directory=File_list('C:/Users/Xizor/Desktop/test'), Switch=True,
     Select=['amqmdnet', 'AutoMapper.Net4.dll', 'AutoMapper.dll'])
