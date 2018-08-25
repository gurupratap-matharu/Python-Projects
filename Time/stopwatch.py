#! python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the programs's instructions.
print('''Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl - C to quit.''')

input()   # Press Enter to begin
print('STARTED')
print('*' * 80)
print('\tLap Time\tTotal Time', end='')
startTime = time.time() # get the first lap's start time.

lastTime = startTime
lapNum = 1

try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)

		print('Lap #%s: %s\t\t%s' % ( lapNum, lapTime, totalTime),end='')
		lapNum += 1
		lastTime = time.time() # reset the last lap time

except KeyboardInterrupt:
	# Handle the Ctrl-C exception to keep its error message from displaying.
	print('\nDone.')

