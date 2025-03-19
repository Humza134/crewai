from crewai.flow import Flow, start, listen
from multiple_agents.crews.dev_crew.dev_crew import DevCrew

class DevFlow(Flow):
    """Dev Flow"""

    @start()
    def run_dev_crew(self):
        output = DevCrew().crew().kickoff(
            inputs={
                "problem": "write a python code for addition two numbers"
            }
        )
        return output.raw
    

def kickoff():
    dev_flow = DevFlow()
    result = dev_flow.kickoff()
    print(result)
