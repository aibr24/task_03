from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
	

    context = { 
    	"my_list": [
    	 {
    	 "restaurant_name": "Dominoes", 
    	 "food_type": "pizza" 
    	 },
    	 {
    	 "restaurant_name": "The Hut",
    	 "food_type": "pizza"
    	 },
    	 {
    	 "restaurant_name": "PapaJohn's",
    	 "food_type": "pizza"
    	 }


    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {"my_object":["Dominoes", "pizza"]

    }
    return render(request, 'detail.html', context)
