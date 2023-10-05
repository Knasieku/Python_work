# def name():
#     your_name=input()
#     print("your name is "+ your_name)
# name()


# def geekbooks():
#       print("Welcome to geekbooks to sign up enter" )
#       user_name=input()
#       password=input()
#       email=input()
#       print("Kindly confirm your username is " + user_name + "Your password is "+password +"your email is "+email)
# geekbooks()

# #operators
# # equals ==
# if 5 == 3:
#     print("5 equals to 3")
# else:
#     print("not equal")

# # not equals !=
# print("Enter your password: ")
# password=input()
# print("Confirm your password: ")
# confirm_password=input()

# if password != confirm_password:
#     print("password is not the same")

# # less than < and less than or equal to <=
# if 10<=2:
#     print("10 is less")
# elif 10<2:
#     print("10 maybe equal to")
# else:
#     print("equal")

# # greater than > and greater than or equal to >=
# if 10>=20:
#     print("10 is more")
# elif 10>2:
#     print("10 maybe equal to")
# else:
#     print("equal")

# # and operator 
# if 5<3 and 10>2:
#     print("conditions met")
# else: 
#     print ("conditions not met")

# lists (array) and for loop
fruits=["apples","bananas", "avocado"]
vegetables=["tomatoes", "cucumber","kale"]

print("Pick a fruit... Any fruit")
fruit=input().lower()
print("Pick a vegetable... Any vegetable")
veg=input().lower()

for fruit in fruits:
#     if (fruit in fruits) and (veg in vegetables):
#         print (fruit+" is available" +veg + " is available")
#         break
#     else:
#       print ("when neither is available")
#       break
    
    if (fruit in fruits) or (veg in vegetables):
        print (fruit+" is available" +veg + " is available")
        break
    else:
      print ("when neither is available")
      break

