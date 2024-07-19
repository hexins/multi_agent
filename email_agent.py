from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_anthropic  import AnthropicLLM

cold_email_template = """
create a personalized cold outreach email according to lead information and provided email sample.
in the email example there are prompts enclosed by square brackets, 
replace these prompts with content generated according to the prompts.
your output should contains two part: subject and content of the email

here is the lead information
Name: {name}
Email: {email}
Company: {company}
Job Title: {job_title}
Industry: {industry}

here is the sample email:

Subject: Introducing {product_service} to Improve {relevant_aspect}

Hi {name},

I hope this email finds you well. My name is {sender_name}, and I am reaching out to you from {sender_company}. I noticed that you are the {job_title} at {company}, and I wanted to share how our {product_service} can help you with [specific challenge or opportunity relevant to the lead's role and provided product/service].

[Personalized message based on the lead's company or job title]

I'd love to discuss this further and see how we can assist you. Please let me know if you're available for a quick call next week.

Best regards,
{sender_name}
"""

warm_email_template = """
create a personalized warm outreach email according to lead information and provided email sample.
in the email example there are prompts enclosed by square brackets, 
replace these prompts with content generated according to the prompts.
your output should contains two part: subject and content of the email

here is the lead information
Name: {name}
Email: {email}
Company: {company}
Job Title: {job_title}
Industry: {industry}

here is the sample email:

Subject: feedback about {product_service} to Improve {relevant_aspect}

Hi {name},

I hope this email finds you well. My name is {sender_name}, and I am reaching out to you from {sender_company}. Several days ago we've talked about our {product_service} which can help you with [specific challenge or opportunity relevant to the lead's role and provided product/service].

[Personalized message based on the lead's company or job title]

I'd love to discuss this further and see how we can assist you. Please let me know if you're available for a quick call next week.

Best regards,
{sender_name}
"""

def get_llm_chain(llm_model, email_type):
    prompt = PromptTemplate.from_template(
            cold_email_template
        )
    if email_type == "warm":
        prompt = PromptTemplate.from_template(
            warm_email_template
        )
    if llm_model == "openai":
        return prompt | OpenAI() | StrOutputParser()
    elif llm_model == "anthropic":
        return prompt | AnthropicLLM() | StrOutputParser()
    return None

class EmailAgent:
    """An email generation agent."""
    def __init__(self, llm_model = "openai", email_type = "cold"):
        self.llm_chain = get_llm_chain(llm_model, email_type)

    # Generate personalized emails using LLM
    def generate_email(self, lead, sender_name, sender_company, product_service, relevant_aspect):
        return self.llm_chain.invoke(input = {'name': lead['name'],
                                        'email': lead['email'],
                                        'company': lead['company'],
                                        'job_title': lead['job_title'],
                                        'industry': lead['industry'],
                                        'product_service': product_service,
                                        'relevant_aspect': relevant_aspect,
                                        'sender_name': sender_name,
                                        'sender_company': sender_company})