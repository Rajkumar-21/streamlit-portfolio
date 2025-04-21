import streamlit as st

st.set_page_config(
    page_title="Home | My Portfolio",
    page_icon="🏠",
    layout="wide",
)

# Custom CSS for React-like UI
st.markdown("""
<style>
.main .block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

.hero-section {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 2rem 0;
}

.hero-section img {
    border-radius: 50%;
    width: 200px;
    height: 200px;
    object-fit: cover;
    margin-bottom: 1rem;
    border: 5px solid #f0f0f0;
}

.hero-section h1 {
    margin-bottom: 0.5rem;
}

.hero-section p {
    color: #666;
    max-width: 600px;
    margin: 0 auto;
}

.card {
    background-color: white;
    border-radius: 10px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <img src="https://via.placeholder.com/200" alt="Profile Picture">
    <h1>John Doe</h1>
    <p>Full Stack Developer & UI/UX Designer</p>
</div>
""", unsafe_allow_html=True)

# About Me Section
st.markdown("<h2 style='text-align: center; margin-top: 2rem;'>About Me</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>Who I Am</h3>
        <p>I'm a passionate developer with 5+ years of experience in creating web applications and designing user interfaces. I love solving complex problems and turning ideas into reality through code.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>What I Do</h3>
        <p>I specialize in full-stack development using modern technologies like React, Python, and cloud services. I'm also experienced in UI/UX design, ensuring that applications are not only functional but also intuitive and visually appealing.</p>
    </div>
    """, unsafe_allow_html=True)

# Featured Projects
st.markdown("<h2 style='text-align: center; margin-top: 2rem;'>Featured Projects</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>Project 1</h3>
        <p>A brief description of project 1 and the technologies used.</p>
        <a href="/Projects">View Details</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>Project 2</h3>
        <p>A brief description of project 2 and the technologies used.</p>
        <a href="/Projects">View Details</a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>Project 3</h3>
        <p>A brief description of project 3 and the technologies used.</p>
        <a href="/Projects">View Details</a>
    </div>
    """, unsafe_allow_html=True)