import re

def extract_captcha_value(captcha: str) -> int:
    match = re.search(r'what is\s*([\d+\-*/\s]+)', captcha, re.IGNORECASE)
    if match:
        expression = match.group(1).strip()
        try:
            return eval(expression)  # Use with caution; only safe here due to controlled input
        except Exception as e:
            print("Evaluation error:", e)
    return None
