from win32api import GetFileVersionInfo
import shutil
import os

s ='C:/Users/Xizor/Desktop/dll_nowe'
d ='C:/Users/Xizor/Desktop/test'
list = []
i = 0


for item in os.listdir(source):
    a= os.path.join(s, item)
    b=os.path.join(d, item)
    if os.path.isdir(s):
        shutil.copytree(a,b, symlinks, ignore)
    else:
            shutil.copy2(a,b)


for root, dirs, files in os.walk(s):
    for filename in files:
        list.append(filename)


for file in list:
     c = GetFileVersionInfo(os.path.join(d, file), "\\")
     d = GetFileVersionInfo(os.path.join(s, file), "\\")
     if c != d:
         i = i + 1
     if i > 0:
         print("Test nie zaliczony, wersje plików się nie zgadzają")

     else:
         print("Test zaliczony, wersje plików się zgadzają")



