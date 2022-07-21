class classroom:
    def __init__(self,na,ag):
        self.name = na
        self.age = ag
#Funtion to greet the user (Name)
    def greeting(self):
        print("Hello ", self.name)

# Self is used to use the class variables


"""
class classroom:
    name = ""
    age = ""
"""
#Creating Objects with their values
s1 = classroom("kush", 12)
s2 = classroom("Nidhi",15)
s3 = classroom("Gaurav",10)

"""
s1.name = "Kush"
s1.age = "12"

s2.name = "Nidhi"
s2.age = "15"
"""

print("Object 1 {} {}".format(s1.name,s1.age))
print("Object 2 {} {}".format(s2.name,s2.age))
print("Object 3 {} {}".format(s3.name,s3.age))


s1.greeting()
s2.greeting()
