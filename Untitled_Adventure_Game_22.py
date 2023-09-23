# Julia Moras
# Final Project
# COP 2500
# 11/14/2022

# The Interactive Story of The Missing Knight
print("Welcome to the Interactive Story of ...\n"
      "The Missing Knight\n")
name = input("Enter your name: ")
name = name.title().strip()
print("Hello",name)

import sys
inventory = []

# Dictionary of Items from Inventory List that give Descriptions
description_list = ["The 'Torn Missing Flyer' reads:\n\n"
                    "MISSING: KNIGH...\n"
                    "REWARD: SPIRIT SPLASH DUCK 22' EDITION\n"
                    "SUSPECTS: ...\n"
                    "\nWhile some of the flyer is missing and illegible, your heart sinks as you identify the\n"
                    "Shimmering Gold Helmet in the missing photo to be none other than UCF's own Knightro.",
                    
                    "The 'Tootsie Pop Wrapper' seems to have holes in it as if someone was eagerly biting at it.\n"
                    "I wonder how many licks does it take to get to the center of a Tootsie Pop ...",

                    "The 'Yellow Jacket' has a tag on the inside that reads:\n"
                    "Property of Buzz",

                    "The 'Photo of \"Yellow Submarine\"' has something highlighted ...\n"
                    "Upon closer inspection, the song 'Hey Bulldog' is highlighted.",

                    "The 'Photo of \"Red Mustang\"' has nothing notable.\n"
                    "You wonder if the Red Mustang is a clue itself ..."]
                    
description = {"Torn Missing Flyer": description_list[0],
               "Tootsie Pop Wrapper": description_list[1],
               "Yellow Jacket": description_list[2],
               "Photo of \"Yellow Submarine\"": description_list[3],
               "Photo of \"Red Mustang\"": description_list[4]}


# Inspection Function for Inventory
def inspect():
    choice = int(input("\nWould you like to inspect an item?\n"
                       "1. Yes\n"
                       "2. No\n"))
    #User inspects
    if choice == 1:
        item = int(input("\nWhich item number would you like to inspect?\n"))
        if item in range (len(inventory)+1):
            #Item 1
            if item == 1:
                print("--------------------")
                print(description["Torn Missing Flyer"])
                if len(inventory)>1:
                    inspect()
            #Item 2
            if item == 2:
                print("--------------------")
                print(description["Tootsie Pop Wrapper"])
                if len(inventory)>1:
                    inspect()
            #Item 3
            if item == 3:
                print("--------------------")
                print(description["Yellow Jacket"])
                if len(inventory)>1:
                    inspect()
            #Item 4
            if item == 4:
                print("--------------------")
                print(description["Photo of \"Yellow Submarine\""])
                if len(inventory)>1:
                    inspect()
            #Item 5
            if item == 5:
                print("--------------------")
                print(description["Photo of \"Red Mustang\""])
                if len(inventory)>1:
                    inspect()

#Chapter Functions
#CHAPTER 1: THE MISSING KNIGHT
def chapter_1():
    print("----------------------------------------")
    print("Chapter 1: The Missing Knight")
    chapter_1 = int(input("Enter '1' to Begin\n"))

    #Waits For Proper Chapter Input
    while chapter_1 != 1:
        print ("...")
        chapter_1 = int(input(""))
        

    print("--------------------")  
    print("The date was October 13th, 2022.")
    print("The day everyone was looking towards: The Space Game vs Temple University.")
    print("There was an autumn rain that brought a chill upon your bones like no other.")
    print("The sky was an unusual grey and the wind viciously blew your coat and hair around.\n")

    print("With hair covering your face and rain blurring your vision,\n"
          "you could barely see the nearly empty campus surrounding you.\n")

    print("As you gaze upwards from shielding your face, you see four oddly shaped silhouettes in the\n"
          "distance; yet as you start to make out any details, they sprint away further into the rain.\n")

    print("What do you do?")
    choice = int(input("1. Go to the unknown figures last location.\n"
                       "2. Check your phone for weather updates.\n"))

    while choice < 1 or choice > 3:
        print ("...")
        choice = int(input(""))
        
    #Go to the unknown figures last location
    if choice == 1:
        print("--------------------")
        print("Your shoes splash through the large puddles coating the slick pavement.")
        print("You dash towards their last location before they ran off into the rain.\n")
        print("You find the top of a torn missing flyer soaking wet.")
        if 'Torn Missing Flyer' not in inventory:
            inventory.append('Torn Missing Flyer')
            print("'Torn Missing Flyer' added to Inventory.")
        print("\nEnd of Chapter: Saving Inventory ...")
        
    #Check your phone for weather updates 
    if choice == 2:
        print("--------------------")
        print("Your shivering cold hands grasp at your phone to check for a weather update.")
        print("Seeing you have received a message from UCF ALERTS, you open the memo reading...\n")

        print("  WARNING: DO NOT ENTER UCF CAMPUS AREA.")
        print("  We regret to inform you that Knightro has been\n"
              "  reported as missing as of October 12th 11:59pm.\n"
              "  Individual last spotted at the FBC Mortgage Stadium.\n\n"
              
              "  Multiple reports of four suspicious individuals,\n"
              "  not yet identified, around the UCF Campus.\n"
              "  If spotted, do not approach; call campus\n"
              "  security and leave location immediately.\n\n"
              
              "  Future updates expected:\n"
              "  UCF ALERTS\n")
        
        print("With your heart and mind racing, you ignore all safety and dash toward\n"
              "the fleeing four's last location before they ran off into the rain.\n")
        print("You find the top of a torn missing flyer soaking wet.")

        #adds items if not in inventory
        if 'Torn Missing Flyer' not in inventory:
            inventory.append('Torn Missing Flyer')
            print("'Torn Missing Flyer' added to Inventory.")
        print("\nEnd of Chapter: Saving Inventory ...")
        
    main_menu()

#CHAPTER 2: THE FLEEING FOUR
def chapter_2():
    print("----------------------------------------")
    print("Chapter 2: The Fleeing Four")
    chapter_2 = int(input("Enter '2' to Begin\n"))

    #Waits For Proper Chapter Input
    while chapter_2 != 2:
        print ("...")
        chapter_2 = int(input(""))


    print("--------------------")
    print("After inspecting the 'Torn Missing Flyer', you quickly look around for\n"
          "clues the four might have left behind during their rushed exit.\n")
    
    print("You scan the area diligently ... and without any luck;\n"
          "you only find trash laying around, a tootsie pop wrapper.\n")

    ##adds items if not in inventory
    if 'Tootsie Pop Wrapper' not in inventory:
        inventory.append('Tootsie Pop Wrapper')
        print("You pick up the trash wondering why people litter.")
        print("'Tootsie Pop Wrapper' added to Inventory.")
 
    print("\nSuddenly, you hear something behind you being blown around in the wind.\n")
    choice = int(input("What do you do?\n"
                       "1. Continue into rain after the four.\n"
                       "2. Look behind you.\n"))
    
    #Continue into rain after the four
    if choice == 1:
        print("--------------------")
        print("You do not have any time for silly distractions.\n")
            
        print("Walking head on into the rain, your clothing becomes heavier\n"
              "limiting your movement, while the ground becomes a shallow pool\n"
              "making it dangerous to run.\n")

        print("... That noise ... you hear it again!")
        print("This time only louder, as if it were following you.\n")

        print("You have had enough!")
        print("You turn around to see who or what was following you.")

        print("With the vicious wind blowing your hair and coat around,\n"
              "you still manage to see the item with ease ...\n")

        print("A yellow jacket?")
        print("You begin to believe that Knightro's disappearance\n"
              "is causing you paranoia.\n")

        print("You quickly grasp the jacket before the wind could whisk it away any further.\n")
        
        print("With a deep chill striking your bones, you put on the yellow jacket\n"
              "as an extra barrier from the weather.")

        #adds items if not in inventory
        if 'Yellow Jacket' not in inventory:
            inventory.append('Yellow Jacket')
            print("'Yellow Jacket' added to Inventory.")

        choice = int(input("\nEnter '2' to Continue\n"))
        while choice != 2:
            print ("...")
            choice = int(input(""))

        print("--------------------")    
        print("You continue into the rain after the four as before you were rudely interrupted by a jacket.")
        print("You trudge along the flooded paths until you happen upon the Campus Store.\n")
        
        print("While they are closed; you find comfort in the protection the concrete structure provides.\n")
        
        print("You begin to window shop the 'Space U' merchandise in hopes of calming your nerves.")
        print("It begins to work!")
        print("Well ... until you spot something peculiar on display ...\n")

        print("A copy of \"Yellow Submarine\" by The Beatles with a Hot Wheels Red Mustang next to it.\n")

        print("You begin to think all of the items you have been finding today are not by accident.")
        print("Even more so with Knightro missing ...\n")

        print("You take a photo of the album and the toy car with your phone.")

        ##adds items if not in inventory
        if 'Photo of "Yellow Submarine"' not in inventory:
            inventory.append('Photo of "Yellow Submarine"')
            print("'Photo of \"Yellow Submarine\"' added to inventory.")

        if 'Photo of "Red Mustang"' not in inventory:
            inventory.append('Photo of "Red Mustang"')
            print("'Photo of \"Red Mustang\"' added to inventory.")
            
    #Look behind you
    if choice == 2:
        print("--------------------")
        print("Turning around with the vicious wind blowing your hair and coat,\n"
              "you still manage to see the item with ease.\n")

        print("A yellow jacket, interesting...\n")
        
        print("You carefully traverse the slippery pavement to grab the jacket\n"
              "before the wind can drag it out of reach.\n")
        
        print("With a deep chill striking your bones, you put on the yellow jacket\n"
              "as an extra barrier from the weather.")

        #adds items if not in inventory
        if 'Yellow Jacket' not in inventory:
            inventory.append('Yellow Jacket')
            print("'Yellow Jacket' added to Inventory.")

        choice = int(input("\nEnter '2' to Continue\n"))
        while choice != 2:
            print ("...")
            choice = int(input(""))

        print("--------------------")
        print("You continue through the rain towards the only landmark you can identify.\n"
              "The Campus Store.")
        print("You trudge along the flooded paths until you make it in one piece.\n")
        
        print("While, of course, the store is closed;\n"
              "you can not help yourself but begin to window shop.\n")

        print("With the 'Space U' merchandise on display,\n"
              "you begin to wonder will the Space Game continue in Knightro's absence?\n")
        
        print("As you were stuck in thought, your eyes spot something peculiar on display ...")
        print("A copy of \"Yellow Submarine\" by The Beatles with a Hot Wheels Red Mustang next to it\n")

        print("You begin to think all of the items you have been finding today are not by accident.")
        print("Even more so with Knightro missing ...\n")

        print("You take a photo of the album and the toy car with your phone.")

        #adds items if not in inventory
        if 'Photo of "Yellow Submarine"' not in inventory:
            inventory.append('Photo of "Yellow Submarine"')
            print("'Photo of \"Yellow Submarine\"' added to inventory.")

        if 'Photo of "Red Mustang"' not in inventory:
            inventory.append('Photo of "Red Mustang"')
            print("'Photo of \"Red Mustang\"' added to inventory.")

    print("\nMaybe you should inspect your inventory ...\n")
    print("End of Chapter: Saving Inventory ...")
        
    main_menu()

#THE FINALE: RETURN OF THE JEDI KNIGHT
def chapter_3():
    print("----------------------------------------")
    print("The Finale: Return of the Jedi Knight")
    chapter_3 = int(input("Enter '3' to Begin\n"))

    #Waits For Proper Chapter Input
    while chapter_3 != 3:
        print ("...")
        chapter_3 = int(input(""))
        
    print("--------------------")
    print("You cannot believe it ...")
    print("It is all beginning to make sense now ...\n")

    print("After inspecting your inventory you could not help but see a pattern.")
    print("All the items mean something, or at least, something to someone ...\n")

    print("UCF has won four games this season, those being against:\n"
          "SCS: the Bulldogs\n"
          "FAU: the Owls\n"
          "GT: the Yellow Jackets\n"
          "SMU: the Mustangs\n")
    
    print("Their mascots must have worked together to sabotage Knightro to bring UCF down for the Space Game!")
    print("But you won't allow that.\n")

    print("You call Campus Security with all the information you have found, and they begin work immediately.\n")

    print("As Knightro was found safe, the skies began to clear and the wind slowed to a breeze.")
    print("Students and Staff alike crowded the campus once the good news was shared.\n")

    print("Knightro is safe and sound, all thanks to you!")
    print("Knightro the Jedi Knight takes his righteous place in the stadium\n"
          "cheering alongside the crowd for UCF that marvelous night.\n")

    print("With a newfound hope, UCF's Football Team wins by a landslide of\n"
          "70-13 against Temple University for the Space Game.\n")

    print("Thank you for your help",name)
    print("Go Knights!\n"
          "Charge On!")


    main_menu()


# Main Menu Function
def main_menu():
    menu = int(input("\nMain Menu:\n"
                     "1. Begin Story\n"
                     "2. Continue Story\n"
                     "3. View Inventory\n"
                     "4. View Rules\n"
                     "5. Exit\n"))
        
    while menu < 1 or menu > 5 and menu != 5:
        print ("...")
        menu = int(input(""))
        
    #Main Menu: Begins Story (Chapter 1)
    if menu == 1:
        chapter_1()
    
    #Main Menu: Continues Story (User Selects Chapter)(not complete)
    if menu == 2:
        chapter = str(input("\nPlease Select a Chapter:\n"
                            "CHAPTER 1: The Missing Knight\n"
                            "CHAPTER 2: The Fleeing Four\n"
                            "THE FINALE: Return of The Jedi Knight\n\n"
                            "Select Chapter: "))
        chapter = chapter.strip().upper()
        
        if chapter == "CHAPTER 1":
            chapter_1()

        if chapter == "CHAPTER 2":
            chapter_2()

        if chapter == "THE FINALE":
            chapter_3()

        else:
            print("Hmm. Try 'View Rules' accessible from the Main Menu.")
            main_menu()
            
    #Main Menu: View Inventory
    if menu == 3:
        print("\nLoading Inventory ...")
        if 'Torn Missing Flyer' not in inventory:
            print("\nYour Inventory is empty.")
            main_menu()
        
        else:
            print("--------------------")
            print("INVENTORY:")
            for i in inventory:
                position = inventory.index(i)+1
                print(str(position) + ". " + str(i))
            print("--------------------")
            inspect()
            main_menu()
    
    #Main Menu: Rule Menu
    if menu == 4:
        def rules():
            rule = int(input("\nRules of 'The Interactive Story of The Missing Knight':\n"
                             "1. Inventory\n"
                             "2. Chapters\n"
                             "3. Back to Main Menu\n"))
            #Rules: Inventory
            if rule == 1:
                print("\nINVENTORY:\n"
                      "- Your 'Inventory' is a list of items and clues you will collect during your adventure.\n"
                      "- At the Main Menu, you can 'View Inventory' to view and inspect your items.\n"
                      "- Inspecting will provide further information of the selected item.\n")
                rules()
            #Rules: Saving
            if rule == 2:
                print("\nCHAPTERS:\n"
                      "- To begin the Interactive Story at Chapter 1;\n"
                      "  go to the Main Menu and select the 'Begin Story' option.\n"
                      "- To select a chapter;\n"
                      "  go to the Main Menu and select the 'Continue Story' option.\n"
                      "  Enter either: CHAPTER 1, CHAPTER 2, or THE FINALE, to 'Continue Story'.\n")
                rules()
            #Rules: Back To Main Menu  
            if rule == 3:
                main_menu()
                
        rules()
    #Main Menu: Exit
    if menu == 5:
        choice = int(input("\nAre you sure you would like to quit?\n"
                           "1. Yes\n"
                           "2. No\n"))
        if choice == 1:
            print("\nGoodbye",name)
            sys.exit()
            
        if choice == 2:   
            main_menu()
    
main_menu()




    
    
