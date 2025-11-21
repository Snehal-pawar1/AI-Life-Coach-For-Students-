from crewai import Task
from agent import (
    life_coach_agent, 
    academic_expert_agent, 
    career_counselor_agent,
    wellness_coach_agent
)

# 1️⃣ Study-Related Guidance (Academic Expert)
study_task = Task(
    description="""
        The student needs study-related help. Provide guidance about:
        - Timetables and study schedules
        - Revision plans and techniques
        - Notes-taking strategies
        - Subject explanations
        - Exam strategies and tips
        - Project topic suggestions
        - Coding help and debugging
        - Assignment explanation
        
        Student Level: {student_level}
        Subject Area: {subject_area}
        Urgency: {urgency}
        Preferred Length: {preferred_length}
        
        Query: {query}
    """,
    expected_output="Clear, step-by-step academic guidance with practical study strategies.",
    agent=academic_expert_agent
)

# 2️⃣ Personal Life Coaching (Life Coach)
personal_task = Task(
    description="""
        Student needs personal life-coaching. Provide:
        - Motivation and encouragement
        - Stress reduction and coping strategies
        - Time management techniques
        - Productivity tips and hacks
        - Habit building and breaking
        - Emotional support
        - Goal-setting and planning
        
        Student Level: {student_level}
        Urgency: {urgency}
        Preferred Length: {preferred_length}
        
        Query: {query}
    """,
    expected_output="Supportive and practical personal development advice with actionable steps.",
    agent=life_coach_agent
)

# 3️⃣ Career Guidance (Career Counselor)
career_task = Task(
    description="""
        Student needs career advice. Provide:
        - Suitable career paths based on their field
        - Career development roadmaps
        - Skills needed for their target role
        - Free and paid course recommendations
        - Resume writing and interview guidance
        - Internship and job search tips
        - Industry insights
        
        Student Level: {student_level}
        Subject Area: {subject_area}
        Preferred Length: {preferred_length}
        
        Query: {query}
    """,
    expected_output="Detailed, structured career guidance with clear action steps.",
    agent=career_counselor_agent
)

# 4️⃣ General Knowledge / Daily Queries (Life Coach)
general_task = Task(
    description="""
        Student needs general information or explanation. Provide:
        - Topic explanations and definitions
        - Life skills guidance
        - Communication and soft skills tips
        - English language improvement
        - General knowledge
        
        Preferred Length: {preferred_length}
        
        Query: {query}
    """,
    expected_output="Simple and clear explanation tailored to the student's level.",
    agent=life_coach_agent
)

# 5️⃣ Friendly Chat & Conversation (Life Coach)
chat_task = Task(
    description="""
        Engage in a friendly, supportive conversation:
        - Small talk and icebreakers
        - Motivational quotes
        - Light advice and encouragement
        - Decision support
        - Quick tips
        
        Query: {query}
    """,
    expected_output="Friendly, conversational response that builds rapport.",
    agent=life_coach_agent
)

# 6️⃣ Mental Health Support (Wellness Coach)
mental_health_task = Task(
    description="""
        Provide SAFE, non-medical well-being guidance:
        - Anxiety management techniques
        - Burnout prevention strategies
        - Relaxation and meditation methods
        - Self-care routines
        - Sleep hygiene tips
        - Mindfulness practices
        
        ⚠️ IMPORTANT: DO NOT give professional medical diagnosis or therapy.
        ⚠️ For serious mental health issues, suggest professional help.
        
        Urgency: {urgency}
        Preferred Length: {preferred_length}
        
        Query: {query}
    """,
    expected_output="Gentle, supportive non-medical well-being advice with practical techniques.",
    agent=wellness_coach_agent
)
