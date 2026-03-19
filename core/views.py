from django.shortcuts import render

def home(request): return render(request, 'core/home.html')
def about(request): return render(request, 'core/about.html')
def gallery(request): return render(request, 'core/gallery.html')
def contacts(request): return render(request, 'core/contacts.html')

def education(request):
    # ТЗ: Данные получать из словарей, которые внедрены в исходный код
    context = {
        'me': {
            'name': 'Иванов Иван Иванович', 'email': 'ivan@student.ru', 
            'phone': '+7 (999) 000-11-22', 'photo': 'assets/images/me.jpg'
        },
        'program': {
            'title': 'Веб-разработка и программная инженерия',
            'desc': 'Программа подготовки специалистов по современным веб-технологиям и проектированию архитектуры.',
            'director': {'name': 'Петров П.П.', 'email': 'petrov@university.ru', 'photo': 'assets/images/dir.jpg'},
            'manager': {'name': 'Сидорова С.С.', 'email': 'sidorova@university.ru', 'photo': 'assets/images/man.jpg'}
        },
        'classmates': [
            {'name': 'Смирнов Алексей', 'email': 'alex@student.ru', 'phone': '+7 (900) 111-22-33', 'photo': 'assets/images/c1.jpg'},
            {'name': 'Кузнецова Мария', 'email': 'maria@student.ru', 'phone': '+7 (900) 444-55-66', 'photo': 'assets/images/c2.jpg'}
        ]
    }
    return render(request, 'core/education.html', context)

def task_1018(request):
    res = None
    if request.method == 'POST':
        y = int(request.POST.get('year', 0))
        res = {'y': y, 'leap': "Да" if (y%400==0) or (y%4==0 and y%100!=0) else "Нет", 'c': (y-1)//100+1}
    return render(request, 'core/task_1018.html', {'result': res})
