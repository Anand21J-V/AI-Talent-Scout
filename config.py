"""
Configuration module for TalentScout Hiring Assistant
"""
import os
from dotenv import load_dotenv

load_dotenv(override=True)

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GEMINI_MODEL = "gemini-2.0-flash"

# Data Storage
DATA_DIRECTORY = "candidate_data"

# Exit Keywords
EXIT_KEYWORDS = ['bye', 'exit', 'quit', 'goodbye', 'no thanks', 'end conversation', 'stop']

# Field Collection Order
FIELD_ORDER = ["full_name", "email", "phone", "years_experience", "desired_position", "current_location", "tech_stack"]

# Technology Keywords
TECH_KEYWORDS = [
    # Programming Languages
    "python", "java", "javascript", "typescript", "c", "c++", "c#", "go", "rust", "ruby", "swift", 
    "kotlin", "scala", "perl", "php", "r", "dart", "objective-c", "elixir", "haskell", "lua",
    "matlab", "shell", "bash", "powershell", "sql", "html", "css", "sass", "less",
    
    # Web Frameworks
    "django", "flask", "fastapi", "streamlit", "gradio", "spring", "springboot", "express", "nextjs", 
    "nestjs", "react", "angular", "vue", "svelte", "nuxtjs", "remix", "ember", "backbone", "meteor", 
    "laravel", "codeigniter", "symfony", "asp.net", "blazor", "rails", "phoenix",
    
    # Mobile & Cross-Platform
    "flutter", "react native", "ionic", "cordova", "capacitor", "xamarin", "kivy", "swiftui", 
    "android", "ios", "jetpack compose",
    
    # Databases
    "mysql", "postgresql", "sqlite", "mongodb", "redis", "cassandra", "dynamodb", "neo4j", 
    "elasticsearch", "couchdb", "firebase", "realm", "supabase", "timescaledb", "snowflake", 
    "oracle", "mariadb", "clickhouse", "hive", "bigquery", "influxdb", "duckdb",
    
    # AI / ML / Data Science
    "machine learning", "deep learning", "artificial intelligence", "data science", "pandas", 
    "numpy", "scipy", "matplotlib", "seaborn", "plotly", "sklearn", "tensorflow", "keras", 
    "pytorch", "huggingface", "transformers", "langchain", "langgraph", "llm", "gpt", "gemini", 
    "llama", "mistral", "groq", "auto-gpt", "ollama", "paddleocr", "openai", "anthropic", 
    "stability ai", "diffusers", "cv2", "opencv", "yolo", "detectron", "llava", "clip", 
    "tesseract", "autogen", "autonomous agent", "reinforcement learning", "nlp", "computer vision",
    "speech recognition", "t5", "bert", "xgboost", "lightgbm", "catboost", "stable diffusion",
    "rag", "vector database", "chroma", "faiss", "pinecone", "weaviate", "milvus",
    
    # DevOps & Cloud
    "aws", "azure", "gcp", "digitalocean", "heroku", "vercel", "netlify", "railway", 
    "terraform", "ansible", "puppet", "chef", "jenkins", "circleci", "travis", "github actions",
    "gitlab ci", "docker", "kubernetes", "helm", "openshift", "prometheus", "grafana", 
    "argo", "tekton", "nginx", "apache", "cloudflare", "cdn", "elastic stack", "logstash",
    "kibana", "s3", "ec2", "lambda", "cloudwatch", "cloudformation", "vpc", "rds", "eks", "aks",
    
    # Tools & Platforms
    "git", "github", "gitlab", "bitbucket", "jira", "notion", "slack", "discord", "trello", 
    "figma", "miro", "postman", "insomnia", "swagger", "openapi", "graphql", "restapi", 
    "soap", "grpc", "websocket", "api gateway", "ngrok", "vscode", "pycharm", "intellij",
    "android studio", "xcode", "colab", "jupyter", "anaconda", "visual studio", "dockerhub",
    
    # Cybersecurity & Networking
    "cybersecurity", "network security", "penetration testing", "ethical hacking", "burp suite",
    "wireshark", "nmap", "kali linux", "metasploit", "firewall", "vpn", "ssl", "tls", 
    "encryption", "hashing", "jwt", "oauth", "auth0", "keycloak", "kerberos", "dns", "tcp/ip",
    "http", "https", "ssh", "ftp", "api security", "sso", "iam", "zero trust",
    
    # Data Engineering & Big Data
    "apache spark", "hadoop", "airflow", "databricks", "kafka", "flink", "beam", "luigi", 
    "dbt", "snowflake", "redshift", "data lake", "data warehouse", "etl", "elt", "data pipeline", 
    "bigquery", "azure data factory", "glue", "athena", "kinesis", "presto", "trino",
    
    # Testing & QA
    "pytest", "unittest", "selenium", "cypress", "playwright", "jest", "mocha", "chai", 
    "karma", "junit", "testng", "robot framework", "postman tests", "load testing", "k6",
    "gatling", "locust", "integration testing", "unit testing", "tdd", "bdd",
    
    # Blockchain & Web3
    "blockchain", "ethereum", "solidity", "web3", "smart contract", "metamask", "polygon",
    "binance smart chain", "nft", "defi", "ipfs", "hardhat", "truffle", "alchemy", "moralis", 
    "near", "solana", "rust smart contract", "ledger", "crypto", "bitcoin", "walletconnect",
    
    # Analytics, BI & Visualization
    "tableau", "powerbi", "looker", "metabase", "superset", "data studio", "mode analytics", 
    "d3.js", "plotly", "dash", "holoviews", "altair", "bokeh", "grafana", "kibana",
    
    # Hardware / IoT / Robotics
    "arduino", "raspberry pi", "esp32", "iot", "mqtt", "ros", "robotics", "embedded systems", 
    "microcontroller", "sensor", "actuator", "jetson", "edge ai", "raspbian", "firmware",
    
    # Misc Emerging Tech
    "quantum computing", "edge computing", "5g", "metaverse", "digital twin", "vr", "ar", "xr",
    "prompt engineering", "autonomous agent", "multi-agent system", "generative ai", "rag agent",
    "ai agent", "langgraph agent", "autogen agent", "openai agent sdk", "groq api", "gemini api",
    "mistral ai", "perplexity", "serper", "tavily", "claude", "replit ai", "cursor ai",
    
    # Operating Systems
    "linux", "ubuntu", "debian", "centos", "fedora", "arch", "macos", "windows", "ios", "android",
    "unix", "freebsd", "kali", "raspbian", "chrome os"
]

# Validation
if not GEMINI_API_KEY:
    raise RuntimeError("❌ GEMINI_API_KEY is not set in environment variables.")