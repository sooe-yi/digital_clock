from flask import Flask
from flask import render_template

from time_controller import show_time


app = Flask(__name__)


@app.route('/')
def display():
    time = show_time()
    print(time)
    return render_template('clock.html', time=time)


def main():
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()
