#!/usr/bin/env python3
"""
Push AutoPCB GitHub repo to GitHub.com
"""

import subprocess
import sys
from pathlib import Path


def push_to_github():
    """Push the AutoPCB repo to GitHub."""
    
    repo_path = Path("C:\Jarvis\workshop\autopcb_marketing\autopcb_github")
    
    print("AutoPCB GitHub Push Script")
    print("=" * 60)
    print()
    
    # Step 1: Initialize git (if not already)
    print("Step 1: Initialize git repository...")
    try:
        subprocess.run(["git", "init"], cwd=repo_path, check=True, capture_output=True)
        print("✓ Git initialized")
    except subprocess.CalledProcessError:
        print("✓ Git already initialized")
    
    print()
    
    # Step 2: Add all files
    print("Step 2: Adding files...")
    try:
        subprocess.run(["git", "add", "."], cwd=repo_path, check=True, capture_output=True)
        print("✓ Files added")
    except subprocess.CalledProcessError:
        print("✓ Files already staged")
    
    print()
    
    # Step 3: Commit
    print("Step 3: Committing...")
    try:
        subprocess.run(
            ["git", "commit", "-m", "Initial commit: AutoPCB demo repository"],
            cwd=repo_path,
            check=True,
            capture_output=True
        )
        print("✓ Committed")
    except subprocess.CalledProcessError:
        print("✓ Already committed")
    
    print()
    
    # Step 4: Ask for GitHub username
    print("Step 4: GitHub credentials")
    print("-" * 60)
    username = input("Enter your GitHub username: ").strip()
    token = input("Enter your GitHub personal access token: ").strip()
    
    # Step 5: Add remote
    print()
    print("Step 5: Adding GitHub remote...")
    remote_url = f"https://{username}:{token}@github.com/{username}/autopcb.git"
    try:
        subprocess.run(
            ["git", "remote", "add", "origin", remote_url],
            cwd=repo_path,
            check=True,
            capture_output=True
        )
        print("✓ Remote added")
    except subprocess.CalledProcessError as e:
        print(f"✗ Remote already exists: {e}")
    
    print()
    
    # Step 6: Push
    print("Step 6: Pushing to GitHub...")
    try:
        subprocess.run(
            ["git", "push", "-u", "origin", "main", "--force"],
            cwd=repo_path,
            check=True,
            capture_output=True,
            text=True
        )
        print("✓ Pushed successfully!")
        print()
        print(f"Your repo is live at: https://github.com/{username}/autopcb")
        print()
        print("Next steps:")
        print("  1. Share this link in LinkedIn posts")
        print("  2. Post in KiCad Discord server")
        print("  3. Submit to Hackaday")
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Push failed: {e}")
        print()
        print("Troubleshooting:")
        print("  - Make sure your GitHub token has 'repo' scope")
        print("  - Check that the repo doesn't already exist")
        print("  - Try creating the repo manually on GitHub.com first")


if __name__ == "__main__":
    push_to_github()
