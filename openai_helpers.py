import os
import openai
from dotenv import load_dotenv, find_dotenv

from prompt import system_message, delimiter

_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.environ["OPENAI_API_KEY"]


def get_completion_from_messages(
    user_messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500
):
    # Combine the system message and the sample input
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"{delimiter}{user_messages}{delimiter}"},
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]
