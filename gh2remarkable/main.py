import os
import typer

from generate_content import generate_html_content
# from markdown.extensions import fenced_code
#import pdfkit
app = typer.Typer()

@app.command()
def generate_html(owner: str, repo: str):
    github_token = os.getenv('GITHUB_TOKEN_GH2REMARKABLE')
    # Call the function that generates the HTML content of the README and issues
    html_content = generate_html_content(owner, repo, "main", "README.md", github_token)
    # Save the HTML content to a file
    html_file = "output.html"
    with open(html_file, "w") as file:
        file.write(html_content)
    typer.echo("HTML content generated successfully!")
    typer.echo(f"HTML file saved as {html_file}")

if __name__ == "__main__":
    app()
