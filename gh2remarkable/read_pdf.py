import fitz

def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

# Example usage
file_path = "../gh2remarkable/sskagemo_gh2remarkable.pdf"
content = read_pdf(file_path)
print(content)

example_issue = """
New issue: Add issues from rM
Description: 
When the PDF is read, any new pages that starts with "New
issue: ..." will create a new issue, where the text following New
issue will be used as the title.
In addition to a title there can be a Descritption and a list of
tags, separated by comma, and an assignee
Tags: enhancement 
Assigned to: sskagemo"""


def parse_issue_text(issue_text):
    issue_dict = {}
    lines = issue_text.strip().split("\n")
    for i, line in enumerate(lines):
        if line.startswith("New issue:"):
            issue_dict["Title"] = line.replace("New issue:", "").strip()
        elif line.startswith("Description:"):
            description = ""
            for j in range(i+1, len(lines)):
                if lines[j].startswith("Tags:"):
                    break
                description += lines[j] + "\n"
            issue_dict["Description"] = description.strip()
        elif line.startswith("Tags:"):
            tags = line.replace("Tags:", "").strip().split(",")
            issue_dict["Labels"] = [tag.strip() for tag in tags]
        elif line.startswith("Assigned to:"):
            issue_dict["Assigned to"] = line.replace("Assigned to:", "").strip()
    return issue_dict

issue_dict = parse_issue_text(example_issue)
for k, v in issue_dict.items():
    print(f"{k}: {v}")
