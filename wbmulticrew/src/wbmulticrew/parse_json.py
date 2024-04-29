import json
import re


# def replace_inner_quotes(match):
#     # Replace inner quotes with escaped quotes
#     return match.group(0).replace('"', '\\"')


# def parse_response(response):
#     # Apply the replacement function to each match of the regular expression
#     response = re.sub(r': ".*?",', replace_inner_quotes, response)

#     try:
#         # Try to parse the response as JSON
#         return json.loads(response)
#     except json.JSONDecodeError as e:
#         print(f"JSONDecodeError: {e}")
#         return None


# # access the json from file section_code.json and parse it
# with open(
#     "/Users/muhammedbilal/Development/wbMultiCrew/wbmulticrew/wbmulticrew_test4/Home/What We Do/section_code.json",
#     "r",
# ) as file:
#     response = file.read()
#     parsed_response = parse_response(response)

#     # print the parsed json
#     print(json.dumps(parsed_response, indent=4))


import re


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


## access the .md file

# with open(
#     "/Users/muhammedbilal/Development/wbMultiCrew/wbmulticrew/wbmulticrew_test4/Home/What We Do/section_code.md",
#     "r",
# ) as file:
#     your_markdown_string = file.read()

# # Use the function
# html_code, css_code, js_code = parse_markdown(your_markdown_string)

# print("HTML Code:")
# print(html_code)
# print("\nCSS Code:")
# print(css_code)
# print("\nJavaScript Code:")
# print(js_code)


# def parse_files(file_list):
#     html_code = ""
#     css_code = ""
#     js_code = ""

#     for file_path in file_list:
#         with open(file_path, "r") as file:
#             file_content = file.read()
#             file_html_code, file_css_code, file_js_code = parse_markdown(file_content)
#             html_code += file_html_code
#             css_code += file_css_code
#             js_code += file_js_code

#     with open("all_html_code.html", "w") as html_file:
#         html_file.write(html_code)

#     with open("all_css_code.css", "w") as css_file:
#         css_file.write(css_code)

#     with open("all_js_code.js", "w") as js_file:
#         js_file.write(js_code)


# file_list = [
#     "/Users/muhammedbilal/Development/wbMultiCrew/wbmulticrew/wbmulticrew_test4/Home/What We Do/section_code.md",
#     "/Users/muhammedbilal/Development/wbMultiCrew/wbmulticrew/wbmulticrew_test4/Home/Learn More/section_code.md",
#     "/Users/muhammedbilal/Development/wbMultiCrew/wbmulticrew/wbmulticrew_test4/Home/Book a Call/section_code.md",
# ]

# parse_files(file_list)


def parse_files(page_name, section_names):
    base_path = (
        "/Users/muhammedbilal/Development/wbMultiCrew/wbmulticrew/wbmulticrew_test4"
    )
    html_code = ""
    css_code = ""
    js_code = ""

    for section_name in section_names:
        file_path = f"{base_path}/{page_name}/{section_name}/section_code.md"
        with open(file_path, "r") as file:
            file_content = file.read()
            file_html_code, file_css_code, file_js_code = parse_markdown(file_content)
            html_code += f"<!-- {section_name} -->\n{file_html_code}\n"
            css_code += f"/* {section_name} */\n{file_css_code}\n"
            js_code += f"// {section_name}\n{file_js_code}\n"

    with open(f"{page_name}.html", "w") as html_file:
        html_file.write(html_code)

    with open(f"{page_name}.css", "w") as css_file:
        css_file.write(css_code)

    with open(f"{page_name}.js", "w") as js_file:
        js_file.write(js_code)


section_names = ["What We Do", "Learn More", "Book a Call"]
page_name = "Home"

parse_files(page_name, section_names)


def edit_html_file(file_list):
    html_code = """
    <!doctype html>
    <html lang="en">
    <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://kit.fontawesome.com/037776171a.js" crossorigin="anonymous"></script>

    <title>Hello, world!</title>
    </head>
    <body>
    <h1>Hello, world!</h1>
    """

    css_links = ""
    js_links = ""

    for file_path in file_list:
        if file_path.endswith(".css"):
            css_links += f'<link rel="stylesheet" href="{file_path}">\n'
        elif file_path.endswith(".js"):
            js_links += f'<script src="{file_path}"></script>\n'

    html_code += css_links
    html_code += js_links

    html_code += """
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>
    </html>
    """

    with open("index.html", "w") as html_file:
        html_file.write(html_code)
