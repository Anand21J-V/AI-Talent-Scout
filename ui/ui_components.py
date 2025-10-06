"""
UI components for TalentScout Hiring Assistant
"""
import streamlit as st


def apply_custom_css():
    """Apply custom CSS styling"""
    st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            color: #1f77b4;
            text-align: center;
            margin-bottom: 1rem;
        }
        .sub-header {
            text-align: center;
            color: #666;
            margin-bottom: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)


def render_header():
    """Render app header"""
    st.markdown('<h1 class="main-header">🎯 TalentScout Hiring Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">AI-Powered Initial Candidate Screening</p>', unsafe_allow_html=True)


def render_sidebar(session_state):
    """Render sidebar with info and controls"""
    with st.sidebar:
        st.header("ℹ️ About This Assistant")
        st.markdown("""
        **TalentScout Hiring Assistant** helps streamline the initial candidate screening process.
        
        **Features:**
        - 📝 Collects candidate information
        - 🧠 Generates relevant technical questions
        - 💬 Natural conversation flow
        - 🔒 Secure data handling
        
        **Privacy & Security:**
        All candidate data is handled in compliance with GDPR and data privacy standards.
        """)
        
        st.divider()
        
        st.header("📊 Session Info")
        st.metric("Messages Exchanged", len(session_state.messages))
        
        current_field_display = session_state.current_field.replace("_", " ").title() \
            if session_state.current_field != "completed" else "Technical Questions"
        st.metric("Current Field", current_field_display)
        
        # Show collected info
        if session_state.candidate_info:
            st.subheader("✅ Collected Information:")
            for key, value in session_state.candidate_info.items():
                if value:
                    display_key = key.replace('_', ' ').title()
                    if key == "tech_stack":
                        st.text(f"{display_key}: {', '.join(value)}")
                    else:
                        st.text(f"{display_key}: {value}")
        
        if st.button("🔄 Start New Session"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
        
        st.divider()
        
        st.markdown("""
        <div style='text-align: center; color: #666; font-size: 0.8rem;'>
        Powered by Gemini AI<br>
        © 2025 TalentScout
        </div>
        """, unsafe_allow_html=True)


def render_chat_history(messages):
    """Render chat message history"""
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def display_conversation_ended():
    """Display message when conversation has ended"""
    st.info("💬 Conversation has ended. Refresh the page to start a new session.")