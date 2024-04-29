import json
import re

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

    with open(f"{page_name}.html", "a") as html_file:
        html_file.write(html_code)

    with open(f"{page_name}.css", "a") as css_file:
        css_file.write(css_code)

    with open(f"{page_name}.js", "a") as js_file:
        js_file.write(js_code)


# def edit_html_file(file_list):


def make_page_files(site_name, page_name, section_names):
    html_starter = """
    <!doctype html>
    <html lang="en">
    <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://kit.fontawesome.com/037776171a.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="{page_name}.css">

    <title>{site_name} - {page_name}</title>
    </head>
    <body>
    """

    html_end = """
    <!-- Optional JavaScript -->
    <script src="{page_name}.js"></script>
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>
    </html>
    """

    # create the html file
    # add html starter
    with open(f"{page_name}.html", "w") as html_file:
        html_file.write(html_starter.format(page_name=page_name, site_name=site_name))
    # add html sections
    parse_files(page_name, section_names)
    # add html end
    with open(f"{page_name}.html", "a") as html_file:
        html_file.write(html_end.format(page_name=page_name))


# section_names = ["What We Do", "Learn More", "Book a Call"]
# page_name = "Home"
# site_name = "wbmulticrew_test4"

# make_page_files(site_name, page_name, section_names)
