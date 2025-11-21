import streamlit as st
from main import run_agent

st.set_page_config(page_title="AI Life Coach", layout="wide")
st.title("🎓 AI Life Coach for Students (Gemini + CrewAI)")

# Sidebar for additional information
with st.sidebar:
    st.header("📋 About You")
    student_level = st.selectbox(
        "Education Level",
        ["High School", "Bachelor's", "Master's", "Other"]
    )
    subject_area = st.text_input("Field of Study (Optional)", placeholder="e.g., Computer Science, Engineering")

# Main input section
col1, col2 = st.columns([3, 1])

with col1:
    query = st.text_area(
        "Ask your question or describe what you need help with:",
        height=100,
        placeholder="E.g., I'm struggling with exam preparation or need career advice..."
    )

with col2:
    category = st.selectbox(
        "Category (Optional)",
        ["Auto-detect", "Study & Academics", "Career Guidance", "Personal Development", "Mental Health", "General Chat"]
    )

# Contact/Additional info
col3, col4 = st.columns(2)
with col3:
    urgency = st.selectbox(
        "How urgent is this?",
        ["Not urgent", "Somewhat urgent", "Very urgent"]
    )

with col4:
    preferred_length = st.selectbox(
        "Response length",
        ["Brief (1-2 sentences)", "Medium (3-5 sentences)", "Detailed (full explanation)"]
    )

# Submit button
if st.button("Get Advice", type="primary", use_container_width=True):
    if query.strip():
        with st.spinner("Thinking..."):
            result = run_agent(
                query=query,
                student_level=student_level,
                subject_area=subject_area,
                category=category,
                urgency=urgency,
                preferred_length=preferred_length
            )
            st.success(result)
    else:
        st.warning("Please enter a question or describe what you need help with.")
