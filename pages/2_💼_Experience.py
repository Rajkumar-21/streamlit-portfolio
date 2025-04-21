import streamlit as st

st.set_page_config(
    page_title="Experience | My Portfolio",
    page_icon="💼",
    layout="wide",
)

# Custom CSS for React-like UI
st.markdown("""
<style>
.main .block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

.experience-card {
    background-color: white;
    border-radius: 10px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}

.experience-card:hover {
    transform: translateY(-5px);
}

.experience-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 1rem;
    border-bottom: 1px solid #f0f0f0;
    padding-bottom: 0.5rem;
}

.company {
    font-weight: bold;
    color: #4CAF50;
}

.period {
    color: #666;
}

.role {
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.skills-tag {
    display: inline-block;
    background-color: #f0f0f0;
    border-radius: 15px;
    padding: 0.3rem 0.8rem;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
    font-size: 0.8rem;
}

.page-title {
    text-align: center;
    margin-bottom: 2rem;
    color: #333;
}
</style>
""", unsafe_allow_html=True)

# Page Header
st.markdown("<h1 class='page-title'>Professional Experience</h1>", unsafe_allow_html=True)

# Experience Data
experiences = [
    {
        "company": "Tech Innovations Inc.",
        "role": "Senior Software Developer",
        "period": "Jan 2021 - Present",
        "description": """
        • Led a team of 5 developers in building a cloud-based analytics platform
        • Implemented CI/CD pipelines using GitHub Actions and Docker
        • Reduced application load time by 40% through code optimization
        • Mentored junior developers and conducted code reviews
        """,
        "skills": ["React", "Python", "AWS", "Docker", "CI/CD"]
    },
    {
        "company": "Digital Solutions LLC",
        "role": "Full Stack Developer",
        "period": "Mar 2018 - Dec 2020",
        "description": """
        • Developed and maintained multiple web applications for clients in finance and healthcare
        • Created responsive UI designs using React and Material UI
        • Built RESTful APIs using Node.js and Express
        • Implemented database solutions with MongoDB and PostgreSQL
        """,
        "skills": ["JavaScript", "React", "Node.js", "MongoDB", "PostgreSQL"]
    },
    {
        "company": "WebTech Startup",
        "role": "Frontend Developer",
        "period": "Jun 2016 - Feb 2018",
        "description": """
        • Designed and implemented user interfaces for web applications
        • Collaborated with UX designers to create intuitive user experiences
        • Optimized applications for maximum speed and scalability
        • Participated in daily stand-ups and sprint planning meetings
        """,
        "skills": ["HTML/CSS", "JavaScript", "Angular", "Sass", "Git"]
    }
]

# Display Experience Cards
for exp in experiences:
    st.markdown(f"""
    <div class="experience-card">
        <div class="experience-header">
            <span class="company">{exp['company']}</span>
            <span class="period">{exp['period']}</span>
        </div>
        <div class="role">{exp['role']}</div>
        <div class="description">
            {exp['description']}
        </div>
        <div class="skills" style="margin-top: 1rem;">
            {''.join([f'<span class="skills-tag">{skill}</span>' for skill in exp['skills']])}
        </div>
    </div>
    """, unsafe_allow_html=True)

# Education Section
st.markdown("<h2 class='page-title' style='margin-top: 3rem;'>Education</h2>", unsafe_allow_html=True)

education = [
    {
        "institution": "University of Technology",
        "degree": "Master of Computer Science",
        "period": "2014 - 2016",
        "description": "Specialized in Software Engineering with focus on distributed systems and cloud computing."
    },
    {
        "institution": "State College",
        "degree": "Bachelor of Science in Computer Science",
        "period": "2010 - 2014",
        "description": "Graduated with honors. Participated in multiple hackathons and coding competitions."
    }
]

# Display Education Cards
for edu in education:
    st.markdown(f"""
    <div class="experience-card">
        <div class="experience-header">
            <span class="company">{edu['institution']}</span>
            <span class="period">{edu['period']}</span>
        </div>
        <div class="role">{edu['degree']}</div>
        <div class="description">
            {edu['description']}
        </div>
    </div>
    """, unsafe_allow_html=True)

# Certifications Section
st.markdown("<h2 class='page-title' style='margin-top: 3rem;'>Certifications</h2>", unsafe_allow_html=True)

certifications = [
    {"name": "AWS Certified Solutions Architect", "year": "2022"},
    {"name": "Google Cloud Professional Developer", "year": "2021"},
    {"name": "Microsoft Certified: Azure Developer Associate", "year": "2020"}
]

cert_cols = st.columns(len(certifications))
for i, cert in enumerate(certifications):
    with cert_cols[i]:
        st.markdown(f"""
        <div class="experience-card" style="text-align: center;">
            <div style="font-weight: bold; margin-bottom: 0.5rem;">{cert['name']}</div>
            <div style="color: #666;">Issued {cert['year']}</div>
        </div>
        """, unsafe_allow_html=True)