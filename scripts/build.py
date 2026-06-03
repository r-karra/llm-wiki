import os
import subprocess
import datetime

# --- CONFIGURATION ---
HOME = os.path.expanduser("~")
WIKI_ROOT = os.path.join(HOME, "llm-wiki")
RAW_DIR = os.path.join(WIKI_ROOT, "raw")
WIKI_DIR = os.path.join(WIKI_ROOT, "wiki")
TOPICS_DIR = os.path.join(WIKI_ROOT, "wiki", "topics")
GITHUB_REPO = os.path.join(HOME, "learn-quantum-AI")
GOOGLE_DOC_URL = "https://docs.google.com/document/d/1RSezpbxa5_VNKxc4tARunh34F83lU8si50qgosN0fbk/edit"

def sync_github():
    """Pulls latest notebooks from GitHub and copies them to raw/."""
    print(f"--- Syncing GitHub: {GITHUB_REPO} ---")
    if os.path.exists(GITHUB_REPO):
        try:
            subprocess.run(["git", "-C", GITHUB_REPO, "pull"], check=True, capture_output=True)
            print("Successfully pulled GitHub updates.")
        except Exception as e:
            print(f"Skipping git pull: {e}")

        # Mapping of folders to search
        folders = ["Hands-on LLMs", "Use a quantum computer today-IBM", "DSA in Python-Jovian_freecodecamp"]
        for folder in folders:
            src = os.path.join(GITHUB_REPO, folder)
            if os.path.exists(src):
                print(f"Copying notebooks from {folder}...")
                os.system(f"cp '{src}'/*.ipynb '{RAW_DIR}/' 2>/dev/null")
    else:
        print("GitHub repo folder not found locally.")

def scan_raw_and_update_wiki():
    """Scans the raw/ folder and ensures they are mentioned in the wiki."""
    print("\n--- Scanning RAW folder for new materials ---")
    raw_files = [f for f in os.listdir(RAW_DIR) if f.endswith(('.ipynb', '.pdf', '.txt', '.md'))]
    
    # Simple logic to ensure each raw file has a mention in the index or a topic
    # In a full 'Auto Mode', the LLM agent runs this and then processes the content.
    print(f"Found {len(raw_files)} raw source files.")
    for f in raw_files:
        print(f" - Ready for ingestion: {f}")

def build_dist():
    """Placeholder for converting Markdown to a static site (HTML)."""
    print("\n--- Building Static Site (dist/) ---")
    dist_dir = os.path.join(WIKI_ROOT, "dist")
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)
    
    # In a real implementation, you would use 'mkdocs build' or a custom MD->HTML converter here.
    with open(os.path.join(dist_dir, "index.html"), "w") as f:
        f.write("<html><body><h1>LLM Wiki Build</h1><p>Last updated: " + str(datetime.datetime.now()) + "</p></body></html>")
    print(f"Static site build complete in {dist_dir}")

def run_all():
    sync_github()
    scan_raw_and_update_wiki()
    build_dist()
    print("\n--- AUTO-MODE COMPLETE ---")
    print(f"NOTE: To fetch the Google Doc, ask the Gemini Agent: 'Fetch my Google Doc and update the wiki.'")

if __name__ == "__main__":
    run_all()
