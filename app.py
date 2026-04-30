from flask import Flask, render_template, request
from modules.file_organizer import organize_files
from modules.resume_builder import generate_resume_points
from modules.search_tool import search_files

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/organize', methods=['POST'])
def organize():
    data = request.get_json()
    organize_files(data['path'])
    return "✅ Files Organized!"

@app.route('/learning', methods=['POST'])
def learning():
    data = request.get_json()
    with open("data/learning_log.txt", "a") as f:
        f.write(data['entry'] + "\n")
    return "✅ Learning Saved!"

@app.route('/resume', methods=['POST'])
def resume():
    data = request.get_json()
    generate_resume_points(data['path'])
    return "✅ Resume Generated (check file)"

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    search_files(data['path'], data['keyword'])
    return "✅ Search completed (check terminal)"

@app.route('/add-task', methods=['POST'])
def task():
    data = request.get_json()
    with open("data/tasks.txt", "a") as f:
        f.write(data['task'] + "\n")
    return "✅ Task Added!"

@app.route('/show-task')
def show():
    with open("data/tasks.txt", "r") as f:
        return f.read()

if __name__ == '__main__':
    app.run(debug=True)