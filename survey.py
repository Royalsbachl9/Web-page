import json

survey = [
    "What is your name?",

    "How old are you?",

    "How tall are you?",

    "What is your date of birth? (MM/DD/YYYY)",

    "How often do you drink coffee?",

    "How many hours do you sleep per day?"

]

keys = ["name", "age", "hight", "DOB", "coffee", "hour of sleep"]

all_surveys = []
done = "NO"
while done == "NO":
    loop = {}
    for i in range(len(survey)):
        ans = input(survey[i])
        loop[keys[i]] = ans
    all_surveys.append(loop)
    done = input("\nAre you done collecting information? Type YES or NO.     ").upper()
    print(all_surveys

f = open("allanswers.json", "w")
f.write('[\n')
index = 0
for t in list_of_answers:
    if (index < len(list_of_answers)-1):
        json.dump(t, f)
        f.write(',\n')
    else:
        json.dump(t, f)
        f.write('\n')
    index += 1

f.write(']')
f.close()
