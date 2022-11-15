# Python-Keep-Alive
A simple python program that will manage some functions of Windows for you

----------

## Pre-Requisites
You will need the following in your imports:
1. PySimpleGUI
2. Time
3. PyGame
4. OS
5. PyAutoGUI
6. Signal
7. Threading

From this list PySimpleGUI, PyGame, and PyAutoGUI will need to be installed through pip.

----------

## Functionality
This program simply supplies you with a clock(in 24h format) and an alarm interface in the first two tabs.  When an alarm is set it will appear in the alarms list directly below the input boxes and when an input time is reached the program will close the primary corporate communication applications which are:
1. Outlook
3. Microsoft Teams

Once those applications are shutdown the program will then kill any other threads it has started then shut itself down.  When a quit time is entered the keep alive function of the application will start up in a separate thread and toggle the volume down and up by 1 every 5 minutes.  This will prevent the machine from sleeping or resetting your status in the communication apps to "away".  Finally the Shutdown/Restart tab is for scheduling a shutdown or reboot of the machine if needed.  It uses the built in Windows function for this and will take the time to shutdown as an amount of seconds the user enters.  There is a quick reference table at the bottom for convenience however if more time is needed then the calculator button will open that app on the machine so a different amount of time can be calculated.

----------

## Screenshots

![Clock](https://user-images.githubusercontent.com/42878642/179229058-0c9f8bdd-2aef-40a3-930a-b9a25269b03b.PNG)

![quit](https://user-images.githubusercontent.com/42878642/179229077-3ef2f937-2f42-4fe8-9516-a6d77ba42812.PNG)

![shutdown](https://user-images.githubusercontent.com/42878642/179229094-f7582ca6-14f7-4208-87ad-bd2469c67e3c.PNG)
