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
Output: """

ANSWER_GENERATION_USER_TEMPLATE = """Generate an answer to the following data analysis interview Question based on the Dataset.

Dataset:
{dataset}

Question: {question}

The answer should be executable Pandas Python code where df refers to the Dataset above.
Always start your answer with a comment explaining what the following code does.
DO NOT DEFINE df IN YOUR RESPONSE.
Answer: """