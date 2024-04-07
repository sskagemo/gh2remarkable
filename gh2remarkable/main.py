import os
import markdown
from html_template import header, footer
# from markdown.extensions import fenced_code
#import pdfkit

from get_content import get_file, get_issues


# Function to generate HTML content from the issues and README
def generate_html_content(owner, repo, branch, file_path, github_token):
    issues = get_issues(owner, repo, github_token)
    readme = get_file(owner, repo, branch, file_path, github_token)

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

    return html_content

# Generate PDF from the HTML file
#pdf_file = "/path/to/output.pdf"
#pdfkit.from_file(html_file, pdf_file)

if __name__ == "__main__":
    github_token = os.getenv('GITHUB_TOKEN_GH2REMARKABLE')

    # Replace 'owner' and 'repo' with the appropriate values for your GitHub project
    owner = "sskagemo"
    repo = "gh2remarkable"

    # Call the function that generates the HTML content of the README and issues
    html_content = generate_html_content(owner, repo, "main", "README.md", github_token)

    # Save the HTML content to a file
    html_file = "output.html"
    with open(html_file, "w") as file:
        file.write(html_content)


    print("HTML content generated successfully!")
    print(f"HTML file saved as {html_file}")
    #print(f"PDF file saved as {pdf_file}")
