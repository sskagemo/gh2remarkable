# gh2remarkable - getting deep work done with your GitHub repo on an e-ink device
Making a PDF-report of the content on your GitHub repo, for you to work with on your favourite e-ink device, such as ReMarkable.

Disclaimer: This project makes massive use of Copilot ...

Ideally, this project should probably have been private for a while longer, but then I would have problems using the project on this project itself ... so please be patient with state of the project :-)

TODO: Change name to more generic? gh2pdf?

## Roadmap

### Version 1 - read only
- generating pdf from content on a GH repo
- specify different types of content (files, issues, discussions)
- filtering content
- as typer CLI, or possibly a textual TUI
- for both public and private repositories

### Version 2 - read and write
- adding checkboxes to the content, for "binary" actions, such as "close issue" or "bug" or priority
- adding textboxes to the content, giving the possibility to add comments
- comments will probably be drafts in new browser-tabs, for manual control before they are submitted