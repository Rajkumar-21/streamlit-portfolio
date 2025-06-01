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
    "🏆 Azure pipeline repo to understand YAML basics": "https://github.com/Rajkumar-21/pipeline-YAML"
}

ACHIEVEMENTS = {
    "🏆 Received an on-the-spot award for utmost dedication and commitment at TCS.",
    "🏆 Received the User Recognition Award for outstanding work on the project at EY in both 2023 and 2024",
    "🏆 Automated application/Vm’s deployment with additional configurations to complete the release of the products.",
    "🏆 Worked on scriptings to get customized reports and other actions which majorly reduced time to find and also saved cost by optimizing the infrastructure.",
}

CERTIFICATIONS = {
"📑 Terraform Associate Certification",
"📑 AWS DevOps Certification - DOP-C02",
"📑 Microsoft certified Devops Engineer - AZ400",
"📑 Passed Exam - Azure Architect Technology",
"📑 Microsoft Certified Azure Administrator Associate",
"📑 Microsoft Azure Fundamentals Certification",
"📑 Microsoft Azure AI Fundamental - AI900",

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
- ► Designed and implemented robust Microsoft Azure infrastructure to support cloud-based applications.
- ► Automated deployment processes and infrastructure management with Azure DevOps, PowerShell which reduced manual works by 90%.
- ► Implemented CI/CD pipelines for reporting and monitoring usage data of azure resources and take action which optimized and reduced cost by 40%.
- ► Developed a PowerShell script to automate the process of stopping VMs based on users' idle time and selective machines which saved $10K annually.
- ► Worked in LLM applications using AzureOpenAI, Streamlit,Flask and Langchain to create DevSecOps applications.
- ► Conducted security audits and vulnerability assessments to ensure compliance and secure application environments.
- ► Optimized network configurations for secure, low-latency communication between cloud resources and on-premises systems.

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
