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

# Check URL parameter for chatbot toggle
params = st.experimental_get_query_params()
if "chat" in params:
    st.session_state.show_chatbot = params["chat"][0] == "true"

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

# Add chatbot button with URL parameter approach
current_chat_state = "true" if not st.session_state.show_chatbot else "false"
st.markdown(
    f"""
    <div class="chatbot-button" onclick="window.location.href='?chat={current_chat_state}'">
        <span style="font-size: 24px;">💬</span>
    </div>
    """,
    unsafe_allow_html=True
)

# Chatbot container
if st.session_state.show_chatbot:
    st.markdown(
        """
        <div id="chatbot-container" class="chatbot-container">
            <div style="padding: 10px; background-color: #4CAF50; color: white; display: flex; justify-content: space-between;">
                <span>Ask AI</span>
                <span onclick="window.location.href='?chat=false'" style="cursor: pointer;">✖</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Chatbot implementation inside the container
    with st.container():
        # Initialize chat messages
        if "messages" not in st.session_state:
            st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm your AI assistant. Ask me anything about this portfolio."}]
        
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Ask something...", key="chatbot_input"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Get response from chatbot
            response = chatbot.get_response(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()  # Rerun to update the chat history