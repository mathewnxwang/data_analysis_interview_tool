import pandas as pd

class CodeExecutor():
    def execute_code(self, df: pd.DataFrame, code: str):
        local_vars = {'df': df}
        try:
            exec(code, {}, local_vars)
        except:
            return "Error in code execution"

        execution_result = local_vars.get('result', None)
        print(execution_result)
        return execution_result