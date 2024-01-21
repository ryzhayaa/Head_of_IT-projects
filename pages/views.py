from django.shortcuts import render

from django.conf import settings
BASE_DIR = settings.BASE_DIR

# Create your views here.

def first_view(request):
    return render(
        request,
        'pages/index.html'

    )

def second_view(request):
    return render(
        request,
        'pages/demand.html'

    )

import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
import pandas as pd

def demand(request):

# Загрузка данных
    data = pd.read_csv('vacancies.csv')

# Преобразование даты публикации в формат datetime
    data['published_at'] = pd.to_datetime(data['published_at'])

# Добавление столбца с годом публикации
    data['year'] = data['published_at'].dt.year

# Фильтрация данных по зарплате и профессии
    filtered_data = data[(data['salary_to'] <= 10000000) & (data['name'].str.contains('team lead|тимлид|тим лид|teamlead|lead|руководит|директор|leader|director|начальник|лидер|управляющий проект|керівник|chief|начальник it', case=False))]

# Группировка данных по году и расчет средней зарплаты
    average_salary_by_year = filtered_data.groupby('year')['salary_to'].mean()

    context = {
        'average_salary_by_year_all': average_salary_by_year_all.to_dict(),
        'job_count_by_year_all': job_count_by_year_all.to_dict(),
        'average_salary_by_year_profession': average_salary_by_year_profession.to_dict(),
        'job_count_by_year_profession': job_count_by_year_profession.to_dict(),
    }

    # Отправка данных на веб-страницу
    return render(request, 'your_template.html', context)





