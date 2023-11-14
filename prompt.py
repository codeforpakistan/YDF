# Define the delimiter for clarity in parsing text
delimiter = "####"

# Refine the system message for enhanced understanding and scope
system_message = f"""
You will be presented with several text snippets, each associated with a unique identifier. 
Each snippet, separated by {delimiter}, may contain statements or questions related to customer service interactions.
Your role is to analyze these texts to identify any expressions of discrimination or disharmony, including but not limited to biases based on race, religion, gender, ethnicity, or other protected categories. 
Output your analysis in JSON format, where each key corresponds to the identifier of a text snippet and the value is a boolean. This boolean should indicate the presence ('true') or absence ('false') of discriminatory content.
"""

# Define a more diverse and inclusive sample input for better testing
sample_input = f"""
1. I don't want to hire anyone who is not a native English speaker.
2. We need a park for all residents of the neighborhood to enjoy.
3. It's important that our team represents a variety of cultural backgrounds.
4. I prefer not to work with people from certain countries.
"""

# Define expected JSON output structure for clarity
expected_output_structure = """
{
    "1": true,  # Discrimination based on language/national origin
    "2": false, # Inclusive statement, no discrimination
    "3": false, # Encourages diversity, no discrimination
    "4": true   # Discrimination based on nationality
}
"""
