"""
Utility functions for TalentScout Hiring Assistant
"""
import os
import json
import re
from datetime import datetime
from typing import List
from core.config import EXIT_KEYWORDS, TECH_KEYWORDS, DATA_DIRECTORY


def is_exit_keyword(message: str) -> bool:
    """Check if message contains exit keywords"""
    return any(keyword in message.lower() for keyword in EXIT_KEYWORDS)


def extract_candidate_info_last_message(last_message: str, field: str) -> dict:
    """Extract specific field information from user message"""
    extracted = {}
    content = last_message.strip()
    lower_content = content.lower()

    if field == "full_name":
        words = content.split()
        if 1 < len(words) <= 3 and all(w.isalpha() for w in words):
            extracted["full_name"] = content
            
    elif field == "email":
        email_match = re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", content)
        if email_match:
            extracted["email"] = content
            
    elif field == "phone":
        phone_match = re.fullmatch(r"\d{10,15}", content)
        if phone_match:
            extracted["phone"] = content
            
    elif field == "years_experience":
        if content.isdigit():
            extracted["years_experience"] = content
            
    elif field == "desired_position":
        if len(content) > 1:
            extracted["desired_position"] = content
            
    elif field == "current_location":
        if len(content) > 1:
            extracted["current_location"] = content
            
    elif field == "tech_stack":
        matched_techs = [tech for tech in TECH_KEYWORDS if tech in lower_content]
        if matched_techs:
            extracted["tech_stack"] = matched_techs

    return extracted


def save_candidate_data(candidate_info: dict, questions: List[str], answers: List[str]) -> str:
    """Save candidate data securely"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{DATA_DIRECTORY}/candidate_{timestamp}.json"
    
    os.makedirs(DATA_DIRECTORY, exist_ok=True)
    
    # Create Q&A pairs
    qa_pairs = []
    for i, (question, answer) in enumerate(zip(questions, answers), 1):
        qa_pairs.append({
            "question_number": i,
            "question": question,
            "answer": answer
        })
    
    data = {
        "timestamp": timestamp,
        "candidate_info": candidate_info,
        "technical_questions": questions,
        "candidate_answers": answers,
        "questions_and_answers": qa_pairs,
        "status": "initial_screening_complete"
    }
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    return filename