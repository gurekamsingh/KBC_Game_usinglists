name = input("Enter your Name :").title()
print("Hi", name, "Welcome to Kon Banega Crorepati\nlet's begin the game!")
# questions = ["In which year did All India Football Federation get FIFA affiliation?", "What are mammals covered with?", "The mountain peak Kedarkantha is situated in which state?", "Which of the following movies became the first Bollywood film ever to release in Saudi Arabia?",
#               "Which of the following author has written the book /‘India of our Dreams’?"]
# answers = ["1948", "Hair or Fur", "Uttarakhand", "Gold", "M.V. Kamath"]
# t = [q for q in questions if questions[q] == answers[q]]
# print("this is the correct answer")
i=0
for i in range(2):
    print("In which year did All India Football Federation get FIFA affiliation?")
    print("A:1960")
    print("B:1943")
    print("C:1948")
    print("D:1961")
    user = input("Enter the correct option :").title()
    if user == "C":
        print("That's the right answer.\nYou won $1000!")
    else:
        print("That's not a right answer")
        break
    print("What are mammals covered with?")
    print("A:Steel")
    print("B:Leather")
    print("C:Velvet")
    print("D:Hair and fur")
    user1 = input("Enter the correct option :").title()
    if user1 == "D":
        print("That's the right answer.\nYou won $10000!")
    else:
        print("That's not a write answer")
        break
    print("The mountain peak Kedarkantha is situated in which state?")
    print("A:Andhra pradesh")
    print("B:Nepal")
    print("C:UP")
    print("D:Uttrakhand")
    user2 = input("Enter the correct option :").title()
    if user2 == "D":
        print("That's the right answer.\nYou won $50000!")
    else:
        print("That's not a write answer")
        break
    print("Which of the following movies became the first Bollywood film ever to release in Saudi Arabia?")
    print("A:Chak de India")
    print("B:Gold")
    print("C:Pathaan")
    print("D:Bhool bhulaiya 2")
    user3 = input("Enter the correct option :").title()
    if user3 == "B":
        print("That's the right answer.\nYou won $75000!")
    else:
        print("That's not a write answer")
        break
    print("Which of the following author has written the book ‘India of our Dreams’?")
    print("A:Chetan bhagat")
    print("B:M.V. Kamath")
    print("C:Durjoy Dutta")
    print("D:John Grisham")
    user4 = input("Enter the correct option :").title()
    if user4 == "B":
        print("That's the right answer.\nYou won $100000!")
        print("CONGRATULATIONS!!!", name)
        u = input("Do you want to replay the game?\n").title()
        if u == "Yes":
            continue
        else:
            break
    else:
        print("That's not a write answer")
        break


