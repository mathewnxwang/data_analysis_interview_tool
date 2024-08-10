import pandas as pd
from flask import Flask, request, render_template, session

from code_executor import CodeExecutor
from data_generator import DataGenerator
from data_generator_resource import InterviewQuestions

app = Flask(__name__)
app.secret_key = '1234'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    company = request.form['company']
    description = request.form['description']

    data_generator = DataGenerator()
    dataset_context: str = data_generator.generate_interview_data(
        company=company, description=description, mock_data=True
    )
    questions: InterviewQuestions = data_generator.generate_interview_questions(dataset_context)
    dataset_df: pd.DataFrame = data_generator.convert_str_to_df(dataset_context)

    session['company'] = company
    session['description'] = description
    session['df'] = dataset_df.to_json()
    session['question_1'] = questions.question_1
    session['question_2'] = questions.question_2
    session['question_3'] = questions.question_3

    return render_template(
        'index.html',
        company=company,
        description=description,
        question_1=questions.question_1,
        question_2=questions.question_2,
        question_3=questions.question_3
    )

@app.route('/submit_code', methods=['POST'])
def submit_code():
    code = request.form['input_code']
    code_executor = CodeExecutor()
    execution_result = code_executor.execute_code(
        df=pd.read_json(session['df']), input_code=code
    )

    return render_template(
        'index.html',
        company = session.get('company'),
        description = session.get('description'),
        question_1=session.get('question_1'),
        question_2=session.get('question_2'),
        question_3=session.get('question_3'),
        input_code=code,
        execution_result = execution_result
    )

if __name__ == '__main__':
    app.run(debug=True)