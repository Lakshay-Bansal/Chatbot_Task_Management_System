from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

def get_current_week():
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week, end_of_week

@app.route('/')
def index():
    start_of_week, end_of_week = get_current_week()

    # Example meetings data (replace with your own data)
    meetings = [
        {'day': 'Monday', 'date': start_of_week.strftime('%Y-%m-%d'), 'time': '10:00 AM'},
        {'day': 'Wednesday', 'date': (start_of_week + timedelta(days=2)).strftime('%Y-%m-%d'), 'time': '02:30 PM'},
        # Add more meetings as needed
    ]

    return render_template('index.html', start_of_week=start_of_week, end_of_week=end_of_week, meetings=meetings)

if __name__ == '__main__':
    app.run(debug=True)