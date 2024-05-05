import time
from openai import AzureOpenAI
import os
import time
from openai import AzureOpenAI


class ChatApp:
    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint="https://wbmulticrew.openai.azure.com/",
            api_key="c76325f5635a45e7adf492263bb15534",
            api_version="2024-02-15-preview",
        )
        self.messages = [
            {
                "role": "system",
                "content": """You are a seasoned senior web developer with over 10 years of experience, specializing in creating stunning, responsive, and user-friendly websites using HTML, CSS, and JavaScript. You have a deep understanding of modern web development principles, best practices, and the latest trends in web design.
                
                You will be provided with a detailed design brief, which includes a comprehensive description of the website or section layout, user interface, and functionality. Your task is to write clean, efficient, and well-structured HTML, CSS, and JavaScript code to bring this design to life.""",
            }
        ]

    def send_message(self, role, content):
        self.messages.append({"role": role, "content": content})
        start_time = time.time()
        completion = self.client.chat.completions.create(
            model="gpt4-wbmulticrew",  # model = "deployment_name"
            messages=self.messages,
            temperature=0.7,
            max_tokens=4000,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
        )
        end_time = time.time()
        print(completion)
        response_time = end_time - start_time
        tokens = completion.usage.total_tokens
        tokens_per_second = tokens / response_time
        print(f"Response time: {response_time} seconds")
        print(f"Tokens in response: {tokens}")
        print(f"Tokens per second: {tokens_per_second}")
        return completion.choices[0].message.content


app = ChatApp()
while True:
    # user_message = input("You: ")
    response = app.send_message(
        "user",
        """
**Concept:** "Aurora Bloom"

**Website Title:** "Unlock the Power of Innovation"

**Color Scheme:**

* Primary Color: #34A853 (A vibrant, energetic green)
* Secondary Color: #FFC107 (A warm, inviting orange)
* Accent Color: #8B9467 (A deep, rich brown)
* Background Gradient: A soft, gradient blend of #F7F7F7 (Light gray) to #E5E5E5 (Medium gray)

**Design:**

The design is divided into three main sections: Hero, Features, and Call-to-Action.

**Hero Section:**

* Background: A stunning, high-resolution image of a blooming flower (e.g., a cherry blossom) with a subtle, animated glow effect to represent innovation and growth.
* Headline: "Unlock the Power of Innovation" in a custom, bold, sans-serif font (e.g., Montserrat) with a dynamic, kinetic text effect that changes color and size as the user interacts with the page.
* Subheading: "Discover the latest advancements in technology and innovation" in a clean, modern sans-serif font (e.g., Open Sans) with a subtle, animated underline effect.

**Features Section:**

* A bento grid layout featuring four interactive cards, each representing a different aspect of innovation (e.g., AI, Robotics, Sustainability, and Cybersecurity).
* Each card has a unique, vibrant gradient background, and when hovered, the card expands to reveal a brief description and a "Learn More" button with a smooth, animated transition.
* The cards are arranged in a staggered, asymmetrical layout to create visual interest and encourage exploration.

**Call-to-Action Section:**

* A prominent, circular button with a bold, white font and a subtle, animated pulse effect, encouraging users to "Explore the Future of Innovation."
* The button is surrounded by a stylized, animated waveform that reacts to user interaction, creating a sense of energy and dynamism.

**Interactive Elements:**

* On page load, the hero image and headline are initially blurred, and as the user scrolls, they come into focus, creating a sense of discovery.
* The kinetic text effect in the headline responds to user interaction, changing color and size as the user hovers or clicks on the text.
* The interactive cards in the Features section have a subtle, animated "breathing" effect, giving the impression of life and energy.
* The waveform surrounding the Call-to-Action button reacts to user interaction, creating a sense of movement and dynamism.

**Motion Effects:**

* On page load, the entire design is initially darkened, and as the user scrolls, the sections fade in, creating a sense of progression and storytelling.
* The hero image has a subtle, animated parallax effect, giving the impression of depth and dimensionality.
* The interactive cards have a smooth, animated transition when hovered or clicked, creating a sense of fluidity and responsiveness.

**Glassmorphism:**

* The design incorporates subtle, minimalist glassmorphism elements, such as soft, rounded corners, and subtle, blurred backgrounds, to create a sense of depth and dimensionality.
""",
    )
    print(f"AI: {response}")
