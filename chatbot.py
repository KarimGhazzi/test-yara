import openai
import os

def get_response(prompt):
    # Fetch the API key and strip out any trailing whitespace or newlines
    api_key = os.getenv("SECRET_API_KEY").strip()

    if not api_key:
        raise ValueError("No API key provided. Please set the SECRET_API_KEY environment variable.")

    # Set the API key for the OpenAI library
    openai.api_key = api_key

    initial_messages = [
        {"role": "system", "content": "You are a helpful shopping assistant. I am a customer looking for a product. I need help finding the best product for my needs. Look up the product on Amazon and provide me with the details."},
        {"role": "user", "content": prompt}
    ]

    # Make the API call to OpenAI's ChatCompletion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=initial_messages,
    )
    return response['choices'][0]['message']['content']
