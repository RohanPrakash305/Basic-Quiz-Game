print("Welcome to rohan's quiz game")
question_bank=[
    {"text":"The ability of one class to aquire methods aand atttributes from another class is called:","answer":"A"},

    {"text":"Which of the following is a type of inheritance?","answer":"D"},
    {"text":"What type of inheritance has multple subclasses to a single suerclass?","answer":"C"},
    {"text":"What is the depth of multilevel inheritance in tpython?","answer":"C"},
    {"text":"What does MRO stand for?","answer":"B"},
]

options=[
     
     ["A.Inheritance","B.Abstraction","C.polymorphism","d.objects"],
     ["A.Single","B.Double","C.Nultiple","D.Both A and C"],
     ["A.two level","B.any level","C.many level","D.None of these"],
     ["A.method Recursive Object","B.Methood Resolution Order","C.Main Resolution Order","D.Method resolution Object"],
]

score=0
def check_answer(user_guess,correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False
    
for question_num in range(len(question_bank)):
    print("------------------------")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
    check = True
    while check:
        guess=input("Enter your answer (A/B/C/D):")
        guess = guess.upper()
        is_correct=check_answer(guess,question_bank[question_num]["answer"])
        #print(guess, question_bank[question_num]["answer"])
        if is_correct:
            print("Corect Answer")
            score += 1
            break
        else:
            print("Incorect Answer")
            break
    continue1 = input("You want to continue if you want the press y and if not then press n:")
    if continue1 == 'y'.lower():
        continue
    else:
        print("********------Thank for quiz ----********")
        break
#Rohan Prakash
#atulraj844114@gmail.com
#6200652230
#