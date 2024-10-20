# 🤖 **Rasa-ChatBot**  
## 📚 **Negotiation Chatbot**  

<p align="center">
  <img src="https://github.com/user-attachments/assets/31d58b18-c1ca-4888-ae6f-56a33b36fcdf" alt="Rasa Logo" width="350"/>
</p>  

---

## 📝 **Overview**  
This negotiation chatbot simulates a **price negotiation process** between a customer and a supplier using a pre-trained AI model. It manages user offers, provides dynamic responses, and guides conversations through realistic negotiation scenarios.

---

## ✨ **Key Features**  
1. **Basic Conversation Flow**:  
   - Starts by asking if the user is interested in buying a book.
   - Users can **negotiate prices** with the bot, proposing their desired offers.  

2. **Pricing Logic**:  
   - **Standard price**: 500 rupees.  
   - Offers below 500 rupees are **rejected** with an explanation about costs.
   - Offers at or above 500 rupees are **accepted**, prompting payment.

3. **API-Integrated Responses**:  
   - Uses an **AI model** to generate personalized, context-aware responses.  
   - Ensures seamless **negotiation logic** and error-free processing.  

---

## 📂 **Directory Structure**  
D:/Rasa-ChatBot/
│
├── domain.yml         # Defines intents, entities, and responses
├── actions/           # Contains custom action implementations
├── models/            # Trained Rasa models stored here
├── config.yml         # Configuration for Rasa pipelines and policies
└── credentials.yml    # API keys and endpoint configurations

---

## 🚀 **Run the Application**  

1. **Prerequisites**  
   - Install [Python](https://www.python.org/downloads/).  
   - Install Rasa and SDK dependencies:  
     ```bash
     pip install rasa rasa-sdk
     ```

2. **Train the Model**  
   - Navigate to the project directory and run:  
     ```bash
     cd D:/Rasa-ChatBot/
     rasa train
     ```

3. **Run the Actions Server**  
   - Start the server to handle custom actions:  
     ```bash
     rasa run actions
     ```

4. **Launch the Chatbot**  
   - Start the chatbot shell:  
     ```bash
     rasa shell
     ```

---

## 💬 **Example Interaction**  
Here's an example of how a conversation with the chatbot might go:

> **User**: "Hello"  
> **Bot**: "Hello! Are you looking to buy a book or just browsing?"  
> **User**: "I want to buy a book."  
> **Bot**: "The standard price for the book is 500 rupees. What would you like to offer?"  
> **User**: "I would like to offer 250 rupees."  
> **Bot**: "Our manufacturing cost is more than the quoted amount. We can't sell our product for less than our profit margin."  
> **User**: "Okay, then I will offer 550 rupees."  
> **Bot**: "Your offer of 550 has been accepted. Shall we proceed with the payment and address details?"  
> **User**: "Let's proceed."  
> **Bot**: "Great! Your order is being processed. Have a wonderful day!"


---

## 🛠️ **Key Functions**  
- **`ActionHandleOffer`**:  
  Handles negotiation logic by evaluating user offers against the standard price.  
- **`utter_message`**:  
  Sends appropriate responses back to the user based on negotiation status.  
- **API Calls**:  
  Integrate the AI model via API to process user input effectively.

---

## 🌐 **Live Demo**  
👉 [Project Matthew](https://projectmatthew-hemanthallugunti.streamlit.app)  

---

## 🤝 **Contributing**  
We appreciate your interest!  
Feel free to **fork** the repository and create a **pull request** to suggest improvements or report issues.

---

## 📄 **License**  
This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for more details.

---

## 📧 **Contact**  
For any inquiries, feel free to reach out via:  
- **Email**: yourname@example.com  
- **LinkedIn**: [Your Profile](https://www.linkedin.com/in/your-profile)

---

## 🎨 **Aesthetic Color Palette**  
- **Background**: #F0F4F8  
- **Primary Accent**: #4A90E2  
- **Secondary Accent**: #50E3C2  
- **Text**: #4A4A4A  

---

Enjoy chatting with the **Rasa-ChatBot**! 😊

