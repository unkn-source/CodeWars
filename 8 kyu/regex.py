import re

def validate_code(code):
    code_str = str(code)

    pattern = r'^[123]'

    return bool(re.match(pattern, code_str))