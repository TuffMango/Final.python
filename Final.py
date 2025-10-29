#LIST OF STUFF TO DO
#DONE:lib, float, list, function, loops, int, str, int, float,
#NOT DONE:
print("Welcome to this NPC generator!")
user_input = int(input("Please enter the amount of NPCs you desire: "))
import random
import time
names = ["Akira", "Rin", "Ulqiorra", "Sora", "Ichi", "Haruto", "Aiko", "Renji", "Natsumi", "Kurosawa"]
melee_attacks = ["Jab", "Kick", "Dropkick"]
weak_magic_attacks = ["Cursed punch", "quick slice", "Piercing blood", "Dismantle", "Mass switch"]
strong_magic_attacks = ["Cleave", "Cero Oscuras", "Detroit", "One Million Slashes", "120%", "Black Flash", "Getsuga Tensho"]
ultimate_moves = ["FINAL FLASH", "ILL USE MY ALL", "1000000%", "FINAL GETSUGA TENSHO"]

for i in range(user_input):
    random_name =(random.choice(names))
    health = random.randint (1 , 100)
    defense = random.randint (1, 100)
    attack_power = random.randint (1, 10)
    agility = random.randint (1, 100)
    mana = random.randint (1, 100)
    melee_move_one = (random.choice(melee_attacks))
    melee_move_two = (random.choice(melee_attacks))
    weak_magic = (random.choice(weak_magic_attacks))
    strong_magic = (random.choice(strong_magic_attacks))
    ultimate = (random.choice(ultimate_moves))
    time.sleep(1.1)
    print(f"-------{random_name}'s stats-------\n Name: {random_name} \n health: {health} \n defense: {defense} \n attack power: {attack_power} \n agility: {agility} \n mana: {mana} \n----MOVES---- \t------DAMAGE----\n{melee_move_one}\tplaceholder\n{melee_move_two}\tplaceholder\n{weak_magic}\tplaceholder\n{strong_magic}\tplaceholder\n")
    if mana >= 90:
      print(f"--ULTIMATE MOVE--\n{ultimate}")


fight_question = ("Do you want these characters to fight?(YOU WILL PLAY AS THE SECOND CHARACTER) ")
if user_input == 2:
 answer = input(fight_question)
if answer == "yes" or "Yes":
  print(f"-------{random_name}'s stats-------\n Name: {random_name} \n health: {health} \n defense: {defense} \n attack power: {attack_power} \n agility: {agility} \n mana: {mana} \n----MOVES---- \t------DAMAGE----\n{melee_move_one}\tplaceholder\n{melee_move_two}\tplaceholder\n{weak_magic}\tplaceholder\n{strong_magic}\tplaceholder\n")
else:
  print("okay!")


    


