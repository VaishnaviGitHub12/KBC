# Welcome to my KBC (Kaun Banega carodpati) Game answer some question to win prize money $$$
ques = [
    ["what is normal body temperature in degree celcius?","37","38","98","36",1],

    ["What is the capital of India?","Mumbai","Kolkata","New Delhi ","Chennai",3],

    ["Which planet is known as the 'Red Planet'?","Venus","Mars ","Jupiter","Saturn",2],

    ["Which is the largest mammal on Earth?","African Elephant","Blue Whale","Giraffe","Rhinoceros",2],

    ["What is the currency of the United States?","Pound","Dollar ","Euro","Yen",2],

    ["Which festival is known as the 'Festival of Lights'?", "Holi", "Diwali", "Eid", "Christmas", 2],

    ["What is the smallest continent by land area?", "Africa", "Antarctica", "Australia", "Europe", 3],

    ["Which organ purifies blood in the human body?", "Heart", "Kidney", "Liver", "Lungs", 2],

    ["What is the national sport of India?", "Cricket", "Hockey", "Football", "Kabaddi", 2],

    ["Who wrote the epic 'Mahabharata'?", "Tulsidas", "Ved Vyasa", "Valmiki", "Kalidasa", 2],

    ["Which gas do plants absorb for photosynthesis?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 3],
]

levels =[ 100,200,500,1000,10000,20000,50000,100000,200000,300000,400000]
money=0
for i in range(0,len(ques)):
    que=ques[i]
    print("-----------------------------")
    print(f"\n\n Question for RS. {levels[i]}")
    print(que[0],"\n")
    print(f"1. {que[1]}    2. {que[2]}")
    print(f"3. {que[3]}    4. {que[4]}")
    reply= int(input("Enter your answer(1-4) : "))
    if (reply==que[-1]):
        print(f"Correct Answer, you Won RS. {levels[i]}")
        if (i == 4):
            money = 1000
        elif(i==9):
             money = 200000
        elif(i==10):
             money = 400000
            
    else:
        print("Wrong Answer!")
        break
print(f"\nYou take home Rs. {money}. Thank you for playing!")