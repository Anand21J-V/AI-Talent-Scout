"""
Conversation prompts and messages for TalentScout Hiring Assistant
"""

GREETING_MESSAGE = """👋 Hello! Welcome to TalentScout!

I'm your AI hiring assistant, and I'm here to help with your initial screening for technology positions.

I'll be collecting some basic information about you and then asking a few technical questions based on your expertise. This should only take about 5-10 minutes.

Let's get started! What's your full name?

*(You can type 'bye' or 'exit' at any time to end our conversation)*
"""

FAREWELL_MESSAGE = """Thank you for your time! 👋

We appreciate you starting the application process with TalentScout. 

If you'd like to continue later, please feel free to return. Our team will review any information you've provided.

Best of luck with your job search!

*[Conversation Ended]*
"""

COMPLETION_MESSAGE = """🎉 Great! We've finished your screening.

✅ Information collected  
✅ Technical questions completed  

Our team will review your profile and contact you soon.  
Thank you for your time and interest with TalentScout! 🎯

*(This conversation will now end)*
"""

FIELD_PROMPTS = {
    "full_name": "Great! Now, could you please share your email address? (e.g., yourname@example.com)",
    "email": "Thank you! May I have your phone number? (digits only, please)",
    "phone": "Perfect! How many years of experience do you have?",
    "years_experience": "Excellent! What role or position are you applying for?",
    "desired_position": "Great! Where are you currently located (city and country)?",
    "current_location": "Thank you! Could you list the main technologies or programming languages you work with?",
    "tech_stack": "Perfect! I've collected all your details. Let me prepare some technical questions for you, PLEASE TYPE ANYTING TO PROCEED..."
}

FIELD_CLARIFICATIONS = {
    "full_name": "Hmm, that doesn't look like a valid full name. Please type your first and last name (e.g., John Smith).",
    "email": "Hmm, that doesn't look like an email address. Please type it like yourname@example.com.",
    "phone": "I didn't catch a valid phone number — please type digits only (e.g., 9876543210).",
    "years_experience": "Please enter the number of years you have worked (e.g., 3).",
    "desired_position": "Please type the role or position you are applying for (e.g., Software Engineer).",
    "current_location": "Please type your current city and country (e.g., New York, USA).",
    "tech_stack": "Please list at least one technology you work with (e.g., Python, JavaScript, Java)."
}

FALLBACK_QUESTION = "Could you tell me about one project you're most proud of?"