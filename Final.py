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
    

    #DAMAGE
    #WEAK MAGIC
    cursed_punch_damage = 0
    quick_slice_damage = 0
    piercing_blood_damage = 0
    dismantle_damage = 0
    mass_switch_damage = 0
    
    if weak_magic == "Cursed punch":
      cursed_punch_damage = 3 * {attack_power}
    if weak_magic == "quick slice":
      quick_slice_damage = 3 * .5 * {agility}
    if weak_magic == "Piercing blood":
      piercing_blood_damage = 5 * {attack_power}
    
    #Strong magic damage
    cleave_damage = 0
    cero_oscuras_damage = 0
    detroit_damage =  0
    one_million_slashes_damage = 0
    one_twenty_damage = 0
    black_flash_damage = 0
    getsuga_tensho_damage = 0
    if strong_magic == "Cleave":
      cleave_damage = 8 *{attack_power}
    if strong_magic == "Cero Oscuras":
      cero_oscuras_damage = 6 * {attack_power}
    if strong_magic == "Detroit":
      detroit_damage = 6 * {attack_power}
    if strong_magic == "One Million Slashes":
      one_million_slashes_damage = 6 * {attack_power}
    if strong_magic == "120%":
      one_twenty_damage = .5 * {agility}
    if strong_magic == "Black Flash":
      black_flash_damage = 7 * {attack_power}
    if strong_magic == "Getsuga Tensho":
      getsuga_tensho_damage = 8 * {attack_power}
  

    #melee damage
    jab_damage = 0
    kick_damage = 0
    dropkick_damage = 0
    


    time.sleep(1.1)
    print(f"-------{random_name}'s stats-------\n Name: {random_name} \n health: {health} \n defense: {defense} \n attack power: {attack_power} \n agility: {agility} \n mana: {mana} \n----MOVES---- \t------DAMAGE----\n{melee_move_one}\tN/A \n{melee_move_two}\tN/A\n{weak_magic}\tN/A\n{strong_magic}\tN/A")
    




    if mana >= 90:
      print(f"--ULTIMATE MOVE--\n{ultimate}")




if user_input == 2:
 answer = input("Do you want these characters to fight?(YOU WILL PLAY AS THE SECOND CHARACTER) Y/N: ")

if answer == "Y" or "y" or "Yes" or "yes":
  print(f"-------{random_name}'s stats-------\n Name: {random_name} \n health: {health} \n defense: {defense} \n attack power: {attack_power} \n agility: {agility} \n mana: {mana} \n----MOVES---- \t------DAMAGE----\n{melee_move_one}\tplaceholder\n{melee_move_two}\tplaceholder\n{weak_magic}\tplaceholder\n{strong_magic}\tplaceholder\n", print(f"--ULTIMATE MOVE--\n{ultimate}"))
else:
  print("okay!")


    


