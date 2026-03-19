# 1. Создаем файлы-заглушки для новых тематических изображений
touch core/static/assets/images/drone.jpg
touch core/static/assets/images/railway.jpg
touch core/static/assets/images/cv_analysis.jpg

# 2. Обновляем home.html (Вводная страница с осмысленным текстом)
cat << 'EOF' > core/templates/core/home.html
{% extends 'core/base.html' %}
{% block content %}
<h1>Система мониторинга инфраструктуры</h1>
<p>Добро пожаловать в веб-панель управления комплексом инспекции железнодорожных путей. Наше решение объединяет использование беспилотных летательных аппаратов (БПЛА) и алгоритмов машинного зрения для оперативного выявления дефектов полотна.</p>
<br>
<a href="{% url 'about' %}" style="display: inline-block; padding: 10px 20px; background: var(--accent); color: white; text-decoration: none; border-radius: 8px; font-weight: bold;">Подробнее о технологиях</a>
{% endblock %}
EOF

# 3. Обновляем about.html (Все виды списков + изображение + текст)
cat << 'EOF' > core/templates/core/about.html
{% extends 'core/base.html' %}
{% load static %}
{% block content %}
<a id="top"></a>
<h1>О проекте инспекции путей</h1>

<div style="background: #e2e8f0; padding: 10px; border-radius: 8px; margin-bottom: 20px;">
    <strong>Навигация по странице:</strong>
    <a href="#section1">Цели и задачи</a> | 
    <a href="#section2">Технологии и процесс</a>
</div>

<h2 id="section1">Цели и задачи проекта</h2>
<figure style="float: right; width: 350px; margin-left: 20px; text-align: center; background: #fff; padding: 10px; border: 1px solid #cbd5e1; border-radius: 8px;">
    <div class="img-placeholder" style="height: 150px; background: #94a3b8; color: white;">[Фото: Дрон над путями]</div>
    <figcaption style="font-size: 0.85em; margin-top: 10px; color: #475569;">
        Рис 1. Промышленный БПЛА, подготовленный для облета заданного участка железной дороги.
    </figcaption>
</figure>

<p>Автоматизация процесса проверки железнодорожных путей — критически важная задача для обеспечения безопасности логистики. Использование дронов позволяет значительно оптимизировать процесс. Основные преимущества внедрения нашей системы:</p>

<ul>
    <li>Повышение безопасности персонала за счет снижения необходимости обхода путей пешком.</li>
    <li>Увеличение скорости мониторинга труднодоступных участков.</li>
    <li>Объективность данных за счет фиксации состояния полотна цифровыми сенсорами.</li>
</ul>

<h2 id="section2" style="clear: both; padding-top: 20px;">Технологии и регламент работы</h2>
<p>Программно-аппаратный комплекс работает как единое целое. Архитектура решения строго разделена на несколько уровней ответственности:</p>

<ul>
    <li><strong>Аппаратное обеспечение:</strong>
        <ul>
            <li>Мультироторные дроны с повышенной ветроустойчивостью.</li>
            <li>Оптические камеры высокого разрешения для детальной съемки шпал и креплений.</li>
        </ul>
    </li>
    <li><strong>Программная часть:</strong>
        <ul>
            <li>Модуль компьютерного зрения (CV) для обнаружения аномалий и трещин на снимках.</li>
            <li>Веб-интерфейс на базе фреймворка Django для визуализации и экспорта отчетов.</li>
        </ul>
    </li>
</ul>

<p>Процесс автоматизированной проверки железнодорожного полотна проходит по строгому регламенту, исключающему человеческий фактор на этапе сбора данных:</p>

<ol>
    <li>Загрузка геопространственного полетного задания в контроллер дрона.</li>
    <li>Автономный облет участка и серийная фотосъемка рельсов.</li>
    <li>Анализ полученного массива фотографий с помощью обученной нейросети.</li>
    <li>Генерация отчета и подсветка проблемных зон в текущей веб-панели для финальной проверки инженером.</li>
</ol>

<br>
<a href="#top" style="display: inline-block; padding: 10px; background: var(--primary); color: white; border-radius: 8px; text-decoration: none;">↑ К началу страницы</a>
{% endblock %}
EOF

# 4. Обновляем gallery.html (Несколько изображений с комментариями)
cat << 'EOF' > core/templates/core/gallery.html
{% extends 'core/base.html' %}
{% load static %}
{% block content %}
<h1>Объекты и результаты анализа</h1>
<p>В данном разделе представлены примеры входных данных и результаты работы алгоритмов машинного зрения.</p>

<div style="display: flex; flex-direction: column; gap: 30px; margin-top: 20px;">
    
    <figure class="card" style="margin: 0; display: flex; gap: 20px; align-items: center;">
        <div style="flex: 1;">
            <div class="img-placeholder" style="height: 200px; background: #64748b; color: white;">[Фото: Макро участок рельса]</div>
        </div>
        <figcaption style="flex: 1;">
            <h3 style="margin-top: 0; color: var(--primary);">Объект мониторинга</h3>
            <p>Стандартный участок железнодорожного полотна. Камера фиксирует болтовые соединения, подкладки и поверхность рельса. Высокая детализация (4K) критична для работы алгоритма, так как микротрещины могут быть не видны на снимках низкого разрешения.</p>
        </figcaption>
    </figure>

    <figure class="card" style="margin: 0; display: flex; gap: 20px; align-items: center;">
        <figcaption style="flex: 1; text-align: right;">
            <h3 style="margin-top: 0; color: var(--accent);">Анализ машинным зрением</h3>
            <p>Результат работы сверточной нейросети. Алгоритм обнаружил отсутствие крепежного элемента и выделил потенциальную аномалию красным маркером (bounding box). Изображение сопровождается координатами GPS для быстрой отправки ремонтной бригады.</p>
        </figcaption>
        <div style="flex: 1;">
            <div class="img-placeholder" style="height: 200px; background: #334155; color: #10b981; border: 2px solid #ef4444;">[Фото: Распознанный дефект]</div>
        </div>
    </figure>

</div>
{% endblock %}
EOF

echo "Контент страниц обновлен! Списки и изображения добавлены в смысловой текст."
