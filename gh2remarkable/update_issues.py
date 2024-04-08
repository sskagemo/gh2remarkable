from github import Github, Issue
from github import Auth


def create_github_issue(issue_data, user, repo, access_token) -> Issue.Issue:
    
    auth = Auth.Token(access_token)
    # Create a PyGithub instance using the access token
    g = Github(auth=auth)

    # Get the repository
    repo = g.get_user(user).get_repo(repo)

    # Extract the issue data
    title = issue_data['title']
    description = issue_data['description']
    labels = issue_data['labels']

    # Create the issue
    issue = repo.create_issue(title=title, body=description, labels=labels)

    g.close()
    return issue

# Example usage

if __name__ == "__main__":
    import os
    github_token = os.getenv('GITHUB_TOKEN_GH2REMARKABLE')


    issue_data = {
        'title': 'Add section for new issues in the generated PDF',
        'description': '''A new section should be added to the generated PDF that indicates that all following text are new issues. 
        The section should be clearly marked and easy to identify, and also include information about how the issues should be formatted.''',
        'labels': ['enhancement'],
    }

    issue = create_github_issue(issue_data, 'sskagemo', 'gh2remarkable', github_token)
        # Print the URL of the created issue

    print(f"New issue created: {issue.html_url}")
