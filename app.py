from calendar import monthrange
from datetime import datetime, timedelta
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    calendar = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    start_date = "19/06/2020"
    start_datetime = datetime.strptime(start_date, "%d/%m/%Y")
    today_datetime = datetime.today()
    next_free_date = start_datetime + timedelta(5)

    next_free_dates = {}
    while today_datetime.month >= next_free_date.month:
        if today_datetime.month == next_free_date.month:
            next_free_dates[next_free_date.day] = next_free_date.day
        next_free_date = next_free_date + timedelta(5)

    # check 31 days
    # Get current month and compare with next_free month
    #           if next-free is greather check if current month has 31 days
    #                next_free_date + 1

    print(next_free_dates)
    return render_template('index.html',
                           month=calendar.get(today_datetime.month),
                           year=today_datetime.year,
                           days=monthrange(today_datetime.year, today_datetime.month)[1],
                           weekday=today_datetime.weekday(),
                           free_days=next_free_dates,
                           next_free_date=f'{next_free_date: %d-%m}')
