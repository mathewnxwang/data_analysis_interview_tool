from io import StringIO
import pandas as pd

from prompts import DATA_GENERATION_SYSTEM_TEMPLATE, DATA_GENERATION_USER_TEMPLATE
from llm_manager import LLMManager

class DataGenerationService():

    def __init__(self):
        self.llm_manager = LLMManager()

    def generate_interview_data(self, company: str, description: str) -> str:
        data_generation_user_prompt = DATA_GENERATION_USER_TEMPLATE.format(company=company, description=description)
        dataset = self.llm_manager.call_llm(
            system_prompt=DATA_GENERATION_SYSTEM_TEMPLATE,
            user_prompt=data_generation_user_prompt,
            temperature=0
        )
        return dataset
    
    def convert_str_to_df(self, dataset: str) -> pd.DataFrame:
        csv_data = StringIO()
        df = pd.read_csv(csv_data)
        return df

data_generation_service = DataGenerationService()
dataset = data_generation_service.generate_interview_data("Uber", "rides")
print(dataset)