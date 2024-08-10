from ast import literal_eval
from io import StringIO
import pandas as pd

from object_resource import InterviewQuestions, InterviewAnswers, AppInterviewData
from prompts import (
    SYSTEM_TEMPLATE,
    DATA_GENERATION_USER_TEMPLATE,
    QUESTION_GENERATION_USER_TEMPLATE,
    ANSWER_GENERATION_USER_TEMPLATE
)
from llm_manager import LLMManager
from mock_data import MOCK_DATASET

class DataGenerator():

    def __init__(self):
        self.llm_manager = LLMManager()

    def generate_interview_app_data(self, company: str, description: str, mock_data: bool) -> AppInterviewData:
        dataset_context: str = self.generate_interview_dataset(
            company=company, description=description, mock_data=mock_data
        )
        questions: InterviewQuestions = self.generate_interview_questions(dataset_context)
        dataset_df: pd.DataFrame = self.convert_str_to_df(dataset_context)

        return AppInterviewData(
            dataset_context=dataset_context,
            questions=questions,
            dataset_df=dataset_df
        )

    def generate_interview_dataset(self, company: str, description: str, mock_data: bool) -> str:
        if not mock_data:
            data_generation_user_prompt = DATA_GENERATION_USER_TEMPLATE.format(company=company, description=description)
            dataset = self.llm_manager.call_llm(
                system_prompt=SYSTEM_TEMPLATE,
                user_prompt=data_generation_user_prompt,
                temperature=0
            )

            dataset = self.clean_llm_dataset_output(dataset)
            return dataset
        
        return MOCK_DATASET
    
    def clean_llm_dataset_output(self, dataset: str) -> str:
        cleaned_dataset = dataset[dataset.index("id,"):]
        return cleaned_dataset

    def convert_str_to_df(self, dataset: str) -> pd.DataFrame:
        csv_data = StringIO(dataset)

        try:
            df = pd.read_csv(csv_data)
        except Exception as e:
            raise ValueError(f"Error in converting LLM csv output to DataFrame: {e}")

        return df

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
    
    def generate_interview_answers(self, dataset: str, questions: InterviewQuestions) -> InterviewAnswers:
        answer_generation_user_prompt = ANSWER_GENERATION_USER_TEMPLATE.format(
            dataset=dataset,
            question_1=questions.question_1,
            question_2=questions.question_2,
            question_3=questions.question_3
        )
        answers = self.llm_manager.call_llm(
            system_prompt=SYSTEM_TEMPLATE,
            user_prompt=answer_generation_user_prompt,
            temperature=0
        )

        try:
            answers_list = literal_eval(answers)
        except Exception as e:
            raise ValueError(f"Error in converting LLM answers output to list: {e}")
        
        answers_structured = InterviewAnswers(
            answer_1=answers_list[0],
            answer_2=answers_list[1],
            answer_3=answers_list[2]
        )

        return answers_structured
