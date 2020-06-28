from datetime import datetime, timedelta
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    start_date = "19/06/2020"
    start_datetime = datetime.strptime(start_date, "%d/%m/%Y")
    today_datetime = datetime.today()
    next_free_date = start_datetime + timedelta(5)
    while today_datetime > next_free_date:
        next_free_date = next_free_date + timedelta(5)

    return f'Hola Edivania, tu siguiente dia libre es : {next_free_date: %d-%m}'
