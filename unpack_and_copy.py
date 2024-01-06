#!/usr/bin/python3

import zipfile
import shutil
import os

source="/home/kryt/Pobrane"
files="/home/kryt/dev/google_backup_unpack/files"
out="/home/kryt/dev/google_backup_unpack/pictures"
#pobranie nazw plikow zip

os.chdir(source)
lista=os.listdir()
for plik in lista:
    if plik.endswith(".zip"):
        print(plik)
        with zipfile.ZipFile(plik,"r") as zip_ref:
            zip_ref.extractall(files)

def doit(files, out):
    os.chdir(files)
    lista = os.listdir()
    for plik in lista:
        print(plik)
        plikAll=files+"/"+plik
        if os.path.isdir(plikAll):
            doit(plikAll, out)
        else:
            if plikAll.endswith(".jpg") or plikAll.endswith(".JPG") or plikAll.endswith(".mp4"):
                print("copy:",plik,"to:",out)
                shutil.move(plikAll, out+"/"+plik)
            else:
                print("HGW co to:", plik)

os.chdir(files)
doit(files, out)



