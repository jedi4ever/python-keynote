# Python Keynote
## Description
> This is still Work in Progress

This package is able to read and write keynote files.

- We use appscript to execute applescript commands
- We are limited to the applescript commands that are exposed to applescript
- To go even further we use applescript UI automation to do more


## Things that won't work
- set background of slide, text item
- bulletlists
- create shapes (rectangle, circle etc)

## TODO
- see if we can the original files (audio, movies, images) using [`keynote-parse`](https://pypi.org/project/keynote-parser/)

## Notes

### Applescript & Python Strategies
- We tried using pyobjc with scriptengine , but found no way to pass a file to create files
- The iWorkAutomation site is still very usefull
- The one thing that was different is that there are no base_layout/masters

- We know appscript is deprecated , but it works and we can pass a file
- Related libraries on `keynote-js` in the Javascript ecosystem

### Applescript & GUI Automation
- We use an app called `ASTranslate` to translate applescript scripts to appscript python code
- To get the UI elements of the Keynote application we tried using Accessibility inspector by we found `UI Elements` to be easier to find them

### Applescript Permissions
- To be able to automate other processes we need Automation access.
- Unfortuneatly we can't set this and it has to be asked on first execution of the app
- If we got `user permission denied`, it won't ask again. Some say reinstalling the app will ask it again

- Privacy & Security > Full Disk Access
- Privacy & Security > Files & Folders
- Privacy & Security > Automation
- Privacy & Security > Accessibility # No difference
