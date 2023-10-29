# Define the delimiter
delimiter = "####"

# Define the system message
system_message = f"""
You will be provided with a list of texts, each associated with a number. 
The customer service query will be delimited with \
{delimiter} characters.
Your task is to determine if each text/or any sentence in the text contains any form of discrimination related to religion, race, gender, or any other protected category. 
Please provide the output in JSON format with the keys as the input number and the value as a boolean indicating whether discrimination is found.
"""

# Define a sample input
sample_input = f"""
1. I don't want to hire anyone who is not a native English speaker.
2. We need a park for all residents of the neighborhood to enjoy.
"""
