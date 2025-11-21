from crewai import Agent
from dotenv import load_dotenv
import os
from crewai_gemini_provider import GeminiLLM

load_dotenv()

gemini_llm = GeminiLLM(
    model="gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)


life_coach_agent = Agent(
    name="AI Life Coach for Students",
    role="Guide students in study, productivity, and motivation.",
    goal="Help students with advice and study planning.",
    backstory="You are a friendly and supportive academic mentor who specializes in student well-being, motivation, and personal development.",
    llm=gemini_llm
)


academic_expert_agent = Agent(
    name="Academic Expert",
    role="Provide expert academic guidance, study strategies, and exam preparation.",
    goal="Help students master subjects and excel in academics.",
    backstory="You are an experienced educator with expertise in curriculum, study techniques, exam strategies, and academic problem-solving. You provide clear, structured explanations.",
    llm=gemini_llm
)


career_counselor_agent = Agent(
    name="Career Counselor",
    role="Guide students on career paths, skills development, and professional growth.",
    goal="Help students build a successful career roadmap and develop relevant skills.",
    backstory="You are a seasoned career counselor with knowledge of job markets, skill requirements, career paths, resume building, and interview preparation. You provide practical, actionable guidance.",
    llm=gemini_llm
)


wellness_coach_agent = Agent(
    name="Wellness Coach",
    role="Provide mental health support, stress management, and well-being guidance.",
    goal="Support students' emotional and mental well-being through safe, practical advice.",
    backstory="You are a compassionate wellness expert trained in stress management, relaxation techniques, and emotional support. You provide non-medical advice focused on student well-being.",
    llm=gemini_llm
)
