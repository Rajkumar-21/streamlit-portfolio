import streamlit as st

st.set_page_config(
    page_title="Projects | My Portfolio",
    page_icon="🚀",
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

.project-card {
    background-color: white;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    height: 100%;
    display: flex;
    flex-direction: column;
}

.project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
}

.project-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.project-content {
    padding: 1.5rem;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
}

.project-title {
    font-size: 1.25rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
    color: #333;
}

.project-description {
    color: #666;
    margin-bottom: 1rem;
    flex-grow: 1;
}

.project-tags {
    display: flex;
    flex-wrap: wrap;
    margin-bottom: 1rem;
}

.project-tag {
    background-color: #f0f0f0;
    border-radius: 15px;
    padding: 0.3rem 0.8rem;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
    font-size: 0.8rem;
}

.project-links {
    display: flex;
    justify-content: space-between;
}

.project-link {
    display: inline-block;
    padding: 0.5rem 1rem;
    background-color: #4CAF50;
    color: white;
    text-decoration: none;
    border-radius: 5px;
    font-weight: bold;
    text-align: center;
    transition: background-color 0.3s ease;
}

.project-link:hover {
    background-color: #45a049;
}

.project-link.secondary {
    background-color: #f0f0f0;
    color: #333;
}

.project-link.secondary:hover {
    background-color: #e0e0e0;
}

.filter-container {
    display: flex;
    justify-content: center;
    margin-bottom: 2rem;
    flex-wrap: wrap;
}

.filter-button {
    background-color: #f0f0f0;
    border: none;
    padding: 0.5rem 1rem;
    margin: 0 0.5rem 0.5rem 0;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.filter-button:hover, .filter-button.active {
    background-color: #4CAF50;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Page Header
st.markdown("<h1 class='page-title'>My Projects</h1>", unsafe_allow_html=True)

# Project Filter Buttons
st.markdown("""
<div class="filter-container">
    <button class="filter-button active" onclick="filterProjects('all')">All</button>
    <button class="filter-button" onclick="filterProjects('web')">Web Development</button>
    <button class="filter-button" onclick="filterProjects('mobile')">Mobile Apps</button>
    <button class="filter-button" onclick="filterProjects('data')">Data Science</button>
</div>

<script>
function filterProjects(category) {
    // Reset all buttons
    document.querySelectorAll('.filter-button').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Activate clicked button
    document.querySelector(`.filter-button[onclick="filterProjects('${category}')"]`).classList.add('active');
    
    // Show all projects initially
    document.querySelectorAll('.project-container').forEach(project => {
        project.style.display = 'block';
    });
    
    // If not "all", hide non-matching projects
    if (category !== 'all') {
        document.querySelectorAll('.project-container').forEach(project => {
            if (!project.classList.contains(category)) {
                project.style.display = 'none';
            }
        });
    }
}
</script>
""", unsafe_allow_html=True)

# Projects Data
projects = [
    {
        "title": "E-Commerce Platform",
        "image": "https://via.placeholder.com/800x400",
        "description": "A full-featured e-commerce platform with product management, shopping cart, and payment processing capabilities.",
        "tags": ["React", "Node.js", "MongoDB", "Stripe"],
        "demo_link": "#",
        "github_link": "#",
        "category": "web"
    },
    {
        "title": "Task Management App",
        "image": "https://via.placeholder.com/800x400",
        "description": "A mobile application for managing tasks and projects with team collaboration features.",
        "tags": ["React Native", "Firebase", "Redux"],
        "demo_link": "#",
        "github_link": "#",
        "category": "mobile"
    },
    {
        "title": "Customer Sentiment Analysis",
        "image": "https://via.placeholder.com/800x400",
        "description": "A machine learning model that analyzes customer reviews to determine sentiment and extract key insights.",
        "tags": ["Python", "NLP", "Scikit-learn", "Streamlit"],
        "demo_link": "#",
        "github_link": "#",
        "category": "data"
    },
    {
        "title": "Portfolio Website",
        "image": "https://via.placeholder.com/800x400",
        "description": "A responsive portfolio website built with Streamlit to showcase projects and skills.",
        "tags": ["Python", "Streamlit", "HTML/CSS"],
        "demo_link": "#",
        "github_link": "#",
        "category": "web"
    },
    {
        "title": "Fitness Tracker",
        "image": "https://via.placeholder.com/800x400",
        "description": "A mobile app that tracks workouts, nutrition, and provides personalized fitness recommendations.",
        "tags": ["Flutter", "Firebase", "Google Fit API"],
        "demo_link": "#",
        "github_link": "#",
        "category": "mobile"
    },
    {
        "title": "Stock Price Predictor",
        "image": "https://via.placeholder.com/800x400",
        "description": "A time series analysis tool that predicts stock prices based on historical data and market trends.",
        "tags": ["Python", "Pandas", "TensorFlow", "Plotly"],
        "demo_link": "#",
        "github_link": "#",
        "category": "data"
    }
]

# Display Projects in Grid
for i in range(0, len(projects), 3):  # Display 3 projects per row
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(projects):
            project = projects[i + j]
            with cols[j]:
                st.markdown(f"""
                <div class="project-container {project['category']}">
                    <div class="project-card">
                        <img src="{project['image']}" alt="{project['title']}" class="project-image">
                        <div class="project-content">
                            <div class="project-title">{project['title']}</div>
                            <div class="project-description">{project['description']}</div>
                            <div class="project-tags">
                                {''.join([f'<span class="project-tag">{tag}</span>' for tag in project['tags']])}
                            </div>
                            <div class="project-links">
                                <a href="{project['demo_link']}" target="_blank" class="project-link">Live Demo</a>
                                <a href="{project['github_link']}" target="_blank" class="project-link secondary">GitHub</a>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# Featured Project Section
st.markdown("<h2 style='text-align: center; margin-top: 3rem;'>Featured Project</h2>", unsafe_allow_html=True)

featured_project = {
    "title": "AI-Powered Content Generator",
    "image": "https://via.placeholder.com/1200x600",
    "description": """
    This is a comprehensive AI-powered content generation platform that helps content creators, marketers, and businesses create high-quality content efficiently.
    
    Key features include:
    • Automated blog post generation based on keywords and topics
    • Social media content creation with customizable templates
    • SEO optimization suggestions for all generated content
    • Multi-language support for global content creation
    
    The application uses advanced natural language processing techniques and was built with a microservices architecture for scalability.
    """,
    "tags": ["Python", "TensorFlow", "NLP", "React", "Docker", "AWS"],
    "demo_link": "#",
    "github_link": "#",
    "case_study_link": "#"
}

st.markdown(f"""
<div style="background-color: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-top: 1rem;">
    <img src="{featured_project['image']}" alt="{featured_project['title']}" style="width: 100%; height: 400px; object-fit: cover;">
    <div style="padding: 2rem;">
        <h3 style="margin-bottom: 1rem;">{featured_project['title']}</h3>
        <div style="white-space: pre-line; margin-bottom: 1.5rem;">{featured_project['description']}</div>
        <div class="project-tags" style="margin-bottom: 1.5rem;">
            {''.join([f'<span class="project-tag">{tag}</span>' for tag in featured_project['tags']])}
        </div>
        <div style="display: flex; gap: 1rem;">
            <a href="{featured_project['demo_link']}" target="_blank" class="project-link">Live Demo</a>
            <a href="{featured_project['github_link']}" target="_blank" class="project-link secondary">GitHub</a>
            <a href="{featured_project['case_study_link']}" target="_blank" class="project-link secondary">Case Study</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
# Call to Action
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding: 2rem; background-color: #f9f9f9; border-radius: 10px;">
    <h3>Interested in collaborating on a project?</h3>
    <p style="max-width: 600px; margin: 1rem auto;">I'm always open to discussing new projects, creative ideas, or opportunities to be part of your vision. Let's create something amazing together!</p>
    <a href="/Contact" style="display: inline-block; padding: 0.75rem 1.5rem; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 5px; font-weight: bold; margin-top: 1rem; transition: background-color 0.3s ease;">Get in Touch</a>
</div>
""", unsafe_allow_html=True)

# GitHub Activity
st.markdown("<h2 style='text-align: center; margin-top: 3rem;'>GitHub Activity</h2>", unsafe_allow_html=True)

st.markdown("""
<div style="background-color: white; border-radius: 10px; padding: 1.5rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <p style="text-align: center; margin-bottom: 1rem;">Check out my contributions and activity on GitHub</p>
    <div style="display: flex; justify-content: center;">
        <img src="https://github-readme-stats.vercel.app/api?username=yourusername&show_icons=true&theme=vue" style="max-width: 100%; height: auto; margin-right: 1rem;">
        <img src="https://github-readme-streak-stats.herokuapp.com/?user=yourusername&theme=vue" style="max-width: 100%; height: auto;">
    </div>
</div>
""", unsafe_allow_html=True)

# Add JavaScript for filtering functionality
st.markdown("""
<script>
// Initial filter to show all projects
window.onload = function() {
    filterProjects('all');
}
</script>
""", unsafe_allow_html=True)