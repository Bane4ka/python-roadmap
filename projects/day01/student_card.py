name=input("Name: ")
age=input("Age: ")
height=input("Height: ")
weight=input("Weight: ")
fav=input("Favorite programming language: ")
stud=input("Are you a student?: ").lower()
if stud=='yes' or stud=='y':
    stud='Student'
else:
    stud='Not a student'
print(f'''(
Name: {name}
Age: {age}
Height: {height}
Weight: {weight}
Favorite programming language: {fav}
status: {stud}''')