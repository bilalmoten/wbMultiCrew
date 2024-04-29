import json
import os
import time
from wbmulticrew.user_requirements_crew import user_requirementsCrew

# from wbmulticrew.main import name


# generate user requirements, website design brief and website structure from user conversation ### START ###
def generate_user_requirements(namee, user_conversation):
    inputs = {"user_conversation": user_conversation}

    start_time = time.time()

    os.makedirs(namee, exist_ok=True)
    user_requirementsCrew().crew().kickoff(inputs=inputs)

    end_time1 = time.time()
    print(
        f"Time taken for generating user requirements and website structure: {end_time1 - start_time}"
    )
