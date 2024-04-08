# gh2remarkable - getting deep work done with your GitHub repo on an e-ink device
Making a PDF-report of the content on your GitHub repo, for you to work with on your favourite e-ink device, such as ReMarkable.

Disclaimer: This project makes massive use of Copilot ...

Ideally, this project should probably have been private for a while longer, but then I would have problems using the project on this project itself ... so please be patient with state of the project :-)

TODO: Change name to more generic? gh2pdf?

## Usage

Basic usage to get the README and open issues on your reMarkable:
```bash
$ gh2remarkable sskagemo gh2remarkable
. . . . . Done!
Created sskagemo_gh2remarkable.html with the content from README.md
and alle open issues. Open the html-file in you browser and use the
"print to reMarkable"-function to get the document on your reMarkable
$
```

User and repo can be read from the current directory, if it is a git-repo that is
set up to push to Github.
```bash
$ gh2remarkable
Fetch content from user sskagemo and repository gh2remarkable? Y/n: y
. . . . . Done!
Created sskagemo_gh2remarkable.html with the content from README.md
and alle open issues. Open the html-file in you browser and use the
"print to reMarkable"-function to get the document on your reMarkable
$
```

Read back a PDF-file that has been on the reMarkable, and look for a "new issues"-section, and add the issues found there to Github:
```bash
$ gh2remarkable sskagemo_gh2remarkable.pdf
. . . . Done
Found 3 issues. Add the issues to Github? Y/n: y
New issue created: https://github.com/sskagemo/gh2remarkable/issues/2
New issue created: https://github.com/sskagemo/gh2remarkable/issues/3
New issue created: https://github.com/sskagemo/gh2remarkable/issues/4
$
```

Read back a PDF_file that has been on the reMarkable, and look for comments to
issues, in the form of new pages added after an existing issue. Add the comments
to the relevant issues.
```bash
$ gh2remarkable sskagemo_gh2remarkable.pdf
. . . . Done
Found a comment to issue 3. Add to issue? Y/n: Y
Link to comment: https://github.com/sskagemo/gh2remarkable/issues/3#issue-3483483
Found a comment to issue 4. Add to issue? Y/n: n
$
```


## Roadmap

- generating pdf from content on a GH repo
- specify different types of content (files, issues, discussions)
- filtering content
- as typer CLI, or possibly a textual TUI
- for both public and private repositories
- adding issues through the use of typed text, for instance with the type portfolio
- adding checkboxes to the content, for "binary" actions, such as "close issue" or "bug" or priority
- adding textboxes to the content, giving the possibility to add comments
- comments will probably be drafts in new browser-tabs, for manual control before they are submitted
