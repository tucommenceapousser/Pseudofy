from flask import Blueprint, render_template, request, jsonify
from app.marker import BlackBox

main = Blueprint('main', __name__)

@main.route('/', methods=['GET','POST'])
def Home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        question = request.json['question']
        language = request.json['language']
        status, response = BlackBox(question, language)
        return jsonify(
            {
                "status": status,
                "data": response,
            }
        )