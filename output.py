import pandas as pd
import json

class Output:
    """An output agent."""
    def __init__(self, output_file_name = "output.json"):
        self.output_file_name = output_file_name
        self.contents = []
        #self.columns = ["name", "email", "company", "job_title", "email_llm_1", "email_llm_2", "selected_email"]

    # add one item
    def add(self, item):
        self.contents.append(item)
    
    def save(self):
        with open(self.output_file_name, "w") as f:
            json.dump(self.contents, f)        
