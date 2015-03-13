from django.shortcuts import render
from django.http import HttpResponse

from minion_generator import Character_Generator,Minion

# Create your views here.

def index(request):

	return render(request,'generator/index.html')



def minion_list(request):


	generator=Character_Generator()
	generator.create_minions(5)



	return render(request,'generator/minionlist.html',{'minions':generator.char_list})