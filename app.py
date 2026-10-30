import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Harvey A. Ortega | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
    <style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 700;
        color: #1E88E5;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #555555;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR & NAVIGATION ---
with st.sidebar:
    st.image("arvs.jpg", caption="Harvey A. Ortega", use_container_width=True)
    st.title("Navigation")
    section = st.radio(
        "Go to section:",
        ["About & Bio", "Skills & Metrics", "Projects", "Interactive Hub & Feedback"]
    )
    
    st.divider()
    st.subheader("Student Info")
    st.write("**Name:** Harvey A. Ortega")
    st.write("**Course & Year:** BSIT - 4th Year")
    st.write("**Subject & Section:** APPLIED AI CSIT342 - G5")
    
    st.divider()
    show_contact_quick = st.checkbox("Show Direct Contact Info", value=True)
    if show_contact_quick:
        st.caption("📧 ortegaharvey013@gmail.com")
        st.caption("📱 +63 931 012 2176")
        st.caption("📍 Cebu, Philippines")

# --- HEADER SECTION ---
st.markdown('<p class="main-title">Harvey A. Ortega</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">BSIT Student | Aspiring Cybersecurity & Systems Specialist | Cebu Institute of Technology - University</p>', unsafe_allow_html=True)
st.divider()

# --- SECTION 1: ABOUT & BIO ---
if section == "About & Bio":
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("arvs.jpg", caption="Harvey A. Ortega", width=250)
        
    with col2:
        st.subheader("👋 About Me")
        st.write("""
        I am a motivated Bachelor of Science in Information Technology student at Cebu Institute of Technology - University. 
        My technical background spans full-stack development, database-driven systems, and hands-on hardware/network support. 
        I am particularly passionate about advancing into **cybersecurity**, focusing on network security, system administration, 
        secure software design, and data protection.
        """)
        
        # Download Resume Button
        resume_data = """HARVEY A. ORTEGA
Cebu, Philippines | +63 931 012 2176 | ortegaharvey013@gmail.com
BSIT Student - Cebu Institute of Technology - University
Target Role: Cybersecurity / Systems / Entry-Level IT"""
        
        st.download_button(
            label="📄 Download Summary Resume",
            data=resume_data,
            file_name="Harvey_Ortega_Resume.txt",
            mime="text/plain"
        )

    st.divider()
    
    st.subheader("📖 Autobiography & Milestones")
    
    tab1, tab2, tab3 = st.tabs(["Educational Background", "Interests & Career Goals", "Milestones"])
    
    with tab1:
        st.markdown("""
        * **University:** Cebu Institute of Technology - University (CIT-U)
        * **Degree:** Bachelor of Science in Information Technology (BSIT)
        * **Expected Graduation:** 2027
        * **Core Competencies:** Web & Mobile Development, Database Management, Network Troubleshooting, and Systems Administration.
        """)
        
    with tab2:
        st.markdown("""
        * **Primary Focus:** Expanding knowledge in Network Security, Windows Server, Active Directory, and System Hardening.
        * **Interests:** Cybersecurity defense strategies, REST API integrations, IT infrastructure maintenance, and community tech initiatives.
        * **Soft Skills:** Problem-solving, team collaboration, analytical thinking, and high attention to detail.
        """)
        
    with tab3:
        st.markdown("""
        * 🏅 **2026:** Awarded Certificate of Participation at the **PSITE 2026 Cebu ICT Student Congress**.
        * 🚀 **2025 - 2026:** Designed and deployed Android, web, and backend applications (**DugoSugbo**, **ALLY**, and **SideL**).
        * 💻 **Ongoing:** Building hands-on experience in PC/laptop troubleshooting, hardware diagnostics, and Active Directory administration.
        """)

# --- SECTION 2: SKILLS & METRICS ---
elif section == "Skills & Metrics":
    st.subheader("📊 Skill Proficiency & Metrics")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Core Projects", value="3", delta="Completed")
    m2.metric(label="Target Degree", value="BSIT", delta="4th Year")
    m3.metric(label="Primary Field", value="Cybersecurity", delta="Focus Area")
    m4.metric(label="Expected Grad", value="2027", delta="On Track")
    
    st.divider()
    
    col_chart, col_table = st.columns([3, 2])
    
    skills_data = {
        "Skill Category": [
            "Hardware & Network Support",
            "Java / Spring Boot",
            "Kotlin / Android",
            "ReactJS / Web UI",
            "MySQL & Database",
            "Git / GitHub Workflow",
            "Windows Server & AD"
        ],
        "Proficiency Level (%)": [88, 85, 80, 78, 82, 85, 75]
    }
    
    df_skills = pd.DataFrame(skills_data)
    
    with col_chart:
        st.write("##### Technical Competency Chart")
        st.bar_chart(df_skills.set_index("Skill Category"))
        
    with col_table:
        st.write("##### Detailed Breakdown")
        st.dataframe(df_skills, hide_index=True, use_container_width=True)

# --- SECTION 3: PROJECTS ---
elif section == "Projects":
    st.subheader("💻 Featured Projects")
    
    filter_tool = st.multiselect(
        "Filter projects by technology stack:",
        options=["Kotlin / Android", "Spring Boot", "ReactJS", "MySQL", "AI / Python"],
        default=["Kotlin / Android", "Spring Boot", "ReactJS", "MySQL"]
    )
    
    st.write("")
    
    # Project 1: DugoSugbo
    with st.expander("🩸 DugoSugbo – Blood Stock Management System", expanded=True):
        st.write("**Role:** Lead Application Developer (Individual Academic Project)")
        st.write("**Tools Used:** Kotlin, Spring Boot, ReactJS, MySQL, REST APIs, HttpSession (JSESSIONID)")
        st.markdown("""
        * Developed an Android mobile application using Kotlin for real-time blood stock monitoring and inventory tracking.
        * Integrated a Spring Boot backend, ReactJS web application, and MySQL database to facilitate centralized data exchange.
        * Designed system features for tracking blood availability across local government health clinics and regional hospitals.
        * Implemented secure REST API endpoints with session-based authentication using `HttpSession` and `JSESSIONID`.
        """)

    # Project 2: ALLY
    with st.expander("🤖 ALLY – AI-Powered Legal Assistant", expanded=True):
        st.write("**Role:** Lead Backend & Systems Developer")
        st.write("**Tools Used:** AI / Legal-Source Retrieval, REST APIs, Python/Java")
        st.markdown("""
        * Developed to help users access understandable legal information more easily using artificial intelligence.
        * Integrated legal-source retrieval with controlled response generation to minimize inaccuracies.
        """)
    
    # Project 3: SideL
    with st.expander("🛠️ SideL – Smart On-Demand Service & Sideline Platform", expanded=True):
        st.write("**Role:** Full-Stack Developer")
        st.write("**Tools Used:** Java, Spring Boot, React, Kotlin, MySQL")
        st.markdown("""
        * Created an on-demand service booking platform connecting customers with local skilled service providers.
        * Designed to open additional income opportunities for individuals offering sideline services.
        """)

# --- SECTION 4: INTERACTIVE HUB & FEEDBACK ---
elif section == "Interactive Hub & Feedback":
    st.subheader("💬 Contact & Interactive Feedback Form")
    
    st.write("##### Rate your experience visiting this portfolio:")
    rating = st.slider("Select Rating (1 to 10)", min_value=1, max_value=10, value=10)
    category = st.selectbox("What brought you here today?", ["Recruitment / Internship", "Academic Evaluation", "General Interest", "Other"])
    
    with st.form(key="contact_form"):
        st.write("##### Send a Message")
        user_name = st.text_input("Your Name:")
        user_email = st.text_input("Your Email:")
        user_message = st.text_area("Your Message / Feedback:")
        
        submitted = st.form_submit_button("Submit Feedback")
        
        if submitted:
            if user_name and user_email and user_message:
                st.success(f"Thank you, {user_name}! Your message has been received.")
                st.info(f"Summary of submission:\n* Category: {category}\n* Rating Given: {rating}/10")
            else:
                st.error("Please fill in all input fields before submitting.")

# Footer
st.divider()
st.caption("APPLIED AI CSIT342 - G5 | Harvey A. Ortega Portfolio App © 2026")
