#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")
strippedPassword = test_password.strip()
# ^ takes out any eaxtra spaces
noFoundPWD = True
for line in f:
    # print (line)
    if strippedPassword == line.strip():
        foundPWD = False
        print("Sorry, try agin with a new password!")
        break

if nofoundPWD:
     print("Great password")
