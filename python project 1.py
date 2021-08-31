x=input("Enter the radius of circle=")
r=float(x)
a=3.14159*r**2
print("Area of circle is",a)

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
