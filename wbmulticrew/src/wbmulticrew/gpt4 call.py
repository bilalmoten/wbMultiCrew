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
                "content": "You are an expert Mergers and Aquisitionss lawyer. Your goal is to advice the user and help him understand the accusation offer and how he can negotiate a better deal.",
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
    user_message = input("You: ")
    response = app.send_message("user", user_message)
    print(f"AI: {response}")
