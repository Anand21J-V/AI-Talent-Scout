"""
Data models for TalentScout Hiring Assistant
"""
from pydantic import BaseModel, Field
from typing import List, Optional


class CandidateInfo(BaseModel):
    """Candidate information model"""
    full_name: Optional[str] = Field(None, description="Candidate's full name")
    email: Optional[str] = Field(None, description="Email address")
    phone: Optional[str] = Field(None, description="Phone number")
    years_experience: Optional[str] = Field(None, description="Years of experience")
    desired_position: Optional[str] = Field(None, description="Desired position")
    current_location: Optional[str] = Field(None, description="Current location")
    tech_stack: Optional[List[str]] = Field(None, description="Technologies the candidate knows")


class TechnicalQuestions(BaseModel):
    """Technical questions model"""
    questions: List[str] = Field(description="List of technical questions")
    tech_category: str = Field(description="Technology category for these questions")