import streamlit as st
import requests

st.title("📄Quickly Tailor Your Resume")

st.set_page_config(
    page_title="Resume Updater",
    layout="wide",
    initial_sidebar_state="auto",
)

# Form
with st.form("Job Info"):
    Industry = st.text_input("Industry")
    Company_name = st.text_input("Company_name")
    Role = st.text_input('Role')
    Job_description = st.text_area("Job_description")
    Submitted = st.form_submit_button("Submit")

    if Submitted:
        with st.spinner():
            # Send input to n8n webhook
            response = requests.post(
                "http://localhost:5678/webhook-test/10043b4e-b551-49c7-9abf-e669fc29bcf6",
                json={"Industry": Industry, "Company_name": Company_name, "Role": Role,
                      "Job_description": Job_description}
            )
            # Show result
            if response.ok:
                result = response.json()

                col1, col2 = st.columns(2)
                # Render matched projects
                with col1:

                    st.subheader("🗝️ Important Keywords")
                    st.markdown(result.get("important_keywords", ""), unsafe_allow_html=True)

                    st.subheader("🎯 Matched Projects")
                    st.markdown(result.get("matched_projects", ""), unsafe_allow_html=True)

                    # Render updated bullet points table
                    st.subheader("✍️ Updated Bullet Points")
                    st.markdown(result.get("updated_bullet_points", ""), unsafe_allow_html=True)

                    # Render updated skill section
                    st.subheader("🛠️ Updated Skills Section")
                    st.markdown(result.get("updated_skill_section", ""), unsafe_allow_html=True)

                with col2:
                    st.subheader("📜Cover Letter")
                    st.markdown(result.get("cover_letter", ""), unsafe_allow_html=True)

            else:
                st.error("Something went wrong with n8n")

