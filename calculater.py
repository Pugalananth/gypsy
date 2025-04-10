#calculator
class calculate:#create class funtion for using arthimetic operation
    def sample(r):#fundtion create the same operation 
         while(r<6):#if the while condition is 6 is greterthen r then condition executed but this condition dummey
            print("1 add")#option 1 using addition operation
            print("2 sub")#option 2 using subtract operation
            print("3 mul")#option 3 using multiply operation
            print("4 div")#option 4 using division operation
            print("5 fdiv")#option 5 using floor division operation
            print("6 expo")#option 6 using exponent operation
            x=int(input("enter the option"))#x is a option storing variable 
            if x==1:#the condition is if x is equal to 1 the condition is execute
              a=int(input("enter the value 1"))#a is first value of calculation
              b=int(input("enter the value 2"))#b is second value of calculation
              c=a+b #if the condition is true then a and b varaible would be add
              print(c)
            elif x==2:#the condition is if x is equal to 2 the condition is execute
              a=int(input("enter the value 1"))#a is first value of calculation
              b=int(input("enter the value 2"))#b is second value of calculation
              c=a-b
              print(c)
            elif x==3:#the condition is if x is equal to 3 the condition is execute
              a=int(input("enter the value 1"))#a is first value of calculation
              b=int(input("enter the value 2"))#b is second value of calculation
              c=a*b
              print(c)
            elif x==4:#the condition is if x is equal to 4 the condition is execute
              a=int(input("enter the value 1"))#a is first value of calculation
              b=int(input("enter the value 2"))#b is second value of calculation
              try:
                c=a/b
              except ZeroDivisionError:
                print("zero")
              else:
                print(c)
            elif x==5:#the condition is if x is equal to 5 the condition is execute
              a=int(input("enter the value 1"))#a is first value of calculation
              b=int(input("enter the value 2"))#b is second value of calculation
              try:
                c=a//b
              except ZeroDivisionError:
                print("zero")
              else:
                print(c)
            if x==6:#the condition is if x is equal to 6 the condition is execute
              a=int(input("enter the value 1"))#a is first value of calculation
              b=int(input("enter the value 2"))#b is second value of calculation
              c=a**b
              print(c)
            elif x>6:
              print("option is not available")
calculate.sample(3)

        
