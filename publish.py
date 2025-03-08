#!/usr/bin/env python
"""Build and publish the package to PyPI."""
import os
import subprocess
import sys

def run_command(command):
    """Run a command and return its exit code."""
    print(f"Running: {command}")
    return subprocess.call(command, shell=True)

def main():
    """Build and publish to PyPI."""
    # Clean previous builds
    if os.path.exists("dist"):
        print("Removing previous builds...")
        run_command("rmdir /s /q dist")  # Windows command
    
    if os.path.exists("build"):
        print("Removing build directory...")
        run_command("rmdir /s /q build")  # Windows command
    
    if os.path.exists("src/lmstudio_client.egg-info"):
        print("Removing egg-info...")
        run_command("rmdir /s /q src/lmstudio_client.egg-info")  # Windows command
        
    # Build the distribution
    print("Building distribution...")
    exit_code = run_command("python -m build")
    if exit_code != 0:
        print("Error: Build failed.")
        sys.exit(exit_code)
    
    # Upload to PyPI
    print("Uploading to PyPI...")
    if "--test" in sys.argv:
        exit_code = run_command("python -m twine upload --repository testpypi dist/*")
    else:
        exit_code = run_command("python -m twine upload dist/*")
    
    if exit_code != 0:
        print("Error: Upload failed.")
        sys.exit(exit_code)
    
    print("Package successfully published to PyPI!")

if __name__ == "__main__":
    main()