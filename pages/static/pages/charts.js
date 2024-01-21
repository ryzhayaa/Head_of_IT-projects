// Функция для построения графика
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: Object.keys(average_salary_by_year),
        datasets: [{
            label: 'Средняя зарплата',
            data: Object.values(average_salary_by_year),
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    }
});

// Получение данных из Django
var averageSalaryByYearAll = JSON.parse(document.getElementById('average-salary-by-year-all').textContent);
var jobCountByYearAll = JSON.parse(document.getElementById('job-count-by-year-all').textContent);
var averageSalaryByYearProfession = JSON.parse(document.getElementById('average-salary-by-year-profession').textContent);
var jobCountByYearProfession = JSON.parse(document.getElementById('job-count-by-year-profession').textContent);

// Построение графиков
buildChart(Object.keys(averageSalaryByYearAll), Object.values(averageSalaryByYearAll), 'Средняя зарплата по годам (все вакансии)');
buildChart(Object.keys(jobCountByYearAll), Object.values(jobCountByYearAll), 'Количество вакансий по годам (все вакансии)');
buildChart(Object.keys(averageSalaryByYearProfession), Object.values(averageSalaryByYearProfession), 'Средняя зарплата по годам (Руководитель ИТ-проектов)');
buildChart(Object.keys(jobCountByYearProfession), Object.values(jobCountByYearProfession), 'Количество вакансий по годам (Руководитель ИТ-проектов)');

console.log(averageSalaryByYearAll);
console.log(jobCountByYearAll);
console.log(averageSalaryByYearProfession);
console.log(jobCountByYearProfession);
