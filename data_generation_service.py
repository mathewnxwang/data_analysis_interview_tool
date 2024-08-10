from ast import literal_eval
from io import StringIO
import pandas as pd

from data_generator_resource import InterviewQuestions
from prompts import (
    SYSTEM_TEMPLATE,
    DATA_GENERATION_USER_TEMPLATE,
    QUESTION_GENERATION_USER_TEMPLATE
)
from llm_manager import LLMManager
from mock_data import MOCK_DATASET

class GenerationService():

    def __init__(self):
        self.llm_manager = LLMManager()

    def generate_interview(self, company: str, description: str) -> pd.DataFrame:
        dataset = self.generate_interview_data(company, description)
        questions = self.generate_interview_questions(dataset)
        return questions

    def generate_interview_data(self, company: str, description: str, mock_data: bool) -> str:
        if not mock_data:
            data_generation_user_prompt = DATA_GENERATION_USER_TEMPLATE.format(company=company, description=description)
            dataset = self.llm_manager.call_llm(
                system_prompt=SYSTEM_TEMPLATE,
                user_prompt=data_generation_user_prompt,
                temperature=0
            )
            return dataset
        return MOCK_DATASET

    def generate_interview_questions(self, dataset: str) -> InterviewQuestions:
        
        question_generation_user_prompt = QUESTION_GENERATION_USER_TEMPLATE.format(dataset=dataset)
        questions = self.llm_manager.call_llm(
            system_prompt=SYSTEM_TEMPLATE,
            user_prompt=question_generation_user_prompt,
            temperature=0
        )
        
        try:
            questions_list = literal_eval(questions)
        except Exception as e:
            raise ValueError(f"Error in converting LLM questions output to list: {e}")
        
        questions_structured = InterviewQuestions(
            question_1=questions_list[0],
            question_2=questions_list[1],
            question_3=questions_list[2]
        )

        return questions_structured

    def convert_str_to_df(self, dataset: str) -> pd.DataFrame:
        csv_data = StringIO()
        df = pd.read_csv(csv_data)
        return df

# generation_service = GenerationService()
# dataset = generation_service.generate_interview_data("Uber", "rides")
# print(dataset)
# questions = generation_service.generate_interview_questions(dataset)
# print(questions)