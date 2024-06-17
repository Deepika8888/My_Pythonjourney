# quiz making lol

print("Welcome to the quiz")

Quiz = input("Do you want to play our quiz? (Yes/No)?")
score = 0
score_1 = 0

if Quiz.lower() == "yes":
    print ("let's begin the journey.")
else:
    print("Goodbye. I am sad.")
    quit()

print("Welcome Welcome Boys and girls")

Name = input("Enter your name first: ")
Age = input("Enter youe age: ")
Fav_color = input ("Choose any color between Blue and Black: ")

if Fav_color.lower() == "blue":
    print ("You have entered in our blue quiz era: ")
    Quiz1 = input("Press 1 if you want to continue and press 2 if you want to go back: ")
    if Quiz1 == "1":
        print("Lets go: ")

        Question1 = input("Whats the biggest river in the earth: ")
        if Question1.lower() == "amazon" :
            print("you have got one point.")
            score +=1
        else: 
            print("oh. you lost it mate.")
        
        Question2 = input("Whats the tallest mountain in the earth: ")
        if Question2.lower() == "everest" :
            print("you have got it right:")
            score +=1
        else: 
            print("oh. you lost it mate.")
        
        Question3 = input ("Whats the biggest country in the world: ")
        if Question2.lower() == "russia":
            print ("you have got it right.")
            score +=1
        else:
            print("oh.you have lost it mate.")
            
            
        
    else:
        print ("Should have told earlier. Now bye")
        quit()

else:
    print("You have enter in our black quiz era.")
    Quiz2 = input(" press a if you want to continue or b if you don't.")
    if Quiz2.lower() == "a":
        print("let's go.")

        Questiona = input("What's the hottest planet in our solar system: ")
        if Questiona.lower() == "mercury" :
            print("You are genius.")
            score_1 += 1
        else: 
            print("I knew you were dumb lol.")
    
        Questionb = input("What's the name of our galaxy: ")
        if Questionb.lower() == "milkyway" :
            print("You are genius.")
            score_1 +=1
        else: 
            print("I knew you were dumb lol.")
       

        Questionc = input("What's the natural satellite of the earth's called: ")
        if Questionc.lower() == "moon":
             print("You are genius.")
             score_1 +=1
        else:
            print ("I knew you were dumb lol.")
            
            
        
    else:
        print("Why bother me if you didn't want to play lol.")
        quit()


Quiz3 = input("to know your score choose the color quiz you played: ")
if Quiz3.lower() == "blue":
    print(f"your total score is: ", score)
    print(f"so, you have gained {score} points miss {Name}")

else:
    print(f"your total score is: ", score_1)
    print(f"So, you have gained {score_1} points miss {Name}")

print("Hope you enjoyed our quiz.")










             



