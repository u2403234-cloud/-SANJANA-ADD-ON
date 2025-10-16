# 📝 To-Do List Web Application

A modern, responsive web-based To-Do List application built with Python Flask, HTML, and CSS. This application allows users to add, view, toggle completion status, and delete tasks with a clean and intuitive interface.

## 🌟 Features

- ✅ **Add Tasks**: Create new tasks with a simple form
- 📋 **View Tasks**: Display all tasks in an organized list
- ✓ **Toggle Completion**: Mark tasks as completed or incomplete
- 🗑️ **Delete Tasks**: Remove individual tasks
- 🧹 **Clear Completed**: Remove all completed tasks at once
- 📊 **Task Statistics**: View total, completed, and pending task counts
- 💾 **Persistent Storage**: Tasks are stored in a JSON file
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile devices
- 🎨 **Modern UI**: Beautiful gradient design with smooth animations

## 🛠️ Technologies Used

- **Backend**: Python 3.x with Flask framework
- **Frontend**: HTML5, CSS3
- **Data Storage**: JSON file-based storage
- **Platform**: Compatible with Linux, Windows, and macOS

## 📁 Project Structure

```
todo-list-app/
│
├── app.py                 # Flask application (backend logic)
├── templates/
│   └── index.html        # HTML template (frontend structure)
├── static/
│   └── style.css         # CSS styles (frontend design)
├── requirements.txt      # Python dependencies
├── tasks.json           # Task storage (created automatically)
└── README.md            # Project documentation
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd todo-list-app
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install Flask manually:

```bash
pip install Flask
```

### Step 3: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000` or `http://0.0.0.0:5000`

### Step 4: Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## 🐧 Hosting on Linux

### Method 1: Development Server

```bash
# Make sure Python and pip are installed
sudo apt-get update
sudo apt-get install python3 python3-pip

# Install Flask
pip3 install Flask

# Run the application
python3 app.py
```

### Method 2: Production Server (using Gunicorn)

```bash
# Install Gunicorn
pip3 install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Method 3: Run as a Service (systemd)

Create a systemd service file:

```bash
sudo nano /etc/systemd/system/todoapp.service
```

Add the following content:

```ini
[Unit]
Description=Todo List Flask App
After=network.target

[Service]
User=your-username
WorkingDirectory=/path/to/todo-list-app
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/python app.py

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl enable todoapp
sudo systemctl start todoapp
sudo systemctl status todoapp
```

## 💻 Usage

1. **Add a Task**: Type your task in the input field and click "Add Task" or press Enter
2. **Complete a Task**: Click the checkbox next to a task to mark it as complete
3. **Delete a Task**: Click the trash icon to remove a task
4. **Clear Completed**: Click "Clear Completed" to remove all finished tasks
5. **View Statistics**: See your total, completed, and pending task counts at the top

## 🎨 Features Overview

### Task Management
- Add new tasks with validation
- View all tasks in a clean list
- Toggle task completion status
- Delete individual tasks
- Clear all completed tasks

### User Interface
- Modern gradient header
- Responsive design for all devices
- Smooth animations and transitions
- Custom checkbox styling
- Empty state with helpful message
- Task statistics dashboard

### Data Persistence
- Tasks stored in `tasks.json` file
- Automatic file creation
- Unique task IDs
- JSON structure for easy data management

## 🔧 API Endpoints

- `GET /` - Display main page with all tasks
- `POST /add` - Add a new task
- `POST /delete/<task_id>` - Delete a specific task
- `POST /toggle/<task_id>` - Toggle task completion status
- `POST /clear` - Clear all completed tasks

## 📝 Task Data Structure

Each task is stored as a JSON object:

```json
{
  "id": 1,
  "text": "Sample task",
  "completed": false
}
```

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as a learning project to demonstrate Flask web development with HTML/CSS frontend.

## 🙏 Acknowledgments

- Flask documentation
- Modern CSS design patterns
- Responsive web design principles

---

**Happy Task Managing! 🎉**
