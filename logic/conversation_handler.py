"""
Conversation handling logic for TalentScout Hiring Assistant
"""
import asyncio
from typing import Optional, Tuple
from agents import Runner
from agent_setup.agents_setup import tech_question_agent
from core.utils import extract_candidate_info_last_message, save_candidate_data
from core.prompts import (
    FIELD_PROMPTS, 
    FIELD_CLARIFICATIONS, 
    FALLBACK_QUESTION, 
    COMPLETION_MESSAGE
)
from core.config import FIELD_ORDER


class ConversationHandler:
    """Handles conversation flow and logic"""
    
    def __init__(self):
        self.candidate_info = {}
        self.current_field = "full_name"
        self.tech_questions = None
        self.conversation_active = True
    
    def process_field_input(self, user_message: str) -> Tuple[Optional[str], bool]:
        """
        Process user input for current field
        Returns: (response_message, should_save)
        """
        field = self.current_field
        
        if field not in FIELD_PROMPTS:
            return None, False
        
        # Try to extract information for current field
        extracted = extract_candidate_info_last_message(user_message, field)
        
        if extracted:
            # Valid input - save and move to next field
            self.candidate_info.update(extracted)
            
            # Determine next field
            current_index = FIELD_ORDER.index(field)
            
            if current_index < len(FIELD_ORDER) - 1:
                # Move to next field
                next_field = FIELD_ORDER[current_index + 1]
                self.current_field = next_field
                return FIELD_PROMPTS[field], False
            else:
                # All info collected - transition to technical questions
                self.current_field = "completed"
                return FIELD_PROMPTS[field], False
        else:
            # Invalid input - ask for clarification
            return FIELD_CLARIFICATIONS[field], False
    
    async def generate_technical_questions(self) -> str:
        """Generate technical questions based on tech stack"""
        tech_stack = self.candidate_info.get("tech_stack", [])
        
        if not tech_stack:
            # Fallback to generic question
            self.tech_questions = {
                "questions": [FALLBACK_QUESTION], 
                "current_index": 0,
                "answers": []
            }
            return f"**Question 1 of 1:**\n\n{FALLBACK_QUESTION}"
        
        tech_stack_msg = ", ".join(tech_stack)
        
        try:
            tech_result = await Runner.run(
                tech_question_agent,
                f"Generate technical questions for candidate with these technologies: {tech_stack_msg}"
            )
            
            if tech_result.final_output:
                questions = tech_result.final_output.questions[:5]
                self.tech_questions = {
                    "questions": questions, 
                    "current_index": 0,
                    "answers": []
                }
                return f"**Question 1 of {len(questions)}:**\n\n{questions[0]}"
        except Exception as e:
            pass
        
        # Fallback on error
        self.tech_questions = {
            "questions": [FALLBACK_QUESTION], 
            "current_index": 0,
            "answers": []
        }
        return f"**Question 1 of 1:**\n\n{FALLBACK_QUESTION}"
    
    def process_technical_answer(self, answer: str) -> Tuple[Optional[str], bool]:
        """
        Process answer to technical question
        Returns: (response_message, conversation_ended)
        """
        if not self.tech_questions:
            return None, False
        
        current_idx = self.tech_questions["current_index"]
        questions = self.tech_questions["questions"]
        
        # Save the answer
        self.tech_questions["answers"].append(answer)
        
        if current_idx < len(questions) - 1:
            # Move to next question
            self.tech_questions["current_index"] += 1
            next_idx = self.tech_questions["current_index"]
            response = f"**Question {next_idx + 1} of {len(questions)}:**\n\n{questions[next_idx]}"
            return response, False
        else:
            # All questions completed
            save_candidate_data(
                self.candidate_info, 
                self.tech_questions["questions"],
                self.tech_questions["answers"]
            )
            self.conversation_active = False
            return COMPLETION_MESSAGE, True
    
    async def process_message(self, user_message: str) -> Tuple[str, bool]:
        """
        Process user message and return response
        Returns: (response_message, conversation_ended)
        """
        # Check if we're still collecting basic info
        if self.current_field in FIELD_ORDER:
            response, _ = self.process_field_input(user_message)
            return response, False
        
        # Handle technical questions after all info collected
        elif self.current_field == "completed":
            if not self.tech_questions:
                # Generate technical questions
                response = await self.generate_technical_questions()
                return response, False
            else:
                # Continue with technical questions
                return self.process_technical_answer(user_message)
        
        return "I'm not sure how to process that. Could you please try again?", False