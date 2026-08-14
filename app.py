from flask import Flask, render_template, request

from github_client import (
    get_repositories,
    get_repository_details,
    change_visibility,
    archive_repository,
    unarchive_repository,
    rename_repository,
    add_topics,
    create_readme,
    add_license,
    delete_repository
)

app = Flask(__name__)


# ==========================================================
# Home Dashboard
# ==========================================================

@app.route("/")
def home():

    repositories = get_repositories()

    return render_template(
        "index.html",
        repositories=repositories
    )


# ==========================================================
# Repository Details
# ==========================================================

@app.route("/repository/<repository_name>")
def repository_details(repository_name):

    result = get_repository_details(repository_name)

    if result["success"]:

        return render_template(
            "details.html",
            repository=result["data"]
        )

    return render_template(
        "details.html",
        repository=None,
        error=result["message"]
    )


# ==========================================================
# Helper Function
# ==========================================================

def process_action(action, repository, form):

    if action == "private":

        return change_visibility(
            repository,
            "private"
        )

    elif action == "public":

        return change_visibility(
            repository,
            "public"
        )

    elif action == "archive":

        return archive_repository(repository)

    elif action == "unarchive":

        return unarchive_repository(repository)

    elif action == "rename":

        prefix = form.get("rename_prefix", "").strip()
        suffix = form.get("rename_suffix", "").strip()

        new_name = f"{prefix}{repository}{suffix}"

        return rename_repository(
            repository,
            new_name
        )

    elif action == "topics":

        topics = form.get("topics", "")

        topic_list = [
            topic.strip()
            for topic in topics.split(",")
            if topic.strip()
        ]

        return add_topics(
            repository,
            topic_list
        )

    elif action == "readme":

        return create_readme(repository)

    elif action == "license":

        return add_license(repository)

    elif action == "delete":

        return delete_repository(repository)

    return {
        "success": False,
        "message": "Unknown Action"
    }
# ==========================================================
# Execute Bulk Action
# ==========================================================

@app.route("/selected", methods=["POST"])
def selected():

    selected_repositories = request.form.getlist("repositories")

    action = request.form.get("action")

    results = []

    if not selected_repositories:

        return render_template(
            "result.html",
            action=action,
            results=[],
            error="No repositories selected."
        )

    for repository in selected_repositories:

        result = process_action(
            action,
            repository,
            request.form
        )

        results.append({

            "repository": repository,

            "success": result.get(
                "success",
                False
            ),

            "message": result.get(
                "message",
                "Unknown Error"
            )

        })

    success_count = len(
        [r for r in results if r["success"]]
    )

    failed_count = len(results) - success_count

    return render_template(

        "result.html",

        action=action,

        results=results,

        total=len(results),

        success=success_count,

        failed=failed_count

    )


# ==========================================================
# Run Application
# ==========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )
