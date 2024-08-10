from pydantic import BaseModel

class InterviewQuestions(BaseModel):
    question_1: str
    question_2: str
    question_3: str