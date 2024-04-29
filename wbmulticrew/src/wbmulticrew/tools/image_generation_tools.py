import json
from langchain.tools import tool
from openai import AzureOpenAI


class Image_generation_tools:

    @tool("Generate Image using Text prompts usng Dall E 3 Text to Image Model")
    def Get_image_url(prompt):
        """
        Useful to generate images with DALL-E, using text prompts that describe the image you want to create.
        The input to this tool should be a text prompt that describes the image you want to create.
        For example, `A cat sitting on a table with a laptop in the background.`
        """
        client = AzureOpenAI(
            api_version="2024-02-01",
            azure_endpoint="https://gpt-pilot-bilal.openai.azure.com/",
            api_key="52525f7715694b989a4249260fd1d07b",
        )

        try:
            result = client.images.generate(
                model="Dalle3",  # the name of your DALL-E 3 deployment
                prompt=prompt,
                n=1,
                quality="hd",
            )
            image_url = json.loads(result.model_dump_json())["data"][0]["url"]
            return image_url
        except Exception as e:
            return f"Error Generating Image: {e} \n\n Please try again with a different prompt."
