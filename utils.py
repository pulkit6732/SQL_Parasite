import re

def check_vulnerability(response):
    # Check for common SQL error messages
    sql_errors = [
        "mysql", "syntax", "error", "warning", "sql", "database", "table", "doesn't exist"
    ]
    return any(error in response.text.lower() for error in sql_errors)

def check_time_based(start_time, end_time, threshold=5):
    # Check if the response time exceeds the expected duration
    return (end_time - start_time) >= threshold

def extract_data(response):
    # Extract potential sensitive data from the response
    return re.findall(r'(\w+@\w+\.\w+)', response.text)