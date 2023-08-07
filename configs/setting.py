import os
from dotenv import load_dotenv

# This loads the variables from .env
load_dotenv()


# General Config
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
API_PREFIX = "/api/v1"

# Database Config

DATABASE_URL = os.getenv("DATABASE_URL")

# HuggingFace Transformers Config
TRANSFORMERS_API_KEY = os.getenv("TRANSFORMERS_API_KEY")

# Vector Search Config
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Visualization Configs (for example, if you have some)
CHART_COLORS = ["#56B4E9", "#D55E00", "#009E73", "#F0E442", "#0072B2", "#D3A487"]
