#LIST OF STUFF TO DO
#DONE:lib, float, list, function, loops, int, str, int, float,
#NOT DONE:
print("Welcome to this NPC generator!")
user_input = int(input("Please enter the amount of NPCs you desire: "))
import random  #Allows for a random name along with stats and moves to be selected
import time
names = ["Akira", "Rin", "Ulqiorra", "Sora", "Ichi", "Haruto", "Aiko", "Renji", "Natsumi", "Kurosawa"]   #The library of names and moves
melee_attacks = ["Jab", "Kick", "Dropkick", "Headbutt"]
weak_magic_attacks = ["Cursed punch", "quick slice", "Piercing blood", "Dismantle", "Mass switch"]
strong_magic_attacks = ["Cleave", "Cero Oscuras", "Detroit", "One Million Slashes", "120%", "Black Flash", "Getsuga Tensho"]
Ultimate_moves = ["FINAL FLASH", "ILL USE MY ALL", "1000000%", "FINAL GETSUGA TENSHO"]

for i in range(user_input):     #takes the number of npcs the player wants and runs it through this command
    random_name =(random.choice(names))  #give one of x npcs a name from the list
    health = random.randint (1 , 100) #give one of x npcs a health 1-100
    defense = random.randint (1, 100) #give one of x npcs a defense 1-100
    attack_power = random.randint (1, 10) #give one of x npcs amoubt of attack power 1-10
    agility = random.randint (1, 100) #give one of x npcs a agility amount 1-100
    mana = random.randint (1, 100) #give one of x npcs a mana amount 1-100
    melee_move_one = (random.choice(melee_attacks))
    melee_move_two = (random.choice(melee_attacks))
    weak_magic = (random.choice(weak_magic_attacks))
    strong_magic = (random.choice(strong_magic_attacks))
    if mana >=90:
        ultimate = (random.choice(Ultimate_moves))



    time.sleep(1.1)
    print(f"-------{random_name}'s stats-------\n Name: {random_name} \n health: {health} \n defense: {defense} \n attack power: {attack_power} \n agility: {agility} \nMOVES\tDAMAGE\n{melee_move_one}\tplaceholder\n{melee_move_two}\tplaceholder\n{weak_magic_attacks}\tplaceholder\n{strong_magic}\tplaceholder\n\t--ULTIMATE MOVE--\n\t{ultimate}")


if user_input == 2:
    fight_question = input("Do you want these characters to fight? ")
else:
    print(" ")