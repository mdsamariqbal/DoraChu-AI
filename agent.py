import ollama

MODEL_NAME = "phi3"


def run_agent(system_prompt, user_input):
    try:
        prompt = f"""
{system_prompt}

User Problem:
{user_input}
"""

        response = ollama.chat(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"Error: {e}"


# Emotional Agent
def emotional_agent(user_input):
    prompt = """
You are DoraChu, a caring emotional companion.
Show empathy, encouragement, and positive support.
"""
    return run_agent(prompt, user_input)


# Logical Agent
def logical_agent(user_input):
    prompt = """
You are DoraChu, a logical assistant.
Give clear step-by-step practical advice.
"""
    return run_agent(prompt, user_input)


# Decision Agent
def decision_agent(user_input, emotional_output, logical_output, career_output, motivation_output, plan_output):
    prompt = f"""
You are Senior DoraChu.

User Problem:
{user_input}

Emotional Advice:
{emotional_output}

Logical Advice:
{logical_output}

Career Advice:
{career_output}

Motivation:
{motivation_output}

Plan:
{plan_output}

Combine all and give balanced final guidance.
"""
    return run_agent(prompt, "")


# Career Advice Agent
def career_advice_agent(user_input):
    prompt = """
You are DoraChu, a career counselor.
Provide professional career advice and growth strategies.
"""
    return run_agent(prompt, user_input)


# Motivation Agent
def motivation_agent(user_input):
    prompt = """
You are DoraChu, a motivational speaker.
Inspire the user to take action and believe in themselves.
"""
    return run_agent(prompt, user_input)


# Plan Agent
def plan_agent(user_input):
    prompt = """
You are DoraChu, a strategic planner.
Create a structured, actionable plan for the user.
"""
    return run_agent(prompt, user_input)