import os
import subprocess

def sync_github_repo():
    home = os.path.expanduser("~")
    repo_path = os.path.join(home, "learn-quantum-AI")
    wiki_raw_path = os.path.join(home, "llm-wiki", "raw")
    
    print(f"--- Syncing GitHub Repo: {repo_path} ---")
    if os.path.exists(repo_path):
        try:
            # Attempt to pull latest changes if it's a git repo
            subprocess.run(["git", "-C", repo_path, "pull"], check=True)
            print("Successfully pulled latest changes from GitHub.")
        except Exception as e:
            print(f"Note: Could not pull from GitHub (might be offline or no remote): {e}")
        
        # Copy new/updated notebooks to raw
        print(f"Copying notebooks to {wiki_raw_path}...")
        os.system(f"cp '{repo_path}/Hands-on LLMs'/*.ipynb '{wiki_raw_path}/' 2>/dev/null")
        os.system(f"cp '{repo_path}/Use a quantum computer today-IBM'/*.ipynb '{wiki_raw_path}/' 2>/dev/null")
        os.system(f"cp '{repo_path}/DSA in Python-Jovian_freecodecamp'/*.ipynb '{wiki_raw_path}/' 2>/dev/null")
    else:
        print(f"Error: Repo path {repo_path} not found.")

def build_wiki():
    print("\n--- Starting Wiki Build ---")
    
    config_path = 'config.yaml'
    if os.path.exists(config_path):
        print(f"Loading configuration from {config_path}")
    
    wiki_dir = 'wiki'
    topics_dir = 'wiki/topics'
    
    for d in [wiki_dir, topics_dir]:
        if os.path.exists(d):
            files = [f for f in os.listdir(d) if f.endswith('.md')]
            print(f"Found {len(files)} markdown files in {d}")

    if not os.path.exists('dist'):
        os.makedirs('dist')
        print("Created 'dist/' directory.")
        
    print("Build complete (simulated).")

if __name__ == "__main__":
    # In a real scenario, we'd also trigger the Google Doc fetch here 
    # via an API call or by asking the agent to fetch the URL.
    sync_github_repo()
    build_wiki()
