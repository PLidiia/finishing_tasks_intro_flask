from flask import Flask
from flask import url_for

app = Flask('__main__')


@app.route('/')
def main():
    return 'Миссия Колонизация Марсa'


@app.route('/image_mars')
def do_image_mars():
    return f'''<html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Привет, Марс!</title>
                </head>
                <body>
                <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}">
                <p>Вот она какая, красная планета!</p>
                </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
