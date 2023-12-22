import time


from datetime import date
import os
import random
import json

def clear():
  print("\033c",end="")
	
time.sleep(2)
user_name = os.environ['REPL_OWNER']
cheat = "bananas are amazing!"
level = 1
reset = "\u001b[0m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
red = "\u001b[31m"
magenta = "\u001b[35m"
black = "\u001b[30m"
money = 0
amount_in_stock = [99, 239, 5239, 49, 1349]
today = date.today()
plane_grid = [[" ", " ", " ", " "],[" ", " ", " ", " "],[" ", " ", " ", " "]]

logo = '''
\u001b[33m
██████╗  █████╗ ███╗   ██╗ █████╗ ███╗   ██╗ █████╗ 
██╔══██╗██╔══██╗████╗  ██║██╔══██╗████╗  ██║██╔══██╗
██████╔╝███████║██╔██╗ ██║███████║██╔██╗ ██║███████║
██╔══██╗██╔══██║██║╚██╗██║██╔══██║██║╚██╗██║██╔══██║
██████╔╝██║  ██║██║ ╚████║██║  ██║██║ ╚████║██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
                                                    
 ██████╗  █████╗ ███╗   ███╗███████╗    ██████╗     
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ╚════██╗    
██║  ███╗███████║██╔████╔██║█████╗       █████╔╝    
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██╔═══╝     
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████╗    
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝    
                                                    \u001b[0m                                                                
'''
logo2 = '''
\u001b[33m /$$$$$$$                                                   
| $$__  $$                                                  
| $$  \ $$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$ 
| $$$$$$$  |____  $$| $$__  $$ |____  $$| $$__  $$ |____  $$
| $$__  $$  /$$$$$$$| $$  \ $$  /$$$$$$$| $$  \ $$  /$$$$$$$
| $$  \ $$ /$$__  $$| $$  | $$ /$$__  $$| $$  | $$ /$$__  $$
| $$$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$
|_______/  \_______/|__/  |__/ \_______/|__/  |__/ \_______/
                                                            
                                                            
                                                            
  /$$$$$$                                           /$$$$$$ 
 /$$__  $$                                         /$$__  $$
| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$       |__/  \ $$
| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$        /$$$$$$/
| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$       /$$____/ 
| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/      | $$      
|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$      | $$$$$$$$
 \______/  \_______/|__/ |__/ |__/ \_______/      |________/\u001b[0m
'''
items = ["stick"]
prompts = [f"You see a {blue}banana tree{reset}.\n1. Pick up bananas. \n2. Walk away from scary bananas!.", f"You see a {blue}banana plane{reset} in the distance. \n1. Walk in the opposite direction. \n2. Walk towards plane.", "1. Fly the banana plane to a city.\n2. Do nothing"]

player_data = {"level":1, "events":[], "items":items, "money":money}
def death(death_reason):
	'''prints the death message
 Arguments include: "bear", "idiot", "brick", "instructions", "cheating", "edge", "x", "zombie", landing, spin, and "archer".'''
	clear()
	if death_reason == "bear":
		print("You got killed by the bear.")
	elif death_reason == "idiot":
		print("Warning! You are an idiot.")
	elif death_reason == "brick":
		print(f"You got hit by a {red}falling brick.{reset}")
	elif death_reason == "instructions":
		print(f"{red}Can't follow instructions{reset}")
	elif death_reason == "cheating":
		print(f"{red}No cheating{reset}")
	elif death_reason == "edge":
		print(f"Your banana plane fell off the {red}edge.{reset}")
	elif death_reason == "x":
		print(f"Your banana plane got hit by a flying {red}X{reset}.")
	elif death_reason == "zombie":
		print(f"You got punched by the {red}zombie{reset} to many times.")
	elif death_reason == "archer":
		print(f"You got shot in the chest by the {red}archer{reset}.")
	elif death_reason == "robot":
		print(f"You got killed by the {red}robot{reset}.")
	elif death_reason == "landing":
		print(f"You crashed your {red}spaceship.{reset}")
	elif death_reason == "old age":
		print(f"You died of {red}old age.{reset}")
	elif death_reason == "troll":
		print(f"You got killed by the {red}troll.{reset}")
	elif death_reason == "boss":
		print(f"You got banana peeled by the {red}boss{reset}")
	elif death_reason == "car":
		print(f"You didn't get {red}top 3!{reset}")
	elif death_reason == "spin":
		print(f"Your car {red}spun out of control.{reset}")
	else:
		pass
	time.sleep(2)
	print(f"{red}You died.{reset}")
	time.sleep(2)
	clear()
	
def level_one():
	global level,player_data,items,money
	print(f"{green}You have spawned.{reset}")
	time.sleep(1)
	rt = time.time()
	if input(prompts[0]) == "1":
		nrt = time.time()
		reaction_t = nrt-rt
		if reaction_t < 5:
			clear()
			time.sleep(1)
			print("You took 3 bananas from the tree. They restore 10 hp each.")
			items.extend(("banana", "banana", "banana"))
			time.sleep(3)
			clear()
			if input(prompts[1]) == "2":
				clear()
				time.sleep(1)
				print("You walk towards the banana plane for 5 minutes.")
				print("You walk into banana plane and realize you know the controls.")
				time.sleep(3)
				clear()
				if input(prompts[2]) == "1":
					print("You arrived at the city and escaped from the forest.")
					time.sleep(5)
				else:
					print("Why don't you fly banana plane???")
					death("idiot")
					return
			else:
				clear()
				print("You walk away from the banana plane.")
				time.sleep(3)
				print("On the way, a brick falls from a banana plane.")
				death("brick")
				return
		else:
			clear()
			print("A brick falls from a banana plane.")
			death("brick")
			return
	else:
		print(f"Why are {red}bananas{reset} scary???")
		time.sleep(3)
		clear()
		death("idiot")
		return
	clear()
	print(f"{green}You beat level 1! Good job!{reset}")
	if level == 1:
		level = 2
		items.append("level one trophy")
		player_data["level"] = 2
	money += 2
	

def level_two():
	global player_data,items,level,money
	print(f"{green}You have spawned.{reset}")
	time.sleep(2)
	clear()
	print("Hello! Welcome to level 2!")
	time.sleep(2)
	print("Today, we will be learning how to fly spaceships as well as eating bananas.")
	time.sleep(2)
	print("Not to worry, level 2 is considerably harder than level 1.")
	time.sleep(3)
	ship_angle = 60
	clear()
	print("BOOM! Your spaceship launches.")
	ship_distance = 20
	time.sleep(2)
	while ship_distance != 0:
		clear()
		print(f"You are {ship_distance} away from the landing site.")
		print(f"angle={ship_angle}")
		print("go left to decrease angle.")
		print("go right to increase angle.")
		print("You are aiming for angle '0'")
		choice = input("press the s key to steer left. press the d key to steer right.")
		if choice == "s":
			print("you turned left.")
			ship_angle -= random.randint(3,4)
			time.sleep(0.7)
		elif choice == "d":
			print("you turned right.")
			ship_angle += random.randint(3,4)
			time.sleep(0.7)
		else:
			print("You did nothing")
			time.sleep(0.7)
		ship_distance -= 1
	if ship_angle < 3 and ship_angle > -3:
		print("You passed the warmup section!")
	else:
		print("Your aiming is horrible! Try again.")
		time.sleep(2)
		death("landing")
		return
	clear()
	time.sleep(1)
	print("Hello! \nToday we will teach you how to eat bananas.")
	time.sleep(2)
	print("To eat the banana, type in the sequence of letters posted:")
	nnow = time.time()
	if input("123456789") == "123456789":
		llater = time.time()
		if llater-nnow > 10:
			death("brick")
			return
		else:
			time.sleep(2)
			print("Now things are going to get hard!")
			time.sleep(2)
			clear()
			nnow = time.time()
			lol = input("13243 ")
			llater = time.time()
			if lol == "13243" and llater-nnow < 7:
				print("You ate the banana!")
				time.sleep(2)
				print("Time to crank things up!")
				nnow = time.time()
				time.sleep(2)
				clear()
				lol = input("1324351 ")
				llater = time.time()
				if lol == "1324351" and llater-nnow < 7:
					print("You ate the banana!")
					time.sleep(2)
					print("Time to crank things up more!!")
					time.sleep(2)
					clear()
					nnow = time.time()
					lol = input("132435612 ")
					llater = time.time()
					if lol == "132435612" and llater-nnow < 7:
						print("You ate the banana!")
						time.sleep(2)

	else:
		death("instructions")
		return
	clear()
	time.sleep(2)
	print(f"{green}You BEAT level 2! Good job!{reset}")
	if level == 2:
		items.append("level two trophy")
		level = 3
		player_data["level"] = 3
	money += 5
	items.extend(("banana", "banana", "banana", "banana", "spaceship"))


def legal_info():
	clear()
	time.sleep(2)
	print("Loltech Corporation is not responsible for any injuries caused by this game, including but not limited to:")
	print("-Attempting to simulate events in this game, such as Epic Battle Arena. \n-Attempting to hack this game \n-Attempting to be an idiot.")
	print("")
	print("In addition, all code and content in this game is copyright © Loltech Corp, including and limited to:")

	print("Epic Battle Arena™, Formula Banana Racing™, The Formula Banana™, \n-The Speed Banana™, The Offroad Banana™, World's Best Banana Cream Pie™, \n-XK-1 Banana Jet™, and XK-2 Banana Jet™")
	time.sleep(10)
	print("(Just Kidding.)")
	input(f"Press {blue}[Enter]{reset} to go back.")
	clear()
	return

def level_three():
	print(f"{green}You have spawned.{reset}")
	time.sleep(2)
	clear()
	global player_data,items,level,money
	print(f"{green}You have spawned.{reset}")
	print(f"Hello, and welcome to {blue}Epic Battle Arena!{reset}")
	time.sleep(2)
	clear()
	if "sword" not in items and "master sword" not in items and "cool sword" not in items and "M9 gun" not in items:
		weapon_damage = 2
		items.append("sword")
	elif "cool sword" in items:
		weapon_damage = 5
	elif "master sword" in items:
		weapon_damage = 3
	elif "M9 gun" in items:
		weapon_damage = 7
	elif "Machine Pistol" in items:
		weapon_damage = 10
	else:
		weapon_damage = 2
	clear()
	print("First opponent: Troll")
	time.sleep(2)
	troll_hp = 30
	player_hp = 10
	while troll_hp > 0:
		clear()
		print(f"Your hp: {player_hp} Troll hp: {troll_hp}")
		en_attack = random.choice(["punch", "giant club", "homing arrow"])
		if en_attack == "punch":
			en_damage = 1
		elif en_attack == "giant club":
			en_damage = 7
		elif en_attack == "homing arrow":
			en_damage = 9
		else:
			print("You have encountered an error. \nError code 'NotEnchantedTroll'. \nPlease paste Error Code into comments.")
			time.sleep(3)
			return
		print(f"Troll chose {en_attack}.")
		attack = input("1. Attack\n2. Parry \n3. Dodge \n4. Eat Banana")
		if attack == "1":
			troll_hp -= weapon_damage
			player_hp -= en_damage
			print(f"You attacked the Troll for {weapon_damage} damage.")
			time.sleep(1)
			print(f"The Troll attacked you for {en_damage} damage.")
			time.sleep(1)
		elif attack == "2":
			if en_attack != "homing arrow":
				troll_hp -= en_damage
				print(f"You parried the Troll's attack for {en_damage} damage.")
				time.sleep(1)
			else:
				print("The homing arrow exploded on contact.")
				time.sleep(1)
				player_hp -= en_damage
		elif attack == "3":
			print("You dodged the Troll's attack.")
			time.sleep(1)
		elif attack == "4":
			if items.count("frosty banana") > 0:
				print(f"You ate one {blue}Frosty Banana{reset}.")
				time.sleep(2)
				print("You restored 15 hp.")
				player_hp += 15
				player_hp -= en_damage
				time.sleep(2)
				print(f"The Troll attacked you for {en_damage} damage.")
				time.sleep(2)
				items.remove("frosty banana")
			elif items.count("banana") > 0:
				print(f"You ate one {blue}banana{reset}.")
				time.sleep(2)
				print("You restored 10 hp.")
				player_hp += 10
				player_hp -= en_damage
				time.sleep(2)
				print(f"The Troll attacked you for {en_damage} damage.")
				time.sleep(2)
				items.remove("banana")
			else:
				print("You ran out of bananas.")
				time.sleep(2)
		if player_hp < 1:
			death("troll")
			return
	clear()
	print("Hmm, not bad.")
	time.sleep(2)
	print("Let's give you a gun!")
	if items.count("Machine Pistol") > 0:
		time.sleep(2)
		print("Wait, you already have a gun!")
	else:
		items.append("M9 gun")
	weapon_damage = 7
	time.sleep(2)
	clear()
	print("Next opponent: War Robot")
	time.sleep(2)
	robot_hp = 50
	player_hp = 10
	while robot_hp > 0:
		clear()
		print(f"Your hp: {player_hp} War Robot hp: {robot_hp}")
		en_attack = random.choice(["punch", "laser eyes", "epic missile"])
		if en_attack == "punch":
			en_damage = 2
		elif en_attack == "laser eyes":
			en_damage = 8
		elif en_attack == "epic missile":
			en_damage = 11
		else:
			print("You have encountered an error. \nError code 'NotEnchantedWarRobot'. \nPlease paste Error Code into comments.")
			return
		print(f"War Robot chose {en_attack}.")
		attack = input("1. Shoot\n2. Parry \n3. Dodge \n4. Eat Banana")
		if attack == "1":
			robot_hp -= weapon_damage
			player_hp -= en_damage
			print(f"You shot the War Robot for {weapon_damage} damage.")
			time.sleep(1)
			print(f"The War Robot attacked you for {en_damage} damage.")
			time.sleep(1)
		elif attack == "2":
			if en_attack != "epic missile":
				robot_hp -= en_damage
				print(f"You parried the War Robot's attack for {en_damage} damage.")
				time.sleep(1)
			else:
				print("The epic missile exploded on contact.")
				player_hp -= en_damage
				time.sleep(1)
		elif attack == "3":
			print("You dodged the War Robot's attack.")
			time.sleep(1)
		elif attack == "4":
			if items.count("frosty banana") > 0:
				print(f"You ate one {blue}Frosty Banana{reset}.")
				time.sleep(2)
				print("You restored 15 hp.")
				player_hp += 15
				player_hp -= en_damage
				time.sleep(2)
				print(f"The War Robot attacked you for {en_damage} damage.")
				time.sleep(2)
				items.remove("frosty banana")
			elif items.count("banana") > 0:
				print(f"You ate one {blue}banana{reset}.")
				time.sleep(2)
				print("You restored 10 hp.")
				player_hp += 10
				player_hp -= en_damage
				time.sleep(2)
				print(f"The War Robot attacked you for {en_damage} damage.")
				time.sleep(2)
				items.remove("banana")
				
			else:
				print("You ran out of bananas.")
				time.sleep(2)
			if player_hp < 1:
				death("robot")
				return
	clear()
	print(f"You defeated the {blue}War Robot.{reset}")
	time.sleep(2)
	clear()
	print("You passed the warm-up stage!")
	time.sleep(2)
	print("Next opponent: Boss")
	time.sleep(2)
	boss_hp = 100
	player_hp = 10
	while boss_hp > 0:
		clear()
		print(f"Your hp: {player_hp} Boss hp: {boss_hp}")
		en_attack = random.choice(["parry", "laser eyes", "epic missile", "banana peel"])
		if en_attack == "parry":
			en_damage = 2
		elif en_attack == "laser eyes":
			en_damage = 8
		elif en_attack == "epic missile":
			en_damage = 11
		elif en_attack == "banana peel":
			en_damage = 5
		else:
			print("You have encountered an error. \nError code 'NotEnchantedBoss'. \nPlease paste Error Code into comments.")
			return
		print(f"Boss chose {en_attack}.")
		attack = input("1. Shoot\n2. Parry \n3. Dodge \n4. Eat Banana")
		if attack == "1":
			if en_attack != "parry":
				boss_hp -= weapon_damage
				player_hp -= en_damage
				print(f"You shot the Boss for {weapon_damage} damage.")
				time.sleep(1)
				print(f"The Boss attacked you for {en_damage} damage.")
				time.sleep(1)
			else:
				player_hp -= weapon_damage
				print(f"The Boss parried your attack for {weapon_damage} damage.")
		elif attack == "2":
			if en_attack != "epic missile":
				boss_hp -= en_damage
				print(f"You parried the Boss's attack for {en_damage} damage.")
				time.sleep(1)
			else:
				print("The epic missile exploded on contact.")
				player_hp -= en_damage
				time.sleep(1)
		elif attack == "3":
			print("You dodged the Boss's attack.")
			time.sleep(1)
		elif attack == "4":
			if items.count("banana") > 0:
				print(f"You ate one {blue}banana{reset}.")
				time.sleep(2)
				print("You restored 10 hp.")
				player_hp += 10
				player_hp -= en_damage
				time.sleep(2)
				print(f"The Boss attacked you for {en_damage} damage.")
				time.sleep(2)
				items.remove("banana")

			else:
				print("You ran out of bananas.")
				time.sleep(2)
		if player_hp < 1:
			death("boss")
			return
	clear()
	time.sleep(2)
	print(f"You defeated the {blue}Boss.{reset}")
	clear()
	time.sleep(2)
	print(f"{green}You BEAT level 3! Good job!{reset}")
	if level == 3:
		items.append("level three trophy")
		level = 4
		player_data["level"] = 4
	money += 7
	items.append("war robot")



def level_four():
	global player_data,level,items,money
	lspeed = 0
	clear()
	print("This level is WIP.")
	time.sleep(2)
	clear()
	return
	print(f"{green}You have spawned.{reset}")
	time.sleep(2)
	clear()
	print(f"You have been invited by the {magenta}BAF{reset} (Banana Air Force) to defend the border of {blue}Pizza Banana Land.{reset}")
	if "XK-1 banana plane" in items:
		pass



def pie_event():
	global items, money, player_data
	print("You walk into the World's Best Banana Cream Pie...")
	time.sleep(2)
	print("You have been hired to make banana cream pie.")
	time.sleep(2)
	if input("1. Mix banana batter with flour.\n2. Mix bananas with banana batter") == "2":
		clear()
		time.sleep(2)
		print("You finished the first step.")
		if input("1. Pour banana cream onto banana pie\n2. Put banana cream on top of banana pie while doing the goofy dance") == "2":
			clear()
			time.sleep(2)
			print(f"{green}The manager hires you!{reset}")
			time.sleep(2)
			clear()
			print("Time to choose your chef's hat!")
			if input("1. Chef Hat\n2. Brick hat") == "2":
				print("You chose the brick hat.")
				time.sleep(1)
				clear()
			else:
				print("You chose the Chef Hat.")
				time.sleep(1)
				death("brick")
				return
		else:
			time.sleep(2)
			death("instructions")
			return
	else:
		time.sleep(2)
		death("instructions")
		return
	time.sleep(2)
	print(f"{green}YOU BEAT THE PIE EVENT!{reset}")
	items.append("banana pie")
	time.sleep(2)
	clear()
	player_data["events"].append("pie")
	money += 1

def plane_dis():
	global plane_grid
	print(plane_grid[0])
	print(plane_grid[1])
	print(plane_grid[2])

def sword_event():
	global items,player_data, money
	print("Welcome to How to Fight with Swords,\nthe number one swordplay course!")
	time.sleep(3)
	if "sword" not in items and "master sword" not in items and "cool sword" not in items:
		weapon_damage = 2
		print("What??? You only have a STICK???")
		time.sleep(3)
		print("Fine, here's a sword.")
		items.append("sword")
		time.sleep(2)
	elif "cool sword" in items:
		weapon_damage = 5
	elif "master sword" in items:
		weapon_damage = 3
	else:
		weapon_damage = 2
	clear()
	print("First enemy: Zombie")
	time.sleep(3)
	zombie_hp = 10
	player_hp = 10
	while zombie_hp > 0:
		clear()
		print(f"Your hp: {player_hp} Zombie hp: {zombie_hp}")
		print("The zombie chose Punch.")
		attack = input("1. Slash\n2. Parry \n3. Dodge")
		if attack == "1":
			zombie_hp -= weapon_damage
			player_hp -= 1
			print(f"You slashed the zombie for {weapon_damage} damage.")
			time.sleep(1)
			print("The zombie attacked you for 1 damage.")
			time.sleep(1)
		elif attack == "2":
			zombie_hp -= 1
			print(f"You parried the zombies attack for 1 damage.")
			time.sleep(1)
		elif attack == "3":
			print("You dodged the zombie's attack.")
			time.sleep(1)
		if player_hp < 1:
			death("zombie")
			return
	clear()
	time.sleep(3)
	print("Next enemy: Archer")
	time.sleep(3)
	archer_hp = 20
	player_hp = 10
	while archer_hp > 0:
		clear()
		print(f"Your hp: {player_hp} Archer hp: {archer_hp}")
		en_attack = random.choice(["arrow", "enchanted arrow"])
		if en_attack == "arrow":
			en_damage = 1
		elif en_attack == "enchanted arrow":
			en_damage = 5
		else:
			print("You have encountered an error. \nError code 'NotEnchantedArcher'. \nPlease paste Error Code into comments.")
			return
		print(f"Archer chose {en_attack}.")
		attack = input("1. Slash\n2. Parry \n3. Dodge")
		if attack == "1":
			archer_hp -= weapon_damage
			player_hp -= en_damage
			print(f"You slashed the Archer for {weapon_damage} damage.")
			time.sleep(1)
			print(f"The Archer attacked you for {en_damage} damage.")
			time.sleep(1)
		elif attack == "2":
			archer_hp -= en_damage
			print(f"You parried the Archers attack for {en_damage} damage.")
			time.sleep(1)
		elif attack == "3":
			print("You dodged the Archer's attack.")
			time.sleep(1)
		if player_hp < 1:
			death("archer")
			return
	clear()
	time.sleep(3)
	print("Next enemy: Robot")
	time.sleep(3)
	robot_hp = 40
	player_hp = 10
	while robot_hp > 0:
		clear()
		print(f"Your hp: {player_hp} Robot hp: {robot_hp}")
		en_attack = random.choice(["punch", "enchanted arrow", "missile"])
		if en_attack == "punch":
			en_damage = 1
		elif en_attack == "enchanted arrow":
			en_damage = 5
		elif en_attack == "missile":
			en_damage = 9
		else:
			print("You have encountered an error. \nError code 'NotEnchantedRobot'. \nPlease paste Error Code into comments.")
			return
		print(f"Robot chose {en_attack}.")
		attack = input("1. Slash\n2. Parry \n3. Dodge")
		if attack == "1":
			robot_hp -= weapon_damage
			player_hp -= en_damage
			print(f"You slashed the Robot for {weapon_damage} damage.")
			time.sleep(1)
			print(f"The Robot attacked you for {en_damage} damage.")
			time.sleep(1)
		elif attack == "2":
			if en_attack != "missile":
				robot_hp -= en_damage
				print(f"You parried the Robot's {en_attack} for {en_damage} damage.")
				time.sleep(1)
			elif en_attack == "missile":
				player_hp -= en_damage
				print("You failed to parry the robot's missile.")
		elif attack == "3":
			print("You dodged the Robot's attack.")
			time.sleep(1)
		if player_hp < 1:
			death("robot")
			return
	clear()
	items.append("cool sword")
	player_data["events"].append("sword")
	time.sleep(2)
	print(f"Congratulations! You have BEATEN the {blue}sword event!{reset}")
	time.sleep(2)
	clear()
	money += 3


def plane_event():
	global plane_grid,items,player_data,money
	plane_grid = [[" ", " ", " ", " "],[" ", " ", " ", " "],[" ", " ", " ", " "]]
	steps = 20
	plane_or = [" ", " ", " ", " "]
	plane_w = ["✈︎", " ", " ", " "]
	
	if input("press 1 to fly the banana plane") == "1":
		clear()
		plane_grid[1][0] = "✈︎"
		plane_dis()
	else:
		death("instructions")
		return
	if input("press w to go up") == "w":
		clear()
		plane_grid[1] = plane_or
		plane_grid[0] = plane_w
		plane_dis()
	if input("press s to go down") == "s":
		clear()
		plane_grid[1] = plane_w
		plane_grid[0] = plane_or
		plane_dis()
	print("Okay. Now start!")
	time.sleep(1)
	plane_grid = [[" ", " ", " ", " "],[" ", " ", " ", " "],[" ", " ", " ", " "]]
	if input("") == "1":
		plane_grid[1][0] = "✈︎"
		while steps > 0:
			clear()
			plane_dis()
			user_input = input("")
			if user_input == "w":
				clear()
				if plane_grid[1][0] == "✈︎":
					plane_grid[1] = plane_or
					plane_grid[0] = plane_w
				elif plane_grid [0][0] == "✈︎":
					death("edge")
				else:
					plane_grid[2] = plane_or
					plane_grid[1] = plane_w
			elif user_input == "s":
				clear()
				if plane_grid[1][0] == "✈︎":
					plane_grid[1] = plane_or
					plane_grid[2] = plane_w
				elif plane_grid [2][0] == "✈︎":
					death("edge")
					return
				else:
					plane_grid[0] = plane_or
					plane_grid[1] = plane_w
			else:
				pass
			if steps == 18:
				plane_grid[0][3] = "x"
			elif steps == 17:
				plane_grid[0][3] = " "
				plane_grid[0][2] = "x"
			elif steps == 16:
				plane_grid[0][2] = " "
				plane_grid[0][1] = "x"
			elif steps == 15:
				plane_grid[0][1] = " "
				if plane_grid[0][0] == "✈︎":
					death("x")
					return
				plane_grid[0][0] = "x"
			elif steps == 14:
				
				if plane_grid[2][0] == "✈︎":
					pass
				else:
					plane_grid[2][0] = " "
			if steps == 13:
				plane_grid[2][3] = "x"
			elif steps == 12:
				plane_grid[2][3] = " "
				plane_grid[2][2] = "x"
			elif steps == 11:
				plane_grid[2][2] = " "
				plane_grid[2][1] = "x"
			elif steps == 10:
				plane_grid[2][1] = " "
				if plane_grid[2][0] == "✈︎":
					death("x")
					return
				plane_grid[2][0] = "x"
			elif steps == 9:
				if plane_grid[2][0] == "✈︎":
					pass
				else:
					plane_grid[2][0] = " "
			steps -= 1
	else:
		death("instructions")
		return
	clear()
	time.sleep(2)
	print(f"Congratulations! \nYou have BEATEN the {blue}banana plane{reset} event!")
	time.sleep(4)
	clear()
	items.append("XK-2 banana plane")
	player_data["events"].append("plane")
	money += 1



def car_event():
	global player_data,items, money
	clear()
	time.sleep(2)
	print(f"Hello, and welcome to {magenta}Formula Banana Racing!{reset}")
	time.sleep(2)
	if items.count("Xmas Banana Sleigh") > 0 and items.count("Nitro Banana") < 1:
		print("You have the banana sleigh!")
		if input("Would you like to use it? (y/n)") == "y":
			print("You equipped the banana sleigh!")
			time.sleep(2)
			tspeed = 15
			handling = 10
			ccar = "Xmas Banana Sleigh"
		else:
			print("Choose car:")
			print("Stats:")
			print("Speed Banana: speed = 10, handling = 5")
			print("Formula Banana: speed = 7, handling = 7")
			print("Offroad Banana: speed = 5, handling = 10")
			car = input("1. Speed Banana \n2. Formula Banana \n3. Offroad Banana")
			if car == "1":
				tspeed = 10
				handling = 5
				print("You have chosen the Speed Banana!")
				time.sleep(2)
				ccar = "Speed Banana"
			elif car == "2":
				tspeed = 7
				handling = 7
				print("You have chosen the Formula Banana!")
				time.sleep(2)
				ccar = "Formula Banana"
			else:
				tspeed = 5
				handling = 10
				print("You have chosen the Offroad Banana!")
				time.sleep(2)
				ccar = "Offroad Banana"
	elif items.count("Nitro Banana") > 0 and items.count("Xmas Banana Sleigh") < 1:
		print("You have the Nitro Banana")
		if input("Would you like to use it? (y/n)") == "y":
			print("You equipped the Nitro Banana!")
			time.sleep(2)
			tspeed = 17
			handling = 9
			ccar = "Nitro Banana"
		else:
			print("Choose car:")
			print("Stats:")
			print("Speed Banana: speed = 10, handling = 5")
			print("Formula Banana: speed = 7, handling = 7")
			print("Offroad Banana: speed = 5, handling = 10")
			car = input("1. Speed Banana \n2. Formula Banana \n3. Offroad Banana")
			if car == "1":
				tspeed = 10
				handling = 5
				print("You have chosen the Speed Banana!")
				time.sleep(2)
				ccar = "Speed Banana"
			elif car == "2":
				tspeed = 7
				handling = 7
				print("You have chosen the Formula Banana!")
				time.sleep(2)
				ccar = "Formula Banana"
			else:
				tspeed = 5
				handling = 10
				print("You have chosen the Offroad Banana!")
				time.sleep(2)
				ccar = "Offroad Banana"
	elif items.count("Nitro Banana") > 0 and items.count("Xmas Banana Sleigh") > 0:
		print("You have the Nitro Banana and the Xmas Banana Sleigh!")
		if input("Would you like to use the Nitro Banana? (y/n)") == "y":
			print("You equipped the Nitro Banana!")
			time.sleep(2)
			tspeed = 17
			handling = 9
			ccar = "Nitro Banana"
		else:
			if input("Would you like to use the Xmas Banana Sleigh? (y/n)") == "y":
				print("You equipped the Xmas Banana Sleigh!")
				time.sleep(2)
				tspeed = 15
				handling = 10
				ccar = "Xmas Banana Sleigh"
			else:
				print("Choose car:")
				print("Stats:")
				print("Speed Banana: speed = 10, handling = 5")
				print("Formula Banana: speed = 7, handling = 7")
				print("Offroad Banana: speed = 5, handling = 10")
				car = input("1. Speed Banana \n2. Formula Banana \n3. Offroad Banana")
				if car == "1":
					tspeed = 10
					handling = 5
					print("You have chosen the Speed Banana!")
					time.sleep(2)
					ccar = "Speed Banana"
				elif car == "2":
					tspeed = 7
					handling = 7
					print("You have chosen the Formula Banana!")
					time.sleep(2)
					ccar = "Formula Banana"
				else:
					tspeed = 5
					handling = 10
					print("You have chosen the Offroad Banana!")
					time.sleep(2)
					ccar = "Offroad Banana"
	else:
		print("Choose car:")
		print("Stats:")
		print("Speed Banana: speed = 10, handling = 5")
		print("Formula Banana: speed = 7, handling = 7")
		print("Offroad Banana: speed = 5, handling = 10")
		car = input("1. Speed Banana \n2. Formula Banana \n3. Offroad Banana")
		if car == "1":
			tspeed = 10
			handling = 5
			print("You have chosen the Speed Banana!")
			time.sleep(2)
			ccar = "Speed Banana"
		elif car == "2":
			tspeed = 7
			handling = 7
			print("You have chosen the Formula Banana!")
			time.sleep(2)
			ccar = "Formula Banana"
		else:
			tspeed = 5
			handling = 10
			print("You have chosen the Offroad Banana!")
			time.sleep(2)
			ccar = "Offroad Banana"
	distance = 60
	ltime = 0
	while distance >= 0:
		clear()
		print(f"You are {round(distance, 1)} km away from the finish line.")
		if not (12 <= distance <= 18) and not (27 <= distance <= 33) and not (42 <= distance <= 48):
			print("You are on a straightaway.")
			terrain = "straight"
		else:
			print("You see a turn ahead.")
			terrain = "turn"
		choice = input("1. Go straight\n2. Brake")
		
		if terrain == "turn" and choice == "1":
			print("The turn forces you to slow down.")
			lspeed = handling/7
			time.sleep(1)
		elif terrain == "turn" and choice != "1":
			print("You slow down a little and accelerate into the turn.")
			lspeed = handling/3
			time.sleep(1)
		elif terrain == "straight" and choice == "1":
			print("You accelerate.")
			lspeed = tspeed/5
			time.sleep(1)
		elif terrain == "straight" and choice != "1":
			print("You slow down.")
			lspeed = tspeed/10
			time.sleep(1)
		else:
			lspeed = tspeed/7.5
		distance -= lspeed
		ltime += 1
	clear()
	time.sleep(3)
	print(f"You took {blue}{ltime}.0{reset} minutes.")
	
	if ltime <= 45:
		print("You got first place!")
		items.append("Formula Banana Gold Trophy")
		money += 3
	elif ltime <= 50:
		print("You got second place!")
		items.append("Formula Banana Silver Trophy")
		money += 3
	elif ltime <= 55:
		print("You got third place!")
		items.append("Formula Banana Bronze Trophy")
		money += 3
	else:
		death("car")
		return
	time.sleep(3)
	clear()
	print(f"Congratulations! \nYou have BEATEN the {blue}car{reset} event using the {blue}{ccar}!{reset}")
	items.append(ccar)
	player_data["events"].append("car")
	time.sleep(4)
	clear()

def shop():
	clear()
	global items,money,amount_in_stock
	print("Welcome to the Traveler's Store!")
	choicee = input("Would you like to buy or sell? (b/s)")
	if choicee == "b":
		buy()
	else:
		sell()

def sell():
	global items,money,amount_in_stock
	print("You currently have:")
	printed_items = []
	for item in items:
		if item not in printed_items:
			printed_items.append(item)
			time.sleep(0.1)
			print(f"{items.count(item)}x {item}")
	itemstb = input("What would you like to sell? l to leave.")
	while itemstb != "l":
		if itemstb in printed_items:
			if itemstb == "Formula Banana Gold Trophy":
				print("That costs 5 BananaCash.")
				if input("Are you sure you would like to sell this? (y/n)") == "y":
					print(f"You sold your {itemstb}")
					items.remove(itemstb)
					money += 5
			elif itemstb == "Formula Banana Silver Trophy":
				print("That costs 3 BananaCash.")
				if input("Are you sure you would like to sell this? (y/n)") == "y":
					print(f"You sold your {itemstb}")
					items.remove(itemstb)
					money += 3
			elif itemstb == "Formula Banana Bronze Trophy":
				print("That costs 1 coin.")
				if input("Are you sure you would like to sell this? (y/n)") == "y":
					print(f"You sold your {itemstb}")
					items.remove(itemstb)
					money += 1
			elif itemstb == "banana":
				print("That costs 2 BananaCash.")
				if input("Are you sure you would like to sell this? (y/n)") == "y":
					print(f"You sold your {itemstb}")
					items.remove(itemstb)
					money += 2
			elif itemstb == "Machine Pistol":
				print("That costs 6 BananaCash.")
				if input("Are you sure you would like to sell this? (y/n)") == "y":
					print(f"You sold your {itemstb}")
					items.remove(itemstb)
					money += 6
			elif itemstb == "M9 gun":
				print("That costs 3 BananaCash.")
				if input("Are you sure you would like to sell this? (y/n)") == "y":
					print(f"You sold your {itemstb}")
					items.remove(itemstb)
					money += 3
			elif itemstb == "war robot":
				print("That costs 15 BananaCash.")
				if input("Are you sure you would like to sell this? (y/n)") == "y":
					print(f"You sold your {itemstb}")
					items.remove(itemstb)
					money += 15
			elif itemstb == "banana pie":
				print("That costs 5 BananaCash.")
				if input("Are you sure you would like to sell this? (y/n)") == "y":
					print(f"You sold your {itemstb}")
					items.remove(itemstb)
					money += 5
			elif itemstb == "Nitro Banana":
				print("That costs 8 BananaCash.")
				if input("Are you sure you would like to sell this? (y/n)") == "y":
					print(f"You sold your {itemstb}")
					items.remove(itemstb)
					money += 5
			elif itemstb == "Xmas Banana Sleigh":
				print("That costs 13 BananaCash.")
				if input("Are you sure you would like to sell this? (y/n)") == "y":
					print(f"You sold your {itemstb}")
					items.remove(itemstb)
					money += 5
			elif itemstb == "spaceship":
				print("That costs 12 BananaCash.")
				if input("Are you sure you would like to sell this? (y/n)") == "y":
					print(f"You sold your {itemstb}")
					items.remove(itemstb)
					money += 12
			elif itemstb == "frosty banana":
				print("That costs 3 BananaCash.")
				if input("Are you sure you would like to sell this? (y/n)") == "y":
					print(f"You sold your {itemstb}")
					items.remove(itemstb)
					money += 3
			elif itemstb == "sword":
				print("That costs 2 BananaCash.")
				if input("Are you sure you would like to sell this? (y/n)") == "y":
					print(f"You sold your {itemstb}")
					items.remove(itemstb)
					money += 2
			elif itemstb == "master sword":
				print("That costs 4 BananaCash.")
				if input("Are you sure you would like to sell this? (y/n)") == "y":
					print(f"You sold your {itemstb}")
					items.remove(itemstb)
					money += 4
			elif itemstb == "cool sword":
				print("That costs 6 BananaCash.")
				if input("Are you sure you would like to sell this? (y/n)") == "y":
					print(f"You sold your {itemstb}")
					items.remove(itemstb)
					money += 6
			else:
				print("The item you tried to sell was not logged yet. Please report this in the comments.")
		else:
			print("You don't have this!")
		printed_items = []
		for item in items:
			if item not in printed_items:
				printed_items.append(item)
				time.sleep(0.1)
				print(f"{items.count(item)}x {item}")
		itemstb = input("What would you like to sell? l to leave.")

def buy():
	global items,money,amount_in_stock
	hack_var = os.environ['HACK_LOL']
	shop_items = ["Nitro Banana", "Machine Pistol", "banana"]
	shop_items_cost = [10, 7, 3, 15, 4]
	
	if today.month == 12:
		shop_items.extend(("Xmas Banana Sleigh", "frosty banana"))
	clear()
	print(f"You have {money} BananaCash.")
	print("The shopowner currently has:")
	for item in shop_items:
		print(f"{item} for {shop_items_cost[shop_items.index(item)]}, with {amount_in_stock[shop_items.index(item)]} in stock.")
	itemstb = input("What would you like to buy? l to leave.")
	if itemstb == hack_var:
		print("lol")
		money += 1000
	while itemstb != "l":
		if itemstb in shop_items:
			if itemstb == "Nitro Banana":
				if money >= 10:
					money -= 10
					items.append("Nitro Banana")
					print("You have bought the Nitro Banana!")
					time.sleep(2)
					shop_items.remove("Nitro Banana")
				else:
					print(f"You tried to buy [Nitro Banana] for [10] BananaCash, but you only have[{money}] BananaCash.")
					input("press enter to continue:")
			elif itemstb == "banana":
				if money >= 3:
					money -= 3
					items.append("banana")
					print("You bought [1] banana!")
				else:
					print(f"You tried to buy [banana] for [3] BananaCash, but you only have[{money}] BananaCash.")
					input("press enter to continue:")
			elif itemstb == "Machine Pistol":
				if money >= 7:
					money -= 7
					items.append("Machine Pistol")
					print("You bought the Machine Pistol!")
					shop_items.remove("Machine Pistol")
				else:
					print(f"You tried to buy [banana] for [3] BananaCash, but you only have[{money}] BananaCash.")
					input("press enter to continue:")
			elif itemstb == "Xmas Banana Sleigh":
				if money >= 15:
					money -= 15
					items.append("Xmas Banana Sleigh")
					print("You bought an Xmas Banana Sleigh!")
					shop_items.remove("Xmas Banana Sleigh")
				else:
					print(f"You tried to buy [Xmas Banana Sleigh] for [15] BananaCash, but you only have[{money}] BananaCash.")
					input("press enter to continue:")
			elif itemstb == "frosty banana":
				if money >= 4:
					money -= 4
					items.append("frosty banana")
					print("You bought [1] frosty banana!")
				else:
					print(f"You tried to buy [frosty banana] for [4] BananaCash, but you only have[{money}] BananaCash.")
					input("press enter to continue:")
		itemstb = input("What else would you like to buy? l to leave.")
	clear()
	
def menu():
	global items, level, prompts, player_data, money
	clear()
	time.sleep(2)
	while True:
		print(f"You currently have {money} BananaCash")
		print("Press p to view the shop")
		print("Press c/l to see copyright/legal content.")
		print("Press r to replay a level.")
		print("Press d to see your data.")
		print("__________________________")
		print("Press l to load your data.")
		print("Press s to save your data.")
		print("Press i to see your inventory.")
		print("Press e to see today's events.")
		print(f"You are at level {level}.")
		action = input(f"Press {blue}[ENTER]{reset} to play.")
		if action == "":
			clear()
			if level == 1:
				level_one()
				time.sleep(1)
				clear()
				menu()
			elif level == 2:
				level_two()
				time.sleep(1)
				clear()
				menu()
			elif level == 3:
				level_three()
				time.sleep(1)
				clear()
				menu()
			elif level == 4:
				level_four()
				time.sleep(1)
				clear()
				menu()
		elif action == "e":
			clear()
			time.sleep(1)
			print("Here are today's events!")
			if today.weekday() == 1:
				print("Today's event is: How to make banana cream pie. \nType 'pie' in the menu to try it out!")

			elif today.weekday() == 2:
				print("Today's event is: How to fly banana planes. \nType 'plane' in the menu to try it out!")
			elif today.weekday() == 3:
				print("Today's event is: How to use a sword. \nType 'sword' in the menu to try it out!")
			elif today.weekday() == 4:
				print("Today's event is: How to drive banana cars. \nType 'car' in the menu to try it out!")
			elif today.weekday() == 5:
				print("Today's event is: How to use a sword. \nType 'sword' in the menu to try it out!")
			elif today.weekday() == 6:
				print("Today's event is: How to fly banana planes. \nType 'plane' in the menu to try it out!")
			elif today.weekday() == 7:
				print("Today's event is: How to drive banana cars. \nType 'car' in the menu to try it out!")
			else:
				print("Sorry, no events are happening today.")
			print('''
			Monday: How to make banana cream pie
			Tuesday: How to fly banana planes
			Wednesday: How to use a sword
			Thursday: How to drive banana cars
			Friday: How to use a sword
			Saturday: How to fly banana planes
			Sunday: How to drive banana cars
			''')
			esc_event = input(f"Press {blue}[ENTER]{reset} to go to main menu.")
			clear()
			if esc_event != "":
				death("instructions")
				break
		elif action == cheat:
			clear()
			print(f"Whoa Whoa Whoa! Is that a {red}cheat code?{reset}")
			time.sleep(2)
			print("It seems like you're on the wrong level!")
			time.sleep(2)
			death("cheating")
			break
		elif action == "pie" and today.weekday() == 1:
			clear()
			pie_event()
		elif action == "plane" and today.weekday() == 2:
			clear()
			plane_event()
		elif action == "sword" and today.weekday() == 3:
			clear()
			sword_event()
		elif action == "car" and today.weekday() == 4:
			clear()
			car_event()
		elif action == "sword" and today.weekday() == 5:
			clear()
			sword_event()
		elif action == "plane" and today.weekday() == 6:
			clear()
			plane_event()
		elif action == "car" and today.weekday() == 7:
			clear()
			car_event()
		elif action == "i":
			
			clear()
			print("Your inventory contains:")
			printed_items = []
			for item in items:
				if item not in printed_items:
					printed_items.append(item)
					time.sleep(0.1)
					print(f"{items.count(item)}x {item}")
			input("Press enter to go to the main menu")
			clear()
		elif action == "s":
			print("Saving... (if you finish reading this, replit may be unstable)")
			player_data["money"] = money
			existing_data = {}
			try:
			    with open('data.json', 'r') as file:
			        existing_data = json.load(file)
			except FileNotFoundError:
			    pass
			# Update with new player data
			player_data = {
			    "name": "John",
			    "score": 100
			}
			existing_data.update(player_data)
			# Save the combined data back to the file
			with open('data.json', 'w') as file:
			    json.dump(existing_data, file)
			clear()
		elif action == "l":
			print("Loading... (if you finish reading this, replit may be unstable)")
			try:
				player_data = db[user_name]
				items = player_data["items"]
				level = player_data["level"]
				money = player_data["money"]
				clear()
				print("Done loading! Note that your current data is now gone.")
				print("If you didn't realize that, you are an idiot.")
				time.sleep(3)
			except KeyError:
				clear()
				print("It appears that you have not saved your data.")
				print("Save your data before trying to load your data.")
				time.sleep(3)
			clear()
		elif action == "r":
			clear()
			if level == 1:
				print("No levels available to replay.")
				time.sleep(3)
				clear()
				menu()
			elif level == 2:
				if input("Level 1 is available. Type '1' to play.") == "1":
					level_one()
				else:
					print("Unidentified input. \nSending back to menu...")
					time.sleep(3)
					menu()
			elif level == 3:
				lolll = input("Levels 1 and 2 are available. Type '1' or '2' to play.")
				if lolll == "1":
					level_one()
				elif lolll == "2":
					level_two()
				else:
					print("Unidentified input. \nSending back to menu...")
					time.sleep(3)
					menu()
			elif level == 4:
				lolll = input("Levels 1, 2, and 3 are available. Type '1', '2', or '3' to play.")
				if lolll == "1":
					level_one()
				elif lolll == "2":
					level_two()
				elif lolll == "3":
					level_three()
				else:
					print("Unidentified input. \nSending back to menu...")
					time.sleep(3)
					menu()
			elif level == 5:
				lolll = input("Levels 1, 2, 3, and 4 are available. Type '1', '2', '3', or '4' to play.")
				if lolll == "1":
					level_one()
				elif lolll == "2":
					level_two()
				elif lolll == "3":
					level_three()
				elif lolll == "3":
					level_four()
				else:
					print("Unidentified input. \nSending back to menu...")
					time.sleep(3)
					menu()
			elif level == 6:
				db[user_name] = "HACKING!!!"
				print("YOU HAZ BEEN HACKING")
				time.sleep(3)
				print("YOU HAZ BEEN HACKING")
				os._exit(0)
		elif action == "c/l":
			legal_info()
		elif action == "p":
			shop()
		elif action == "d":
			clear()
			player_data["money"] = money
			db[user_name] = player_data
			print(player_data)
			input("Press enter to go to the main menu")
			clear()
		else:
			print("unknown input.")
try:
	if db[user_name] == "HACKING!!!":
		print("GET OUTTA MY CAR!!!")
		time.sleep(1.41421)
		os._exit(0)
except KeyError:
	pass
print(logo2)
now_n = time.time()
start = input(f"Press {blue}[ENTER]{reset} to start:")
if start == "":
	later = time.time()
	if later - now_n > 60:
		death("old age")
	else:
		clear()
		menu()
elif start == "goofyguy382":
	
	later = time.time()
	if later - now_n > 60:
		death("old age")
	else:
		print("You have unlocked some bonus content!")
		time.sleep(2)
		print("You now have cool items in your inventory.")
		items.extend(("master sword", "XK-1 banana plane", "golden banana"))
		time.sleep(2)
		clear()
		menu()
else:
	later = time.time()
	if later - now_n > 60:
		death("old age")
	else:
		death("instructions")
