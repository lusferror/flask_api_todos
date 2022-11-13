from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

todos = [{"label":"my first task", "done":False},
        
]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body= request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify((todos))

# @app.route('/todos', methods=['GET'])
# def hello_world():
#     json_text = jsonify(todos)
#     return json_text

if __name__=='__main__':
    app.run(host='0.0.0.0', port=3245, debug =True)