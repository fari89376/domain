#decisions in python
#multi-decisions program!
print("*********welcome to netflix********")
name=input("enter your Name:")
email=input("enter your email:")
password=input("enter your password:")
age=int(input("enter your age:"))
if age>=18:
    print(f"dear {name}, wellcome to netflix!")
    if email=="rafaysheikh67@gmail.com" and password=="admin567":
        print(f"dear {name}, welcome to the netflix sessions, please select category")
    elif email=="rafaysheikh67@gmail.com" and password=="admin567":
        print(f"dear {name}, welcome to the netflix sessions, please select category")
    elif email=="khankhan90@gmail.com" and password=="jhkl67":
        print(f"dear {name}, welcome to the netflix sessions, please select category")
    elif email=="alikhan76@gmail.com" and password=="opiu45":
        print(f"dear {name}, welcome to the netflix sessions, please select category")
    elif email=="uzairjaved@gmail.com" and password=="fatima":
        print(f"dear {name}, welcome to the netflix sessions, please select category")
    else:
        print(f"dear {name}, your login credentials are invalid!")
else:
    print("dear {name}, please watch pogo")