# Overview
This project is to show how to use LLM application framework like Langchain to create a multi-agent system.  
In multi-agent system, there are different agents working together to complete the whole job,  
each agent will focus on one task which will call LLM to execute.  
This program will generate outreach emails according to the personal information in the csv input file.  
The emails are generated using two different language models: Openai and Anthropic.  
Then a judge agent will check which language model is doing better.
# Installation and run
make sure you have installed Python 3.10 environment
We recommend you to create a local venv environment
and activate the environment
```bash
git clone https://github.com/hexins/multi_agent.git
cd multi_agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="xxxx"
export ANTHROPIC_API_KEY="xxxx"
python orchestrator.py
```
replace the "xxxx" with your OPENAI_API_KEY and ANTHROPIC_API_KEY   
the output file is "cold.json", which will contain the generated emails and judge result   

entry point is orchestrator.py

There are also command line arguments to change the input/output file name and email prompt type in orchestrator.py   
please refer to orchestrator.py for explaination

the orchestrator will firstly load the input csv file, then generate two email using email agent, 
after that it call judge agent to get the judge result, then save all the results to json format.
there are two types of prompt, one is cold outreach prompt, one is warm outreach prompt, 
user could specify the type in command line, default to "cold"
