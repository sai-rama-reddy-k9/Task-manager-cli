# 🧰 Command Line Task Manager

A simple and lightweight **Command Line Task Manager** built using Python.  
This tool lets you add, update, delete, list, and manage tasks with statuses like `todo`, `in-progress`, and `done`.  
All tasks are stored locally in a `tasks.json` file.

👉 **Project Repository:** https://github.com/sai-rama-reddy-k9/Task-manager-cli

## 🔗 Project page URL
https://roadmap.sh/projects/task-tracker
---

## 🚀 Features

- Add new tasks  
- Update existing tasks  
- Delete tasks  
- Mark tasks as `in-progress` or `done`  
- List all tasks or filter by status  
- Persistent storage using JSON  

---

## 🛠️ Installation

```
git clone https://github.com/sai-rama-reddy-k9/Task-manager-cli
cd Task-manager-cli

```

Make sure you have **Python 3.13.1** installed.

---

## ▶️ Usage

```
task-cli [command] [arguments]
```

### Add a task
```
task-cli add "Buy groceries"
```

### Update a task
```
python task-cli.py update 1 "Buy vegetables and fruits"
```

### Delete a task
```
task-cli delete 1
```

### Mark a task as In-Progress
```
task-cli mark-in-progress 2
```

### Mark a task as Done
```
task-cli mark-done 2
```

### List all tasks
```
task-cli list
```

### List tasks by status
```
task-cli list todo
task-cli list in-progress
task-cli list done
```

---

## 📂 Data Storage

Tasks are stored in a local JSON file:

```
tasks.json
```

Do not delete this file unless you want to reset all tasks.

---

## 🤝 Contributions

Feel free to fork the repo and submit pull requests to improve the project.

---

## 📜 License

This project is released under the MIT License.

---

### ⭐ Don’t forget to star the repository if you find it useful!
