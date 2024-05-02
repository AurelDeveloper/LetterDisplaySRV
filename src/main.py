import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

def main():
    env_vars = os.environ.copy()
    subprocess.run(["python", "./utils/fetcher.py"], env=env_vars)
    subprocess.run(["python", "./utils/extractor.py"], env=env_vars)

if __name__ == "__main__":
    main()