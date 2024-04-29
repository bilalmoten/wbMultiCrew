Multi Crew Agentic Workflow to create a full website, functional, aesthetically designed and responsive, based on user requirements. the workflow utilises AI Agents, using Crew AI, to create the full website, with out any human input.

the process to be followed is detailed below. the process will then be used to create a multi crew workflow.

the full process starts with the workflow getting a user conversation, and ends with the complete website code base.

1. User Conversation
   the user conversation contains a users conversation with an ai chat bot that asks detailed questions about the website to the user to know what kind of a website does the user want. the conversation mostly would include details about the users business, the things he wants the website to have, the design language that user wants the website to have and details about the users target audience, and other details that the user wants to include in the website.

2. User Requirements
   the user requirements are then extracted from the user conversation, and are then used to create a user requirements document that contains all the details about the website that the user wants. this user requirements document includes all the details of the website that were present in the user conversation in a proper structured format, along with enhancements from the AI Agent that generates this document.

3. Gneral Website Design Brief
   based on the users requirements, a design breif for the website is generated, that contains the design language that the website should have.
   the design brief contains the following details in general for the whole website, and does not contain any specific details about any section of the website. the design brief is supposed to act as background information for the AI agents that will be creating the individual sections of the website.

- color scheme
- typography
- design language
- target audience
- business details
- website purpose

4. website structure
   the user requirements document is then used to create a website structure document that contains the structure of the website, in a proper json format. the website structure includes the pages that the website will have, the sections that each page will have, and the elements that each section should have.

5. Section Loop
   the website structure document is then used to create a loop that goes through each section of each page, and creates a section breif that contain everything needed to write the fornt end HTML, CSS and JS code for that section of the website.
   the section design document has 4 main parts.

- Section Name and Page Name
- design brief for the section
- curated content to be included into the section
- image urls and description of images to be used in that section

  5a. Section Design Brief
  the section design brief is the base of how the section will look to the final user. it starts with the layout of that section, and then goes on to the design language that the section should have. the design language includes the color scheme, typography, and other design elements that the section should have. the design language is extracted from the general design brief that was created in step 3. the design brief include full details for each element of the section, including images, text, button, sliders, cards and any element that is supposed to be built in that section. the design brief needs to give full details of the styling of each element and how the entire section would be in terms of design, aesthetics, and functionality.
  the design brief includes details of any and all anymations, micro interactions, hover effects and other interactive elements that the section should have.
  the output would be expected in a markdown format.

  5b. Section Curated Content brief
  For the section Curated content, an ai agent will be used to curate the content that will be included in the section. the agent would understand the user requirements document(that include website purpose and business details etc) along with the website structure and the section design brief to curate the text content that would be included in the section, including text for headlines, subheadlines, image captions/alt text, button labels, and any other text that is supposed to be included in the section. the output would be expected in a markdown format.

  5c. Section Image URLs brief
  the section design brief, user requirements, and section curated content is then passed on to an ai agent, who understand the design brief and content brief to find out the images that would be required for this section. the agent would be responsible for using the image generation tools(generate image with dall e 3) to create all images that would be required for this section, by passing a detailed text prompt for the image. the agent would then output a markown file with the image urls and the description of the images that would be used in the section.

the three briefs(design, content and iamge) are then combined with the section and page name to create a full section brief that contains all the details needed to create the HTML, CSS and JS code for that section.

6. Section Code Generation
   the section brief is then passed on to an ai agent that understands the section brief and is responsible for creating the HTML, CSS and JS code for that section. The agent would be responsible for creating the code for the section, including all the elements that are supposed to be present in the section, and the styling that is supposed to be present in the section. the agent would be responsible for creating the code in a proper format, that can be used in the final website. the output would be expected in a JSON format that has the section name, page name, html code, css code, and js code for that section. The Agent should make sure that the json is properly formatted, so that it can be parsed without any errors.

7. Website Code Generation
   the section code generation process is repeated for all the sections of all the pages of the website, and the output of all the sections is then combined to create the full website code base. the full website code base is then passed on to an ai agent that understands the website structure and is responsible for creating the full website code base. the agent would be responsible for creating the code for the full website, including all the sections that are supposed to be present in the website, and the styling that is supposed to be present in the website. the agent would be responsible for creating the code in a proper format, that can be used in the final website. The agent would have access to the website files directory and should use the file tools(file write tool) to write the code for each section into the website files.

8. Website Deployment

For the first version of the workflow, steps 1-6 will be implemented using 3 seperate crews of ai agents.

- Crew 1: User Conversation, User Requirements, General Website Design Brief
- Crew 2: Website Structure, Section Loop(Section Design Brief, Section Curated Content brief, Section Image URLs brief)
- Crew 3: Section Code Generation

For the second version of the workflow, steps 7 and 8 will be implemented using a single crew of ai agents.
