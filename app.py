from flask import Flask, request, render_template

# Создаем Flask приложение
app = Flask(__name__)

# Определяем маршрут для обработки запросов
@app.route('/')
def hello_recruto():
    # Получаем параметры из GET-запроса
    name = request.args.get('name', 'Recruto')  # Если параметр не передан, используем значение по умолчанию
    message = request.args.get('message', 'Давай дружить')
    
    # Формируем ответ
    return render_template('index.html', name=name, message=message)

# Запускаем сервер
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
