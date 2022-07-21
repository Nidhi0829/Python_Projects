Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> user = "Kush"
>>> print("Hello %s", user)
Hello %s Kush
>>> print("Hello %s", %user)
SyntaxError: invalid syntax
>>> print("Hello %s" %user)
Hello Kush
>>> print("Hello {}".format(user))
Hello Kush
>>> print("Hello",user," Excellent")
Hello Kush  Excellent
>>> fname = "Kush"
>>> lname = "Rawal"
>>> print("Hello {} {}".format(fname,lname))
Hello Kush Rawal
>>> name = "John"
>>> age = 23
>>> if name == "John" and age == 23:
	print("Your name is John, and you are also 23 years old.")

	
Your name is John, and you are also 23 years old.
>>> if name == "John" and name == "Rick":
	print("yes")

	
>>> if name == "John" or age = 21:
	
SyntaxError: invalid syntax
>>> if name == "John" or age == 21:
	print(True)

	
True
>>> if name == "John" and age = 21:
	
SyntaxError: invalid syntax
>>> if name == "John" and age == 21:
	print(True)

	
>>> x= 1
>>> y = 1
>>> x is y
True
>>> y is x
True
>>> x = [1,2,3]
>>> y= [1,2,3]
>>> x is y
False
>>> y is x
False
>>> x == y
True
>>> for i in range(10):
	if i == 6:
		break
	print(i)

	
0
1
2
3
4
5
>>> for i in range(10):
	if i == 6:
		continue
	print(i)

	
0
1
2
3
4
5
7
8
9
>>> for i in range(10):
	print(i)
	if i == 6 :
		continue

	
0
1
2
3
4
5
6
7
8
9
>>> 
