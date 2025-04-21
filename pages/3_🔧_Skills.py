import streamlit as st

st.set_page_config(
    page_title="Skills | My Portfolio",
    page_icon="🔧",
    layout="wide",
)

# Custom CSS for React-like UI
st.markdown("""
<style>
.main .block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

.page-title {
    text-align: center;
    margin-bottom: 2rem;
    color: #333;
}

.skill-category {
    margin-bottom: 2rem;
}

.skill-category h2 {
    border-bottom: 2px solid #4CAF50;
    padding-bottom: 0.5rem;
    margin-bottom: 1rem;
}

.skill-card {
    background-color: white;
    border-radius: 10px;
    padding: 1.5rem;
    height: 100%;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

.skill-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
}

.skill-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.skill-name {
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.skill-level {
    width: 100%;
    background-color: #f0f0f0;
    border-radius: 10px;
    margin-top: 1rem;
}

.skill-progress {
    height: 10px;
    border-radius: 10px;
    background-color: #4CAF50;
}

.tools-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}

.tool-item {
    background-color: #f9f9f9;
    border-radius: 5px;
    padding: 0.5rem;
    text-align: center;
    font-size: 0.9rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# Page Header
st.markdown("<h1 class='page-title'>Skills & Expertise</h1>", unsafe_allow_html=True)

# Skills Overview
st.markdown("""
<div style="text-align: center; max-width: 800px; margin: 0 auto 2rem auto;">
    <p>I've developed a diverse set of technical skills throughout my career. Below is an overview of my expertise in various technologies, programming languages, and tools.</p>
</div>
""", unsafe_allow_html=True)

# Programming Languages
st.markdown("<div class='skill-category'><h2>Programming Languages</h2></div>", unsafe_allow_html=True)

languages = [
    {"name": "Python", "icon": "🐍", "level": 90, "description": "Expert in Python development with experience in web frameworks, data analysis, and automation."},
    {"name": "JavaScript", "icon": "📜", "level": 85, "description": "Proficient in modern JavaScript including ES6+ features, async/await, and functional programming."},
    {"name": "TypeScript", "icon": "📘", "level": 80, "description": "Strong TypeScript skills for building type-safe applications and improving code quality."},
    {"name": "Java", "icon": "☕", "level": 75, "description": "Experienced in Java development for enterprise applications and Android development."},
    {"name": "C#", "icon": "🔷", "level": 70, "description": "Skilled in C# for .NET applications and Unity game development."}
]

cols = st.columns(len(languages))
for i, lang in enumerate(languages):
    with cols[i]:
        st.markdown(f"""
        <div class="skill-card">
            <div class="skill-icon">{lang['icon']}</div>
            <div class="skill-name">{lang['name']}</div>
            <div>{lang['description']}</div>
            <div class="skill-level">
                <div class="skill-progress" style="width: {lang['level']}%;"></div>
            </div>
            <div style="margin-top: 0.5rem; font-size: 0.8rem;">{lang['level']}%</div>
        </div>
        """, unsafe_allow_html=True)

# Frontend Development
st.markdown("<div class='skill-category'><h2>Frontend Development</h2></div>", unsafe_allow_html=True)

frontend_skills = [
    {"name": "React", "icon": "⚛️", "level": 90},
    {"name": "HTML/CSS", "icon": "🌐", "level": 85},
    {"name": "Angular", "icon": "🅰️", "level": 75},
    {"name": "Vue.js", "icon": "🔰", "level": 70}
]

cols = st.columns(len(frontend_skills))
for i, skill in enumerate(frontend_skills):
    with cols[i]:
        st.markdown(f"""
        <div class="skill-card">
            <div class="skill-icon">{skill['icon']}</div>
            <div class="skill-name">{skill['name']}</div>
            <div class="skill-level">
                <div class="skill-progress" style="width: {skill['level']}%;"></div>
            </div>
            <div style="margin-top: 0.5rem; font-size: 0.8rem;">{skill['level']}%</div>
        </div>
        """, unsafe_allow_html=True)

# Frontend Tools
st.markdown("""
<div style="background-color: #f9f9f9; border-radius: 10px; padding: 1rem; margin-top: 1rem;">
    <h3 style="margin-bottom: 0.5rem;">Frontend Tools & Libraries</h3>
    <div class="tools-grid">
        <div class="tool-item">Redux</div>
        <div class="tool-item">Webpack</div>
        <div class="tool-item">Sass/SCSS</div>
        <div class="tool-item">Bootstrap</div>
        <div class="tool-item">Material UI</div>
        <div class="tool-item">Tailwind CSS</div>
        <div class="tool-item">Jest</div>
        <div class="tool-item">Cypress</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Backend Development
st.markdown("<div class='skill-category'><h2>Backend Development</h2></div>", unsafe_allow_html=True)

backend_skills = [
    {"name": "Node.js", "icon": "🟢", "level": 85},
    {"name": "Django", "icon": "🎸", "level": 80},
    {"name": "Flask", "icon": "🧪", "level": 85},
    {"name": "ASP.NET", "icon": "🔷", "level": 70}
]

cols = st.columns(len(backend_skills))
for i, skill in enumerate(backend_skills):
    with cols[i]:
        st.markdown(f"""
        <div class="skill-card">
            <div class="skill-icon">{skill['icon']}</div>
            <div class="skill-name">{skill['name']}</div>
            <div class="skill-level">
                <div class="skill-progress" style="width: {skill['level']}%;"></div>
            </div>
            <div style="margin-top: 0.5rem; font-size: 0.8rem;">{skill['level']}%</div>
        </div>
        """, unsafe_allow_html=True)

# Backend Tools
st.markdown("""
<div style="background-color: #f9f9f9; border-radius: 10px; padding: 1rem; margin-top: 1rem;">
    <h3 style="margin-bottom: 0.5rem;">Backend Tools & Technologies</h3>
    <div class="tools-grid">
        <div class="tool-item">Express.js</div>
        <div class="tool-item">GraphQL</div>
        <div class="tool-item">REST APIs</div>
        <div class="tool-item">MongoDB</div>
        <div class="tool-item">PostgreSQL</div>
        <div class="tool-item">MySQL</div>
        <div class="tool-item">Redis</div>
        <div class="tool-item">Docker</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Cloud & DevOps
st.markdown("<div class='skill-category'><h2>Cloud & DevOps</h2></div>", unsafe_allow_html=True)

devops_skills = [
    {"name": "AWS", "icon": "☁️", "level": 80},
    {"name": "Azure", "icon": "🔷", "level": 75},
    {"name": "CI/CD", "icon": "🔄", "level": 85},
    {"name": "Kubernetes", "icon": "🚢", "level": 70}
]

cols = st.columns(len(devops_skills))
for i, skill in enumerate(devops_skills):
    with cols[i]:
        st.markdown(f"""
        <div class="skill-card">
            <div class="skill-icon">{skill['icon']}</div>
            <div class="skill-name">{skill['name']}</div>
            <div class="skill-level">
                <div class="skill-progress" style="width: {skill['level']}%;"></div>
            </div>
            <div style="margin-top: 0.5rem; font-size: 0.8rem;">{skill['level']}%</div>
        </div>
        """, unsafe_allow_html=True)

# Other Skills
st.markdown("<div class='skill-category'><h2>Other Skills</h2></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="skill-card">
        <h3>Soft Skills</h3>
        <ul style="text-align: left;">
            <li>Team Leadership</li>
            <li>Project Management</li>
            <li>Problem Solving</li>
            <li>Communication</li>
            <li>Time Management</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="skill-card">
        <h3>Additional Technical Skills</h3>
        <ul style="text-align: left;">
            <li>UI/UX Design</li>
            <li>Data Analysis</li>
            <li>Machine Learning</li>
            <li>Mobile Development</li>
            <li>Version Control (Git)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)