from pydantic import BaseModel

class InterviewQuestions(BaseModel):
    question_1: str
    question_2: str
    question_3: str

class InterviewAnswers(BaseModel):
    answer_1: str
    answer_2: str
    answer_3: str