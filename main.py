from fastapi import FastAPI
from crewai import Agent, Task, Crew

app = FastAPI()

@app.get("/")
def home():
    return {"status": "CrewAI Agent is running 24/7!"}

@app.get("/run-agent")
def run_agent(topic: str = "AI Automation"):
    # సింపుల్ ఏజెంట్ సెటప్
    researcher = Agent(
        role='Senior Researcher',
        goal=f'Research about {topic}',
        backstory='You are an expert researcher.',
        verbose=False
    )
    
    task = Task(
        description=f'Give 3 key insights about {topic}.',
        expected_output='A bulleted list of 3 insights.',
        agent=researcher
    )
    
    crew = Crew(
        agents=[researcher],
        tasks=[task],
        verbose=0
    )
    
    result = crew.kickoff()
    return {"result": str(result)}
  
