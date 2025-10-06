"""
Main application file for TalentScout Hiring Assistant
"""

import sys
import os

# --- Universal Root Path Setup ---
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

import nest_asyncio
nest_asyncio.apply()

import asyncio
import streamlit as st
from logic.conversation_handler import ConversationHandler
from ui.ui_components import (
    apply_custom_css,
    render_header,
    render_sidebar,
    render_chat_history,
    display_conversation_ended
)
from core.prompts import GREETING_MESSAGE, FAREWELL_MESSAGE
from core.utils import is_exit_keyword


# Page configuration
st.set_page_config(
    page_title="TalentScout Hiring Assistant",
    page_icon="🎯",
    layout="wide"
)

# Apply styling
apply_custom_css()

# Render header
render_header()


def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({"role": "assistant", "content": GREETING_MESSAGE})
    
    if "handler" not in st.session_state:
        st.session_state.handler = ConversationHandler()
    
    if "conversation_active" not in st.session_state:
        st.session_state.conversation_active = True
    
    # Sync handler state to session state for UI display
    if "candidate_info" not in st.session_state:
        st.session_state.candidate_info = st.session_state.handler.candidate_info
    
    if "current_field" not in st.session_state:
        st.session_state.current_field = st.session_state.handler.current_field


def sync_handler_to_session():
    """Sync handler state to session state"""
    st.session_state.candidate_info = st.session_state.handler.candidate_info
    st.session_state.current_field = st.session_state.handler.current_field
    st.session_state.conversation_active = st.session_state.handler.conversation_active


async def handle_user_message(user_message: str):
    """Handle user message and generate response"""
    # Check for exit keywords
    if is_exit_keyword(user_message):
        st.session_state.messages.append({"role": "assistant", "content": FAREWELL_MESSAGE})
        st.session_state.conversation_active = False
        st.session_state.handler.conversation_active = False
        with st.chat_message("assistant"):
            st.markdown(FAREWELL_MESSAGE)
        return
    
    # Process message through handler
    with st.spinner("💭 Processing..."):
        response, conversation_ended = await st.session_state.handler.process_message(user_message)
    
    if response:
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)
    
    # Sync state
    sync_handler_to_session()


def main():
    """Main application logic"""
    # Initialize session state
    initialize_session_state()
    
    # Render chat history
    render_chat_history(st.session_state.messages)
    
    # Chat input and processing
    if st.session_state.conversation_active:
        if prompt := st.chat_input("Type your message here..."):
            # Display user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Handle the message
            asyncio.run(handle_user_message(prompt))
    else:
        display_conversation_ended()
    
    # Render sidebar
    render_sidebar(st.session_state)


if __name__ == "__main__":
    main()