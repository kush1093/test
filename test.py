import os
import sys
import os

def func():
	#return "Hi there! this is my first repository on GIT-HUB"
    try:
        #a=pow(2,100000000000)
        a=1/0 
    except ArithmeticError:
        print("yay")
    except ZeroDivisionError:
        print("yo yo honey singh")
    except Exception as e:
        print(e)

if(__name__ == "__main__"):
    #print ("Testing testing")
    func()
    #print (a)
    #print ("from t2-folder")

    #print("In Boulder")
    #print("with new SSH")

    # 2
    # removed the line in branch1 
    # the one with branch2	
