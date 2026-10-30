from flask import Flask, render_template, request

app = Flask(__name__)

SCHEDULE = {
    'mon': {
        'name': 'Понедельник',
        'lessons': [
            {'time': '08:30 – 10:00', 'subject': 'Математика', 'room': '201'},
            {'time': '10:10 – 11:40', 'subject': 'Программирование', 'room': '208'},
            {'time': '12:10 – 13:40', 'subject': 'Английский язык', 'room': '207'},
        ]
    },
    'tue': {
        'name': 'Вторник',
        'lessons': [
            {'time': '08:30 – 10:00', 'subject': 'Физика', 'room': '201'},
            {'time': '10:10 – 11:40', 'subject': 'История', 'room': '302'},
        ]
    },
    'wed': {
        'name': 'Среда',
        'lessons': [
            {'time': '08:30 – 10:00', 'subject': 'Информатика', 'room': '212'},
            {'time': '10:10 – 11:40', 'subject': 'Русский язык', 'room': '201'},
            {'time': '14:00 – 15:30', 'subject': 'Философия', 'room': '208'},
        ]
    },
    'thu': {
        'name': 'Четверг',
        'lessons': [
            {'time': '08:30 – 10:00', 'subject': 'Программирование', 'room': '301'},
            {'time': '10:10 – 11:40', 'subject': 'Философия', 'room': '205'},
        ]
    },
    'fri': {
        'name': 'Пятница',
        'lessons': [
            {'time': '08:30 – 10:00', 'subject': 'Английский язык', 'room': '205'},
            {'time': '10:10 – 11:40', 'subject': 'Физкультура', 'room': 'Спортзал'},
        ]
    },
}

DAYS = [
    ('mon', 'Пн'),
    ('tue', 'Вт'),
    ('wed', 'Ср'),
    ('thu', 'Чт'),
    ('fri', 'Пт'),
]


@app.route('/')
def index():
    day = request.args.get('day', 'mon')
    if day not in SCHEDULE:
        day = 'mon'

    current_day = SCHEDULE[day]

    return render_template(
        'index.html',
        days=DAYS,
        current_day_code=day,
        day_name=current_day['name'],
        lessons=current_day['lessons']
    )


if __name__ == '__main__':
    app.run(debug=True)