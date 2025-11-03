#LIST OF STUFF TO DO
#DONE:lib, float, list, function, loops, int, str, int, float,
#NOT DONE:
print("Welcome to this NPC generator!")
user_input = int(input("Please enter the amount of NPCs you desire: ")) #asking the user how many npcs they want and it reads the amount asked for
import random
import time
names = ["Akira", "Rin", "Ulqiorra", "Sora", "Ichi", "Haruto", "Aiko", "Renji", "Natsumi", "Kurosawa"] # lists of stuff so the npc has values for the names and moves
melee_attacks = ["Jab", "Kick", "Dropkick"]
weak_magic_attacks = ["Cursed punch", "quick slice", "Piercing blood", "Dismantle", "Mass switch"]
strong_magic_attacks = ["Cleave", "Cero Oscuras", "Detroit", "One Million Slashes", "120%", "Black Flash", "Getsuga Tensho"]
ultimate_moves = ["FINAL FLASH", "ILL USE MY ALL", "1000000%", "FINAL GETSUGA TENSHO"]







for i in range(user_input): #determains the amount of npcs the users asks and runs these commands x amount of times (X = the  number the user asked for)
    random_name =(random.choice(names)) #running random commands for the NPCs stats, like deciding  what moves or its health etc.
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
    cursed_punch_damage = "" #setting up variables for later use
    quick_slice_damage = ""
    piercing_blood_damage = ""
    dismantle_damage = ""
    mass_switch_damage = ""
    
    if weak_magic == "Cursed punch": # making so if the move selected by the loop is this move, it will run the command under, creating a damage amount.
      cursed_punch_damage = 3 * attack_power
    if weak_magic == "quick slice":
      quick_slice_damage = 3 * .5 * agility
    if weak_magic == "Piercing blood":
      piercing_blood_damage = 5 * attack_power
    if weak_magic == "Dismantle":
      dismantle_damage = 3 * agility
    if weak_magic == "Mass switch":
      mass_switch_damage = 50 / mana
    
    #Strong magic damage
    cleave_damage = ""
    cero_oscuras_damage = ""
    detroit_damage =  ""
    one_million_slashes_damage = ""
    one_twenty_damage = ""
    black_flash_damage = ""
    getsuga_tensho_damage = ""
    if strong_magic == "Cleave":
      cleave_damage = 8 *attack_power
    if strong_magic == "Cero Oscuras":
      cero_oscuras_damage = 6 * attack_power
    if strong_magic == "Detroit":
      detroit_damage = 6 * attack_power
    if strong_magic == "One Million Slashes":
      one_million_slashes_damage = 6 * attack_power
    if strong_magic == "120%":
      one_twenty_damage = .5 * agility
    if strong_magic == "Black Flash":
      black_flash_damage = 7 * attack_power
    if strong_magic == "Getsuga Tensho":
      getsuga_tensho_damage = 8 * attack_power
  

    #melee damage
    jab_damage = ""
    kick_damage = ""
    dropkick_damage = ""
    if melee_move_one or melee_move_two == "Jab":
      jab_damage = 1 * attack_power
    if melee_move_two or melee_move_one == "Kick":
      kick_damage = 1.5 * attack_power
    if melee_move_one or melee_move_two == "Dropkick":
      dropkick_damage = 2 * agility
    


    time.sleep(1.1) #printing the states of the npc,  x amount of times.
    print(f"-------{random_name}'s stats-------\n Name: {random_name} \n health: {health} \n defense: {defense} \n attack power: {attack_power} \n agility: {agility} \n mana: {mana} \n----MOVES---- \t------DAMAGE----\n{melee_move_one}\t{jab_damage}{kick_damage}{dropkick_damage} \n{melee_move_two}\t{jab_damage}{kick_damage}{dropkick_damage}\n{weak_magic}\t{cursed_punch_damage}{quick_slice_damage}{piercing_blood_damage}{dismantle_damage}{mass_switch_damage}\n{strong_magic}\t{cleave_damage}{cero_oscuras_damage}{detroit_damage}{one_million_slashes_damage}{one_twenty_damage}{black_flash_damage}{getsuga_tensho_damage}")
    




    if mana >= 90: #makes it so if the mana is below 90, a random ultimate move isn't printed, and if it is 90 or above, the ultimate move selected is printed
      print(f"--ULTIMATE MOVE--\n{ultimate}")
