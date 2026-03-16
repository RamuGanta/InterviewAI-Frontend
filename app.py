import streamlit as st
import requests

API_BASE_URL = "https://interviewai-fastapi.onrender.com"

st.set_page_config(page_title="InterviewAI", page_icon="💬")
st.title("💬 InterviewAI")

if "session_id" not in st.session_state:
    st.session_state.session_id = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "interview_complete" not in st.session_state:
    st.session_state.interview_complete = False

if st.session_state.session_id is None:
    st.subheader("Personal Information")
    name = st.text_input("Name", placeholder="Enter your name")
    experience = st.text_area("Experience", placeholder="Describe your experience")
    skills = st.text_area("Skills", placeholder="List your skills")

    st.subheader("Company and Position")
    col1, col2 = st.columns(2)

    with col1:
        level = st.radio("Level", ["Junior", "Mid-level", "Senior"])

    with col2:
        position = st.selectbox(
            "Position",
            ["Data Scientist", "Data Engineer", "ML Engineer", "BI Analyst", "Financial Analyst"]
        )

    company = st.selectbox(
        "Company",
        ["Amazon", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify"]
    )

    if st.button("Start Interview"):
        try:
            resp = requests.post(
                f"{API_BASE_URL}/start-interview",
                json={
                    "name": name,
                    "experience": experience,
                    "skills": skills,
                    "level": level,
                    "position": position,
                    "company": company
                },
                timeout=60
            )

            if resp.status_code != 200:
                st.error(f"Backend error: {resp.text}")
            else:
                data = resp.json()
                st.session_state.session_id = data["session_id"]
                st.session_state.messages = [
                    {"role": "assistant", "content": data["message"]}
                ]
                st.rerun()

        except Exception as e:
            st.error(f"Could not connect to backend: {e}")

elif not st.session_state.interview_complete:
    st.info("Start by introducing yourself", icon="👋")

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Your response"):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            with st.spinner("Thinking..."):
                resp = requests.post(
                    f"{API_BASE_URL}/chat/{st.session_state.session_id}",
                    json={"message": prompt},
                    timeout=60
                )

            if resp.status_code != 200:
                st.error(f"Backend error: {resp.text}")
            else:
                data = resp.json()

                if data.get("message"):
                    st.session_state.messages.append(
                        {"role": "assistant", "content": data["message"]}
                    )
                    with st.chat_message("assistant"):
                        st.markdown(data["message"])

                if data.get("interview_complete"):
                    st.session_state.interview_complete = True
                    st.rerun()

        except Exception as e:
            st.error(f"Could not connect to backend: {e}")

else:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if st.button("Get Feedback"):
        try:
            with st.spinner("Generating feedback..."):
                resp = requests.get(
                    f"{API_BASE_URL}/feedback/{st.session_state.session_id}",
                    timeout=60
                )

            if resp.status_code != 200:
                st.error(f"Backend error: {resp.text}")
            else:
                data = resp.json()
                st.subheader("📝 Interview Feedback")
                st.write(data["feedback"])

        except Exception as e:
            st.error(f"Could not get feedback: {e}")

    if st.button("Restart", type="primary"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()