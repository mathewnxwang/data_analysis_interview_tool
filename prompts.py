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
Output: "
"""

ANSWER_GENERATION_USER_TEMPLATE = """

"""