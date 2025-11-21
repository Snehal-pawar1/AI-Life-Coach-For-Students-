from crewai import Crew
from agent import (
    life_coach_agent, 
    academic_expert_agent, 
    career_counselor_agent,
    wellness_coach_agent
)
from task import (
    study_task, personal_task, career_task,
    general_task, chat_task, mental_health_task
)
from safety_filter import is_unsafe


def select_task(query, category="Auto-detect"):
    """Select the appropriate task based on query content or user category selection."""
    
    # If user explicitly selected a category, use it
    if category != "Auto-detect":
        if category == "Study & Academics":
            return study_task
        elif category == "Career Guidance":
            return career_task
        elif category == "Personal Development":
            return personal_task
        elif category == "Mental Health":
            return mental_health_task
        elif category == "General Chat":
            return chat_task
    
    # Auto-detect based on keywords
    q = query.lower()

    if any(w in q for w in ["study", "exam", "notes", "timetable", "assignment", "project", "revision", "homework", "class", "subject"]):
        return study_task

    if any(w in q for w in ["motivation", "stress", "routine", "habit", "productivity", "emotion", "time management", "procrastination"]):
        return personal_task

    if any(w in q for w in ["career", "job", "skills", "resume", "interview", "internship", "salary", "role"]):
        return career_task

    if any(w in q for w in ["anxiety", "burnout", "relax", "mental", "depressed", "sad", "worried", "sleep", "meditation"]):
        return mental_health_task

    if any(w in q for w in ["explain", "define", "what is", "gk", "how to", "why"]):
        return general_task

    # Default fallback
    return chat_task


def run_agent(query, student_level="High School", subject_area="", category="Auto-detect", 
              urgency="Not urgent", preferred_length="Medium (3-5 sentences)"):
    """
    Run the appropriate agent based on query and preferences.
    
    Args:
        query: The student's question or request
        student_level: The student's education level
        subject_area: The field of study (optional)
        category: The category selected by user or auto-detect
        urgency: How urgent the response needs to be
        preferred_length: Desired response length
    """
    
    # 1️⃣ Safety check
    block_message = is_unsafe(query)
    if block_message:
        return block_message

    # 2️⃣ Select appropriate task category
    task = select_task(query, category)

    # 3️⃣ Prepare inputs with all available context
    task_inputs = {
        "query": query,
        "student_level": student_level,
        "subject_area": subject_area if subject_area else "Not specified",
        "urgency": urgency,
        "preferred_length": preferred_length
    }

    # 4️⃣ Create crew with selected agent and task
    crew = Crew(
        agents=[task.agent],  # Use the agent assigned to the selected task
        tasks=[task],
        verbose=False
    )

    # 5️⃣ Run and return response
    result = crew.kickoff(inputs=task_inputs)
    return result
