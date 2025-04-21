import streamlit as st

# Resume data dictionary - this contains all the information from your resume
# You can expand this with more details as needed
RESUME_DATA = {
    "name": "Rajkumar R",
    "role": "DevOps Engineer",
    "experience": [
        {
            "company": "Ernst & Young",
            "role": "Senior Consultant",
            "period": "Nov/2022 - Present",
            "details": [
                "Designed and implemented robust Microsoft Azure infrastructure",
                "Automated deployment processes with Azure DevOps and PowerShell",
                "Implemented CI/CD pipelines for monitoring and reporting",
                "Developed PowerShell scripts for VM automation",
                "Worked with LLM applications using AzureOpenAI, Streamlit, Flask and Langchain",
                "Conducted security audits and vulnerability assessments",
                "Optimized network configurations"
            ]
        },
        {
            "company": "Epam Systems",
            "role": "System Engineer",
            "period": "August 2022 - October 2022",
            "details": [
                "Worked on Azure DevOps, CI/CD pipelines, and infrastructure as code",
                "Provided Tech talk sessions about Azure DevOps",
                "Involved in Azure infrastructure design and implementation"
            ]
        },
        {
            "company": "Tata Consultancy Services",
            "role": "System Engineer",
            "period": "May 2019 – August 2022",
            "details": [
                "Maintained Azure infrastructure and On-Prem data centers",
                "Automated alerts for infrastructure and applications",
                "Migrated on-premises infrastructure to Azure cloud",
                "Managed domain controllers, DNS, DHCP, and other services"
            ]
        }
    ],
    "skills": {
        "CI/CD": ["Azure DevOps", "GitHub Actions"],
        "Containers": ["Docker", "Kubernetes", "AKS"],
        "Scripting": ["PowerShell", "Python"],
        "IaC": ["Terraform", "Ansible", "Pulumi"],
        "Monitoring": ["Prometheus", "Grafana", "Azure Automation"],
        "Cloud": ["Azure", "AWS"],
        "Other": ["Linux", "Networking", "AI/ML", "LLM applications"]
    },
    "projects": [
        "Flet Counter App - Deployed using Github Action",
        "Powershell Script for Automation",
        "Streamlit - URL Shortner & deployed in HuggingFace",
        "Deployed .Net application in Azure WebAPP using Github Action",
        "Azure pipeline repo to understand YAML basics"
    ],
    "certifications": [
        "Terraform Associate Certification",
        "AWS DevOps Certification - DOP-C02",
        "Microsoft certified Devops Engineer - AZ400",
        "Azure Architect Technology",
        "Microsoft Certified Azure Administrator Associate",
        "Microsoft Azure Fundamentals Certification",
        "Microsoft Azure AI Fundamental - AI900"
    ],
    "achievements": [
        "On-the-spot award for dedication at TCS",
        "User Recognition Award at EY in 2023 and 2024",
        "Automated application/VM deployments",
        "Optimized infrastructure through scripting"
    ]
}

def get_response(prompt):
    """
    Generate a response based on the user's prompt about the resume
    """
    prompt_lower = prompt.lower()
    
    # Check for different types of queries
    if any(word in prompt_lower for word in ["hello", "hi", "hey", "greetings"]):
        return "Hello! I'm Raj's AI assistant. How can I help you learn more about his experience and skills?"
    
    # Experience related queries
    elif any(word in prompt_lower for word in ["experience", "work", "job", "career", "company"]):
        if "ey" in prompt_lower or "ernst" in prompt_lower or "young" in prompt_lower:
            exp = next((e for e in RESUME_DATA["experience"] if e["company"] == "Ernst & Young"), None)
            return f"At {exp['company']} ({exp['period']}), Raj works as a {exp['role']}. His responsibilities include:\n- " + "\n- ".join(exp["details"])
        
        elif "epam" in prompt_lower:
            exp = next((e for e in RESUME_DATA["experience"] if e["company"] == "Epam Systems"), None)
            return f"At {exp['company']} ({exp['period']}), Raj worked as a {exp['role']}. His responsibilities included:\n- " + "\n- ".join(exp["details"])
        
        elif "tcs" in prompt_lower or "tata" in prompt_lower:
            exp = next((e for e in RESUME_DATA["experience"] if e["company"] == "Tata Consultancy Services"), None)
            return f"At {exp['company']} ({exp['period']}), Raj worked as a {exp['role']}. His responsibilities included:\n- " + "\n- ".join(exp["details"])
        
        else:
            return f"Raj has over 5 years of experience as a DevOps Engineer, working at:\n\n1. Ernst & Young (Senior Consultant, Nov/2022 - Present)\n2. Epam Systems (System Engineer, Aug 2022 - Oct 2022)\n3. Tata Consultancy Services (System Engineer, May 2019 - Aug 2022)\n\nAsk about a specific company for more details!"
    
    # Skills related queries
    elif any(word in prompt_lower for word in ["skill", "technology", "tech", "know", "expertise"]):
        if "azure" in prompt_lower or "cloud" in prompt_lower:
            return "Raj has extensive experience with Azure cloud services, including:\n- Azure DevOps for CI/CD pipelines\n- Azure Kubernetes Service (AKS)\n- Azure Infrastructure as a Service (IaaS)\n- Azure Automation for VM management\n\nHe holds multiple Azure certifications including AZ-400 (DevOps Engineer) and Azure Administrator Associate."
        
        elif "devops" in prompt_lower or "ci/cd" in prompt_lower or "pipeline" in prompt_lower:
            return "Raj is skilled in DevOps practices and tools including:\n- Azure DevOps for CI/CD pipelines\n- GitHub Actions for workflow automation\n- Infrastructure as Code using Terraform, Ansible, and Pulumi\n- Container orchestration with Docker and Kubernetes"
        
        elif "container" in prompt_lower or "docker" in prompt_lower or "kubernetes" in prompt_lower:
            return "Raj is proficient with containerization technologies:\n- Docker for creating and managing application containers\n- Kubernetes for container orchestration\n- Experience with AKS (Azure Kubernetes Service)\n- Understanding of Pods, Replica Sets, Deployments, and Services"
        
        elif "script" in prompt_lower or "automation" in prompt_lower or "powershell" in prompt_lower or "python" in prompt_lower:
            return "Raj is skilled in automation and scripting:\n- PowerShell for Windows automation tasks\n- Python for various DevOps tasks\n- Automated VM management based on idle time\n- Created scripts for infrastructure reporting and optimization"
        
        else:
            skills_list = []
            for category, items in RESUME_DATA["skills"].items():
                skills_list.append(f"- {category}: {', '.join(items)}")
            
            return "Raj has a diverse set of technical skills:\n" + "\n".join(skills_list)
    
    # Projects related queries
    elif any(word in prompt_lower for word in ["project", "portfolio", "build", "develop"]):
        return "Raj has worked on several projects including:\n- " + "\n- ".join(RESUME_DATA["projects"]) + "\n\nYou can find these projects on his GitHub profile."
    
    # Certifications related queries
    elif any(word in prompt_lower for word in ["certification", "certificate", "certified", "exam"]):
        return "Raj holds several professional certifications:\n- " + "\n- ".join(RESUME_DATA["certifications"])
    
    # Achievements related queries
    elif any(word in prompt_lower for word in ["achievement", "award", "recognition", "accomplish"]):
        return "Raj's professional achievements include:\n- " + "\n- ".join(RESUME_DATA["achievements"])
    
    # General information
    elif any(word in prompt_lower for word in ["about", "who", "summary", "overview"]):
        return f"{RESUME_DATA['name']} is an experienced {RESUME_DATA['role']} with 5+ years in automating and optimizing cloud infrastructure and deployment strategies. He has expertise in Azure DevOps, CI/CD pipelines, container orchestration, and infrastructure automation. He's currently working as a Senior Consultant at Ernst & Young."
    
    # Default response for unrecognized queries
    else:
        return "I'm not sure I understand your question. You can ask about Raj's experience, skills, projects, certifications, or achievements. How can I help you learn more about Raj's professional background?"

# For testing the chatbot directly
if __name__ == "__main__":
    test_prompts = [
        "Tell me about Raj's experience",
        "What skills does Raj have?",
        "What projects has Raj worked on?",
        "What certifications does Raj have?",
        "What are Raj's achievements?"
    ]
    
    for prompt in test_prompts:
        print(f"Q: {prompt}")
        print(f"A: {get_response(prompt)}")
        print()