from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.templatetags.static import static
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import pandas
import os
import random
from django.shortcuts import redirect
from gamelands.models import User, Table, Games
from django.urls import reverse
import operator
from django.db.models import Q
from functools import reduce


def return_index(request):
    context = {
        "games":[]
    }
    url = static("content/database.xlsx")
    base_path = str(os.path.join (settings.BASE_DIR))
    data = pandas.read_excel(base_path + url)
    number_of_rows = (data[data.columns[0]].count())
    for i in random.sample(list(range(number_of_rows)), k= 12):
        context["games"].append({
            "game_id":i,  
            "name":data.iloc[i]["Game name"],
            "year":data.iloc[i]["Release Year"],
            "image":data.iloc[i]["Image"],
            "metacritic":data.iloc[i]["Metacritic score"],
         }) 
    return render (request, 'html/index.html', context=context)
def excel_page(request):
    if request.method == "POST":
        print (request.POST)
        if request.POST.get('add a row') is not None:
            new_game = Games(id = request.POST.get('id'),
                        game_name = request.POST.get('name'),
                        release_year = request.POST.get('release'), 
                        metacritic_score = request.POST.get('score'),
                        developers = request.POST.get('devs'),
                        howlongtobeat = request.POST.get('howlong'),
                        image = request.POST.get('img'))
            print(request.POST.get('add a row'))
            new_game.save()
        if request.POST.get('delete') is not None:
            game = Games.objects.all().filter(id = request.POST.get('delete'))
            game.delete()
        if request.POST.get('change') is not None:
            print('1')
            game = Games.objects.get(id = int(request.POST.get('choose_id')))
            if request.POST.get('change_game_name'):
                game.game_name = request.POST.get('change_game_name')
            if request.POST.get('change_release'):
                game.release_year = request.POST.get('change_release')
            if request.POST.get('change_meta'):
                game.metacritic_score = request.POST.get('change_meta')
            if request.POST.get('change_devs'):    
                game.developers = request.POST.get('change_devs')
            game.save()

    context = {
        'games': Games.objects.all()
        }
    #print(Games.objects.all())
    return render(request, 'html/excel.html', context = context)
def page(request):
    num_visits = request.session.get('num_visits', 0)
    print(num_visits)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'html/counter.html')
def registration_page(request):
    if request.POST.get('logout'):
        del request.session['name']
        return render(request, 'html/registration.html')
    if request.session.get('name'):
        return redirect("/gamelands/")
    user = User.Email
    print(*User.objects.all())
    print(f" email: {request.POST.get('email')}") 
    print(f"username: {request.POST.get('nick')}")
    if  User.objects.all().filter(Email = request.POST.get('email')):
        return render(request, 'html/registration.html')
    if User.objects.all().filter(username = request.POST.get('nick')):
        return render(request, 'html/registration.html')
    if request.POST.get('submit'):
        return render(request, 'html/registration.html')    
    else:
        return render(request, 'html/registration.html')
def login_page(request):
    return render(request, 'html/login.html')
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
    for value in Games.objects.values("developers"):
        all_devs_arr.append(value["developers"])
    all_devs_arr = ", ".join(all_devs_arr)
    all_devs_arr  = all_devs_arr.split(", ")
    all_devs_arr = list(set(all_devs_arr))
    #print(request.POST.keys())
    #print(all_devs_arr)
    dev_filter = []
    for keys in request.POST.keys():
        if keys.startswith("checkbox"):
            dev_filter.append(keys[9:])
    
    filtered = Games.objects.filter(release_year__range = (from_year, to_year))
    filtered = filtered.filter(game_name__icontains = search_auto)
    if len(dev_filter) >= 1:
        filtered = filtered.filter(reduce(operator.or_,(Q(developers__icontains = x) for x in dev_filter)))
    filtered = filtered.order_by(variable)
    # filters_dict = {"release_year__range" : (from_year, to_year), "game_name__icontains" : search_auto,}
    # if len(dev_filter) >= 1:
    #     filters_dict.update({"developers__icontains" : (reduce(operator.or_,(Q(developers__icontains = x) for x in dev_filter)))})
    # print(filters_dict)
    # print(*filters_dict)
    # ###filtered = Games.objects.filter(**filters_dict).order_by(variable)
    # #filtered = Games.objects.filter(reduce(operator.or_,(Q(developers__icontains = x) for x in dev_filter))).order_by(variable)
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
def return_cabinet(request):
    if request.method == "POST":
        name = request.POST.get('nick')
        birthyear = request.POST.get('birthyear')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(name)
        request.session['name'] = name
        request.session['birthyear'] = birthyear
        request.session['email'] = email
        request.session['password'] = password
    return render(request, 'html/cabinet.html')
def return_mgs(request):
    if request.method == "POST":
        user = Table (name = request.POST.get('name'), username = request.POST.get('username'))
        user.save()
    print(Table.objects.all())
    context = {
        'key' : Table.objects.all()
    }
    return render(request, 'html/mgs.html', context=context)
def games_table(request):
    print (Games.objects.all())
    context = { 
        'games' : Games.objects.all() 
    }
    return render(request, 'html/mgs.html', context = context)
def return_base_game_page(request):
    return render(request, 'html/base_game.html')
def get_base_page(request):
    user = User(username = "user", Email = "user@gmail.com" )
    user.save()
    return render(request, 'html/base.html')
def get_title_page(request, game_id):
    url = static("content/database.xlsx")
    base_path = str(os.path.join (settings.BASE_DIR))
    print(base_path)
    data = pandas.read_excel(base_path + url)
    number_of_rows = (data[data.columns[0]].count())
    if game_id >= number_of_rows:
         return render(request, "html/mgs.html")
    context = {
        "name":data.iloc[game_id]["Game name"],
        "year":data.iloc[game_id]["Release Year"],
        "image":data.iloc[game_id]["Image"],
        "developers":data.iloc[game_id]["Developers"],
        "howlongtobeat":data.iloc[game_id]["HowLongToBeat"],
        "metacritic":data.iloc[game_id]["Metacritic score"],
    }
    return render(request,"html/base_game.html", context=context)

# Create your views here.
