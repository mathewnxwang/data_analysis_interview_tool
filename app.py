import pandas as pd
from flask import Flask, request, render_template, session

from code_executor import CodeExecutor
from data_generation_service import GenerationService

app = Flask(__name__)
app.secret_key = '1234'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    company = request.form['company']
    description = request.form['description']

    generation_service = GenerationService()
    dataset: pd.DataFrame = generation_service.generate_interview_data(company, description)
    questions: list[str] = generation_service.generate_interview_questions(dataset)

    session['company'] = company
    session['description'] = description
    session['dataset'] = dataset
    session['questions'] = questions

    return render_template(
        'index.html',
        company=company,
        description=description,
        questions=questions
    )

@app.route('/submit_code', methods=['POST'])
def submit_code():
    code = request.form['input_code']
    code_executor = CodeExecutor()
    execution_result = code_executor.execute_code(session['dataset'], code)

    return render_template(
        'index.html',
        company = session.get('company'),
        description = session.get('description'),
        questions = session.get('questions'),
        execution_result = execution_result
    )

if __name__ == '__main__':
    app.run(debug=True)