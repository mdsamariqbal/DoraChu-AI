from fastapi import FastAPI
from pydantic import BaseModel
from agent import emotional_agent, logical_agent, decision_agent, career_advice_agent, motivation_agent, plan_agent

app = FastAPI(title="DoraChu Local AI API")


class UserInput(BaseModel):
    problem: str


@app.get("/")
def home():
    return {"message": "DoraChu API is running locally"}


@app.post("/solve")
def solve_problem(data: UserInput):
    user_input = data.problem

    emotional = emotional_agent(user_input)
    logical = logical_agent(user_input)
    career_advice = career_advice_agent(user_input)
    motivation = motivation_agent(user_input)
    plan = plan_agent(user_input)
    
    final = decision_agent(user_input, emotional, logical, career_advice, motivation, plan)

    return {
        "user_problem": user_input,
        "emotional_response": emotional,
        "logical_response": logical,
        "final_advice": final
    }