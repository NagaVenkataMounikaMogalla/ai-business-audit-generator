from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key ="YOUR_OPENROUTER_API_KEY"
)


def generate_ai_insights(company_name, website_data):

    prompt = f"""
    
    Analyze the following company and generate a professional AI business audit report.

    Company Name:
    {company_name}

    Website Title:
    {website_data['title']}

    Meta Description:
    {website_data['description']}

    Website Content:
    {website_data['content']}

    Generate:
    
    1. Company Overview
    2. Business Analysis
    3. AI Automation Opportunities
    4. Website Improvement Suggestions
    5. Growth Recommendations
    6. Customer Engagement Suggestions

    Keep the report professional and personalized.
    """

    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content