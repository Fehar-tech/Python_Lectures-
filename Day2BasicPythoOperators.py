# print(6*3)
# print(5-4)
# print(4/2)
# print(6//3)
# print(2**3)

#########################################################################PEMDAS########################################################
#Peranthesis Exponent Multipy Division Addition Sustraction 
# ( Left to Right Sequence for M D & A S) We will learn it later in course
#print((2+2*3+7**2))


#########################################################################STRINGS#########################################################
# print("Hello World My name is Fehar")
# print("We are going to learn Pyhton from Begining")
# print("learning Pyhton ka chilla wth Dr.Ammar day 01 ended here")
# print("Pyhton ka chilla with Dr.Ammar day 2 Starts from here from the next file")

# print('Test for Fehar')
# print("Genetic Engineering")
# print("' Test will be held on Friday '")

################################################################## COMMENTS IN PYTHON####################################################
# print('How are you Fehar') #These green or # are comments.

######################################################################## VARIABLES########################################################
# x=5.9
# y=("How are you World")
# print(x)
# print(y)
# a=x+10
# print(a)
# q=9
# w=1
# print(q+w)

# TYPES OF VARIABLES
# type(a)
# print(type(x))
#RULES
#1-variables can be number letter or underscores
#2-it cant start with number
#3-Dont use python keywords eg print, type etc
#4-Spaces not allow
#5-keep short names
#6-always use low case letters

# fruit_basket="Mangoes and Oranges" 
# print(fruit_basket)
# fruit_basket=77
# others="Hello"
# print(type(fruit_basket))
# print(type(others))

#########################################################INPUT FUNCTION STAGE 1###########################################################
# fruit_basket="Mangoes and Oranges" 
# print(fruit_basket)
# interviewer=input("What is your name gentlemen?")
# print(interviewer)

#INPUT FUNCTION STAGE 2
# interviwer= ("What is your Name?")
# me=("Fehar")
# greetings= input(" Good Morning, You're Welcome to our office")
# print (greetings, interviwer,me)
# print("Hello!", me)

# INPUT FUNCTION STAGE 3 
# name=input("Whats's your name Young man? ")
# age=input("How old are you? ")
# greet=input("Welcome! Mr.Fehar")
# sir1=input("So, You applied for the Admissions at Penn State University, Right? in what major")
# print=("Thats Great to hear its a wonderful subject")
# me2=("Thankyou Sir! Indeed It is")
# ques=f("Any Scholarship?")
# print=("yES fully funded with RA and stipend of 900 usd per month" )
# print("Youre Welcome")


##########################################################CONDITIONAL LOGICS#############################################################
# equal to             ==
# not equal to         !=
# greater than         >
# smaller than         <
# greter n equal to    >=
# smaller n euqal to   <=
# they are either true or false , yes or no , 0 or 1
# print(3!=1)
# print(5<8)
# print(100>101)
# print(4!=4)
# #APPLICATION OF LOGICAL OPERATORS
# fehar_age=22
# ugrad_age=26
# print(fehar_age<ugrad_age)
# #INPUT FUNCTION OF LOGICAL OPERATORS
# ageatschool=10
# hammad= input("How old is Hammad" )
# print (type(hammad))
# print (hammad==ageatschool)

################################################################TYPE CONVERSION######################################################
# X=5
# Y=7.3
# Z=("fehar")
# print(type(Z))
# print(type(X))
# print(type(Y))
# #Implicit type conversion
# x=X*Y
# y=X+Y
# print(type(y))

#Explicit Type Conversion
# age=input("What is you age" )
# age=int(age)
# print(type(age))


####################################################### IF, ELSE , ELIF STATEMENTS####################################################
# requiredageatschool=15
# ahmedage=20
# if ahmedage==requiredageatschool :
#     print("Yes! Ahmed can join school")
# elif ahmedage < requiredageatschool:
#     print("He is a baby")                      #need some concept on it


###########################################################FUNCTIONS###################################################################
#1 Defining a Function
# def printcode():
#     print("we are learning")
#     print("we are learning")
#     print("we are learning")
# printcode()

#2
# def printcode():
#     text=("Hy Fehar How are you")
#     print(text)
#     print(text)
#     print(text)
#     print(text)
#     print(text)
# # printcode()

# # #3
# # def printcode(text):
#     print (text)
#     print (text)
#     print (text)
# printcode("Hello Fehar! Howday")

#4 Defining function with if else elif 
# def school_calc(age):
#     if age==6:
#        print("Ahmed can go school")
#     elif age>5:
#         print(" He should")
#     else:
#         print("he's a baby")
# school_calc(6)


#Defining Future Function
# def futureage(age):
#     newage=age+27
#     return newage
#     print(newage)
# futureagepr= futureage(8470)
# print(futureagepr)



#####################################################################LOOPS##########################################################
#1 while loops
# x=3
# while(x<9):
#     print(x)
#     x=x+1

#2 For Loop
# for x in range (7,17):
#     print(x)

#array
# days=("Mon","Tues", "Weds", "Thurs", "Fri", "Sat", "Sun")
# for d in days:
#     # if (d=="Fri"):break
#     if(d=="Fri"):continue
#     print(d)


#####################################################IMPORTANT LIBRARIES##################################################
# if you want to get the value of pi
# import math
# print("The value of pi ", math.pi)

# import statistics
# x=(382,282,22,2928,292)
# print(statistics.median (x))           #Some imp libraries are math. , statistics. , numpy , pandas



# ########################################################TROUBLESHOOTING#############################################################
# #How to trouble shoot errors in pyhton
# print(we are learing) #syntax error
# print(25/0)           #runtime error
# name=fehar
# print("hello name")  #symentic error most diffiult error to remove
# print("hello" , name )

# dna="ATCG"
# for base in dna:
#     print(base)



def printcode():
    text=("hello world Univers Earth universe")
    print(text)
    print(text)
    print(text)
    print(text)
    print(text)
printcode()
