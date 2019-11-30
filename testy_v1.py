from win32api import GetFileVersionInfo
import shutil
import os

a = 'C:/Users/Xizor/Desktop/dll_nowe1'
ciastko = 'C:/Users/Xizor/Desktop/dll_nowe/'
ciastko1 = 'C:/Users/Xizor/Desktop/dll_nowe/AutoMapper.dll'
ciastko2 = 'C:/Users/Xizor/Desktop/dll_nowe/AutoMapper.Net4.dll'
ciastko3 = 'C:/Users/Xizor/Desktop/dll_nowe/amqmdnet'
karmel = 'C:/Users/Xizor/Desktop/test/'
karmel1 = 'C:/Users/Xizor/Desktop/test/AutoMapper.dll'
karmel2 = 'C:/Users/Xizor/Desktop/test/AutoMapper.Net4.dll'
karmel3 = 'C:/Users/Xizor/Desktop/test/amqmdnet'
czekolada = []
symlinks=False
ignore=None

for root, dirs, files in os.walk(a):
        for filename in files:
            czekolada.append(filename)

for item in os.listdir(a):
        if os.path.isdir(item):
            shutil.copytree(os.path.join(a, item), os.path.join(karmel, item), symlinks, ignore)
        else:
            shutil.copy2(os.path.join(a, item), os.path.join(karmel, item))
i = 0


shutil.copy(ciastko1, karmel)
shutil.copy(ciastko2, karmel)
shutil.copy(ciastko3, karmel)

for root, dirs, files in os.walk(a):
    for filename in files:
        czekolada.append(filename)

for file in czekolada:
    c = GetFileVersionInfo(os.path.join(ciastko, file), "\\")
    d = GetFileVersionInfo(os.path.join(karmel, file), "\\")

    if c != d:
        i = i + 1

c = GetFileVersionInfo(ciastko1, "\\")
d = GetFileVersionInfo(karmel1, "\\")
if c != d:
    i = i + 1
c = GetFileVersionInfo(ciastko2, "\\")
d = GetFileVersionInfo(karmel2, "\\")
if c != d:
    i = i + 1
c = GetFileVersionInfo(ciastko3, "\\")
d = GetFileVersionInfo(karmel3, "\\")
if c != d:
    i = i + 1

if i > 0:
    print("Test nie zaliczony, wersje plików się nie zgadzają")

else:
    print("Test zaliczony, wersje plików się zgadzają")
