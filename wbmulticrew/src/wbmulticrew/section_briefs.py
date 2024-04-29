import json
import os
import time
from wbmulticrew.section_design_crew import Section_design_Crew


def generate_section_briefs(
    namee, user_requirements, website_design_brief, website_structure
):
    website_structure = json.loads(website_structure)

    for page in website_structure["pages"]:
        page_name = page["name"]
        for section in page["sections"]:
            section_name = section["name"]
            start_time = time.time()

            os.makedirs(f"{namee}/{page_name}/{section_name}", exist_ok=True)
            inputs = {
                "user_requirements": user_requirements,
                "website_design_brief": website_design_brief,
                "website_structure": website_structure,
                "page_name": page_name,
                "section_name": section_name,
            }
            Section_design_Crew(
                page_name=page_name, section_name=section_name
            ).crew().kickoff(inputs=inputs)
            end_time1 = time.time()
            print(
                f"Time taken for creating design, content and images for {section_name} section of {page_name} page of the website : {end_time1 - start_time}"
            )
