from groq import Groq

import streamlit as st
import json
from openai import AzureOpenAI

# # Initialize the Azure OpenAI client
# client = AzureOpenAI(
#     azure_endpoint="https://wbmulticrew.openai.azure.com/",
#     api_key="c76325f5635a45e7adf492263bb15534",
#     api_version="2024-02-15-preview",
# )


client = Groq(
    api_key="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",
)  # Create a Groq client


# Function to generate a response from the chat history
def generate_response(chat_history):
    chat_completion = client.chat.completions.create(
        messages=chat_history,
        model="llama3-70b-8192",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )
    return chat_completion.choices[0].message.content


# Function to initialize chat history in session state
def init_chat_history():
    return [
        {
            "role": "system",
            "content": """
                # Senior Project Manager - Web Development Agency

                As the Senior Project Manager at AI Website Builder (a one stop website design and development agency), your role is to engage in detailed discussions with potential clients about their desired website. This conversation will form the basis for the design and development team's work, so it's crucial to gather as much information as possible.

                ## Your Responsibilities Include:

                1. **Understanding the Client's Vision:** Ask the user about the website they envision. This includes the website's purpose, target audience, and desired outcomes.
                
                2. **Design Preferences:** Talk about the client's design preferences. This could include color schemes, typography, imagery, and overall aesthetic.

                3. **Offering Suggestions:** Based on your expertise, offer the client options and suggestions, when they are not sure. This will help them understand what's possible and make informed decisions.
                
                Remember, this is a conversation, not an interrogation. Don't ask all questions at once. Instead, let the conversation flow naturally. Respond to the client's answers, ask follow-up questions, and provide information, and suggestions and advice when necessary. This will make the interaction more engaging and productive. Your job is to guide the client and ensure that their vision is translated into a website that meets their needs and exceeds their expectations.
                
                Start the conversation by asking the user about the name of the website or the business they want the website for.
                
                Then ask the user to give any information they have about the website, such as the purpose of the website, target audience, and any specific features they would like to include, any general info about the business that would help in making the website.
                Then analyse their response and ask any additional questions as needed to clarify the website requirements.
                
                Remember, AI website Builder only works with basic informative based websites, with high focus on design of the website. AI website builder cant handle complex websites like e-commerce, social media, etc. which require extensive backend development. 
                
                if at any point, the client asks for a feature that is not supported by AI website builder, you can inform them that it is not possible with AI website builder and suggest an alternative feature that is supported.
                
                once you feel all the information is gathered, say "Exit" to end the conversation. 
                You donot need to generate a summary, or tell the user that u are exiting the conversation, 
                once you are done asking questions, just return "EXIT" to end the conversation.
                Your final message should have no other text, only say "Exit" once you have gathered all the information.
                
                """,
        },
    ]


# Initialize session state for chat history if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = init_chat_history()


# Function to display the chat messages
def display_chat():
    for i, message in enumerate(st.session_state.chat_history):
        if message["role"] == "user":
            st.markdown(
                f"<div style='display: inline-block; float: right; text-align: right; color: white; background-color: blue; padding: 5px; margin: 5px; border-radius: 5px;'>{message['content']}</div>",
                unsafe_allow_html=True,
            )
        elif message["role"] == "assistant":
            st.markdown(
                f"<div style='display: inline-block; float: right;  text-align: left; color: black; background-color: lightgrey; padding:5px; margin: 5px; border-radius: 5px;'>{message['content']}</div>",
                unsafe_allow_html=True,
            )


# Title of the app
st.title("AI Website Builder Chatbot")

# Display chat history at the top
display_chat()

# Input field for user message and Send button at the bottom
user_input = st.text_input("Type your message here:", key="user_input")

# Send button or pressing Enter sends the message
if st.button("Send"):
    st.session_state.enter_pressed = False
    if user_input.strip():
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        response = generate_response(st.session_state.chat_history)

        if response.lower() == "exit":
            st.session_state.chat_history.append(
                {
                    "role": "assistant",
                    "content": "Thank you for your time! I have noted all the details, I'll get the team started on your website. Have a great day!\n\nYou will receive an email as soon as the website is ready for review.",
                }
            )
            # Save conversation to file
            filtered_chat_history = [
                msg for msg in st.session_state.chat_history if msg["role"] != "system"
            ]
            with open("conversation2.json", "w") as f:
                json.dump(filtered_chat_history, f)
        else:
            st.session_state.chat_history.append(
                {"role": "assistant", "content": response}
            )

        # Clear input field by re-rendering
        st.experimental_rerun()
