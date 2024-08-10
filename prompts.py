SYSTEM_TEMPLATE = """You are a senior staff data analyst at a world class tech company.
You are designing a data analysis interview for hiring candidates."""

DATA_GENERATION_USER_TEMPLATE = """Create a dataset for a data analysis interview that contains interesting insights.
Specifically, generate comma delimited csv output with the following characteristics:
- Relevant to company: {company}
- Dataset description: {description}
- Number of rows: 100
- Number of columns: 5

Only include csv data in your response. Do not include any other information.
Start your output with the first header of the csv: "id,".

Output: """

QUESTION_GENERATION_USER_TEMPLATE = """Generate 3 data analysis interview questions that can be solved with Python pandas code based on the dataset below:

Dataset:
{dataset}

Output the questions in a Python list where each element is a question. Start your output with [".
Do not include question indexes like "1." in your output.
Output: 
"""

ANSWER_GENERATION_USER_TEMPLATE = """Generate answers to the following data analysis interview Questions based on the Dataset.
Each answer should be executable Pandas Python code that starts with "df", where df refers to the Dataset.

Dataset:
{dataset}

Questions:
1. {question_1}
2. {question_2}
3. {question_3}

Output the answers in a Python list where each element is an answer. Start your output with [".
Output: 
"""