#! python3
# countdown.py - A simple countdown script.

import time, subprocess, webbrowser


timeLeft = 20
while timeLeft > 0:
	print(timeLeft)
	time.sleep(1)
	timeLeft -= 1



subprocess.Popen(['open', '/Applications/Calculator.app'])

