# Rasa-ChatBot
# Negotiation Chatbot

## Overview
This negotiation chatbot simulates a price negotiation process between a customer and a supplier using a pre-trained AI model. The chatbot is designed to handle user offers, respond appropriately, and guide the user through the negotiation flow.

## Key Features
1. **Basic Conversation Flow**:
   - The bot initiates a conversation, asking if the user is interested in purchasing a book.
   - Users can express their intent to buy, propose an offer, and negotiate prices.

2. **Pricing Logic**:
   - The bot uses a standard price of 500 rupees for the book.
   - Offers below the standard price are rejected with a message about manufacturing costs.
   - Offers equal to or above the standard price are accepted, with the option to proceed with the transaction.

3. **User Interaction**:
   - The chatbot allows users to input their desired price.
   - Based on the user’s offer, it provides tailored responses, simulating a realistic negotiation process.

4. **Model Integration**:
   - The chatbot leverages a pre-trained AI model (e.g., ChatGPT or Gemini) to handle conversational aspects.
   - Integration is done via API calls to the model, processing user inputs and generating responses.

## Integration Steps

### 1. Set Up the Environment
- Ensure you have Python installed along with necessary libraries such as `rasa` and `rasa-sdk`.
- Install any required dependencies for the chosen AI model.

### 2. Define Intents and Entities
- In `domain.yml`, define intents such as `greet`, `offer`, `confirm`, and entities like `amount` to capture user inputs.

### 3. Implement Actions
- Implement custom actions (e.g., `ActionHandleOffer`) that encapsulate the logic for handling offers and responses.
- Use the AI model to generate responses based on user input.

### 4. Model Integration
- Use the API of the selected AI model to handle user interactions, ensuring to handle API keys securely and include error handling for API requests.

### 5. Testing and Deployment
- Test the bot locally to ensure it handles negotiations as expected.
- Deploy the chatbot using a web server or cloud service as needed.

## Key Functions
- `ActionHandleOffer`: Manages the negotiation logic, evaluating user offers against the standard price and responding accordingly.
- `utter_message`: Sends messages back to the user based on their offers and negotiation status.
- API Calls: Ensure API calls to the AI model are correctly set up to process and respond to user queries effectively.

## Example Interaction
Here’s an example of how a conversation with the bot might go:

1. **User**: "Hello"
   - **Bot**: "Hello! Are you looking to buy a book or just browsing?"
   
2. **User**: "I want to buy a book."
   - **Bot**: "The standard price for the book is 500 rupees. What would you like to offer?"

3. **User**: "I would like to offer 250 rupees."
   - **Bot**: "Our manufacturing cost is more than the quoted amount. We can't sell our product for less than our profit margin."

4. **User**: "Okay, then I will offer 550 rupees."
   - **Bot**: "Your offer of 550 has been accepted. Shall we proceed further with the payment and address details?"

5. **User**: "Let's proceed."
   - **Bot**: "Goodbye! Have a great day!"

## License
This project is licensed under the Apache License 2.0. See the LICENSE file for details.

