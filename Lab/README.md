# Лаб. работа 1: 
Веб-приложение на **Flask**, которое возвращает количество дней до Нового года.  
# 1. Клонирование репозитория
```bash
git clone https://github.com/andreimamonov/lab1
cd <папка-проекта>
```

# 2. Сборка образа
```bash
docker build -t new-year-app .
```

# 3. Запуск контейнера
```bash
docker run -p 4200:4200 new-year-app
```

После запуска приложение будет доступно по адресу `http://localhost:4200/info`.

Пример ответа:
```JSON
{
  "days_before_new_year": 285
}
```