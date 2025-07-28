# option 1
import imports_module

album = imports_module.make_album("porcupine tree", "deadwing", 9)
print(album)
print()



# option 2
from imports_module import make_album

album = make_album("porcupine tree", "deadwing", 9)
print(album)
print()



# option 3
from imports_module import make_album as ma

album = ma("porcupine tree", "deadwing", 9)
print(album)
print()



# option 4
import imports_module as im

album = im.make_album("porcupine tree", "deadwing", 9)
print(album)
print()



# option 5
from imports_module import *

album = make_album("porcupine tree", "deadwing", 9)
print(album)
print()
