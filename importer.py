import mod
print (mod.s)
mod.a
print (mod.a)
print (mod.foo)
import sys
print(sys.path)
mod.__file__
from mod import *
print(mod)
import fact
from fact import *
print(mod.__file__)
print(fact._file_)
