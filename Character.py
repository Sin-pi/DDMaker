import secrets
import math

Recomended = {"Barbarian":"Strength And Constitution",
			  "Bard":"Charisma and Dexterity",
			  "Cleric":"Wisdom and Dexterity",
			  "Druid":"Wisdom and Dexterity",
			  "Fighter": "Strength And Constitution",
			  "Monk": "Dexterity and Wisdom",
			  "Paladin": "Character and Constitution",
			  "Ranger": "Dexterity and Constitution",
			  "Rouge": "Dexterity and Constitution",
			  "Sorcerer":"Charisma and Dexterity",
			  "Warlock":"Charisma and Dexterity",
			  "Wizard":"Intelligence and Constitution"}


class Character():

	def __init__(self, name,lvl):
		self.charName=name
		self.speed = 30
		self.alignment = {"Lawful Good" : False,"Neutral Good" : False,"Chaotic Good": False,"Lawful Neutral": False,"True Neutral": False,"Chaotic Neutral": False,"Lawful Evil": False,"Neutral Evil": False, "Chaotic Evil":False}
		self.proficiencyScore = (2+math.floor(lvl/4))
		self.skills = { "Str": {"Athletics": False},
					"Dex": {"Acrobatics" : False,"Sleight of Hand" : False,"Stealth" : False},
					"Int" : {"Arcana" : False,"History": False,"Investigation" : False,"Nature" : False,"Religion" : False},
					"Wis" : {"Animal Handling" : False,"Insight" : False,"Medicine" : False,"Perception" : False, "Survival" : False},
					"Char" : {"Deception": False, "intimidation" : False,"Performance" : False,"Persuasion" : False},
				}
		self.Langauge = ["Common"]
		self.features={}
		self.inventory = {}
		self.Weapons = {}
		self.Armor = {}
		self.spells = {}


	def RollMyScores(self):
		scores = []
		for x in range(6):
			rolls = []
			for x in range(4):
				rolls.append(secrets.randbelow(6)+1)
			rolls.sort()
			rolls.pop(0)
			scores.append(sum(rolls))
		scores.sort(reverse=True)
		return scores

	def setMyScorces(self,recomend=""):
		myRolls = self.RollMyScores()
		abilityScores = {}
		Abilities = ["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]
		chosen = 0
		print("Choose your AbilityScores(High to low)")
		while chosen < 6:
			print(Abilities)
			print("Choose Ability for Score "+str(myRolls[chosen])+"("+recomend+" is recomended)\n") if chosen < 2 else print("Choose Ability for Score "+str(myRolls[chosen])+"\n")
			value = input()
			if value in Abilities:
				abilityScores[value] = myRolls[chosen]
				Abilities.remove(value)
				chosen +=1
			else:
				print("Incorrect Value")
		print(abilityScores)
		return abilityScores

	def calculateModifiers(self,AbilityScore):
		modifier = math.floor((AbilityScore -10)/2)
		return modifier












class Barbarian(Character):
	def __init__(self,*args,**kwargs):
		super(Barbarian,self).__init__(args[0],args[1])
		self.AbilityScores = super(Barbarian,self).setMyScorces(Recomended["Barbarian"])
		
class Bard(Character):
	def __init__(self,*args,**kwargs):
		super(Bard,self).__init__(args[0],args[1])
		self.AbilityScores = super(Bard,self).setMyScorces(Recomended["Bard"])

class Cleric(Character):
	def __init__(self,*args,**kwargs):
		super(Cleric,self).__init__(args[0],args[1])
		self.AbilityScores = super(Cleric,self).setMyScorces(Recomended["Cleric"])
	
class Druid(Character):
	def __init__(self,*args,**kwargs):
		super(Druid,self).__init__(args[0],args[1])
		self.AbilityScores = super(Druid,self).setMyScorces(Recomended["Druid"])
	
class Fighter(Character):
	def __init__(self,*args,**kwargs):
		super(Fighter,self).__init__(args[0],args[1])
		self.AbilityScores = super(Fighter,self).setMyScorces(Recomended["Fighter"])
	
class Monk(Character):
	def __init__(self,*args,**kwargs):
		super(Monk,self).__init__(args[0],args[1])
		self.AbilityScores = super(Monk,self).setMyScorces(Recomended["Monk"])	

class Paladin(Character):
	def __init__(self,*args,**kwargs):
		super(Paladin,self).__init__(args[0],args[1])
		self.AbilityScores = super(Paladin,self).setMyScorces(Recomended["Paladin"])	

class Ranger(Character):
	def __init__(self,*args,**kwargs):
		super(Ranger,self).__init__(args[0],args[1])
		self.AbilityScores = super(Ranger,self).setMyScorces(Recomended["Ranger"])

class Rouge(Character):
	def __init__(self,*args,**kwargs):
		super(Rouge,self).__init__(args[0],args[1])
		self.AbilityScores = super(Rouge,self).setMyScorces(Recomended["Rouge"])	

class Sorcerer(Character):
	def __init__(self,*args,**kwargs):
		super(Sorcerer,self).__init__(args[0],args[1])
		self.AbilityScores = super(Sorcerer,self).setMyScorces(Recomended["Sorcerer"])	

class Warlock(Character):
	def __init__(self,*args,**kwargs):
		super(Warlock,self).__init__(args[0],args[1])
		self.AbilityScores = super(Warlock,self).setMyScorces(Recomended["Warlock"])

class Wizard(Character):
	def __init__(self,*args,**kwargs):
		super(Wizard,self).__init__(args[0],args[1])
		self.AbilityScores = super(Wizard,self).setMyScorces(Recomended["Wizard"])



class Background():

	def __init__(self,skills,prof1,prof2,items,feat,tooltype=''):
		self.skills = skills
		if (prof1 == 1):
			self.prof1 = input("pick any "+tooltype+".\n")
		elif (prof1 == 2):
			self.prof1 = input("pick any Langauge.\n")
		else:
			self.prof1 = prof1

		if (prof2 == 1):
			self.prof2 = input("pick any "+tooltype+".\n")
		elif (prof1 == 2):
			self.prof2 = input("pick any Langauge.\n")
		else:
			self.prof2 = prof2
		self.items = items
		self.feat = feat

AcolEquip = ['A holy symbol', 'prayer book or prayer wheel','5 sticks of incense',' vestments','set of common clothes','belt pouch containing 15 gp']
AcolFeat = 'As an acolyte, you command the respect of those who share your faith, and you can perform the religious cerem onies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. Those w ho share your religion will support you (but only you) at a modest lifestyle. You might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This could be the temple where you used to serve, if you remain on good terms with it, or a temple where you have found a new home. W hile near your temple, you can call upon the priests for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple.'
Acolyte = Background(["Insight","Religion"],2,2,AcolEquip,AcolFeat)

CharlatainEquip = ['set of fine clothes','disguise kit','tools of the con of your choice (ten stoppered bottles filled with colored liquid, a set of weighted dice, a deck of marked cards, or a signet ring of an imaginary duke)','belt pouch containing 15 gp']
CharlatainFeat = 'Favorite Schemes\nEvery charlatan has an angle he or she uses in preference to other schemes. Choose a favorite scam or roll on the table below.\n1:I cheat at games of chance.\n2:I shave coins or forge documents.\n3:I insinuate myself into people’s lives to prey on their weakness and secure their fortunes.\n4: I put on new identities like clothes.\n5: I run sleight-of-hand cons on street corners.\n6 I convince people that worthless junk is worth their hard-earned money.\n\nFalse Identitiy\nYou have created a second identity that includes documentation, established acquaintances, and disguises that allow you to assume that persona. Additionally, you can forge documents including official papers and personal letters, as long as you have seen an example of the kind of document or the handwriting you are trying to copy.'
Charlatan = Background(["Deception","Sleight of Hand"],"Disguise kit","forgery kit",CharlatainEquip,CharlatainFeat)

CriminalEquip = ['crowbar','set of dark common clothes with hood','belt pouch containing 15 gp']
CriminalFeat = 'Criminal Specialty\nThere are many kinds of criminals, and within a thieves’ guild or similar criminal organization, individual mem bers have particular specialties. Even criminals who operate outside of such organizations have strong preferences for certain kinds of crim es over others. Choose the role you played in your criminal life, or roll on the table below.\n1: Blackmailer\n2: Burglar\n3: Enforcer\n4: Fence\n5: Highway Robber\n6: Hired Killer\n7: Pickpocket\n8: Smuggler\n\n Criminal Contact\nYou have a reliable and trustworthy contact w ho acts as your liaison to a network of other criminals. You know how to get m essages to and from your contact, even over great distances; specifically, you know the local m essengers, corrupt caravan masters, and seedy sailors who can deliver m essages for you.'
Criminal = Background(['Deception','Stealth'],1,'Thieve\'s tools',CriminalEquip,CriminalFeat,'Gaming set')

EntertainerEquip =['Musical Instrument','love letter,lock of hear, or trinket','costume','belt pouch containing 15gp']
EntertainerFeat = 'By Popular Demand\nYou can always find a place to perform, usually in an inn or tavern but possibly with a circus, at a theater, or even in a noble’s court. At such a place, you receive free lodging and food of a modest or comfortable standard (depending on the quality of the establishment), as long as you perform each night. In addition, your performance makes you something of a local figure. W hen strangers recognize you in a town where you have performed, they typically take a liking to you'
Entertainer = Background(['Acrobatics','Performance'],'Disguise kit',1,EntertainerEquip,EntertainerFeat,'Musical Instrument')

FolkEquip = ['any Artisan\'s tools','shovel','iron pot','common clothes','belt pouch with 15gp']
FolkFeat = 'Rustic Hospitality\nSince you com e from the ranks of the com m on folk, you fit in among them with ease. You can find a place to hide, rest, or recuperate among other commoners, unless you have shown yourself to be a danger to them. They will shield you from the law or anyone else searching for you, though they will not risk their lives for you.'
FolkHero = Background(['Animal Handling','Survival'],1,'Vehicles(land)',FolkEquip,FolkFeat,'Artisan\'s tools')

GuildEquip = ['any Artisan\'s tools','letter of introduction from guild','traveler\'s clothes','belt pouch with 15gp']
GuildFeat  = 'Guild Membership\nAs an established and respected member of a guild, you can rely on certain benefits that membership provides. Your fellow guild mem bers will provide you with lodging and food if necessary, and pay for your funeral if needed. In som e cities and towns, a guildhall offers a central place to meet other members of your profession, which can be a good place to meet potential patrons, allies, or hirelings. Guilds often wield tremendous political power. If you are accused of a crime, your guild will support you if a good case can be made for your innocence or the crime is justifiable. You can also gain access to powerful political figures through the guild, if you are a member in good standing. Such connections might require the donation of money or magic items to the guild’s coffers. You must pay dues of 5 gp per month to the guild. If you m iss payments, you must make up back dues to remain in the guild’s good graces.'
GuildArtisan = Background(['Insight','Persuasion'],1,2,'Artisan\'s tool')

HermitEquip = ['scroll of notes from studies/religion','winter blanket','common clothes','herbalism kit','5gp']
HermitFeat = 'Discovery\nThe quiet seclusion of your extended hermitage gave you access to a unique and powerful discovery. The exact nature of this revelation depends on the nature of your seclusion. It might be a great truth about the cosm os, the deities, the powerful beings of the outer planes, or the forces of nature. It could be a site that no one else has ever seen. You might have uncovered a fact that has long been forgotten, or unearthed som e relic of the past that could rewrite history. It might be information that would be damaging to the people w ho or consigned you to exile, and hence the reason for your return to society. Work with your DM to determine the details of your discovery and its impact on the campaign.'
Hermit = Background(['Medicine','Religion'],'Herbalism kit',2,HermitEquip,HermitFeat)

NobleEquip = 
NobleFeat = 
Noble = Background()


'''
1. pick class
2. pick name
3. race
4.roll abilities
5 set based on class
6 add race bonuses
7 choose Background
8 choose skills
9 choose equiment
10 fill out weapons 
11 fill out armor
12 pick out spells
13
'''