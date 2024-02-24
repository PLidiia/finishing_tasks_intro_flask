from flask import Flask

app = Flask('__main__')


@app.route('/')
def main():
    return 'Миссия Колонизация Марса'


@app.route('/image_mars')
def do_image_mars():
    return '''<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Привет, Марс!</title>
</head>
<body>
<h1>Жди нас, Марс!</h1>
<figure><img src="static/img/Mars.png" alt="Фото Марса"> <figcaption>Вот она какая, красная планета</figcaption></figure>
</body>
    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
