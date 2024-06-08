from dotenv import load_dotenv
import os

load_dotenv()

NASA_API_KEY = os.getenv('NASA_API_KEY')
print("NASA_API_KEY:", NASA_API_KEY)
