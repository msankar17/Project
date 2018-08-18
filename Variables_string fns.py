#This module will help us understand various functions used with a string
t3="test String for Learning Purpose"
print("Capitailize fn to make first letter caps -",t3.capitalize())
print("Casefold fn to give string in small caps for compare -",t3.casefold())
print("Center fn will place string centrally to width(45) mentioned -",t3.center(45," "))
print("Count fn to count ocurrences of a substring(ng), optional strt and end arguments -"\
,t3.count("ng"))
print("find fn to find lowest occurence of substring(ng), optional strt and end arguments -"\
,t3.find("ng"))
print("index fn to find lowest occurence of substring(ng), optional strt and end arguments -"\
,t3.index("ng"),end=".")
print("Index fn raises valueerror if substring not found")
print("rfind fn to find highest occurence of substring(ng), optional strt and end arguments -"\
,t3.rfind("ng"))
print("rindex fn to find highest occurence of substring(ng), optional strt and end arguments -"\
,t3.rindex("ng"),end=".")
print("endswith fn to string ends with a substring(ose), optional strt and end arguments -"\
,t3.endswith("ose"))

print("\nString validation functions(Is?)")  #String validation functions
print("--------------------------")
print("isalnum fn will return true if string only has alphanumeric char eg-a3e$ will be false,\
a3e will be true-","a3e$".isalnum()," ","a3e".isalnum())
print("isalpha fn will return true if string only has alphabets  eg:'aa3' will be false-\
'aa' will be true","aa3".isalpha()," ",'aa'.isalpha())
print("isdecimal fn will return true if string only has decimal values eg-123 will be True-\
12a will return false","123".isdecimal()," " ,"12a".isdecimal())
print("isdigit fn will return true if string only has decimal values eg-123 will be True-\
subscript 2 00B2 is a digit","123".isdigit(),"\u00B2".isdigit())
print("isidentifier fn will return true if string has an identifier eg-for will be true -"\
,"for".isidentifier())
print("islower fn will return true if string only has lower chars eg-abcd will be True but \
Abcd will be false","abcd".islower()," ", "Abcd".islower())
print("isupper fn will return true if string only has upper chars eg-ABCD will be True but \
Abcd will be false","ABCD".isupper()," ", "Abcd".isupper())
print("isnumeric fn will return true if string only has numeric values eg-234 will be True-"\
,"234".isnumeric())
print("isprintable fn will return true if string has only printable chars eg-print will be True-\
 \\nprint will be false","print".isprintable()," ", "\nprint".isprintable())
print("isspace fn will return true if string only has spaces eg-spaces will be True-\
but space btween is false","  ".isspace()," ","space between".isspace())
print("Istitle fn will return true if string Firstchar of words in uppercase eg-This Is Title will be true but This is title will be false-", \
"This Is Title".istitle(), " ", "This is title".istitle())
s=("append","string","together","with","comma","inbetween")
print("Join fn will append strings from an iterable with seperator from called string -",",".join(s))

print("Convert string to lower case -",t3.lower())
print("Convert string to upper case -",t3.upper())
print("Left justify for given width and also optional fill char -" ,t3.ljust(40,"."))
print("Right justify for given width and also optional fill char -" ,t3.rjust(40,"."))
print("Remove specified chars from the string,if arg not given leading white spaces removed -","  "+t3.lstrip())
print("Remove specified chars from the string,if arg not given trailing white spaces removed -",t3+"  ".rstrip())
t3.maketrans

t4="Test string      two tabs were typed before"
print("expandtabs fn wil replace tab in string wtih nbr. of spaces in argument -",t4.expandtabs(3))
print("This is to {1} {2} {0}".format("capablities","show","format"),end=".")
print(" Format function replaces string with arguments")
print("This is to {first} {second} {third}".format_map({'third':"capablities",'first':"show",\
'second':"format_map"}),end=".")
print(" Format_map function replaces string with arguments from a dictioanry")
print("encode function convering string to UTF8 -",t3.encode(),flush=True)
