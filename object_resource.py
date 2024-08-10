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

class AppInterviewData(BaseModel):
    dataset_context: str
    questions: InterviewQuestions
    dataset_df: DataFrame

    class Config:
        arbitrary_types_allowed = True

class GreetData(BaseModel):
    company: str
    description: str
    df: Dict[str, Any] #json
    question_1: str
    question_2: str
    question_3: str