Rasengan
========

Validate &amp; Add Python package versions files to a repository in an Automated Way

### Workflow
![Workflow](https://raw.github.com/none-da/rasengan/master/work_flow.png)

User Story
---
User logs-in to the website using Github Authentication.
Authorizes the App in Github UI
A big text area is presented
Fills-in the versions of all packages(Could be a copy/paste from old versions files)
Clicks on `Validate` button at the bottom of the page
A new screen comes listing the versions submitted with a green(latest) or red(old) flags
There is a checkbox available against each package. Called `Pick Latest`. Latest ones(if already supplied) are checked by default.
A textbox containing the file name prefilled with the name `versions_2012_Nov_12.txt`
Clicks on `Generate Versions File` button at the bottom of the page.
A new screen comes telling `Versions file is ready :D` **Download** with a hyperlink
In the same screen you would find a empty textbox ask for the repo name to save the versions file which is built just now.
Clicks on `Save to Repo` and it gets committed and pushed.
