import streamlit as st
from pathlib import Path
from PIL import Image


# --- Path Setting

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Rajkumar-Resume.pdf"
profile_pic = current_dir / "assets" / "picofme.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Rajkumar | Resume"
PAGE_ICON = ":wave:"
NAME = "Rajkumar R"
DESCRIPTION = """
Experienced DevOps Engineer in automating and optimizing infrastructure, driving operational excellence through Azure tools.
"""
EMAIL = "rajkumar218.r@gmail.com"
SOCIAL_MEDIA = {
    "Instagram": "https://www.instagram.com/im.rajkumar_21/",
    "LinkedIn": "https://www.linkedin.com/in/rajkumarravi218/",
    "GitHub": "https://github.com/Rajkumar-21",
}
PROJECTS = {
    "🏆 Flet Counter App - Deployed using Github Action": "https://github.com/Rajkumar-21/flet-counter-app",
    "🏆 Powershell Script for Automation": "https://github.com/Rajkumar-21/PowerShell-Scripts",
    "🏆 Streamlit - URL Shortner & deployed in HuggingFace": "https://github.com/Rajkumar-21/streamlit-urlshortner",
    "🏆 Worked in deploying application with DevSecOps enabled": "https://github.com/rajkumar-r-org/apps-ci-cd",
    "🏆 Azure MCP Server - For GenAI application this azure mcp server will help to interact with our private MCP server":"https://github.com/Rajkumar-21/azure-mcp-server",
    "🏆 GitHub to Markdown - This will make any GitHub repo into markdown will helps giving context to LLM for helping in developing reference for the developments":"https://github.com/Rajkumar-21/Github2Markdown",
    "🏆 MCP Sample - This Repo contains sample about MCP concepts for personal learning and learning new AI concepts":"https://github.com/Rajkumar-21/mcp-samples",
    "🏆 Google Books Search - This projects uses Google Books API and using FastAPI as backend and React as frontend able to search any books available in google API and show in frontend react application":"https://github.com/Rajkumar-21/google-books-react-fastapi-app",
    "🏆 PowerShell Script - This Repo contains all PowerShell scripts using for devops engineer to working with cloud and regular activities by automating the process":"https://github.com/Rajkumar-21/PowerShell-Scripts",
    "🏆 URL Shortener - This repo will help to shorten the long weburl to shorten to use - Link Azure pipeline repo to understand YAML basics": "https://github.com/Rajkumar-21/pipeline-YAML",
}

ACHIEVEMENTS = {
    "🏆 Received an on-the-spot award for utmost dedication and commitment at TCS.",
    "🏆 Received 3X User Recognition Award for outstanding work on the project at EY in both 2023 - Present",
    "🏆 Automated application/Vm’s deployment with additional configurations to complete the release of the products.",
    "🏆 Worked on scriptings to get customized reports and other actions which majorly reduced time to find and also saved cost by optimizing the infrastructure.",
    "🏆 Developed Chatbot using AI Agents, MCP Server for Azure Resources, Azure Openai, FastAPI",
}

CERTIFICATIONS = {
"📑 Terraform Associate Certification",
"📑 AWS DevOps Certification - DOP-C02",
"📑 Microsoft certified Devops Engineer - AZ400",
"📑 Passed Exam - Azure Architect Technology",
"📑 Microsoft Certified Azure Administrator Associate",
"📑 Microsoft Azure Fundamentals Certification",
"📑 Microsoft Azure AI Fundamental - AI900",
"📑 Microsoft Certified: Azure AI Fundamentals (AI-900)",
"📑 Github Foundation Certified",
"📑 Earned 3 EY Bronze Badge for Azure & Cloud & AI Engineering"
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap='medium' )
with col1:
    st.image(profile_pic, width=250)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("---")
# --- EXPERIENCE & QUALIFICATIONS ---
st.subheader("Experience & Qulifications")
st.write("---")
st.write(
    """
- ✔️ Experienced Azure DevOps Engineer with 6+ years in automating and optimizing cloud infrastructure and deployment strategies.

- ✔️ Proven expertise in leveraging Azure tools to enhance operational excellence, ensuring scalable, secure, and resilient systems.

- ✔️ Skilled in CI/CD pipeline management, container orchestration with Kubernetes and Docker, and infrastructure automation using Terraform and scripting languages.

- ✔️ Strong background in monitoring and troubleshooting using Prometheus and Grafana, with a focus on high availability and security compliance.

- ✔️ Passionate about embracing new challenges and fostering innovation in DevOps practices, with a commitment to continuous improvement.

- ✔️ Excellent communication and collaboration skills, with a proven track record of working effectively in cross-functional teams to deliver high-quality solutions.

- ✔️ Azure Certified DevOps Engineer, Administrator Expert


"""
)
st.write("---")
# --- Projects & Accomplishments ---
st.subheader("Projects & Accomplishments")
st.write("---")
st.write("🎨", "Projects")

for project, link in PROJECTS.items():
    st.markdown(f"<div style='padding-left: 40px;'><a href='{link}' style='text-decoration: none;'>{project}</a></div>", unsafe_allow_html=True)
st.write('\n')
st.write("---")
st.write("🏆", "Achievements")
for achievement in ACHIEVEMENTS:
    st.markdown(f"<div style='padding-left: 40px;'>{achievement}</div>", unsafe_allow_html=True)
st.write('\n')
st.write("---")
# --- SKILLS ---
st.subheader("Technical Skills")
st.write("---")
st.write(
    """

- 📚 CI/CD:

    - ● Azure DevOps: Proficient in managing CI/CD pipelines, infrastructure
    provisioning, and deployment using Azure DevOps.
    - ● GitHub Actions: Experience with GitHub Actions for automating workflows
    and CI/CD processes.

    
- 📚 Containers and Orchestration:

    - ● Docker: Skilled in containerization using Docker for creating, deploying, and
    managing application containers.
    - ● Kubernetes: Familiar with Kubernetes concepts (Pods, Replica Sets,
    Deployments, Services) for container orchestration.
    - ● Terraform: Understanding of provisioning AKS (Azure Kubernetes Service)
    clusters using Terraform.

    
- 📚 Scripting and Automation

    - ● PowerShell: Proficient in scripting using PowerShell for automation tasks.
    - ● Python: Skilled in Python scripting for various DevOps tasks.

    
- 📚 Infrastructure as Code (IaC) & Confirmation Management

    - ● Terraform: Experience with Terraform for declarative infrastructure
    provisioning.
    - ● Ansible: Knowledgeable about Ansible for configuration management and
    automation.
    - ● Worked in Pulumi to deploy azure resources.


- 📚 Monitoring and Logging

    - ● Prometheus and Grafana: Experience in monitoring and troubleshooting
    issues using Prometheus and Grafana.
    - ● Automated stopping VM based on users idle time & selective machines
    using Automation Runbook, LogicAPP in Azure

    
- 📚 Cloud Services

    - ● Azure Cloud (IaaS): Demonstrated understanding of Azure Infrastructure as
    a Service (IaaS) components.
    - ● AKS RBAC (Azure Kubernetes Service Role-Based Access Control):
    Experience with cluster roles and binding in AKS.
    - ● AWS: Familiar with AWS services and concepts.


- 📚 Other Skills

    - ● Linux Basic Administration: Proficient in basic Linux administration tasks.
    - ● Networking: Knowledge of networking principles and configurations.
    - ● Good understanding of generative AI
    - ● Experience in Langchain, AzureOpenAI and Streamlit to create LLM
    applications.
    - ● Developed LLM application for DevSecOps using Flask, AzureOpenAI,
    ChromaDB, and Streamlit.
    - ● Developed a URL shortener application using Streamlit and deployed in HuggingFace.
    - ● Developed a Flet Counter application and deployed in Github Pages using Github Actions.
"""
)

st.write("---")
# --- WORK HISTORY ---
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Consultant | Ernst & Young**")
st.write("Nov/2022 - Present")
st.write(
    """
Built and maintained secure CI/CD pipelines using Azure 
DevOps and GitHub Actions with integrated SAST/DAST 
tools (SonarQube, Mend), ensuring early vulnerability 
detection and secure deployments. 
- ►Led IaC-based environment provisioning 
(Dev/Test/Stage/Prod) and pipeline integrations using 
Terraform and Git. 
- ►Deployed containerized apps with Docker, Kubernetes 
(AKS), and Helm using Blue-Green and Canary 
strategies to ensure zero-downtime rollouts. 
- ►GenAI DevSecOps Assistant: Built an AI-powered tool 
using Python, FastAPI, Azure OpenAI, and Langchain to 
analyse CI/CD failures. 
- ►VM Automation: Reduced VM deployment time from 3 
days to 2 hours through automated setup, config, and 
software install. 
- ► Cost Optimization: Saved 35% monthly cloud costs by 
automating VM shutdowns based on idle time using 
Azure Runbooks and Logic Apps. 
- ► Built a centralized Azure dashboard using Power Apps 
to track resource usage, VM status, costs, and scaling 
actions. 
- ► Developed a GenAI-powered chatbot for managing 
Azure VMs, storage, and DevOps work items via natural 
language. 
- ►  Earned 3× User Recognition Awards for automation 
excellence and impactful DevOps solutions 

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**System Engineer | Epam Systems**")
st.write("August 2022 - October 2022")
st.write(
    """
- ► Worked on Azure DevOps, CI/CD pipelines, and infrastructure as code to automate the deployment process. 
- ► Provided Tech talk session about Azure DevOps and build pipelines to internal audiences and its importance in the current market.
- ► Involved in the design and implementation of Azure infrastructure to support cloud-based applications.

"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**System Engineer | Tata Consultancy Services**")
st.write("May 2019 – August 2022")
st.write(
    """
- ► Maintained and optimized Azure infrastructure and On-Prem data centers of client to support applications.
- ► Automated alert related to infrastructres and application which reduced manual works by 30%.
- ► Worked on large client projects to migrate on-premises infrastructure to Azure cloud and In-place upgrade of Windows Servers
- ► Managed and support to domain controllers, DNS, DHCP, and other services of client.

"""
)

st.write("---")
