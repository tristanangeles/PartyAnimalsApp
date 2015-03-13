import math,xlrd,random

from .models import Trait,Name



species_list=['Rooster','Monkey','Buffalo','Elephant','Lizard',	'Owl','Turtle',	'Bear',	'Lion',	'Crow','Mouse']



class Character_Generator():

	def __init__(self):

		self.char_list=[]





	def create_minions(self,number):

		#create minions
		for i in range(number):
			new_minion=self.create_minion()
			self.char_list.insert(i,new_minion)



	def create_minion(self):

		#create minion
		species=species_list[random.randrange(0,len(species_list))]
		
		new_minion=Minion(species,3)

		return new_minion






class Minion():

	def __init__(self,species,num_traits):

		self.species=species
		self.name=self.__random_name()
		self.traits=self.__random_traits(num_traits)
		self.salary=self.__random_salary()
		


	def __random_name(self):
		names=list(Name.objects.filter(species=self.species))
		name=names[random.randrange(0,len(names))]

		print(name)

		return name


	def __random_traits(self,num_traits):
		pass



	def __random_salary(self):
		pass


