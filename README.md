# 🎯 TalentScout Hiring Assistant

An AI-powered intelligent hiring assistant that streamlines the initial candidate screening process using conversational AI. Built with Streamlit and powered by Google's Gemini 2.0 Flash model.

## 📋 Overview

TalentScout automates the initial stages of candidate screening by:
- Collecting essential candidate information through natural conversation
- Dynamically generating relevant technical questions based on the candidate's tech stack
- Providing a smooth, user-friendly chat interface
- Securely storing candidate data and interview responses

## ✨ Features

- **🤖 Conversational AI Interface**: Natural, human-like interaction powered by Gemini AI
- **📝 Smart Data Collection**: Validates and extracts candidate information (name, email, phone, experience, location, tech stack)
- **🧠 Dynamic Question Generation**: Automatically creates relevant technical questions based on candidate's expertise
- **🔍 Tech Stack Recognition**: Recognizes 200+ technologies across multiple domains
- **💾 Secure Data Storage**: Saves candidate profiles and interview responses as structured JSON files
- **🎨 Modern UI**: Clean, professional Streamlit interface with real-time chat
- **🚪 Graceful Exit**: Handles conversation termination naturally
- **📊 Session Tracking**: Real-time display of collected information and progress

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.0 Flash (via OpenAI-compatible API)
- **Agent Framework**: Custom Agent/Runner framework
- **Data Validation**: Pydantic
- **Async Support**: asyncio, nest_asyncio
- **Environment Management**: python-dotenv

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Anand21J-V/AI-Talent-Scout.git
   cd AI-Talent-Scout
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit nest-asyncio pydantic openai python-dotenv
   ```

4. **Install the agents framework**
   ```bash
   pip install agents  # or the specific package name for your agent framework
   ```

5. **Create a `.env` file**
   ```bash
   touch .env
   ```

6. **Add your Gemini API key to `.env`**
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## 🚀 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Workflow

1. **Greeting**: The assistant welcomes the candidate and explains the process
2. **Information Collection**: Collects the following in sequence:
   - Full name
   - Email address
   - Phone number
   - Years of experience
   - Desired position
   - Current location
   - Tech stack/technologies
3. **Technical Questions**: Generates 3-5 relevant questions based on the tech stack
4. **Completion**: Saves all data and thanks the candidate

### Exit Keywords

Users can end the conversation at any time by typing:
- `bye`
- `exit`
- `quit`
- `goodbye`
- `no thanks`
- `end conversation`
- `stop`

## 📁 Project Structure

```
talentscout-hiring-assistant/
│
├── app.py                      # Main application file
├── .env                        # Environment variables (not committed)
├── .gitignore                  # Git ignore file
├── README.md                   # This file
├── requirements.txt            # Python dependencies
│
└── candidate_data/             # Stored candidate information
    └── candidate_YYYYMMDD_HHMMSS.json
```

## 💾 Data Storage

Candidate data is stored in JSON format with the following structure:

```json
{
  "timestamp": "20250106_143022",
  "candidate_info": {
    "full_name": "John Doe",
    "email": "john@example.com",
    "phone": "1234567890",
    "years_experience": "5",
    "desired_position": "Senior Python Developer",
    "current_location": "New York, USA",
    "tech_stack": ["python", "django", "postgresql", "docker"]
  },
  "technical_questions": [...],
  "candidate_answers": [...],
  "questions_and_answers": [...],
  "status": "initial_screening_complete"
}
```

## 🔧 Configuration

### Supported Technologies

The system recognizes 200+ technologies including:
- **Languages**: Python, Java, JavaScript, TypeScript, C++, Go, Rust, etc.
- **Frameworks**: Django, Flask, React, Angular, Vue, Spring Boot, etc.
- **Databases**: PostgreSQL, MongoDB, Redis, MySQL, etc.
- **Cloud & DevOps**: AWS, Azure, GCP, Docker, Kubernetes, etc.
- **AI/ML**: TensorFlow, PyTorch, scikit-learn, Hugging Face, etc.
- **And many more...**

### Customization

You can customize the following in `app.py`:

- **AI Model**: Change `GEMINI_MODEL` to use different Gemini versions
- **Question Count**: Modify the technical question generation logic
- **Tech Keywords**: Update `tech_keywords` list to add/remove technologies
- **Validation Rules**: Adjust regex patterns in `extract_candidate_info_last_message()`

## 🔒 Privacy & Security

- All candidate data is stored locally
- No data is transmitted to third parties (except Gemini API for question generation)
- Implements GDPR-compliant data handling practices
- Secure file storage with timestamped filenames

## 🐛 Troubleshooting

### Common Issues

**Issue**: `GEMINI_API_KEY is not set`
- **Solution**: Ensure your `.env` file contains the correct API key

**Issue**: Import errors for `agents` module
- **Solution**: Install the required agent framework package

**Issue**: Streamlit doesn't start
- **Solution**: Check if port 8501 is available or specify a different port:
  ```bash
  streamlit run app.py --server.port 8502
  ```

## 📝 Requirements.txt

```
streamlit>=1.28.0
nest-asyncio>=1.5.8
pydantic>=2.0.0
openai>=1.0.0
python-dotenv>=1.0.0
agents>=0.1.0
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Your Name - Anand Vishwakarma

## 🙏 Acknowledgments

- Google Gemini AI for powering the conversational intelligence
- Streamlit for the amazing web framework
- The open-source community for various tools and libraries

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: anandvishwakarma21j@gmail.com

---

**Made with ❤️ by TalentScout Team**

*Powered by Gemini AI | © 2025 TalentScout*
