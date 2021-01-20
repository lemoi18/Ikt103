
string1 = input()
string2 = input()

if  string1 == string2 :
    print("are equal")
else:
    print("are not equal")


    if string2 in string1 or  string1 in string2 :
        print(" is a substring")
    else:
        print("is not a substring")
