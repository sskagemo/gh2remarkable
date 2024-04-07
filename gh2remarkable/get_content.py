import requests

def get_file(owner, repo, branch, file_path, github_token) -> bytes:
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


def get_issues(owner, repo, github_token) -> list:
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
