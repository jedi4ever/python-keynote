# Python Keynote Library
## Description
> This is still Work in Progress

This package is able to read and write keynote files.

- We use appscript to execute applescript commands
- We are limited to the applescript commands that are exposed to applescript
- To go even further we use applescript UI automation to do more

Remarks: 
- This will only work on MacOS as it needs applecript
- It can't be headless and needs a running UI/Login session
- It needs to have Keynote installed
- Needs a working installed Xcode environment

## TODO
- see if we can the original files (audio, movies, images):
    - using [`keynote-parse`](https://pypi.org/project/keynote-parser/)
    - or <https://github.com/paulhildebrandt/python-keynote/blob/master/keynote_api.py>
- set background of slide, text item
- create text items as bulletlists
- create shapes (rectangle, circle etc)

## Notes

### Applescript & Python Strategies
- We first tried to use pyobjc with scriptengine , but found no way to pass a file to create files or export a file
    - <https://github.com/DominikPalo/scripting-bridge-definitions/blob/master/com.apple.iWork.Keynote/Keynote.swift#L233>
    - <https://majestysoftware.wordpress.com/2015/03/31/swift-scripting-part-1/>
    - <https://github.com/tingraldi/SwiftScripting>
- It was certainly trial and error to get the right properties and syntax

- The iWorkAutomation site is very usefull to find those
    - <https://iworkautomation.com/keynote/application.html>
    - The one property that was different then expected was that there are no masters properties as described

- Appscript can be found at : <https://appscript.sourceforge.io/py-appscript/index.html>
- We know appscript is deprecated , but hey it works and we can pass a file
- We use an app called `ASTranslate` to translate applescript scripts to appscript python code
    - <https://appscript.sourceforge.io/tools.html>
    - beware that the indexed in applescript start from 1 , in appscript from 0

- A related library `keynote-js` can be found for the Javascript ecosystem:
    - <https://github.com/macintoshhelper/keynote-js/blob/master/src/document.ts>
    - <https://stackoverflow.com/questions/44422191/how-to-create-or-edit-keynote-master-slides-using-javascript-for-automation>


### Applescript & GUI Automation
- Some things are not possible with plain scripting keynote and we have to resort to UI Automation
- Initially we tried using Accessibility inspector but we found executing `UI Elements` in applescript made it easier to find them

### Applescript Permissions
- To be able to automate other processes we need Automation permission on MacOS.
- Unfortuneatly we can't set this and it has to be asked on first execution of the app
- If we got `user permission denied`, it won't ask again. Some say reinstalling the app will ask it again

- Privacy & Security > Full Disk Access
- Privacy & Security > Files & Folders
- Privacy & Security > Automation
- Privacy & Security > Accessibility # No difference
