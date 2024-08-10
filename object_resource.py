from pandas import DataFrame
from pydantic import BaseModel
from typing import Dict, Any

class InterviewQuestions(BaseModel):
    question_1: str
    question_2: str
    question_3: str

class InterviewAnswers(BaseModel):
    answer_1: str
    answer_2: str
    answer_3: str

class InterviewData(BaseModel):
    dataset_context: str
    questions: InterviewQuestions
    answers: InterviewAnswers
    dataset_df: DataFrame

    class Config:
        arbitrary_types_allowed = True

class AppGreetData(BaseModel):
    company: str
    description: str
    interview_data: InterviewData

    def unpack_into_dict(self):
        return {
            'company': self.company,
            'description': self.description,
            'question_1': self.interview_data.questions.question_1,
            'question_2': self.interview_data.questions.question_2,
            'question_3': self.interview_data.questions.question_3,
            'answer_1': self.interview_data.answers.answer_1,
            'answer_2': self.interview_data.answers.answer_2,
            'answer_3': self.interview_data.answers.answer_3
        }

class AppSubmitCodeData(AppGreetData):
    input_code: str
    execution_result: Any

    def unpack_into_dict(self):
        return {
            'company': self.company,
            'description': self.description,
            'question_1': self.interview_data.questions.question_1,
            'question_2': self.interview_data.questions.question_2,
            'question_3': self.interview_data.questions.question_3,
            'answer_1': self.interview_data.answers.answer_1,
            'answer_2': self.interview_data.answers.answer_2,
            'answer_3': self.interview_data.answers.answer_3,
            'input_code': self.input_code,
            'execution_result': self.execution_result
        }