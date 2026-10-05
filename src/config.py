import os
from dotenv import load_dotenv

load_dotenv()

# Specify the maximum population size
max_population = int(os.getenv("MAX_POPULATION", 100))

# The N-queen
N = int(os.getenv("N", 8))