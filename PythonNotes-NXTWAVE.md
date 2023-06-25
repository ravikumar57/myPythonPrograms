#### 17/06/2023 ####
# Variables and Data Types: 
    --String: Stream of Characters that enclosed in quotes
    Eg.: "Cricket", "Ravi Kumar", "1235"
    --integer: All numbers(Positive and Negative) without fractional part
    Eg.: -1, -2, 0, 8, 2, 65
    --float: all the numbers(Positive and Negative) with decimal point
    Eg.: 5.3 --> 3 is float value
         -89.47 --> 47 is float value
    --Boolean: Data that have one of two possible values. 
    Eg.: Either Yes or No, On or Off, True or False etc., 
            Syntax for Boolean::-- First letter should be capital
                Eg.: True or False--> Correct where true or false-->Incorrect
2      --> integer
"2.0"  --> string
2.0    --> float
True   --> Boolean
"True" --> string
** Assigning Value to a variable
--- Assigning an integer 10 to a variable age 
    age = 10 --> age is Variable name, = is Assignment Operator, 10 is the Value


# Sequence of Instructions: 
** Printing and Assignments of Variables:
---A program is a sequeence of instructions to a computer to execute.
    Eg.: **age = 10
           print(age) --> A variable gets created when you assign a value to it for the first time. Output is 10. 
        **age = 10
          print("age") --> Output is age
        **print(age)
          age = 10  --> Python executes line by line. Variable 'age' is not yet created by the time we tried to print. Output is Error: name 'age' is not defined
        **age=10
            print(age) --> Having spaces at the begining of line causes errors. 
                            Error: File "main.py", line 3
                                     b = a + b
                                        ^
                            IndentationError: unexpected indent
        **a = 1
          print(a)
          a = 2        --> Values in variables will changes. Output is 1
        **a = 1
          print(a)
          a = 2
          print(a)    --> Values in variables will cahnges. Output is 1
                                                                      2
        **a = 1
          a = 2
          print(a)    --> Values in variables will cahnges. Output is 2
        **a = 1
          a = 2
          print(a)
          print(a)    --> Values in variables will cahnges. Output is 2
                                                                      2  
        **a = 2
          print(a)
          a = a + 1
          print(a)    --> Output is 2   3
        **a = 1
          b = 2
          a = b + 1
          print(a)
          print(b)   --> Output is 3    2
** Order of Evaluation for Expressions: 
---An expression is a valid combination of values, variables and operators.
    Eg.: a * b
        a + 2
        5 * 2 + 3 * 4
---Expressions- a = 2 + 3
                b = 3 * 2
                c = a + b
                print(a)
                print(b)
                print(c)     --> Output is  5    6   11
---Order of Operations- BODMAS
                        The standard order of evaluating an expression
                        Brackets (B)
                        Orders (O)
                        Division (D)
                        Multiplication (M)
                        Addition (A)
                        Subtraction (S)
                    Eg.: print(10 / 2 + 3)
                         print(10 / (2 + 3))    --> Output is 8.0   2.0


#### 18/06/2023 ####
# Basics of Input and Output
** Concatenation Repetation of Strings:
--- Adding two or more no.of strings is called String Concatenation.
    Eg.: ***a = 1 + 2
            print(a)  --> Out is 3
         ***a = "1" + "2"
            print(a)  --> Out is 12 (Not Twelve It is One Two)
         ***a = "Hello" + " " + "World"
            print(a)  --> Output is Hello World
         ***username = "Ravi"
            print("Hi " + username)  --> Output is Hi Ravi

     --- Cancatenation Errors: String Concatenation is possible only with strings.
        Eg.:***a = "*" + 10
               print(a)   --> Output is  File "main.py", line 1
                                            a = "*" + 10
                                                  ^
                                              TypeError: 
                                  can only concatenate str (not "int" ) to str
     --- String Repetation: '*' operator is used for repeating strings any number of times as required.
       Eg.: ***a = "*" * 10
               print(a)     ---> Output is **********
            ***s = "Python"
               s = ("* " * 3) + s + (" *" * 3)
               print(s)      ---> Output is   * * * Python * * *

     --- Length of String: 'len()' returns the number of characters in a given string.
       Eg.: ***username = "Ravi"
               length = len(username)
               print(length)  ---> Output is 4
            ***

** Reading inputs I/O Basics:
--- Take input from User: input() Allows flexibility to take the input from user. It Reads a line of input as a string. 
    Eg.: username = input()
        ***username = input()
           length = len(username)
           print(length)  ---> Input: Ravikumar-- Output:9 ; Input: Ravi Kumar-- Output:10.
        ***username = input()
           age= input()
           print(username + " is " + age + " years old" ) --> Input: RaviKumar 23 --- Output: RaviKumar is 23 years old
           
** Accessing a character Indexing:
--- We can access individual character in the string using their positions (which starts from 0) is called "Indexing".These positions are also called as index.
    Eg.: username = "Ravi"  0123  ---> username[0] is R, username[1] is a, username[2] is v
        ***username = "Ravi"
           print(username[0])
           print(username[1])
           print(username[2])
           print(username[3])  --> Output is: R
                                              a
                                              v
                                              i
        ***username = "Ravi"
           print(username[4])   --> Output is: IndexError: string index out of Range. IndexError: Attempting to use an index that is too large will result in an error.



#### 19/06/2023 ####
# Type Conversions: 
** Strings Slicing:
--- Obtaining a part of a string is called String Slicing.
    Syntax: variable_name[start_index:end_index]  --> Start from the start_index and stops at end_index. And end_index is not included in the slice.
    Eg.: --message = "Hi Ravi"
           part = message[3:6]
           print(part)          --> Output is Rav
         --message = "Hi Ravi"
           part = message[3:7]
           print(part)          --> Output is Ravi

--- Slicing to End: If end index is not specified, slicing stops at the end of the string. 
    Eg.: message = "Hi Ravi"
         part = message[3:]
         print(part)            --> Output is Ravi
--- Slicing from Start: If start index is not specified, slicing starts from the index 0.
    Eg.: message = "Hi Ravi"
         part = message[:2]
         print(part)            --> Output is Hi
--- Slicing for No start and No End: If Start and End index are not specified, then sliced string is same as the original string.
    Eg.: message = "Hi Ravi"
         part = message[:]
         print(part)            --> Output is Hi Ravi


** Identifying Data Types type():
--- Check the datatype of the variable or value using type().
    Printing Data Type: Eg.: print(type(10))
                             print(type(4.2))
                             print(type("Hi"))      --> Output is <class 'int'>
                                                                  <class 'float'>
                                                                  <class 'str'>

** Type Conversions- Changing Data Types:  
--- Converting the value of one data type to another data type is called Type Conversion or Type Casting.
--- We can convert: String to Integer
                    Integer to Float
                    Float to String and so on.
--- String to Integer: int() converts valid data of any type to integer.
 Eg.: ***a = "5"
         a = int(a)
         print(type(a))
         print(a)             --> Output is <class 'int'>
                                                  5
      ***a = "Five"
         a = int(a)
         print(type(a))       --> Output is ValueError: 
                                            invalid literal for int() with base 
      ***a = "5.0"
         a = int(a)
         print(type(a))        -->Output is ValueError: 
                                            invalid literal for int() with base 

int() -> Converts to integer data type
float() -> Converts to float data type
str() -> Converts to string data type
bool() -> Converts to boolean data type 

#### 20/06/2023 ####
# Operational & Conditional Operators:
--- Releational Operators Comparing Numbers: 
    Relational Operators are used to compare the values and gives True or False as the result of Comparision.
    > is greater than
    < is less than
    Eg.: print(6<5)     --> Output is False
         print(2>1)     --> Output is True
         print(3 = 3)   --> Output is SyntaxError: expression cannot contain assignment, perhaps
         print(3 < = 6) --> Output is SyntaxError: invalid (Space between relational operators ==, >=, <= , != is not valid in Python.)
--- COmparing integers and floats:
    Eg.: print(12 == 12.0)      --> Output is True
         print(12 == 12.1)      --> Output is False
--- Comparing Strings:
    Eg: print("ABC" == "ABC")   --> Output is True
        print("CBA" != "ABC")   --> Output is True
        print("ABC" == "abc")   --> Output is False (Python is case sensitive. It means X (Capital letter) and x (small letter) are not the same in Python.)

Operator	Name
>         Is greater than
<	        Is less than
==	      Is equal to
<=	      Is less than or equal to
>=	      Is greater than or equal to
!=	      Is not equal to


--- Equality Comparing Strings:
    Eg.: print(True == "True")    --> Output is False
         print(123 == "123")      --> Output is False
         print(1.1 == "1.1")      --> Output is False


#### 21/06/2023 ####
# Operational & Logical Operators:
--- Logical Operators (and, or, not): The logical operators are used to perform logical operations on Boolean values.
Gives True or False as the result.  

# and operator: AND operator gives True if both the boolean values are true else it gives False.
--- A(True) and B(True) --> True 
--- A(True) and B(False) --> False 
--- A(False) and B(True) --> False 
--- A(False) and B(False) --> False 
    Eg.: print(True and True)   --> Output is True
         print((2 < 3) and (1 < 2))     --> Output is True.

# or operator: or operator gives True if any one of the boolean values is true else it gives False.
--- A(True) or B(True) --> True 
--- A(True) or B(False) --> True 
--- A(False) or B(True) --> True 
--- A(False) or B(False) --> False 
    Eg.: print(False or False)        --> Output is False
         print((2 < 3) or (2 < 1))    --> Output is True

# not operator: not operator gives the opposite value.
--- not(True)    --> False
--- not(False)   --> True
    Eg.: print(not(False))      --> Output is True
         print(not(2 < 3))      --> Output is False


# Operational & Conditional Statements:
--- If Statement Conditions & Conditional Block Identation:

***Conditional Statement: Conditional Statement allows you to execute a block of code only when a specific condition is True.
      if CONDITION:
***Conditional Block: Block of code which executes only if a condition True.(Block of Code: A sequence of instructions are called block of code.)
* Syntax: if CONDITION:
             Block of Code         --> Executes only when condition is True.

***Indentation: Space(s) in front of the conditional block is called indentation.
                Indentation(spacing) is used to identify Conditional Block.
                Standard practice is to use four spaces for indentation.      

      Eg.: **a = int(input())   
             b = int(input())
             if a > b:
                 print(a-b)
             print(a+b)           ---> Input: 1,2 --> Output is 3
           **a = int(input())   
             b = int(input())
             if a > b:
                 print(a-b)
             print(a+b)           ---> Input: 2,1 --> Output is 1 3


--- If- Else Syntax:
When If - Else conditional statement is used, Else block of code executes if the condition is False.
* Syntax: if CONDITION:
              Block of Code         --> Executes only when condition is True.
          else:
              Block of Code         --> Executes only when condition is False.
Eg.: name = input()
     age = input()
     age = int(age)

     if age >= 18:
         print(name + " is eligible to vote.")
     else:
         print(name + " is not eligible to vote.")


#### 21/06/2023 ####
# Nested Conditions:
* Problem Solving and Debugging:
--- Problem Solving and Approachong Problem:
Approaching Problems (Coding): Reading Inputs, Processing and Printing Outputs.

1. Write a program to print greatest between two numbers.:
    a = input()
    b = input()
    a = int(a)
    b = int(b)
    if a > b:
        print(a)
    else:
        print(b)

2. Write a program that reads a single line of input and prints the first and last character of given input and prints the asterisk character (*) in place of remaining characters.
    a = input()
    l = len(a)
    first_letter = a[0]
    last_letter = a[l-1]
    remaining_string = "*" * (l-2)
    result = first_letter + remaining_string +last_letter
    print(result)

3. Write a program to check if the given two digit number is greater than 25 and its first digit is greater than its second digit.
# Comparing Digits
    n = int(input())
    if n > 25:
        n_string = str(n)
        first_digit = n_string[0]
        second_digit = n_string[1]
        first_digit = int(first_digit)
        second_digit = int(second_digit)
        if first_digit > second_digit:
            print(True)
        else:
            print(False)
    else:
        print(False)

#### 24/06/2023 ####
* Modulus and Exponent - Arithmetic Operators:
--- Modulus Operator(%): To find the remainder, we use Modulus Operator(%).
    Eg.: print(6%3)     --> Output: 0
         print(8%3)     --> Output: 2

1. Write a program that determines if the given number is "Even" or "Odd".
# evenorodd
    n = int(input())
    if (n%2 == 0):
        Number = str(n)
        print(Number + " is Even Numer")
    else:
        Number = str(n)
        print(Number + " is Odd Numer")

--- Exponent Operator(**): To calculate a power b we use exponent operator( ** )
                    Eg.: a ** b     --> Output: a*a*a*a*a*a*a*a*a*a*a*a*a....... b times(a power b)
                         print(2**3)    --> Output: 8
                         print(5**2)    --> Output: 25
2. Given Two integers a and b, Find the greatest among (a power b) and (b power a) and print the value.
# greaterofapowerbandbpowera
a = int(input())
b = int(input())
a_power_b = (a ** b)
b_power_a = (b ** a)
if a_power_b > b_power_a:
    print(a_power_b)
else:
    print(b_power_a)

3. Given a two digit number. Print "Lucky Number" if any of the conditions are satisfied: The Number is multiple of 9. One of the digits is 9., Print "Unlucky Number" in all Other Cases.
# LuckyNumber
n = input()
if len(n) == 2:
    int_n = int(n)
    remainder = int_n % 9
    is_multipleof_9 = (remainder == 0)
    n_string = str(int_n)
    first_digit = int(n_string[0])
    second_digit = int(n_string[1])
    first_with_9 = (first_digit == 9)
    Second_with_9 = (second_digit ==9)
    any_digit_is_9 = first_with_9 or Second_with_9
    condition = any_digit_is_9 or is_multipleof_9
    if condition:
        print("Lucky Number")
    else:
        print("Unlucky Number")
else:
    print("Unlucky Number")












--- Debugging and Printing Statements:




    








