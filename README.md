Rasengan
========

Validate &amp; Add Python package versions files to a repository in an Automated Way

### Workflow
![Workflow](https://raw.github.com/none-da/rasengan/master/work_flow.png)

User Story
---
User logs-in to the website using Github Authentication.
    url:/users/login
Authorizes the App in Github UI
    url:/ (redirected to home after siging in)
A big text area is presented
Fills-in the versions of all packages(Could be a copy/paste from old versions files)
Clicks on `Validate` button at the bottom of the page
    url: submits to /versions/validate
A new screen comes listing the versions submitted with a green(latest) or red(old) flags
    url: @ /versions/validate
There is a checkbox available against each package. Called `Pick Latest`. Latest ones(if already supplied) are checked by default.
A textbox containing the file name prefilled with the name `versions_2012_Nov_12.txt`
Clicks on `Generate Versions File` button at the bottom of the page.
    url: submits to /versions/generate_file/
A new screen comes telling `Versions file is ready :D` **Download** with a hyperlink
    url: /versions/download?file=versions_2012_Nov_12.txt (application/text)
In the same screen you would find a empty textbox ask for the repo name to save the versions file which is built just now.
Clicks on `Save to Repo` and it gets committed and pushed.
    url: /versions/save_to_repo/ and redirects to the homepage
