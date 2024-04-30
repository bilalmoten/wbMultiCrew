#!/usr/bin/env python
import json
import os
import time
from wbmulticrew.page_code import generate_section_code
from wbmulticrew.parse_json import make_page_files

namee = "wbmulticrew_test5"

user_conversation = """ [
  {
    "role": "user",
    "content": "i want t a website for my ai automation agency named acceleron ai"
  },
  {
    "role": "assistant",
    "content": "Exciting! So, you want a website for your AI automation agency, Acceleron AI. That's a great start! Can you tell me a bit more about what Acceleron AI does and what kind of audience you're targeting with this website? For example, are you focused on a specific industry or type of automation?"
  },
  {
    "role": "user",
    "content": " Acceleron AI Home About What We Do Learn More Book a Call Supercharge your systems with AI Future-proof your business by bringing AI into your team. Boost efficiency, cut costs, and stay ahead effortlessly. Book A Call  From Outdated to AI Leader AI Agents Have AI employees - they never ask for a raise! Full-fledged team's weekly work done by AI in hours. Connect  Apps Connect your apps to the AI agents Give AI access to work on your behalf.  Overtake Competitors Whoosh past your competition! Boost efficiency, cut costs, save time, and outperform competitors effortlessly.  More Juice, Less Squeeze. It's truly effortless.  With AI agents in your team, you get to: Experience 100% efficiency, no human errors. Eliminate costs by assigning low ROI tasks to an AI assistant. Achieve upto 5x faster work cycles; no employee friction.  When will you Adapt? Embrace the AI revolution, and join the 85% of  enterprises implementing AI by 2026!"
  },
  {
    "role": "assistant",
    "content": "It looks like you have a clear vision for your website and a good idea of the message you want to convey to your audience. I've taken note of the key points you've mentioned, including the emphasis on boosting efficiency, cutting costs, and staying ahead of the competition with AI automation.\n\nFrom a design perspective, I can see that you might be interested in a modern, futuristic aesthetic to match the innovative and cutting-edge nature of AI automation. Perhaps we could explore a color scheme that incorporates blues and whites to convey a sense of technology and innovation?\n\nCan you tell me a bit more about the type of design elements you envision for the website? For example, would you like to feature any specific imagery, such as robots or circuits, or do you have any specific typography or layout preferences?"
  },
  { "role": "user", "content": "your ideas sound great, " },
  {
    "role": "assistant",
    "content": "I'm glad you like the direction we're headed. Now, let's dive a bit deeper into the design preferences. \n\nFor the imagery, would you like to feature any specific types of images or graphics on the website? For example, would you like to showcase AI-related visuals like robots, circuits, or futuristic landscapes, or perhaps more abstract representations of innovation and technology?\n\nAdditionally, are there any specific typography or font styles that you're drawn to? For instance, would you like a clean and minimalist sans-serif font or a more futuristic, high-tech font with a bold and edgy feel?\n\nLastly, are there any specific layout or UI elements that you envision for the website? For example, would you like to feature a prominent hero section, a showcase of case studies or testimonials, or a prominent call-to-action (CTA) to encourage visitors to book a call or learn more?\n\nLet me know your thoughts, and I can start to get a better sense of your design preferences!"
  },
  {
    "role": "user",
    "content": "i dont have any other specifics, you can think about everything else yourself."
  },
  {
    "role": "assistant",
    "content": "With the information you've provided, I have a good understanding of the overall direction and tone you're aiming for. I'll use my expertise to make suggestions and recommendations for the design and development of your website.\n\nSince we're focusing on a modern, futuristic aesthetic, I'll explore design elements that incorporate clean lines, minimalism, and a touch of innovation. I'll also ensure that the typography and color scheme align with the AI automation theme.\n\nAs we're done discussing the project details, I'll wrap up our conversation here. I'll say... Exit"
  },
  { "role": "user", "content": "okay" }
]
"""


# from wbmulticrew.user_requirements_crew import user_requirementsCrew

from wbmulticrew.section_design_crew import Section_design_Crew


def run():

    # # generate user requirements, website design brief and website structure from user conversation ### START ###
    # inputs = {
    #     "user_conversation": user_conversation,
    #     "example_website_structure": """{
    #   "sitename": "My Website",
    #   "pages": [
    #     {
    #       "name": "Home",
    #       "sections": [
    #         {
    #           "name": "Hero"
    #         },
    #         {
    #           "name": "About Us"
    #         },
    #         {
    #           "name": "Features"
    #         },
    #         {
    #           "name": "Testimonials"
    #         },
    #         {
    #           "name": "Contact Us"
    #         }
    #       ]
    #     },
    #     {
    #       "name": "About",
    #       "sections": [
    #         {
    #           "name": "Mission"
    #         },
    #         {
    #           "name": "Vision"
    #         },
    #         {
    #           "name": "Values"
    #         },
    #         {
    #           "name": "Team"
    #         },
    #         {
    #           "name": "Contact Us"
    #         }
    #       ]
    #     }
    #   ]
    #   //any other pages and sections as needed by the user requirements.
    # }""",
    # }

    # start_time = time.time()

    # os.makedirs(namee, exist_ok=True)
    # user_requirementsCrew().crew().kickoff(inputs=inputs)

    # end_time1 = time.time()
    # print(
    #     f"Time taken for generating user requirements and website structure: {end_time1 - start_time}"
    # )

    # website_structure = open(f"{namee}/website_structure.json", "r").read()

    # user_requirements = open(f"{namee}/user_requirements.md", "r").read()
    # website_design_brief = open(f"{namee}/website_design_brief.md", "r").read()

    # website_structure = json.loads(website_structure)

    # for page in website_structure["pages"]:
    #     page_name = page["name"]
    #     for section in page["sections"]:
    #         section_name = section["name"]
    #         start_time = time.time()

    #         os.makedirs(f"{namee}/{page_name}/{section_name}", exist_ok=True)
    #         inputs = {
    #             "user_requirements": user_requirements,
    #             "website_design_brief": website_design_brief,
    #             "website_structure": website_structure,
    #             "page_name": page_name,
    #             "section_name": section_name,
    #         }
    #         Section_design_Crew(
    #             page_name=page_name, section_name=section_name
    #         ).crew().kickoff(inputs=inputs)
    #         end_time1 = time.time()
    #         print(
    #             f"Time taken for creating design, content and images for {section_name} section of {page_name} page of the website : {end_time1 - start_time}"
    #         )

    website_structure = open(f"{namee}/website_structure.json", "r").read()
    website_structure = json.loads(website_structure)

    for page in website_structure["pages"]:
        page_name = page["name"]
        for section in page["sections"]:
            section_name = section["name"]
            start_time = time.time()
            section_code_json = generate_section_code(
                section_name,
                open(f"{namee}/{page_name}/{section_name}/design_brief.md", "r").read(),
                open(f"{namee}/{page_name}/{section_name}/text_content.md", "r").read(),
                open(f"{namee}/{page_name}/{section_name}/image_urls.md", "r").read(),
            )

            with open(f"{namee}/{page_name}/{section_name}/section_code.md", "w") as f:
                f.write(section_code_json)
            end_time1 = time.time()
            print(
                f"Time taken for generating code for {section_name} section of {page_name} page of the website : {end_time1 - start_time}"
            )
        make_page_files(
            namee, page_name, [section["name"] for section in page["sections"]]
        )
        return
