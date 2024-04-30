import openai

# Function to get response from OpenAI's GPT model
def get_response(prompt, api_key):
    openai.api_key = api_key
    initial_messages = [
        {"role": "system", "content": "You are a helpful shopping assistant. I am a customer looking for a product. I need help finding the best product for my needs. Look up the product on Amazon and provide me with the details."},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=initial_messages,
    )
    return response['choices'][0]['message']['content']

