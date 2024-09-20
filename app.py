from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq

# Load API key from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print(f"API Key Loaded: {GROQ_API_KEY}")

app = Flask(__name__)

# Set the price range for negotiation
MIN_PRICE = 80
MAX_PRICE = 100
current_offer = MAX_PRICE

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Function to send a message to Groq API and get a response
def get_ai_response(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "you are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            model="mixtral-8x7b-32768"
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Error with Groq API: {e}")
        return "Sorry, I couldn't process that."

# Negotiation logic
def negotiate(user_offer):
    if user_offer < MIN_PRICE:
        return f"I can't accept less than ${MIN_PRICE}. How about ${MIN_PRICE}?"
    elif MIN_PRICE <= user_offer <= MAX_PRICE:
        return f"Great! I can accept your offer of ${user_offer}."
    else:
        return f"Your offer is too high. Let's settle at ${current_offer}."

# API endpoint for negotiation
@app.route('/negotiate', methods=['POST'])
def negotiate_route():
    user_data = request.get_json()
    user_offer = user_data.get('offer')

    # Apply negotiation logic
    negotiation_response = negotiate(user_offer)

    # Get AI response from Groq API
    ai_response = get_ai_response(f"The customer offers ${user_offer}.")

    return jsonify({
        "negotiation": negotiation_response,
        "ai_response": ai_response
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
