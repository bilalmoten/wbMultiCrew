# from langchain.tools import tool


# class FileTools:

#     @tool("Write File with content")
# #     def write_file(data):
#         """Useful to write a file to a given path with a given content.
#         The input to this tool should be a pipe (|) separated text
#         of length two, representing the full path of the file,
#         including the /workdir/template, and the HTML or CSS or JS code you want to write to it.
#         For example, `./{pagename}.html|HTML_CODE_PLACEHOLDER` or `./{pagename}.css|CSS_CODE_PLACEHOLDER`.
#         Replace HTML_CODE_PLACEHOLDER with the actual
#         code you want to write to the file."""
#         try:
#             path, content = data.split("|")
#             path = path.replace("\n", "").replace(" ", "").replace("`", "")
#             if not path.startswith("./workdir"):
#                 path = f"./workdir/{path}"
#             with open(path, "w") as f:
#                 f.write(content)
#             return f"File written to {path}."
#         except Exception:
#             return "Error with the input format for the tool."


# import json
from crewai_tools import BaseTool

# from openai import AzureOpenAI


class file_write_tool(BaseTool):
    name: str = "Write content into a file in a given path"
    description: str = (
        """Useful to write a file to a given path with a given content.
        The input to this tool should be a pipe (|) separated text
        of length two, representing the full path of the file, and the HTML or CSS or JS code you want to write to it.
        For example, `{website_name}/codefiles/{pagename}.html|HTML_CODE_PLACEHOLDER` or `{website_name}/codefiles/{pagename}.css|CSS_CODE_PLACEHOLDER`.
        Replace HTML_CODE_PLACEHOLDER with the actual
        code you want to write to the file."""
    )

    def _run(self, data: str) -> str:

        try:
            path, content = data.split("|")
            path = path.replace("\n", "").replace(" ", "").replace("`", "")
            # if not path.startswith("./workdir"):
            #     path = f"./workdir/{path}"
            with open(path, "w") as f:
                f.write(content)
            return f"File written to {path}."
        except Exception:
            return "Error with the input format for the tool."
