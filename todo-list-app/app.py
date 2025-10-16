from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from JSON file"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

@app.route('/')
def index():
    """Display the main page with all tasks"""
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task"""
    task_text = request.form.get('task')
    if task_text and task_text.strip():
        tasks = load_tasks()
        # Create new task with unique ID
        task_id = max([task['id'] for task in tasks], default=0) + 1
        new_task = {
            'id': task_id,
            'text': task_text.strip(),
            'completed': False
        }
        tasks.append(new_task)
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """Delete a task by ID"""
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    """Toggle task completion status"""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear_completed():
    """Clear all completed tasks"""
    tasks = load_tasks()
    tasks = [task for task in tasks if not task['completed']]
    save_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
