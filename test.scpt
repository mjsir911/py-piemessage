tell application "Messages"
    set targetService to 1st service whose service type = iMessage
    set targetBuddy to buddy '+15712411115' of targetService
    send "hi" to targetBuddy
end tell
