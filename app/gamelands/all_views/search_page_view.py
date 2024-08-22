from django.shortcuts import render
from gamelands.models import  Games, Genres
import operator
from django.db.models import Q
from functools import reduce
def search_page(request):
    from_year = 1980
    to_year = 2040
    variable = "-metacritic_score"
    search_auto = ""
    if request.POST.get("from_year"):
        from_year = request.POST.get("from_year")
    if request.POST.get("to_year"):
        to_year = request.POST.get("to_year")
    if request.POST.get("game_filters"):
        variable =  request.POST.get('game_filters')
    if request.POST.get("searchbar"):
        search_auto = request.POST.get("searchbar")
    all_devs_arr = []

    raw_genres_db = Genres.objects.all().values_list('genre')
    all_genres_arr = list(map(lambda x: x[0], raw_genres_db))
    
           
    for value in Games.objects.values("developers"):
        all_devs_arr.append(value["developers"])
    all_devs_arr = ", ".join(all_devs_arr)
    all_devs_arr  = all_devs_arr.split(", ")
    all_devs_arr = list(set(all_devs_arr))
    dev_filter = []
    for keys in request.POST.keys():
        if keys.startswith("checkbox"):
            dev_filter.append(keys[9:])
    filtered = Games.objects.filter(release_year__range = (from_year, to_year))
    filtered = filtered.filter(game_name__icontains = search_auto)
    if len(dev_filter) >= 1:
        filtered = filtered.filter(reduce(operator.or_,(Q(developers__icontains = x) for x in dev_filter)))
    filtered = filtered.order_by(variable)
    option_text = {"-metacritic_score": "From highest to lowest",
                   "metacritic_score" : "From lowest score to highest" ,
                   "release_year" : "Release year", 
                   "howlongtobeat" : "HowLongToBeat",
                   }
    print(request.POST.get("refresh"))          
    if request.POST.get("refresh") is not None:
        from_year = 1980
        to_year = 2040
        variable = "-metacritic_score"
        search_auto = ""
        dev_filter = []
        genre_filter = []
    context = {
        "games": filtered,
        "search_filter" : search_auto, 
        "all_devs": all_devs_arr,      
        "from_year" : from_year if from_year != 1980 else "",
        "to_year" : to_year if to_year != 2040 else "",
        "sorted_options" : option_text,
        "drop_list" : variable,
        "checkbox_check" : dev_filter,
       
    }
    return render(request, 'html/search.html', context=context)