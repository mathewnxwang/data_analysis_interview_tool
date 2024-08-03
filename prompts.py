DATA_GENERATION_SYSTEM_TEMPLATE = """You are a senior staff data analyst at a world class tech company.
You are tasked with designing a data analysis interview for hiring candidates."""

DATA_GENERATION_USER_TEMPLATE = """Generate comma delimited csv output with the following characteristics:
- Relevant to company: {company}
- Dataset description: {description}
- Number of rows: 100
- Number of columns: 5

Only include csv data in your response. Do not include any other information.
I will start the csv with the first id field which you should build off of.

Output: id,"""