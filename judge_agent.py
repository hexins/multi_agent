from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

judge_template = """
you are given two emails, each email include subject and content, the email is personalized outreach email, 
you should judge which email is better in terms of relevance, tone, and engagement potential, 
according to the lead information provided in the email.
if first email is better, just output '1_better', if second email is better, just output '2_better'
do not output any other text except '1_better' or '2_better'

first email:
{email1}

second email:
{email2}
"""


class JudgeAgent:
    """A judge agent."""

    def __init__(self):
        judge_prompt = PromptTemplate.from_template(
            judge_template
            )
        self.judge_chain = judge_prompt | OpenAI() | StrOutputParser()        

    def judge(self, email1, email2):
        return self.judge_chain.invoke(input = {'email1': email1, 
                                        'email2': email2})