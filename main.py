
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule():
    tasks = request.form.getlist('tasks')
    time_slots = request.form.getlist('time_slots')
    return render_template('planner.html', tasks=tasks, time_slots=time_slots)

if __name__ == '__main__':
    app.run(debug=True)
