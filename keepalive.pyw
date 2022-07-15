import PySimpleGUI as sg
import time, pygame, os, pyautogui, signal, threading

pygame.init()

list_of_alarms = []

def get_time():
	'''Updates the time, checks if alarm should go off'''

	global list_of_alarms
	now = time.strftime("%H:%M:%S")
	window["-TIME-"].update(now)

	if list_of_alarms:
		for index, alarm in enumerate(list_of_alarms):
			if now == alarm:
				window["Stop"].update(disabled=False)
				list_of_alarms = list_of_alarms[index:]
				update()
				# Create and initialize the system for killing processes
				try:
					os.system("taskkill /f /im OUTLOOK.EXE")
				except:
					print("Outlook not running")
				try:
					os.system("taskkill /f /im lync.exe")
				except:
					print("Skype not running")
				try:
					os.system("taskkill /f /im Teams.exe")
				except:
					print("Teams not running")
				
				os.system("taskkill /f /im python.exe")
				os.system("taskkill /f /im pythonw.exe")
				window.close()
				exit()

def confirm_alarm():
	'''Obtains the alarm time, adds it to the list'''

	hour_val = values["-HR-"]
	minute_val = values["-MIN-"]
	keep = threading.Thread(target=dontsleep)
	keep.start()

	if hour_val and minute_val:
		list_of_alarms.append(f"{hour_val}:{minute_val}:00")
		window["Stop"].update(disabled=False)
	update()

def stop_alarm():
	'''Stops the alarm currently going off'''

	window["Stop"].update(disabled=True)
	list_of_alarms.pop(0)
	update()

def update():
	'''Updates the list of alarms'''

	window["-LST-"].update("")
	for alarm in list_of_alarms:
		window["-LST-"].update(window["-LST-"].get() + alarm + '\t')

def dontsleep():
	'''Keeps the computer from sleeping without interfering with main input'''
	
	while True:
		pyautogui.press('volumedown')
		time.sleep(1)
		pyautogui.press('volumeup')
		time.sleep(300)

clock_layout = [[sg.Text("", key="-TIME-",font=("ds-digital", 100),background_color="black",text_color="cyan")],
		[sg.Text("Set a Quit Time to turn on keep alive", size=(50, 1))],
		[sg.Text("When quit time happens the program will close Outlook, Skype, Teams, & itself", size=(60, 1))]]

alarm_layout = [[sg.Text("Hour", size=(20, 1)), sg.Text("Minute", size=(20, 1))],
		[sg.Input(key="-HR-", size=(20, 1)), sg.Input(key="-MIN-", size=(20, 1))],
		[sg.Text("", size=(40, 5), key="-LST-")],
		[sg.Button("Confirm", button_color=("white", "black")), sg.Button("Stop", disabled=True, button_color=("white", "black"))],
		[sg.Text("Stopping time will prevent closing but leave Keep Alive running", size=(60, 1))]]

shutdown_layout = [[sg.Text("Seconds", size=(20, 1))],
		[sg.Input(key="-SEC-", size=(20, 1))],
		[sg.Button("Shutdown", button_color=("white", "black")), sg.Button("Restart", button_color=("white", "black")), sg.Button("Calculator", button_color=("white", "black"))],
		[sg.Text("Input the amount of wait time you want in SECONDS then click either shutdown/restart", size=(65, 1))],
		[sg.Text("Consult the following quick reference table:", size=(60, 1))],
		[sg.Text("1800 = 30 Minutes", size=(30, 1))],
		[sg.Text("3600 = 1 Hour", size=(30, 1))],
		[sg.Text("7200 = 2 Hours", size=(30, 1))]]

layout = [[sg.TabGroup([[sg.Tab("Clock", clock_layout),
			sg.Tab("Quit Time", alarm_layout),
			sg.Tab("Shutdown/Restart", shutdown_layout)]])]]

window = sg.Window('Keep Alive', layout)

while True:
	event, values = window.read(timeout=100)
	if event == sg.WINDOW_CLOSED:
		break
	if event == "Confirm":
		confirm_alarm()
	if event == "Stop":
		stop_alarm()
	if event == "Shutdown":
		sec_val = values["-SEC-"]
		os.system("shutdown /s /t sec_val")
	if event == "Restart":
		sec_val = values["-SEC-"]
		os.system("shutdown /r /t sec_val")
	if event == "Calculator":
		os.system("start calc.exe")

	get_time()

window.close()
os.system("taskkill /f /im python.exe")
os.system("taskkill /f /im pythonw.exe")
exit()
