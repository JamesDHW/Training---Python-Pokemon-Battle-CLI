from random import randint  # Generates a random integer


# This isn't executed until later when 'battle()' is called
def battle(monster, mon_hp, my_hp, my_xp, gold):
    # Set up a loop until the monster dies
    # Player inputs a choice of their attack
    # Whole battle happens in here
    # Return the player's new health and xp
    gold_found = randint(0, mon_hp // 2)
    xp_gained = randint(0, mon_hp // 2)
    while mon_hp > 0:
        # Check my hp every move to see if I'm dead
        if my_hp <= 0:
            return 0, my_xp, gold
        # If I'm still alive
        print("\nyour hp:", my_hp, "\nenemy hp:", mon_hp, "\n")
        action = input("Will you: \na)" + moves[0] + "\nb)" + moves[1] + "\nc)" + moves[2] + "\nd)" + moves[3] + "\n").lower()
        if action == "a":
            action = moves[0]
        elif action == "b":
            action = moves[1]
        elif action == "c":
            action = moves[2]
        elif action == "d":
            action = moves[3]
        else:
            print("invalid move")
            continue

        # Get some value for damages
        try:
            my_damage = randint(my_xp * randint(0, mon_hp), mon_hp)
            damage = randint(0, my_hp)
        except:
            my_damage = mon_hp
            damage = my_hp

        mon_hp -= damage
        print("You hit the", monster, "with a", action, "for", damage, "damage")
        my_hp -= my_damage
        print("The", monster, "hits you back for", my_damage, "damage")

    gold += gold_found
    my_xp += xp_gained
    print()
    print("The wild", monster, "was vanquished")
    print("You found", gold, "gold and earned", xp_gained, "xp")
    return my_hp, my_xp, gold


hp = 100
xp = 0
gold = 0

moves = [input("choose attack 1: "), input("choose attack 2: "), input("choose attack 3: "), input("choose attack 4: ")]
mon_names = ["Pikachu", "Eevee", "Snorlax", "Mewtwo", "Charizard", "Celebi", "Jigglypuff"]
mon_hp = [30, 25, 45, 85, 150, 100, 35]

monsters = {'Pikachu': 30, 'Charizard': 150}

pokemon = [{
    'name': 'Venasuar',
    'health': 30,
    'type': 'Grass'
},{
    'name': 'Charizard',
    'health': 150,
    'type': 'Fire'
},{
    'name': 'Blastoise',
    'health': 150,
    'type': 'Water'
}]

weakness = {
    'Grass': 'Fire',
    'Fire': 'Water',
    'Water': 'Grass'
}


# Program starts here
while hp > 0:
    i = randint(0, len(mon_names) - 1)  # This is a random number within the index of the list
    cont = input("A wild " + mon_names[i] + " enters the arena - will you fight? (y/n)\n")
    if cont.lower() == "y" or cont.lower() == "yes":
        hp, xp, gold = battle(mon_names[i], mon_hp[i], hp, xp, gold)
    else:
        print("You exit the arena with", hp, "health remaining and", xp, "xp.")
        print("You earned", gold, "gold")
        break

    if hp == 0:
        print("You died")
        break

# Print out the final score and stats

# Additional features:
# xp increases after each round
# higher xp acts as a MULTIPLIER on DAMAGE
# Print which monster appears
# Add more monsters
# Allow a user to CUSTOMISE their ATTACKS at the very beginning (cho0se 4 from a long list)
# Add in RANDOM HEALTH for monsters - with the current health list acting as a max health
# Add in randomly appearing HEALTH POTIONS
# Add in a type system (so different attacks work differently on different monsters)
# Looting monsters randomly for gold after each round counts as a score
# Give player the OPTION TO LEAVE (decide if they want to continue on
# to the next round and risk dying or leave with the gold they've earned - they get some score)
# If they die they lose - if they chose not to fight they exit the game (win) with that score/ gold

