questions=[
    'who is the developer of python language?',
    'when did India get independent?',
    'what is the currency in India?',
    'which state does banglore belong to?',
    'which is the latest iphone?',
    ]
answers=[
    'guido van',
    '1947',
    'INR',
    'karnataka',
    'iphone 12',
    ]
options=[
    ['Denniscritchi','Alan Frank','Albent','guido van'],
    ['1947','1959','2000','1985'],
    ['pounds','dollars','INR','euros'],
    ['rajasthan','karnataka','west bengal','assam'],
    ['iphone SE','iphone 13','iphone 12','iphone 11'],
   ]

def play_game(username,questions,answers,options):
    print("Hello",username,"to the KBC game")
    score = 0
    for i in range(len(questions)):
        current_question = questions [i]
        current_answer = answers[i]
        current_question_options = options[i]
        print("Question :",current_question)
        for index,each_option in  enumerate(current_question_options):
            print(index+1,") ",each_option,sep ='')
        user_answer_index = int(input("enter your choice(1,2,3 or 4): "))
        user_answer = current_question_options[user_answer_index - 1]
        if user_answer == current_answer:
            print("correct answer")
            score = score+1
        else:
            print("wrong answer")
            break
    print("your final score is",score)
    return username,score
    
def veiw_scores(names_and_scores):
    for name,score in names_and_scores.items():
        print(name,"has scored",score)

def KBC(questions,answers,options):
    names_and_scores={}

    while True:
        print("welcome to the KBC game!")
        print("1.play Game\n,2.view scores\n,3.Exit")
        choice=int(input("please enter yout choice:"))
        if choice == 1:
            username = input("please enter your name:")
            username,score = play_game(username,questions,answers,options)
            names_and_scores[username]=score
            

        elif choice == 2:
            veiw_scores(names_and_scores)

        elif choice == 3:
            break

        else:
            print("your choice is valid")
                
KBC(questions,answers,options)
