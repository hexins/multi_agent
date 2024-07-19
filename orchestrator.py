import argparse
from email_agent import EmailAgent
from loader import extract_lead_data
from judge_agent import JudgeAgent
from output import Output

class Orchestrator:
    """An Orchestrator agent."""
    def __init__(self, email_type = 'cold', input_file_name = 'sample_leads_10.csv', output_file_name = 'cold.json',
                 sender_name = 'Xin', sender_company = 'Food device solutions', 
                 product_service = 'coffee machine',
                 relevant_aspect = 'beverage quality'):
        self.email_type = email_type
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.sender_name = sender_name
        self.sender_company = sender_company
        self.product_service = product_service
        self.relevant_aspect = relevant_aspect

    def run(self):
        leads = extract_lead_data(self.input_file_name)
        agent_openai = EmailAgent(llm_model='openai', email_type=self.email_type)
        agent_anthropic = EmailAgent(llm_model='anthropic', email_type=self.email_type)
        agent_judge = JudgeAgent()
        output = Output(output_file_name=self.output_file_name)
        for lead in leads:
            email1 = agent_openai.generate_email(lead, self.sender_name, self.sender_company, self.product_service, self.relevant_aspect)
            print(f"\nemail1:\n{email1}")
            email2 = agent_anthropic.generate_email(lead, self.sender_name, self.sender_company, self.product_service, self.relevant_aspect)
            print(f"\nemail2:\n{email2}")
            judge_str = agent_judge.judge(email1, email2)
            print(f"\njudge_str:\n{judge_str}")

            selected_email = ''
            if '1_better' in judge_str:
                selected_email = 'LLM 1'
            elif '2_better' in judge_str:
                selected_email = 'LLM 2'
            output.add({'name':lead['name'], 'email':lead['email'], 'company':lead['company'], 
                        'job_title':lead['job_title'], 'email_llm_1':email1, 'email_llm_2':email2, 'selected_email':selected_email})

        output.save()
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", type=str, default="sample_leads_10.csv", help="Specify the name of the input csv file"
    )
    parser.add_argument(
        "--output", type=str, default="cold.json", help="Specify the name of the output json file"
    )
    parser.add_argument("--type", type=str, default="cold", help="Specify the type of email, 'cold' or 'warm'")
    args = parser.parse_args()
    orc = Orchestrator(email_type=args.type, input_file_name=args.input, output_file_name=args.output)
    orc.run()



