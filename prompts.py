DATA_GENERATION_SYSTEM_TEMPLATE = """You are a senior staff data analyst at a world class tech company.
You are tasked with designing a data analysis interview for hiring candidates."""

DATA_GENERATION_USER_TEMPLATE = """Generate comma delimited csv output with the following characteristics:
- Relevant to company: {company}
- Dataset description: {description}
- Number of rows: 100
- Number of columns: 5

Output:"""