import os

# Define the directory and the structure
base_dir = "sections"

structure = {
    "Blog": 4,
    "Collections": 3,
    "Content": 2,
    "Call_To_Action": 4,
    "FAQ": 4,
    "Features": 5,
    "Navigation": 3,
    "Footer": 8,
    "Form": 2,
    "Heading": 3,
    "Hero": 8,
    "logo_cloud": 3,
    "newsletter_signup": 3,
    "Pricing": 4,
    "Product_detail": 2,
    "Product_grid": 3,
    "Reviews": 3,
    "Stats": 3,
    "Team": 4,
    "testimonials": 3,
}

# Create the directories and files
for folder, count in structure.items():
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    for i in range(1, count + 1):
        file_name = f"{folder}_{i}.html"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "w") as file:
            pass  # Create an empty file

print("Folders and files created successfully.")

# print current directory
print(os.getcwd())
