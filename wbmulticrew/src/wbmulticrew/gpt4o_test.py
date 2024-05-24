import re
from wbmulticrew.page_code import call_gpt4o
import time
import os


def parse_markdown(md_text):
    # Regular expression to match code blocks and their languages
    pattern = r"```(.*?)\n(.*?)```"

    # Find all matches
    matches = re.findall(pattern, md_text, re.DOTALL)

    # Initialize variables
    html_code = css_code = js_code = ""

    # Assign the matched code to the appropriate variables
    for language, code in matches:
        if language.lower() == "html":
            html_code = code
        elif language.lower() == "css":
            css_code = code
        elif language.lower() == "javascript":
            js_code = code

    return html_code, css_code, js_code


def enhance_ui(page_name, htmlcode, csscode, jscode):
    system_prompt = """ You are an expert web developer with 10 years of experience in the worlds top web design agency. You have a knack for figuring out the best UI an UX for even the most basic websites using HTML CSS and JS. Your speciality is to take the simple html and css code for a website or webpage that user has made and enhance it into a cohesive, aesthetically designed website that promises a great user experience, and jaw dropping UI deisgn.
    
    You will be given the code for one webpage of the website at a time.
    
    Your output is expected to be a markdown file containing the updated HTML CSS and JS Code for the page.
    
    Do Not add any additional Placeholders, comments, backticks (```) or any other text in your response

    Only Respond with a Properly Formatted MARKDOWN with the following
    - html: the html code for the webpage
    - css: the css code for the webpage
    - js: the js code for the webpage (if needed)

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

    NOTHING ELSE.
    """

    user_prompt = """   hello, this is the code for the {page_name} page of the website. 
    
    html:
    {html_code}
    
    CSS:
    {css_code}
    
    JS:
    
    {js_code}
"""

    start_time = time.time()

    # Call the gpt4o function using the system and user prompts
    output = call_gpt4o(
        system_prompt,
        user_prompt.format(
            page_name=page_name,
            html_code=htmlcode,
            css_code=csscode,
            js_code=jscode,
        ),
    )

    # save the output to a file
    with open(
        f"wbmulticrew/src/wbmulticrew/{site_name}/{page_name}_enhanced.md", "w"
    ) as file:
        file.write(output)

    # Process the response from the gpt4o model
    enhanced_html, enhanced_css, enhanced_js = parse_markdown(output)
    # Create a new folder for the enhanced_filess
    os.makedirs(
        f"wbmulticrew/src/wbmulticrew/{site_name}/enhanced_files", exist_ok=True
    )

    # Save the enhanced HTML code to a file
    with open(
        f"wbmulticrew/src/wbmulticrew/{site_name}/enhanced_files/{page_name}.html",
        "w",
    ) as html_file:
        html_file.write(enhanced_html)

    # Save the enhanced CSS code to a file
    with open(
        f"wbmulticrew/src/wbmulticrew/{site_name}/enhanced_files/{page_name}.css",
        "w",
    ) as css_file:
        css_file.write(enhanced_css)

    # Save the enhanced JS code to a file
    with open(
        f"wbmulticrew/src/wbmulticrew/{site_name}/enhanced_files/{page_name}.js",
        "w",
    ) as js_file:
        js_file.write(enhanced_js)

    print("Enhanced files saved successfully.")

    end_time = time.time()
    execution_time = end_time - start_time
    print("Time taken:", execution_time, "seconds")


site_name = "test13_pharma"
page_name = "Home"

# import os

# get html code form the page_name.html file
with open(
    f"wbmulticrew/src/wbmulticrew/{site_name}/files/{page_name}.html", "r"
) as html_file:
    html_code = html_file.read()

# get css code form the page_name.css file
with open(
    f"wbmulticrew/src/wbmulticrew/{site_name}/files/{page_name}.css", "r"
) as css_file:
    css_code = css_file.read()

# get js code form the page_name.js file
with open(
    f"wbmulticrew/src/wbmulticrew/{site_name}/files/{page_name}.js", "r"
) as js_file:
    js_code = js_file.read()

enhance_ui(page_name, html_code, css_code, js_code)
