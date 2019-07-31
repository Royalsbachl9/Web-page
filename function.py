# def example():
#     print("hello")
# example()


# --- Define your functions below! ---
def introduction():
    print("Hi, my name is Heven")

valid_responses = [".."]
def is_valid_input(user_input , valid_responses):
    if user_input in valid_responses:
        return True
    else:
        return False


def no_help():
    question = input(" What is your favorite song? ")
    print("Mine too!")

def process_input(answer):
    if answer == "yes":
        say_greeting()

    else:
        no_help()

def say_greeting():
    say = input(" What can I help you with? ")
    if say == "play music":
        no_help()
    else:
        print("No resualt")
def say_default():
    print("That's cool")

# --- Put your main program below! ---
def main():
    introduction()
    while True:
        answer = input(" Can I help you? ")
        process_input(answer)
        break
main()


# example

# def say_hello(name):
#     print("Hi " + name)
#
# def main():
#     name = "Michelle"
#     name1 = "Genet"
#     name3 = "Heven"
#     say_hello(name, )
#
# main()

# Even numbers
# def is_even():
#     num = int(input("Enter a number : "))
#     if (num % 2) == 0:
#         print ("True")
#     else:
#         print("False")
# is_even()
