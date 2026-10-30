def subscription():
    try:
        awnser = input("How old are you? \n")
        if awnser < 18:
            awnserparent = input("Do you have parent permission? -----type YES or NO \n")
            if awnserparent == "yes" or "Yes":
                awnsertwo = input("What is your bank account balence? \n ")
                if awnsertwo > 140:
                    



                    if 140 < awnsertwo:
                        awnserthree = input("Do you want to buy?----- type YES OR NO \n")
                        if awnserthree == "YES":
                            print("Purchass sucess")
                        else:
                            print("purchase rejected")
                    else:
                        print("purchase rejected")
                
    except:
        print("purchaces denied")
                