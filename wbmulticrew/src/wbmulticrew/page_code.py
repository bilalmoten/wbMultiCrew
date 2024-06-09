import os

# import time
import json
from groq import Groq
from openai import AzureOpenAI

from dotenv import load_dotenv

load_dotenv()

# AzureOpenAI.api_key = os.environ["AZURE_OPENAI_API_KEY"]


from dotenv import load_dotenv
import time

load_dotenv()


client = Groq(
    api_key=os.environ["GROQ_API_KEY"],
)  # Create a Groq client

system_prompt = """
You're the Lead Developer at the worlds top website development agency. You have 10 years of experience in developing highly interactive, beautifully designed websites. Your expertise in HTML, CSS and JS based front-end web development is unmatched.

Do Not add any Placeholders, comments, backticks (```) or any other text in your response

Only Respond with a Properly Formatted MARKDOWN with the following
- html: the html code for the section
- css: the css code for the section
- js: the js code for the section (if needed)

the markdown should include each codeblock seperatly with language specified as HTML, CSS or JS

such as

## <section name>
### HTML

```html
<html code here>
```

### CSS
```css
<css code here>
```

### JS (if needed)
```javascript
<js code here>
```

NOTHING ELSE. """

user_promptf = """
Please write the front end HTML, CSS and JS code for the {section_name} section of the website. You should use the design brief, text content, and image urls given to you for the {section_name} section of the page to write the HTML CSS and JS(if needed) code. Your primary goal is to make a nice looking, responsive, and user-friendly page that matches the design brief and the user requirements.

the website will be using bootstrap.css, bootstrap.js and jquery.js, so you should write the code accordingly to benefit from these libraries.


Section_design_brief for {section_name} section:
{section_design_brief}

Text_content for {section_name} section:
{text_content}

Image_urls to use in the {section_name} section:
{image_urls}


REMEMBER
---------
Do Not add any Placeholders, comments, backticks (```) or any other text in your response

Only Respond with a Properly Formatted Markdown with the following
- html: the html code for the section
- css: the css code for the section
- js: the js code for the section (if needed)


"""
# NOTHING ELSE. ONLY A JSON OBJECT WITH THE ABOVE KEYS.

# Rules For JSON OUTPUT
# ---------------------------------
# Enclose all keys and string values in double quotes (""). For example, "html": "<div>...</div>".
# Make sure to escape any special characters within string values. For example, if your HTML, CSS, or JavaScript code contains double quotes("), replace them with (\") to avoid breaking the JSON format.
# Remember to close all JSON Curly Braces (}}).
# If the value of a key is a multi-line string, replace line breaks with \n.


def call_gpt4o(system_prompt, user_prompt, assistant_messages=None):
    client = AzureOpenAI(
        azure_endpoint="https://answerai-bilal.openai.azure.com/",
        api_version="2024-02-01",
        api_key="523a50ed7a7444468d1ae5a384f032bf",
        # azure_deployment="gpt4o-azure",
    )
    start_time = time.time()
    messageshistory = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    if assistant_messages is not None:
        for message in assistant_messages:
            messageshistory.append({"role": "assistant", "content": message})
            messageshistory.append({"role": "user", "content": "Continue."})

    completion = client.chat.completions.create(
        model="gpt4o-azure",
        messages=messageshistory,
        temperature=1.2,
        max_tokens=4000,
        # top_p=1,
        stop=None,
        stream=False,
    )
    end_time = time.time()
    print("Time taken for the call:", end_time - start_time, "seconds")
    return completion.choices[0].message.content


def call_groq(system_prompt, user_prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        model="llama3-70b-8192",
        temperature=1.3,
        max_tokens=6000,
        top_p=1,
        stop=None,
        stream=False,
    )

    return chat_completion.choices[0].message.content


def generate_section_code(
    section_name,
    section_design_brief,
    text_content,
    image_urls,
):
    user_prompt = user_promptf.format(
        section_name=section_name,
        section_design_brief=section_design_brief,
        text_content=text_content,
        image_urls=image_urls,
    )

    response = call_gpt4o(system_prompt, user_prompt)
    return response
