print("You wake up in an place that looks like an empty basement, and you have no idea where you are.")
print("As you're looking around you are tied to a wall around your waist. As you are looking around you see: A hammer, A lighter, A knife, A shelf, and a half bottle of water.")
print("-------------------------------------")


def start():
    print("As your looking the only things in reach are the water bottle and the lighter.")
    print("1. Grab the lighter.")
    print("2. Grab the water bottle.")

    choice = input("Which do you choose?\n> ")

    if choice == "1":
        lighter()
    elif choice == "2":
        water()
    else:
        print("Invalid input. Please enter a number 1 or 2.")
        start()


def water():
    print("You grab the water bottle, and open it. It doesn't smell like water, so you pour some onto the rope to see what happens. The rope starts to disintegrate, and you get out!\n")
    print("----------------------")
    print("Now that you got out of the rope what do you want to do?\n")
    print("1. Look around to see if you can escape.")
    print("2. Explore the basment for other people.")

    choice = input("Which do you choose?\n> ")

    if choice == "1":
        escape()
    elif choice == "2":
        people()
    else:
        ("Invalid input. Please enter a number 1 or 2.")
        water()


def lighter():
    print("You grab the lighter and start to burn the rope. The rope starts on fire, and you back away from it once its off of you.")
    print("---------------------------")
    print("Now that you are out of the rope what do you want to do?\n")
    print("1. Pour the 'water' on the rope to put out the fire.")
    print("2. Leave the fire, and start to look around.")

    choice = input("Which do you choose?\n> ")

    if choice == "1":
        death()
    elif choice == "2":
        people()
    else:
        print("Invalid input. Please enter a number 1 or 2.")
        lighter()


def escape():
    print("As you are looking around you can only find one door, and one window.")
    print("--------------------------------")
    print("1. Try to escape out the window.")
    print("2. Try to escape out the door.")

    choice = input("Choose 1 or 2.\n> ")

    if choice == "1":
        window()
    elif choice == "2":
        door()
    else:
        print("Invalid Input.")
        escape()


def people():
    print("While looking around you see a door and hear strange noises coming from inside.")
    print("-------------------------")
    print("1. Open the door to see what's inside.")
    print("2. Try leaving out the window.")

    choice = input("Choose 1 or 2.\n> ")

    if choice == "1":
        door()
    elif choice == "2":
        window()
    else:
        print("Invalid input.")
        people()


def death():
    print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
    print("The fire starts to get bigger and bigger. You have nothing else to put it out with, and you burn to death with no escape.")
    print("Ending 1: Fire")


def window():
    print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
    print("You break the glass and look outside. It's pitch black out so you try taking a step, but you slip and fall 3 stories down and landing on your head.")
    print("Ending 2: The Fall")


def door():
    ("________________________________________________")
    print("You open the door and see 3 people inside. They are all tied up just as you were.")
    print("1. Help them.")
    print("2. Go back to the room.")
    print("3. Don't help them and explore the room.")

    choice = input("Choose 1,2, or 3.\n> ")

    if choice == "1":
        help()
    elif choice == "2":
        leave()
    elif choice == "3":
        nohelp()
    else:
        print("Invalid input.")
        door()

def help():
    print("_--------------------------------")
    print("They are very grateful for your kindness and decide to help you.")
    print("You see stairs and a small door.")
    print("1. Go down the stairs.")
    print("2. Go through the door.")

    choice = input("Choose 1 or 2.\n> ")

    if choice == "1":
        stairstwo()
    elif choice == "2":
        smalldoor()
    else:
        print("Invalid input.")
        help()


def leave():
    print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
    print("You go back to the room and see a strange man dressed in all black. He throws a potato at you...\n You notice the window is open and before you can react you are falling out the window. You die from ᵖᵒᵗᵃᵗᵒ.")
    print("Ending 3: ᵖᵒᵗᵃᵗᵒ...")
    print("ʸᵒᵘ ˢʰᵒᵘˡᵈ ʰᵃᵛᵉ ʰᵉˡᵖᵉᵈ ᵗʰᵉᵐ...")


def nohelp():
    print("ʸᵒᵘ ᵃʳᵉ ᵐᵃᵏᶦⁿᵍ ᵃ ᵐᶦˢᵗᵃᵏᵉ...")
    print("----------------------------------")
    print("You see a stairway and realize that you are not in a basment.")
    print("1. Go down the stairs.")
    print("2. Go back to the room...")

    choice = input("Choose 1 or 2.\n> ")

    if choice == "1":
        stairstwo()
    elif choice == "2":
        leave()
    else:
        print("Invalid input.")
        nohelp()

def stairsone():
    print("-------------------------------")
    print("You go down 3 flights of stairs and you don't see anything that catches your attention. You hear screaming in the distance and someone in your group says run.")
    print("1. Run.")
    print("2. Go towards the screaming.")

    choice = input("Choose 1 or 2.\n> ")

    if choice == "1":
        run()
    elif choice == "2":
        yes()
    else:
        print("Pick 1 or 2")
        stairsone()


def stairstwo():
    print("----------------------------------")
    print("As you're walking down the stairs you hear someone screaming in the distance. It sounds like its coming from below you.")
    print("Do you want to keep going?")

    choice = input(" No\n> ")
    if choice == "No":
        no()
    else:
        print("Say Yes or No.")
        stairstwo()


def smalldoor():
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("As you enter the room you notice that it is very cold. There is someone sleeping inside and the room is dark. Then you start to hear screaming in the distance.")
    print("Hide!")
    print("You find the nearest hiding spot and so do the others. The screamming gets closer and closer...")
    print("The screaming come in the room then stops. The person that was sleeping finally wakes up and says 'Whats wrong son' you peek out you hiding spot a bit and see a little kid.")
    print("-----------------------------------------")
    print("The kid says 'They're not where we left them...' you realize hes talking about you and the people... you have to leave.")
    print("They both rush out of the room to go and search for you.")
    print("1. Stay hidden.")
    print("2. Try to escape.")

    choice = input("Choose 1 or 2.\n> ")

    if choice == "1":
        hidden()
    elif choice == "2":
        escap()
    else:
        ("Choose 1 or 2.")
        smalldoor()


def yes():
    print("--------------------------------")
    print("The screaming gets louder and louder, then you see someone running up the stairs. He stops and looks at you and then keeps running.")
    print("1. Follow him.")
    print("2. Run.")

    choice = input("Enter 1 or 2.\n> ")

    if choice == "1":
        follow()
    elif choice == "2":
        runbad()
    else:
        print("Invalid input.")
        yes()


def no():
    print("-----------------------------------------")
    print("The sceaming is getting louder.")
    print("You go up the stairs and see a door.")
    print("1. Hide.")

    choice = input("Enter 1.\n> ")

    if choice == "1":
        hide()
    else:
        print("Enter 1")
        no()


def run():
    print("---------------------------------------------------------------------------------------------------------------------")
    print("You run down the stairs, while you are running you see a little boy screaming. He stops on the stair and watches you them runs up the stairs.")
    print("1. Go and hide.")
    print("2. Escape.")

    choice = input("Choose 1 or 2.\n> ")

    if choice == "1":
        hides()
    elif choice == "2":
        go()
    else:
        print("Invalid input enter 1 or 2.")
        run()


def runbad():
    print("As you're running the lights go out and you hear an alarm going off.\n You hear someone running down the stairs and you turn around to look and you get tackled to the ground. \n You hit your head and everything goes dark. You thought you died?")
    print("Wake up...")
    print("Ending 4: The end... or is it?")
    print("_________________________________________________________")
    print("_________________________________________________________")
    print("_________________________________________________________")
    print("_________________________________________________________")
    print("_________________________________________________________")
    print("_________________________________________________________")
    start()

def hidden():
    print("-----------------------------------------------------------------------------------------")
    print("They start looking and never think to look in the room. You're safe. For now...")
    print("They soon give up after searching the whole house. The little boy says, 'But where could they have gone. We have alarms on the door they have to be in here.")
    print("They go to sleep. Now it your time.")
    print("1. Escape.")
    
    choice = input("Enter 1 or 2.\n> ")

    if choice == "1":
        escap()
    else:
        print("Invalid input. Enter 1.")
        hidden()

def escap():
    print("-------------------------------------------------------------------------------------------------------------------")
    print("You run down the stairs as quiet as possible. Everyone comes with you and once your on the 1st floor you see a very secured door. You go up to the door to see if you can unlock it. \n you realize you need 2 diffrent keys and ask your group if they know where any keys are.")
    print("Someone from your group says yes and you guys go and search for keys. There's one on the 1st floor, one on the 2nd, and one on the 3rd. 2 people choose the 3rd floor.")
    print("1. 1st floor.")
    print("2. 2nd floor.")

    choice = input("1 or 2.\n> ")

    if choice == "1":
        first()
    elif choice == "2":
        second()
    else:
        print("Invlid input.")
        escape()

        
def follow():
    print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")
    print("You follow him up the stairs and into a room. You try to stay out of site as you don't know who he is.\nYou overhear his conversation with somesome in the room, 'dad they aren't where we leave them. They're trying to escape we has to get them.")
    print("Before you can react they both run out of the room and see you right away. They grab you and throw you back into a room. \n It's very dark and you can't see anything in the room.")
    print("You try getting out of the room and you just fall to the floor. You try to stand back up but you can't move. Soon your vision goes black...")
    print("Ending 5: ???")

def hides():
    print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")
    print("You try to hide and little do you know they saw you hide. As soon as you think you're safe, they find you they rip you out of the closet, take your socks off, and start tickling your toes.")
    print("Ending 6: Tickle Tickle")

def hide():
    print("-------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("You all go and hide into diffrent spots in hope not to be found. You heard lots of searching and fear that you will be found. \n After a long time of waiting you stop hearing noises. You peak out of your hiding spot and see the people you were with.")
    print("You all go out of you hiding spots and go down the stairs. The door is locked with 3 locks and you need 3 diffrent keys.")
    print("Someone in your group says that we need to get out of here and get the keys. 2 of them called the 3rd floor.")
    print("1st floor")
    print("2nd floor")

    choice = input("1 or 2.\n> ")

    if choice == "1":
        first()
    elif choice == "2":
        second()
    else:
        print("Invalid input 1 or 2.")
        hide()

def go():
    print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")
    print("You try to escape and see that there are many locks on the door. You need 3 keys to get out. The others in your group didn't follow you and you have no idea where the keys are. \n The little boy has came back and the lights turn off.")
    print("You realized that he is what we need to run from...Do you want to run?")
    print("--------------------------------------------------------------------------------------")

    choice = input("Yes or no?\n> ")

    if choice == "Yes":
        print("You have already been caught. You can't move.")
        print("Ending 7: Escape")
    elif choice == "No":
        print("You got caught...")
        print("Ending 7: Escape")
    else:
        print("You can't get out of this one... Yes or No.")
        go()

def first():
    print("-------------------------------------------------------------------------------------------------------------------")
    print("You picked the 1st floor so you don't go up any stairs. The other guy with you said 'I will go to second then, it should be in one of the rooms next to you.")
    print("He goes up the the 2nd floor and you now have to find a key.")
    print("Go into 1st room")
    print("Go into 2nd room.")

    choice = input("1 or 2.\n> ")

    if choice == "1":
        roomone()
    elif choice == "2":
        roomtwo()
    else:
        print("Invalid input. Enter 1 or 2.")
        first()


def second():
    print("-------------------------------------------------------------------------------------------------------------------")
    print("The other guy your're with said 'I will stay on this floor, the key is in the room with the cow'.")
    print("You go up to the 2nd floor and theres a door with a cow on it so you go in and see a cow inside. \n You walk in and there is a cabnet and a closet.")
    print("1. Check the closet.")
    print("2. Check the cabnet.")

    choice = input("1 or 2.\n> ")

    if choice == "1":
        closet()
    elif choice == "2":
        cabnet()
    else:
        print("Invalid input try again.")
        second()


def roomone():
    print("-------------------------------------------------------------------------------------------------------------------")
    print("You walk into the first roon and you only see a closet in the room. You go and check the closet and there is nothing in it.")
    print("Go to the 2nd room.")
    
    choice = input("Yes or no..?\n> ")

    if choice == "Yes":
        roomtwo()
    elif choice == "No":
        first()
    else:
        print("Invalid input")
        roomone()


def roomtwo():
    print("-------------------------------------------------------------------------------------------------------------------")
    print("As you enter the room there is only a little book. You go up to it and open the book and a key falls out.\n You go back out to the door and unlock one of the locks with your key.")
    print("1. Wait for others.")
    print("2. Go to the 2nd floor and help look.")

    choice = input("1 or 2?\n> ")

    if choice == "1":
        wait()
    elif choice == "2":
        two()
    else:
        print("Invalid input.")
        roomtwo()


def closet():
    print("-------------------------------------------------------------------------------------------------------------------")
    print("You open the closet and you don't see anything at first and you look in a little drawer and see and key. You grab the key and the cow starts to walk towards you.")
    print("1. run.")
    print("2. Walk slowly so it doesn't chase.")

    choice = input("Enter 1 or 2.\n> ")

    if choice == "1":
        cow()
    elif choice == "2":
        walk()
    else:
        print("Invalid input.")
        closet()


def cabnet():
    print("-------------------------------------------------------------------------------------------------------------------")
    print("You check the cabinet and its just empty and there's only the closet left to check.")
    print("Check the closet?")

    choice = input("Yes or No?\n> ")

    if choice == "Yes":
        closet()
    elif choice == "No":
        print("You need the key or they will find you.")
        cabnet()
    else:
        print("Invalid input.")
        cabnet()


def wait():
    print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
    print("You hear a loud bang and it sounds like its coming from upstairs. Then you look over and a cow is running full speed towards you. You get trampled by the cow.")
    print("Ending 8: Cow")


def two():
    print("----------------------------------------------------------------------------")
    print("You go up to the 2nd floor and you see the other guy got the key but he's slowly backing away. Then from out of a door a cow starts to walk out of the room towards him.")
    print("He looks out you and mouthes 'Help")
    print("1. Help him")
    print("2. Don't help")

    choice = input("1 or 2.\n> ")

    if choice == "1":
        save()
    elif choice == "2":
        boi()
    else:
        print("Invalid input.")
        two()


def cow():
    print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
    print("The cow starts to run at you but it runs pretty fast. You run down the stairs and see everyone downstairs. The cow catches up to you and runs you over.")
    print("You struggle to get up and see someone take the key from you and they all leave...")
    print("Ending 9: Betrayal...")
    print("Do you want a 2nd chance?")

    choice = input("Yes or No.\n> ")

    if choice == "Yes":
        escap()
    elif choice == "No":
        ohok()
    else:
        print("Invalid input. Yes or No.")
        cow()


def walk():
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("The cow just keeps walking toward you and as your walking you turning around and go down the stairs. The others are downstairs also. They see the cow and look frightend.")
    print("You calmly go to the door and open the only lock that isn't unlocked. The door opens!")
    print("You all walk outside and an alarm goes off inside someone in you group starts running.")
    print("Do you want to go with them?")

    choice = input("Yes or No?\n> ")

    if choice == "Yes":
        ending()
    elif choice == "No":
        what()
    else:
        print("Invalid input. Yes or No.")
        walk()


def save():
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("You see a rock on the floor so you grab it and throw it across the room. The cow starts running at it and you both go downstairs.")
    print("The others and already downstairs so you go and unlcok the door with the keys. You all go out of the door and suddenly an alarm starts going off and one of the people start to run.")
    print("Do you want to follow him?")

    choice = input("Yes or No.\n> ")

    if choice == "Yes":
        ending()
    elif choice == "No":
        what()
    else:
        print("Invalid input.")
        save()


def boi():
    print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
    print("The cow runs into him and you look away and the cow then going toward you and pushes you down the stairs.")
    print("ending 12: Stairs")


def ohok():
    print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
    print("Docimedis perdidit manicilia dua qui illas involavit ut mentes suas perdat et oculos suos in fano ubi destinat...")
    print("Ending 10: The curse")


def ending():
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("You guys all run as fast as you can. Your in a dark forest ajd it's cold out. You run for what feels like hours and you see lights ahead.")
    print("There's a building up ahead it looks like a gas staition. You guys run to the gas station and walk in out of breath. One person in your group asks for a phone.")
    print("He calls the police and the guy on the phone say 'Stay right there we were told you escaped from a facility and are dangerous.")
    print("You need to run...")
    print("1. Steal a car and go")
    print("2. Run.")

    choice = input("1 or 2.\n> ")

    if choice == "1":
        car()
    elif choice == "2":
        cold()
    else:
        print("Invalid input.")
        ending()


def what():
    print("????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
    print("You don't follow them and run a diffrent way. You then hear someone behind you and it sounds like running. Someone comes up behind you and grabs you and pushes you to the floor.")
    print("They put something over your mouth and you start getting tired. Before you fall asleep you hear 'They're getting smarter we need to make this place more secure or people will start asking questions...")
    print("Ending 11: Is this a game?")
    print("??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
    start()


def car():
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("You jump into the car and everyone else jumps in also. You're driving... You start to drive but you're not very experienced so you back into the wall.")
    print("You floor it and zoom away from the gas station. You turn on the radio and the first thing you hear is 'There are 4 escaped prisoners and they are very dangerous please bewear.")
    print("As you are driving you notice that there is a city up ahead. You start to slow down so that the police don't pull you over.")
    print("As you enter the city there is a part of town with 2 hotels. Everyone looks through the car and you have $400 total.")
    print("1. Hotel $200 a night.")
    print("2. Hotel $50 a night.")

    choice = input("Which hotel?\n> ")

    if choice == "1":
        niceh()
    elif choice == "2":
        badh
    else:
        print("Choose a hotel.")
        car()


def cold():
    print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
    print("You start to run and the others don't follow you. It starts to snow and you are in shorts and a T-shirt. You start to become tired from all of the running. ")
    print("You're very cold and the snow is falling faster and faster.")
    print("You are now walking and you don't feel cold anymore. You see a building ahead and try running towards it be you fall to the ground.")
    print("Ending 13: The cold")


def niceh():
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("You guys only plan on staying for one night. You get a 3 bed room with a pullout couch. You guys walk into the room and its really nice.")
    print("You all take showers because you don't know how long you have been there.")
    print("The next morning you check out of your hotel and see a police car in the parking lot.")
    print("1. Sneak out to your car and leave.")
    print("2. Stay at the hotel.")

    choice = input("1 or 2.\n> ")

    if choice == "1":
        sneak()
    elif choice == "2":
        stay()
    else:
        print("Invalid input.")
        niceh()


def badh():
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("You get to the hotel and you're only staying one night. You got a 3 bed room which was the highest one they had. You enter the room and everyone takes a shower.")
    print("The room doesn't look very good but it's fine for one night. The next morning you check out of the hotel and see a police car in the parking lot.")
    print("1. Sneak out to your car and leave.")
    print("2. Stay at the hotel.")

    choice = input("1 or 2.\n> ")
    
    if choice == "1":
            sneak()
    elif choice == "2":
            stay()
    else:
            print("Invalid input.")


def sneak():
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("You sneak out the door and go to your car. Everyone follows behind. You make it to the car and zoom away. The cop starts chasing you and you see this turbo button.")
    print("1. Press turbo.")
    print("2. Don't")

    choice = input("1 or 2.\n> ")

    if choice == "1":
        turbo()
    elif choice == "2":
        police()
    else:
        print("Invalid input.")
        sneak()


def stay():
    print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
    print("You stay in the hotel and hope he just leaves. He gets out of his car and you go and hide where the food it.")
    print("You are waiting for him to leave and you see him walk in. He sees you and starts to walk towards you. You try to run but he pulls out a tazer and tazes you.")
    print("Ending 14: Tazer")


def turbo():
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("Your car starts to go faster and faster. You lose the police very quickly. You enter a new town but this time you notice a sign that says 'Virgina City, Nevada' which is the most haunted city in the USA.")
    print("You enter the city and it doesn't look like it has very many people. Then out of nowhere a local cop starts to follow you and turns on his lights.")
    print("1. Pull over.")
    print("2. Floor it.")

    choice = input("1 or 2.\n> ")

    if choice == "1":
        pull()
    elif choice == "2":
        bomb()
    else:
        print("Invalid input.")
        turbo()


def police():
    print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
    print("You keep driving but the cop is catching up. He hits your car and you start spinning on the road. The car flips and flips.")
    print("Ending 15: Cop")


def bomb():
    print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
    print("The cop starts chasing you and suddenly missle launcher come out of the sides of his car.")
    print("The he starts to lauch missles torwads your car and you blow up.")
    print("Ending 16: Missle")


def pull():
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("You pull over and the cop comes up to the window and asks what brings you through the city.")
    print("1. Tell the truth.")
    print("2. Say you were just passing through.")

    choice = input("1 or 2.\n> ")

    if choice == "1":
        truth()
    elif choice == "2":
        lie()
    else:
        print("Invalid input.")
        pull()


def truth():
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("He says 'Oh I've heard about that but it's okay I believe you.'")
    print("He tell you that your safe here and you can pick any house and live here. They won't come looking for you here.")

    choice = input("Do you want to agree?\n> ")

    if choice == "Yes":
        agree()
    elif choice == "No":
        nope()
    else:
        print("Invald input. Yes or No.")
        truth()


def lie():
    print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
    print("He see right through your lies and eats you.")
    print("Ending 16: Dinner time")


def agree():
    print("You say yes to staying so you follow he to a selection of houses. There are 4 houses for all 4 of you. ")
    print("You get 3 to pick from.")
    print("1. Normal pink house.")
    print("2. Normal blue house.")
    print("3. Evil white house.")

    choice = input("Which house?\n> ")

    if choice == "1":
        pink()
    elif choice == "2":
        blue()
    elif choice == "3":
        white()
    else:
        print("Invalid input. Pick 1,2, or 3.")
        agree()


def nope():
    print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
    print("You say no to staying there and he becomes very angry. He doesn't accept that as an awnser. He takes you out of the car and brings you to this house and theres other people there.")
    print("They all look scared and he throws you into the house and locks the door.")
    print("Ending 17: You were so close...")


def pink():
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("You enter the house and it smells clean and like flowers.")
    print("You now have a nice new free house.")
    print("You win!")

    choice = input("Would you like to play again?\n> ")

    if choice == "Yes":
        start()
    elif choice == "No":
        print("The end you win!")
    else:
        print("Invalid input. Enter Yes or No.")
        pink()


def blue():
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("You enter the house and its clean and smells like lavender.")
    print("You win!")

    choice = input("Do you want to play again?\n> ")

    if choice == "Yes":
        start()
    elif choice == "No":
        print("The end you win!")
    else:
        print("Invalid input. Enter Yes or No.")
        blue()


def white():
    print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
    print("You enter the house and it's very dark in the room. As you walk in you fall through the floor.")
    print("You lose...")
    print("Ending 18: Floor")




start()

