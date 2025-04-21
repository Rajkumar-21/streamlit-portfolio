"""
portfolio/
├── app.py                # Main entry point
├── pages/                # Pages directory
│   ├── 1_🏠_Home.py      # Home page
│   ├── 2_💼_Experience.py # Experience page
│   ├── 3_🔧_Skills.py     # Skills page
│   ├── 4_🚀_Projects.py   # Projects page
│   └── 5_📞_Contact.py    # Contact page
├── chatbot.py            # Chatbot functionality
├── styles/               # CSS styles
│   └── main.css          # Main CSS file
└── assets/               # Images and other assets

"""

import streamlit as st
from pathlib import Path
import chatbot

# Path settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

# Page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="👨‍💻",
    layout="wide",
)

# Load CSS
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Custom CSS for React-like UI and chatbot button
st.markdown("""
<style>
/* React-like UI styles */
.main .block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* Chatbot button styles */
.chatbot-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
    background-color: #4CAF50;
    color: white;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

/* Chatbot container styles */
.chatbot-container {
    position: fixed;
    bottom: 90px;
    right: 20px;
    width: 350px;
    height: 450px;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    z-index: 1000;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state for chatbot visibility
if "show_chatbot" not in st.session_state:
    st.session_state.show_chatbot = False

# Home page content
st.title("Welcome to My Portfolio")
st.write("This is the main page of my portfolio. Navigate using the sidebar to explore different sections.")

# Add chatbot button (visible on all pages)
st.markdown(
    f"""
    <div class="chatbot-button" onclick="this.style.display='none'; document.getElementById('chatbot-container').style.display='block';">
        <span style="font-size: 24px;">💬</span>
    </div>
    
    <div id="chatbot-container" class="chatbot-container" style="display: {'block' if st.session_state.show_chatbot else 'none'};">
        <div style="padding: 10px; background-color: #4CAF50; color: white; display: flex; justify-content: space-between;">
            <span>Ask AI</span>
            <span onclick="this.parentElement.parentElement.style.display='none'; document.querySelector('.chatbot-button').style.display='block';" style="cursor: pointer;">✖</span>
        </div>
        <div id="chatbot-content" style="padding: 10px; height: calc(100% - 40px); overflow-y: auto;">
            <iframe src="/?show_chatbot=true" style="border: none; width: 100%; height: 100%;"></iframe>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Chatbot implementation
if st.query_params.get("show_chatbot"):
    with st.container():
        st.subheader("Chat with AI Assistant")
        
        # Initialize chat messages
        if "messages" not in st.session_state:
            st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm your AI assistant. Ask me anything about this portfolio."}]
        
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Ask something..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Get response from chatbot
            with st.chat_message("assistant"):
                response = chatbot.get_response(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})