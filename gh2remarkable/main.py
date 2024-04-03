import requests
import os
import markdown
from html_template import header, footer
# from markdown.extensions import fenced_code
#import pdfkit

github_token = os.getenv('GITHUB_TOKEN_GH2REMARKABLE')

def get_file(owner, repo, branch, file_path):
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file_path}"
    headers = {
        'Authorization': f'Bearer {github_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to download file. Status code: {response.status_code}, response: {response.text}")
        return None


def get_issues(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {
        'X-GitHub-Api-Version': '2022-11-28',
        'Authorization': f'Bearer {github_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        issues = response.json()
        for issue in issues:
            if issue['comments'] > 0:
                comments_url = issue['comments_url']
                comments_response = requests.get(comments_url, headers=headers)
                if comments_response.status_code == 200:
                    comments = comments_response.json()
                    issue['comment_content'] = [comment['body'] for comment in comments]
                else:
                    print(f"Failed to fetch comments for issue {issue['number']}. Status code: {comments_response.status_code}, response: {comments_response.text}")
        return issues
    else:
        print(f"Failed to fetch issues. Status code: {response.status_code}, response: {response.text}")


# Replace 'owner' and 'repo' with the appropriate values for your GitHub project
owner = "sskagemo"
repo = "gh2remarkable"

issues = get_issues(owner, repo)
readme = get_file(owner, repo, "main", "README.md")



# Generate HTML content from the issues and README
html_content = header.replace("[[[title]]]", f"{owner}/{repo}")
html_content += f'<h1 style="text-align: center; background-color: white">Fra GitHub: {owner}/{repo}</h1>'
html_content += markdown.markdown(readme.decode('utf-8'))
html_content += '<div id="issues"><h1>Issues: Alle åpne issues</h1>'
for issue in issues:
    html_content += f"<h2><a href={issue['html_url']}>#{issue['number']}</a>: {issue['title']}</h2>"
    html_content += f"<p>{markdown.markdown(issue['body'], extensions=['fenced_code'])}</p>" if issue['body'] else ""
    html_content += "<ul>"
    html_content += f"<li>State: {issue['state']}</li>"
    html_content += f"<li>Created: {issue['created_at']} and last updated {issue['updated_at']}</li>"
    html_content += f"<li>Assignee: {'no assignee' if issue['assignee'] == None else issue['assignee'].get('login', 'no assignee')}</li>"
    html_content += f"<li>Author: {issue['user']['login']}</li>"
    html_content += f"<li>Comments: {issue['comments']}</li>"
    if issue['comments'] > 0:
        html_content += "<ul>"
        for comment in issue['comment_content']:
            html_content += f"<li>{markdown.markdown(comment, extensions=['fenced_code'])}</li>"
        html_content += "</ul>"
    html_content += "</ul>"
html_content += "</div>" + footer
# Save the HTML content to a file
html_file = "output.html"
with open(html_file, "w") as file:
    file.write(html_content)

# Generate PDF from the HTML file
#pdf_file = "/path/to/output.pdf"
#pdfkit.from_file(html_file, pdf_file)