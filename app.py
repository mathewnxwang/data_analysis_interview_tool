import pandas as pd
from flask import Flask, request, render_template, session

from code_executor import CodeExecutor
from data_generator import DataGenerator
from object_resource import InterviewData, AppGreetData, AppSubmitCodeData

class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = '1234'
        self.setup_routes()

        self.data_generator = DataGenerator()
        self.code_executor = CodeExecutor()

        self.app_greet_data = None
        self.app_submit_code_data = None
        self.submit_state = {
            'config_submitted': False,
            'code_submitted': False
        }

    def setup_routes(self):

        @self.app.route('/')
        def home():
            return render_template('base.html')

        @self.app.route('/greet', methods=['POST'])
        def greet():
            company = request.form['company']
            description = request.form['description']

            interview_data: InterviewData = self.data_generator.generate_interview_app_data(
                company=company, description=description, mock_data=True
            )
            self.app_greet_data = AppGreetData(
                company=company,
                description=description,
                interview_data=interview_data
            )

            self.submit_state['config_submitted'] = True

            return render_template(
                'base.html',
                **self.app_greet_data.unpack_into_dict(),
                **self.submit_state
            )

        @self.app.route('/submit_code', methods=['POST'])
        def submit_code():
            code = request.form['input_code']
            execution_result = self.code_executor.execute_code(
                df=pd.read_json(session['df']), input_code=code
            )

            self.app_submit_code_data = AppSubmitCodeData(
                **self.app_greet_data.dict(),
                input_code=code,
                execution_result=execution_result
            )

            self.submit_state['code_submitted'] = True

            return render_template(
                'base.html',
                **self.app_submit_code_data.unpack_into_dict(),
                **self.submit_state
            )

if __name__ == '__main__':
    flask_app = FlaskApp()
    flask_app.app.run(debug=True)