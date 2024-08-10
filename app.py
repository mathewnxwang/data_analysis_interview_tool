import pandas as pd
from flask import Flask, request, render_template, session

from code_executor import CodeExecutor
from data_generator import DataGenerator
from object_resource import AppInterviewData

app = Flask(__name__)
app.secret_key = '1234'

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/greet', methods=['POST'])
def greet():
    company = request.form['company']
    description = request.form['description']

    data_generator = DataGenerator()
    interview_data: AppInterviewData = data_generator.generate_interview_app_data(
        company=company, description=description, mock_data=True
    )

    session['company'] = company
    session['description'] = description
    session['df'] = interview_data.dataset_df.to_json()
    session['question_1'] = interview_data.questions.question_1
    session['question_2'] = interview_data.questions.question_2
    session['question_3'] = interview_data.questions.question_3
    session['answer_1'] = interview_data.answers.answer_1
    session['answer_2'] = interview_data.answers.answer_2
    session['answer_3'] = interview_data.answers.answer_3

    return render_template(
        'base.html',
        company=company,
        description=description,
        question_1=interview_data.questions.question_1,
        question_2=interview_data.questions.question_2,
        question_3=interview_data.questions.question_3,
        answer_1=interview_data.answers.answer_1,
        answer_2=interview_data.answers.answer_2,
        answer_3=interview_data.answers.answer_3
    )

@app.route('/submit_code', methods=['POST'])
def submit_code():
    code = request.form['input_code']
    code_executor = CodeExecutor()
    execution_result = code_executor.execute_code(
        df=pd.read_json(session['df']), input_code=code
    )

    return render_template(
        'base.html',
        company = session.get('company'),
        description = session.get('description'),
        question_1=session.get('question_1'),
        question_2=session.get('question_2'),
        question_3=session.get('question_3'),
        answer_1=session.get('answer_1'),
        answer_2=session.get('answer_2'),
        answer_3=session.get('answer_3'),
        input_code=code,
        execution_result = execution_result
    )

if __name__ == '__main__':
    app.run(debug=True)