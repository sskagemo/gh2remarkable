from github import Github

def create_github_issue(issue_data):
    # Replace 'YOUR_ACCESS_TOKEN' with your actual GitHub access token
    access_token = 'YOUR_ACCESS_TOKEN'
    # Replace 'YOUR_USERNAME' with your actual GitHub username
    username = 'YOUR_USERNAME'
    # Replace 'YOUR_REPOSITORY' with your actual GitHub repository name
    repository = 'YOUR_REPOSITORY'

    # Create a PyGithub instance using the access token
    g = Github(access_token)

    # Get the repository
    repo = g.get_user(username).get_repo(repository)

    # Extract the issue data
    title = issue_data['title']
    description = issue_data['description']
    labels = issue_data['labels']
    assignee = issue_data['assignee']

    # Create the issue
    issue = repo.create_issue(title=title, body=description, labels=labels, assignee=assignee)

    # Print the URL of the created issue
    print(f"New issue created: {issue.html_url}")

# Example usage
issue_data = {
    'title': 'Example Issue',
    'description': 'This is an example issue',
    'labels': ['bug', 'enhancement'],
    'assignee': 'octocat'
}

create_github_issue(issue_data)