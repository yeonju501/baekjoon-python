from django.shortcuts import render
import requests
import random
# Create your views here.

def dinner(request, menu, people):
    context = {
        'menu' : menu,
        'people' : people,
    }
    return render(request, 'pages/dinner.html', context)

def lotto(request):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=978'

    response = requests.get(url)
    lotto = response.json()

    winner = []
    bonus = lotto['bnusNo']
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])

    win_rate = {'1등': 0, '2등': 0, '3등': 0, '4등' : 0, '5등' : 0, '꽝' : 0}

    posts = ['2', '3', '4']
    for i in range(1000):
        my_numbers = random.sample(range(1, 46), 6)
        matched = 0
        for num in my_numbers:
            if num in winner:
                matched += 1
        
        if matched == 6:
            win_rate['1등'] += 1
        elif matched == 5 and bonus in my_numbers:
            win_rate['2등'] += 1
        elif matched == 5:
            win_rate['3등'] += 1
        elif matched == 4:
            win_rate['4등'] += 1
        elif matched == 3:
            win_rate['5등'] += 1
        else:
            win_rate['꽝'] += 1
    
    context = {
        'winner' : winner,
        'bonus' : bonus,
        'win_rate' : win_rate,
        'posts' : posts,
    }


    
    return render(request, 'pages/lotto.html', context)