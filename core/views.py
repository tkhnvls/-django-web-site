from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def gallery(request):
    return render(request, 'core/gallery.html')

def contacts(request):
    return render(request, 'core/contacts.html')

def education(request):
    context = {
        'me': {
            'name': 'Тихонов Елизавета Витальевна',
            'email': 'elvitikhonov@edu.hse.ru',
            'phone': '+79632985909',
            'photo': 'assets/images/IMG_7597.jpg'
        },
        'program': {
            'title': 'Реклама и связи с общественностью',
            'desc': 'Программа готовит универсальных специалистов по коммуникациям за счёт интеграции дисциплин.',
            'director': {
                'name': 'Каткова С.В.',
                'email': 'skatkova@hse.ru',
                'photo': 'assets/images/IMG_4792.PNG'
            },
            'manager': {
                'name': 'Санакова Т.Ю.',
                'email': 'tsanakova@hse.ru',
                'photo': 'assets/images/IMG_4790.JPG'
            }
        },
        'classmates': [
            {
                'name': 'Германова Мария',
                'email': 'magermanova@edu.hse.ru',
                'phone': '+7 (967) 471-49-69',
                'photo': 'assets/images/IMG_4817.PNG'
            },
            {
                'name': 'Шаповалова Елизавета',
                'email': 'ershapovalova@edu.hse.ru',
                'phone': '+7 (926) 121-03-33',
                'photo': 'assets/images/IMG_4816.PNG'
            }
        ]
    }
    return render(request, 'core/education.html', context)

def task_1018(request):
    result = None
    shop_result = None

    if request.method == 'POST':

        # ЗАДАЧА 1018 
        if 'year' in request.POST:
            try:
                y = int(request.POST.get('year'))
                result = {
                    'y': y,
                    'leap': "Да" if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0) else "Нет",
                    'c': (y - 1) // 100 + 1
                }
            except:
                result = None

        # ЗАДАЧА 8
        if 'products' in request.POST:
            try:
                line = request.POST.get('products')
                budget = 500

                items = line.split(', ')
                available = []
                total_cost = 0 

                for item in items:
                    name, price = item.split(': ')
                    price = int(price)

                    if total_cost + price <= budget:
                        available.append(name)
                        total_cost += price 

                available.sort()
                shop_result = " ".join(available)

            except:
                shop_result = "Ошибка ввода"

    return render(request, 'core/task_1018.html', {
        'result': result,
        'shop_result': shop_result
    })
