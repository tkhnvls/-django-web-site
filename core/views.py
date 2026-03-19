from django.shortcuts import render

def home(request): return render(request, 'core/home.html')
def about(request): return render(request, 'core/about.html')
def gallery(request): return render(request, 'core/gallery.html')
def contacts(request): return render(request, 'core/contacts.html')

def education(request):
    # ТЗ: Данные получать из словарей, которые внедрены в исходный код
    context = {
        'me': {
            'name': 'Тихонов Елизавета Витальевна', 'email': 'elvitikhonov@edu.hse.ru', 
            'phone': '+79632985909', 'photo': 'assets/images/me.jpg'
        },
        'program': {
            'title': 'Реклама и связи с общественностью',
            'desc': 'Программа готовит универсальных специалистов по коммуникациям за счёт интеграции дисциплин.',
            'director': {'name': 'Каткова С.В.', 'email': 'skatkova@hse.ru', 'photo': 'assets/images/dir.jpg'},
            'manager': {'name': 'Санакова Т.Ю.', 'email': 'tsanakova@hse.ru', 'photo': 'assets/images/man.jpg'}
        },
        'classmates': [
            {'name': 'Германова Мария', 'email': 'magermanova@edu.hse.ru', 'phone': '+7 (967) 471-49-69', 'photo': 'assets/images/c1.jpg'},
            {'name': 'Шаповалова Елизавета', 'email': 'ershapovalova@edu.hse.ru', 'phone': '+7 (926) 121-03-33', 'photo': 'assets/images/c2.jpg'}
        ]
    }
    return render(request, 'core/education.html', context)

def task_1018(request):
    res = None
    if request.method == 'POST':
        y = int(request.POST.get('year', 0))
        res = {'y': y, 'leap': "Да" if (y%400==0) or (y%4==0 and y%100!=0) else "Нет", 'c': (y-1)//100+1}
    return render(request, 'core/task_1018.html', {'result': res})
