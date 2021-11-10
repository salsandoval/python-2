Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisset = ("car", "bike", "plane")
>>> print(thisset)
('car', 'bike', 'plane')
>>> thisset.add("boat")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    thisset.add("boat")
AttributeError: 'tuple' object has no attribute 'add'
>>> thisset = ("car", "bike", "plane")
>>> thisset.add("boat")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    thisset.add("boat")
AttributeError: 'tuple' object has no attribute 'add'
>>> thisset.remove("car")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    thisset.remove("car")
AttributeError: 'tuple' object has no attribute 'remove'
>>> 