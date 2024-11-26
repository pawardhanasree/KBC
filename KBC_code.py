questions = [
    ["Who developed Python Programming Language?", 
     "Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom",3],
    ["Which type of Programming does Python support?",
     "object-oriented programming","structured programming","functional programming"," all of the mentioned",4],
    ["Is Python case sensitive when dealing with identifiers?",
     "no","yes","machine dependent","none of the mentioned",2],
    ["Which of the following is the correct extension of the Python file?",
     ".python",".pl",".py",".p",3],
    ["Is Python code compiled or interpreted?","Python code is both compiled and interpreted","Python code is neither compiled nor interpreted",
     "Python code is only compiled","Python code is only interpreted",1],
    ["All keywords in Python are in _________",
     "Capitalized","lower case","UPPER CASE","None of the mentioned",4],
    ["Which of the following is used to define a block of code in Python language?",
     "Indentation","Key","Brackets","All of the mentioned",1],
    ["Which keyword is used for function in Python language?","Function","def","Fun","Define",2],
    ["Which of the following character is used to give single-line comments in Python?",
     "//","#","!","/*",2],
    ["Which of the following functions can help us to find the version of python that we are currently working on?",
     "sys.version(1)","sys.version(0)","sys.version()","sys.version",4],
    ["Python supports the creation of anonymous functions at runtime, using a construct called",
     "pi","anonymous","lambda","none of the mentioned",3],
    ["What is the order of precedence in python?",
     "Exponential, Parentheses, Multiplication, Division, Addition, Subtraction",
     "Exponential, Parentheses, Division, Multiplication, Addition, Subtraction",
     "Parentheses, Exponential, Multiplication, Addition, Division, Subtraction",
     "Parentheses, Exponential, Multiplication, Division, Addition, Subtraction",4],
    ["What does pip stand for python?","Pip Installs Python","Pip Installs Packages",
     "Preferred Installer Program","All of the mentioned",3],
    ["Which of the following is true for variable names in Python?", 
     "underscore and ampersand are the only two special characters allowed",
     "unlimited length",
     "all private members must have leading and trailing underscores",
     "none of the mentioned", 2],
    ["Which of the following functions is a built-in function in python?",
     "factorial()", "print()","seed()","sqrt()", 2]
]

amount = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000,
           1250000, 25000000, 5000000, 10000000]

money_earned = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\r\nQuestion {i+1} : {question[0]}")
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")
    option = int(input("Enter a number(0-4) - 0 to quit: "))
    if option == 0:
        money_earned = amount[i-1]
        break
    if (option == question[-1]):
        print(f"You have won Rs.{amount[i]}")
        if amount[i] == 10000:
            money_earned = amount[i]
        elif amount[i] == 320000:
            money_earned = amount[i]
    else:
        break
print(f"Congratulations, You have earned Rs.{money_earned}.")
