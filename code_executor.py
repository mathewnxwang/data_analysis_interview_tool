import pandas as pd

class CodeExecutor():
    
    def execute_code(self, df: pd.DataFrame, input_code: str):

        print(f"type of df variable: {type(df)}")

        local_vars = {'df': df}
        code_prefix = """import pandas as pd\nresult = """
        try:
            exec(code_prefix + input_code, {}, local_vars)
        except Exception as e:
            return f"Error in code execution: {e}\nCompiled code: {code_prefix + input_code}"
        
        execution_result = local_vars.get('result', None)
        print(f"execution_result variable: {execution_result}")
        print(f"execution_result variable type: {type(execution_result)}")

        if isinstance(execution_result, pd.DataFrame):
            return execution_result.to_html()

        return execution_result
    
    @staticmethod
    def test_if_code_is_executable(df: pd.DataFrame, input_code: str):
        local_vars = {'df': df}
        code_prefix = "import pandas as pd\n"
        try:
            print(f"Tested execution code: {code_prefix + input_code}")
            exec(code_prefix + input_code, {}, local_vars)
        except Exception as e:
            raise ValueError(f"Error in code execution: {e}\nCompiled code: {code_prefix + input_code}")
        print("Code is executable")