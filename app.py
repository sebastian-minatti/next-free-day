from datetime import datetime, timedelta
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    start_date = "19/06/2020"
    start_datetime = datetime.strptime(start_date, "%d/%m/%Y")
    today_datetime = datetime.today()
    next_free_date = start_datetime + timedelta(5)
    while today_datetime > next_free_date:
        next_free_date = next_free_date + timedelta(5)
    # check 31 days
    # Get current month and compare with next_free month
    #           if next-free is greather check if current month has 31 days
    #                next_free_date + 1

    return render_template('index.html', next_free_date=f'{next_free_date: %d-%m}')
