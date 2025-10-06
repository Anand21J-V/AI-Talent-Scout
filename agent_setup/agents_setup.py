"""
AI agents configuration for TalentScout Hiring Assistant
"""
from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
from core.config import GEMINI_BASE_URL, GEMINI_API_KEY, GEMINI_MODEL
from core.models import TechnicalQuestions


def setup_gemini_model():
    """Initialize and return Gemini model"""
    gemini_client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=GEMINI_API_KEY)
    return OpenAIChatCompletionsModel(
        model=GEMINI_MODEL,
        openai_client=gemini_client
    )


def create_tech_question_agent(model):
    """Create and return technical question generator agent"""
    return Agent(
        name="Technical Question Generator",
        instructions="""
You are an expert technical interviewer for TalentScout.

Given a candidate's tech stack, generate 3-5 relevant technical questions for each major technology they listed.

Guidelines:
1. Questions should assess practical knowledge and real-world application
2. Mix difficulty levels: some basic, some intermediate, some advanced
3. Questions should be specific to the technology mentioned
4. Avoid yes/no questions - ask open-ended questions
5. Focus on problem-solving and understanding, not just memorization

Format your response as JSON:
{
    "questions": ["question1", "question2", ...],
    "tech_category": "technology name"
}

Make questions relevant, challenging, and professional.
""",
        model=model,
        output_type=TechnicalQuestions,
    )


# Initialize agents
set_tracing_disabled(True)
gemini_model = setup_gemini_model()
tech_question_agent = create_tech_question_agent(gemini_model)