# Shane Steiner
# Python version 3.10.0
# Pirate Swashbuckle Fight Milestone 3


# 1. Import the utilities file
import utilities

# 2. Import the pirates.txt file
with open('pirates.txt', 'r') as f:
    pirates = f.read().splitlines()
    f.close()

# dodge > parry > thrust > dodge
attack = ['dodge', 'parry', 'thrust']

# 3. Use the utilites to randomly pick pirates for player and opponent
player = utilities.randopick(pirates)
opponent = utilities.randopick(pirates)
# 4. Add a while loop so that the pirates are not the same
while player == opponent:
    opponent = utilities.randopick(pirates)

print ("Advast ye swabs, a fight betwixt \n" + player + " & " + opponent + " 'tis bout to commence! ")

pscore = 0
oscore = 0
gameover = False

while gameover == False:
    # This has changed for milestone 3. The game will still end when the player or opponent reaches 3. 
    if pscore >= 3:
        print(player + " has vanquished " + opponent)
        print ("Hip hip huzzah!")
        gameover = True
        break
    elif oscore >= 3:
        print (opponent + " has vaquished " + player)
        print ("Oh Captain, my Captain!")
        gameover = True
        break
    # 5. Exception - Add a while True and exception. 
    # Example: the player attack variable should allow the user to pick between the different types     
    while True:
        try:
            pattack = int(input("Enter [1] Dodge, [2] Parry, [3] Thrust: "))
            break
        except ValueError:
            print("Invalid input please try again.")

    # 6. Player only - Create an if/elif statement to set the number entry to the correct attack.
    if pattack == 1:
        pattack = 'dodge'
    elif pattack == 2:
        pattack = 'parry'
    elif pattack == 3:
        pattack = 'thrust'
    else:
        print("Invalid input please try again.")



    # The program randomly picks the attack for the opponent
    oattack = utilities.randopick(attack)
    
    # 7. Add a while loop so that the attacks are not the same. Use the utilities module.
    while pattack == oattack:
        oattack = utilities.randopick(attack)



    print (player + " attacks with a " + pattack)
    print (opponent + " attacks with a " + oattack)

    # 8. Change your if/elif statment from milestone 2. Use the and to compare the attacks. All attacks must be used correctly.
    if pattack == 'dodge' and oattack == 'parry':
        print("Dodge beats parry")
        pscore += 1
    elif pattack == 'parry' and oattack == 'thrust':
        print("Parry beats thrust")
        pscore += 1
    elif pattack == 'thrust' and oattack == 'dodge':
        print("Thrust beats dodge")
        pscore += 1
    elif oattack == 'dodge' and pattack == 'parry':
        print("Dodge beats parry")
        oscore += 1
    elif oattack == 'parry' and pattack == 'thrust':
        print("Parry beats thrust")
        oscore += 1
    elif oattack == 'thrust' and pattack == 'dodge':
        print("Thrust beats dodge")
        oscore += 1
        
    # 9. Print a string that includes the player and the players score.
    print(player + "Has a score of: " + str(pscore))
    # 10. Print a string that includes the opponent and the opponents score.
    print(opponent + "Has a score of: " + str(oscore))

