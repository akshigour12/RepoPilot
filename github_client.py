import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()


# ==========================================================
# Configuration
# ==========================================================

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER = os.getenv("GITHUB_OWNER")

BASE_URL = "https://api.github.com"

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}


# ==========================================================
# Standard GitHub Request Helper
# ==========================================================

def github_request(method, endpoint, payload=None):

    url = f"{BASE_URL}{endpoint}"

    try:
        response = requests.request(
            method=method,
            url=url,
            headers=HEADERS,
            json=payload,
            timeout=15
        )
    except requests.RequestException as error:
        return {
            "success": False,
            "status_code": 0,
            "data": {},
            "message": f"Network error: {error}"
        }

    if response.status_code == 204:
        return {
            "success": True,
            "status_code": 204,
            "data": None,
            "message": "Success"
        }

    try:
        data = response.json()
    except ValueError:
        data = {}

    if response.ok:
        return {
            "success": True,
            "status_code": response.status_code,
            "data": data,
            "message": "Success"
        }

    return {
        "success": False,
        "status_code": response.status_code,
        "data": data,
        "message": data.get(
            "message",
            f"GitHub API error: {response.status_code}"
        )
    }


# ==========================================================
# List All Repositories
# ==========================================================

def get_repositories():

    result = github_request(
        "GET",
        "/user/repos?per_page=100&sort=updated"
    )

    if result["success"]:
        return result["data"]

    print(
        f"GitHub repository request failed "
        f"({result['status_code']}): {result['message']}"
    )

    return []


# ==========================================================
# Get Repository Details
# ==========================================================

def get_repository_details(repository_name):

    return github_request(
        "GET",
        f"/repos/{GITHUB_OWNER}/{repository_name}"
    )


# ==========================================================
# Change Repository Visibility
# ==========================================================

def change_visibility(repository_name, visibility):

    payload = {
        "private": visibility == "private"
    }

    result = github_request(
        "PATCH",
        f"/repos/{GITHUB_OWNER}/{repository_name}",
        payload
    )

    if result["success"]:
        return {
            "success": True,
            "message": f"Repository changed to {visibility}"
        }

    return result


# ==========================================================
# Archive Repository
# ==========================================================

def archive_repository(repository_name):

    result = github_request(
        "PATCH",
        f"/repos/{GITHUB_OWNER}/{repository_name}",
        {
            "archived": True
        }
    )

    if result["success"]:
        return {
            "success": True,
            "message": "Repository archived successfully"
        }

    return result


# ==========================================================
# Unarchive Repository
# ==========================================================

def unarchive_repository(repository_name):

    result = github_request(
        "PATCH",
        f"/repos/{GITHUB_OWNER}/{repository_name}",
        {
            "archived": False
        }
    )

    if result["success"]:
        return {
            "success": True,
            "message": "Repository unarchived successfully"
        }

    return result


# ==========================================================
# Rename Repository
# ==========================================================

def rename_repository(repository_name, new_name):

    if not new_name:
        return {
            "success": False,
            "message": "New repository name cannot be empty"
        }

    result = github_request(
        "PATCH",
        f"/repos/{GITHUB_OWNER}/{repository_name}",
        {
            "name": new_name
        }
    )

    if result["success"]:
        return {
            "success": True,
            "message": f"Repository renamed to {new_name}"
        }

    return result


# ==========================================================
# Get Repository Topics
# ==========================================================

def get_topics(repository_name):

    result = github_request(
        "GET",
        f"/repos/{GITHUB_OWNER}/{repository_name}/topics"
    )

    if result["success"]:
        return result["data"].get("names", [])

    return []


# ==========================================================
# Replace Repository Topics
# ==========================================================

def replace_topics(repository_name, topics):

    payload = {
        "names": topics
    }

    result = github_request(
        "PUT",
        f"/repos/{GITHUB_OWNER}/{repository_name}/topics",
        payload
    )

    if result["success"]:
        return {
            "success": True,
            "message": "Topics updated successfully"
        }

    return result


# ==========================================================
# Add Topics
# ==========================================================

def add_topics(repository_name, new_topics):

    if not new_topics:
        return {
            "success": False,
            "message": "No topics were provided"
        }

    current_topics = get_topics(repository_name)

    merged_topics = sorted(
        set(current_topics + new_topics)
    )

    return replace_topics(
        repository_name,
        merged_topics
    )


# ==========================================================
# Check README
# ==========================================================

def has_readme(repository_name):

    result = github_request(
        "GET",
        f"/repos/{GITHUB_OWNER}/{repository_name}/readme"
    )

    return result["success"]


# ==========================================================
# Create README
# ==========================================================

def create_readme(repository_name):

    if has_readme(repository_name):
        return {
            "success": False,
            "message": "README already exists"
        }

    content = (
        f"# {repository_name}\n\n"
        "Created automatically using RepoPilot."
    )

    payload = {
        "message": "Add README using RepoPilot",
        "content": base64.b64encode(
            content.encode("utf-8")
        ).decode("utf-8")
    }

    result = github_request(
        "PUT",
        f"/repos/{GITHUB_OWNER}/{repository_name}/contents/README.md",
        payload
    )

    if result["success"]:
        return {
            "success": True,
            "message": "README created successfully"
        }

    return result


# ==========================================================
# Check LICENSE
# ==========================================================

def has_license(repository_name):

    result = github_request(
        "GET",
        f"/repos/{GITHUB_OWNER}/{repository_name}/license"
    )

    return result["success"]


# ==========================================================
# Add MIT LICENSE
# ==========================================================

def add_license(repository_name):

    if has_license(repository_name):
        return {
            "success": False,
            "message": "LICENSE already exists"
        }

    license_text = f"""MIT License

Copyright (c) 2026 {GITHUB_OWNER}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

    payload = {
        "message": "Add MIT License using RepoPilot",
        "content": base64.b64encode(
            license_text.encode("utf-8")
        ).decode("utf-8")
    }

    result = github_request(
        "PUT",
        f"/repos/{GITHUB_OWNER}/{repository_name}/contents/LICENSE",
        payload
    )

    if result["success"]:
        return {
            "success": True,
            "message": "LICENSE added successfully"
        }

    return result


# ==========================================================
# Delete Repository
# ==========================================================

def delete_repository(repository_name):

    result = github_request(
        "DELETE",
        f"/repos/{GITHUB_OWNER}/{repository_name}"
    )

    if result["success"]:
        return {
            "success": True,
            "message": "Repository deleted successfully"
        }

    return result
