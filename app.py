from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for todos
todos = []

@app.route('/')
def home():
    return jsonify({
        "message": "DevOps Flask To-Do API",
        "status": "healthy",
        "version": "1.0"
    })

@app.route('/health')
def health():
    return jsonify({"status": "UP"}), 200

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({"todos": todos, "count": len(todos)})

@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.get_json()
    if not todo or 'task' not in todo:
        return jsonify({"error": "Task is required"}), 400
    
    new_todo = {
        "id": len(todos) + 1,
        "task": todo['task'],
        "completed": False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({"message": "Todo deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
