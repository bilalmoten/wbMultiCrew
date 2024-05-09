import json
import os
from crewai_tools import BaseTool
from openai import AzureOpenAI
import requests


class Dalle_Image(BaseTool):
    name: str = "Image Generation with Dall E"
    description: str = (
        """
        Generate images with DALL-E, using text prompts that describe the image you want to create.
        The tool takes in a text prompt and generates an image based on the description provided.
        the image Path will be returned to you, which you should add to the final output of the task.
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
            # Download the image
            response = requests.get(image_url)
            image_name = f"generated_image_{prompt.replace(' ', '_')}.jpg"
            # Extract the first 5 words from the prompt
            first_5_words = " ".join(prompt.split()[:5])
            image_name = f"generated_image_{first_5_words.replace(' ', '_')}.jpg"
            image_path = os.path.join("images", image_name)

            # Save the image
            with open(image_path, "wb") as f:
                f.write(response.content)

            return f"Image Generated Successfully! Image saved at: {image_path}"

        except Exception as e:
            return f"Error Generating Image: {e} \n\n Please try again with a different prompt."
