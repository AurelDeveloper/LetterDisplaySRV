import subprocess

def main():
    subprocess.run(["python", "./utils/fetcher.py"])
    subprocess.run(["python", "./utils/extractor.py"])
    subprocess.run(["python", "./utils/upload.py"])

if __name__ == "__main__":
    main()