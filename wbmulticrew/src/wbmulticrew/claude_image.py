import os
import anthropic
import base64
from html2image import Html2Image


def call_claude_api(html_code, css_code, image_path, sectioname, pagename):
    client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
    )
    with open(image_path, "rb") as file:
        image1_data = base64.b64encode(file.read()).decode("utf-8")
    image1_media_type = "image/png"

    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=4000,
        temperature=0.7,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": image1_media_type,
                            "data": image1_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": """I am creating a website for a client. the Website is for ""{pagename}"" and the section is ""{sectioname}"".
                     the following is the HTML and CSS code for the section. Please provide feedback on the design and layout of the section. the image provided is the current output of the code, please analyse the image and the code, to find out issues, areas of improvement and suggestions for the design and layout of the section. Your goal is to improve the section as much as possible, to acheive an amazing design and layout for the section. Thank you!
                     please give bullet points on what is wrong, what needs to be improved and what changes should be made in the html or css code.
                     """,
                    },
                ],
            }
        ],
    )
    return message


# response = call_claude_api()
# print(response)


def generate_image(html_code, css_code, sectionname, pagename):
    # Create an instance of the HTML2Image class
    h2i = Html2Image()

    image_path = f"{pagename}_{sectionname}.png"

    h2i.screenshot(html_str=html_code, css_str=css_code, save_as=image_path)

    return image_path


def review_code(html_code, css_code, sectioname, pagename):
    image_path = generate_image(html_code, css_code, sectioname, pagename)
    response = call_claude_api(html_code, css_code, image_path, sectioname, pagename)
    print(response)


review_code(
    """
    <section class="pricing-table">
  <div class="container">
    <h2 class="section-title">Choose Your Plan</h2>
    <p class="section-subtitle">Select the plan that fits your needs</p>
    <div class="pricing-grid">
      <div class="pricing-column">
        <div class="plan-header">
          <h3 class="plan-name">Starter</h3>
          <p class="plan-description">Ideal for small teams and individuals</p>
        </div>
        <ul class="plan-features">
          <li>100 PDFs per month</li>
          <li>Basic AI features</li>
          <li>Limited customer support</li>
        </ul>
        <div class="plan-price">$9.99/mo</div>
        <button class="btn btn-primary">Sign up</button>
      </div>
      <div class="pricing-column">
        <div class="plan-header">
          <h3 class="plan-name">Growth</h3>
          <p class="plan-description">Perfect for growing teams and businesses</p>
        </div>
        <ul class="plan-features">
          <li>500 PDFs per month</li>
          <li>Advanced AI features</li>
          <li>Prioritized customer support</li>
        </ul>
        <div class="plan-price">$29.99/mo</div>
        <button class="btn btn-primary">Sign up</button>
      </div>
      <div class="pricing-column">
        <div class="plan-header">
          <h3 class="plan-name">Enterprise</h3>
          <p class="plan-description">Custom solutions for large enterprises</p>
        </div>
        <ul class="plan-features">
          <li>Unlimited PDFs per month</li>
          <li>Custom AI features</li>
          <li>Dedicated customer success manager</li>
        </ul>
        <div class="plan-price">Custom quote</div>
        <button class="btn btn-primary">Contact us</button>
      </div>
    </div>
  </div>
</section>""",
    """
.pricing-table {
    background-color: #f7f7f7;
    padding: 40px 0;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.section-title {
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 10px;
    color: #333;
    text-align: center;
}

.section-subtitle {
    font-size: 18px;
    color: #666;
    margin-bottom: 20px;
    text-align: center;
}

.pricing-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    justify-items: center;
}

.pricing-column {
    background-color: #fff;
    border: 1px solid #ddd;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease-in-out;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.pricing-column:hover {
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
    transform: translateY(-5px);
}

.plan-header {
    background-color: #663399;
    /* Purple accent color */
    padding: 10px;
    border-radius: 10px 10px 0 0;
    display: flex;
    justify-content: center;
    align-items: center;
}

.plan-name {
    font-size: 24px;
    font-weight: bold;
    color: #fff;
    margin-bottom: 10px;
}

.plan-description {
    font-size: 16px;
    color: #fff;
    margin-bottom: 20px;
}

.plan-features {
    list-style: none;
    padding: 0;
    margin: 0;
}

.plan-features li {
    font-size: 16px;
    color: #666;
    margin-bottom: 10px;
}

.plan-price {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
    color: #333;
    text-align: center;
}

.btn {
    background-color: #663399;
    /* Purple accent color */
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 10px;
    transition: all 0.3s ease-in-out;
}

.btn:hover {
    background-color: #552688;
    /* Darker purple accent color */
    transform: translateY(-2px);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}
""",
    "pricing",
    "Ai-SaaS",
)
