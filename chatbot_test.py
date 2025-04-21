import streamlit as st

# Resume data dictionary - this contains information about the portfolio owner
PORTFOLIO_DATA = {
    "name": "John Doe",
    "role": "Full Stack Developer & UI/UX Designer",
    "experience": [
        {
            "company": "Tech Innovations Inc.",
            "role": "Senior Software Developer",
            "period": "Jan 2021 - Present",
            "details": [
                "Led a team of 5 developers in building a cloud-based analytics platform",
                "Implemented CI/CD pipelines using GitHub Actions and Docker",
                "Reduced application load time by 40% through code optimization",
                "Mentored junior developers and conducted code reviews"
            ]
        },
        {
            "company": "Digital Solutions LLC",
            "role": "Full Stack Developer",
            "period": "Mar 2018 - Dec 2020",
            "details": [
                "Developed and maintained multiple web applications for clients in finance and healthcare",
                "Created responsive UI designs using React and Material UI",
                "Built RESTful APIs using Node.js and Express",
                "Implemented database solutions with MongoDB and PostgreSQL"
            ]
        }
    ],
    "skills": {
        "Frontend": ["React", "Angular", "HTML/CSS", "JavaScript", "TypeScript"],
        "Backend": ["Node.js", "Python", "Django", "Flask", "Express"],
        "Database": ["MongoDB", "PostgreSQL", "MySQL", "Redis"],
        "DevOps": ["Docker", "Kubernetes", "AWS", "CI/CD", "Git"]
    },
    "projects": [
        "E-Commerce Platform",
        "Task Management App",
        "Customer Sentiment Analysis",
        "Portfolio Website",
        "Fitness Tracker",
        "Stock Price Predictor"
    ],
    "education": [
        {
            "institution": "University of Technology",
            "degree": "Master of Computer Science",
            "period": "2014 - 2016"
        },
        {
            "institution": "State College",
            "degree": "Bachelor of Science in Computer Science",
            "period": "2010 - 2014"
        }
    ]
}

def get_response(prompt):
    """
    Generate a response based on the user's prompt about the portfolio
    """
    prompt_lower = prompt.lower()
    
    # Check for different types of queries
    if any(word in prompt_lower for word in ["hello", "hi", "hey", "greetings"]):
        return f"Hello! I'm {PORTFOLIO_DATA['name']}'s AI assistant. How can I help you learn more about their experience and skills?"
    
    # Experience related queries
    elif any(word in prompt_lower for word in ["experience", "work", "job", "career", "company"]):
        experience_text = f"{PORTFOLIO_DATA['name']} has worked at:\n\n"
        for exp in PORTFOLIO_DATA["experience"]:
            experience_text += f"• {exp['company']} as {exp['role']} ({exp['period']})\n"
        return experience_text
    
    # Skills related queries
    elif any(word in prompt_lower for word in ["skill", "technology", "tech", "know", "expertise"]):
        skills_text = f"{PORTFOLIO_DATA['name']}'s skills include:\n\n"
        for category, skills in PORTFOLIO_DATA["skills"].items():
            skills_text += f"• {category}: {', '.join(skills)}\n"
        return skills_text
    
    # Projects related queries
    elif any(word in prompt_lower for word in ["project", "portfolio", "build", "develop"]):
        projects_text = f"{PORTFOLIO_DATA['name']}'s projects include:\n\n"
        for project in PORTFOLIO_DATA["projects"]:
            projects_text += f"• {project}\n"
        return projects_text
    
    # Education related queries
    elif any(word in prompt_lower for word in ["education", "university", "college", "degree", "study"]):
        education_text = f"{PORTFOLIO_DATA['name']}'s education:\n\n"
        for edu in PORTFOLIO_DATA["education"]:
            education_text += f"• {edu['degree']} from {edu['institution']} ({edu['period']})\n"
        return education_text
    
    # General information
    elif any(word in prompt_lower for word in ["about", "who", "summary", "overview"]):
        return f"{PORTFOLIO_DATA['name']} is a {PORTFOLIO_DATA['role']} with experience at {PORTFOLIO_DATA['experience'][0]['company']} and {PORTFOLIO_DATA['experience'][1]['company']}. They specialize in {', '.join(PORTFOLIO_DATA['skills']['Frontend'][:2])} for frontend and {', '.join(PORTFOLIO_DATA['skills']['Backend'][:2])} for backend development."
    
    # Default response for unrecognized queries
    else:
        return f"I'm not sure I understand your question. You can ask about {PORTFOLIO_DATA['name']}'s experience, skills, projects, or education. How can I help you learn more about their professional background?"

# For testing the chatbot directly
if __name__ == "__main__":
    test_prompts = [
        "Tell me about your experience",
        "What skills do you have?",
        "What projects have you worked on?",
        "Where did you study?"
    ]
    
    for prompt in test_prompts:
        print(f"Q: {prompt}")
        print(f"A: {get_response(prompt)}")
        print()