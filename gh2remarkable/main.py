import os
from typing import Optional, Annotated
import typer

from .generate_content import generate_html_content

app = typer.Typer()


@app.command()
def generate_html(
        owner: Annotated[str, typer.Argument(help='The owner of the GitHub repository/ies to generate HTML content from.')],
        repo: Annotated[Optional[str], typer.Argument(
            help='The name of the GitHub repository to generate HTML content from, unless all repositories of the owner should be included.')]=None):
    '''Generate HTML content from the README and issues of a GitHub repository and
    save it to a file that can be printed to your reMarkable.

    \b
    NB! You need to have a GitHub access token with the `repo` scope to use this command, and the
    token must be stored in an environment variable named `GITHUB_TOKEN_GH2REMARKABLE`.
    '''
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
