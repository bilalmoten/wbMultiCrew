import json
from crewai_tools import BaseTool
from openai import AzureOpenAI


class Dalle_Image(BaseTool):
    name: str = "Image Generation with Dall E"
    description: str = (
        """
        Generate images with DALL-E, using text prompts that describe the image you want to create.
        The tool takes in a text prompt and generates an image based on the description provided.
        the image URL will be returned to you, which you should add to the final output of the task.
        """
    )

    def _run(self, prompt: str) -> str:
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
            return (
                "Image Generated Successfully! Here is the image: \n"
                + image_url
                + "\n\n and the text prompt that was used: \n"
                + prompt
            )
        except Exception as e:
            return f"Error Generating Image: {e} \n\n Please try again with a different prompt."
