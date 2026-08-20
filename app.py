import streamlit as st

# 1. Page Setup
st.set_page_config(page_title="Skill Gap Analyzer", layout="centered")
st.title("🎯 Skill Gap Analyzer")
st.write("Compare your skills against role requirements to see what you should learn next.")

# 2. Mock Database for Role Requirements
ROLES_DB = {
    "Machine Learning Engineer": {
        "Must-Have": ["python", "sql", "machine learning", "statistics", "scikit-learn"],
        "Nice-to-Have": ["deep learning", "docker", "mlops", "aws"]
    },
    "Software Engineer": {
        "Must-Have": ["python", "java", "data structures", "algorithms", "sql"],
        "Nice-to-Have": ["git", "docker", "agile", "system design"]
    },
    "Data Analyst": {
        "Must-Have": ["sql", "excel", "python", "data visualization", "statistics"],
        "Nice-to-Have": ["tableau", "power bi", "business logic"]
    }
}

# 3. User Input Section
st.header("1. Candidate Profile")
selected_role = st.selectbox("Select Target Role:", list(ROLES_DB.keys()))
user_skills_input = st.text_input("Enter your skills (comma-separated, e.g.: Python, SQL, Java):")

# 4. Processing Button
if st.button("Analyze My Skills"):
    if user_skills_input:
        # Clean user input: make it lowercase and remove extra spaces
        user_skills = [skill.strip().lower() for skill in user_skills_input.split(",")]
        user_skills_set = set(user_skills)
        
        # Get role requirements
        role_reqs = ROLES_DB[selected_role]
        must_have_set = set(role_reqs["Must-Have"])
        nice_to_have_set = set(role_reqs["Nice-to-Have"])
        
        # Gap Analysis Math using Python Sets
        missing_must_have = must_have_set.difference(user_skills_set)
        missing_nice_to_have = nice_to_have_set.difference(user_skills_set)
        matched_skills = user_skills_set.intersection(must_have_set.union(nice_to_have_set))
        
        # 5. Dashboard Output
        st.header("📊 Role-Specific Gap Report")
        
        # Calculate Readiness Score
        total_core = len(must_have_set)
        score = ((total_core - len(missing_must_have)) / total_core) * 100
        st.metric(label="Core Readiness Score", value=f"{score:.0f}%")
        
        st.subheader("✅ Matched Skills")
        if matched_skills:
            st.success(", ".join([skill.title() for skill in matched_skills]))
        else:
            st.write("No matching skills found yet.")
            
        st.subheader("🚨 High Priority Missing Skills (Core)")
        if missing_must_have:
            for skill in missing_must_have:
                st.error(skill.title())  # Red color for missing core skills
        else:
            st.success("You have all the core skills!")
            
        st.subheader("💡 Medium Priority Missing Skills (Bonus)")
        if missing_nice_to_have:
            for skill in missing_nice_to_have:
                st.warning(skill.title()) # Yellow color for nice-to-have
        else:
            st.success("You have all the bonus skills!")
            
    else:
        st.warning("Please enter your skills before analyzing.")