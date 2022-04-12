# Max value of int

# x = 10000000000000000000000000000000000000000000
# x = x + 22
# print (x)

########################################################################################################################
# Global and Local Variables

# x = 23                  # global variable

# def test():
#     y = 10              # local variable
#     print(x+y)

# test()
#print(y)    # This through a error

########################################################################################################################
# Packing and Unpacking Arguments in Python

# # UnPacking
# def lst(x,y,z):
#     print(x, y, z)

# a = ["Hello", "Good", "Morning"]
# lst(*a)

# # Packing
# def fun(*x):                    # In Dic we use two staric (**)
#     print(sum(x))

# fun(45, 25, 85, 6)

########################################################################################################################
# Type Conversion

# x = "15"
# print(type(x))

# x = int(x)
# print(type(x))

########################################################################################################################
# Byte Objects vs String in Python

# print('Best Tutorials'.encode('ASCII'))                         # encoding

# print(b'Best Tutorials'.decode('ASCII'))                        # decoding



########################################################################################################################
 # Print Single and Multiple variable in Python

# a = "Python"
# print(a)
# print(45, 25, 48, 85, 88, "Python", 2.5)

########################################################################################################################
# Swap Two Variables

# x = 10
# y = 30

# temp = y
# y = x
# x = temp

# print(x)
# print(y)

########################################################################################################################
# Private variable

# class A: 
#     __a = 10
#     def __sample(self):
#         print("ok")

#     def __demo(self):
#         print(self.__a)
#         self.__sample()

# obj = A()
# #obj.print_detail()             #this will through error

########################################################################################################################
# __name__ variable 

# if __name__ == "__main__": 
#     print ("Name is equal to Main")
# else: 
#     print ("Name does not equal to Main")

########################################################################################################################












########################################################################################################################