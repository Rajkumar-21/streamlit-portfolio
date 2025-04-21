import streamlit as st

st.set_page_config(
    page_title="Contact | My Portfolio",
    page_icon="📞",
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

.contact-container {
    display: flex;
    flex-direction: column;
    max-width: 800px;
    margin: 0 auto;
}

.contact-card {
    background-color: white;
    border-radius: 10px;
    padding: 2rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
}

.contact-info-item {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
}

.contact-icon {
    font-size: 1.5rem;
    margin-right: 1rem;
    width: 40px;
    height: 40px;
    background-color: #f0f0f0;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.social-links {
    display: flex;
    justify-content: center;
    margin-top: 1.5rem;
}

.social-link {
    width: 50px;
    height: 50px;
    background-color: #f0f0f0;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 0.5rem;
    font-size: 1.5rem;
    text-decoration: none;
    color: #333;
    transition: background-color 0.3s ease, transform 0.3s ease;
}

.social-link:hover {
    background-color: #4CAF50;
    color: white;
    transform: translateY(-3px);
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
}

.form-input {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1rem;
}

.form-textarea {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1rem;
    min-height: 150px;
    resize: vertical;
}

.submit-button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 5px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.submit-button:hover {
    background-color: #45a049;
}

.map-container {
    width: 100%;
    height: 300px;
    border-radius: 10px;
    overflow: hidden;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# Page Header
st.markdown("<h1 class='page-title'>Get In Touch</h1>", unsafe_allow_html=True)

# Contact Introduction
st.markdown("""
<div style="text-align: center; max-width: 600px; margin: 0 auto 2rem auto;">
    <p>I'm interested in freelance opportunities, especially ambitious or large projects. However, if you have other requests or questions, don't hesitate to contact me using the form below.</p>
</div>
""", unsafe_allow_html=True)

# Contact Information and Form
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div class="contact-card">
        <h2 style="margin-bottom: 1.5rem;">Contact Information</h2>
        
        <div class="contact-info-item">
            <div class="contact-icon">📧</div>
            <div>
                <div style="font-weight: bold;">Email</div>
                <a href="mailto:hello@example.com">hello@example.com</a>
            </div>
        </div>
        
        <div class="contact-info-item">
            <div class="contact-icon">📱</div>
            <div>
                <div style="font-weight: bold;">Phone</div>
                <a href="tel:+1234567890">+1 (234) 567-890</a>
            </div>
        </div>
        
        <div class="contact-info-item">
            <div class="contact-icon">📍</div>
            <div>
                <div style="font-weight: bold;">Location</div>
                <div>San Francisco, CA</div>
            </div>
        </div>
        
        <div class="contact-info-item">
            <div class="contact-icon">⏰</div>
            <div>
                <div style="font-weight: bold;">Working Hours</div>
                <div>Monday - Friday: 9:00 AM - 5:00 PM</div>
            </div>
        </div>
        
        <div class="social-links">
            <a href="#" class="social-link">
                <span>📘</span>
            </a>
            <a href="#" class="social-link">
                <span>📱</span>
            </a>
            <a href="#" class="social-link">
                <span>🐦</span>
            </a>
            <a href="#" class="social-link">
                <span>📸</span>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="contact-card">', unsafe_allow_html=True)
    st.markdown("<h2 style='margin-bottom: 1.5rem;'>Send Me a Message</h2>", unsafe_allow_html=True)
    
    # Contact Form
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name", placeholder="Your Name")
        email = st.text_input("Email", placeholder="Your Email")
        subject = st.text_input("Subject", placeholder="Subject")
        message = st.text_area("Message", placeholder="Your Message")
        
        # Submit Button
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            if name and email and message:
                st.success("Thanks for your message! I'll get back to you soon.")
                # Here you would typically add code to send the email or store the message
            else:
                st.error("Please fill out all required fields.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# FAQ Section
st.markdown("<h2 style='text-align: center; margin-top: 3rem;'>Frequently Asked Questions</h2>", unsafe_allow_html=True)

# Create expandable FAQ items
faq_items = [
    {
        "question": "What services do you offer?",
        "answer": "I offer web development, mobile app development, UI/UX design, and consulting services. My expertise includes frontend and backend development, responsive design, and creating intuitive user experiences."
    },
    {
        "question": "What is your typical project timeline?",
        "answer": "Project timelines vary depending on complexity and scope. A simple website might take 2-4 weeks, while a complex web application could take 2-3 months. I'll provide a detailed timeline during our initial consultation."
    },
    {
        "question": "Do you offer maintenance services after project completion?",
        "answer": "Yes, I offer maintenance packages to ensure your application stays up-to-date and secure. This includes regular updates, bug fixes, and performance optimization."
    },
    {
        "question": "How do you handle project pricing?",
        "answer": "I offer both fixed-price and hourly rate options depending on the project requirements. For most projects, I prefer to provide a fixed quote after understanding the full scope to avoid any surprises."
    }
]

# Display FAQs in two columns
col1, col2 = st.columns(2)

for i, faq in enumerate(faq_items):
    if i % 2 == 0:
        with col1:
            with st.expander(faq["question"]):
                st.write(faq["answer"])
    else:
        with col2:
            with st.expander(faq["question"]):
                st.write(faq["answer"])

# Location Map
st.markdown("<h2 style='text-align: center; margin-top: 3rem;'>My Location</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="map-container">
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d100939.98555098464!2d-122.50764017948551!3d37.75781499657633!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80859a6d00690021%3A0x4a501367f076adff!2sSan%20Francisco%2C%20CA!5e0!3m2!1sen!2sus!4v1636587330279!5m2!1sen!2sus" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
</div>
""", unsafe_allow_html=True)

# Call to Action
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding: 2rem; background-color: #f9f9f9; border-radius: 10px;">
    <h3>Let's Work Together</h3>
    <p style="max-width: 600px; margin: 1rem auto;">Have a project in mind? Looking for a developer to join your team? I'm currently available for freelance work and open to discussing new opportunities.</p>
    <a href="mailto:hello@example.com" style="display: inline-block; padding: 0.75rem 1.5rem; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 5px; font-weight: bold; margin-top: 1rem; transition: background-color 0.3s ease;">Email Me</a>
</div>
""", unsafe_allow_html=True)