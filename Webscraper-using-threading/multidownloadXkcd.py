#! python3
# multiownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd


def downloadXkcd(startComic, endComic):
	for urlNumber in range(startComic, endComic):
		# Download the page.
		print('Downloading page https://xkcd.com/%s...' % (urlNumber))

		res = requests.get('https://xkcd.com/%s' % (urlNumber))
		res.raise_for_status()

		soup = bs4.BeautifulSoup(res.text)

		# Find the URL of the comic image element.
		comicElem = soup.select('#comic img')
		if comicElem == []:
			print('I couldn\'t find the comic image.')
		else:
			comicUrl = 'https:' + comicElem[0].get('src')
			#Download the image.

			print('Downloading image %s...'  % (comicUrl))

			res = requests.get(comicUrl)
			res.raise_for_status()


			# Save the image to ./xkcd.

			imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

			for chunk in res.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()



# Create and start the Thread objects.

downloadThreads = [] # a list of all the Thread Objects.

for i in range(0, 1400, 100):   # loops 14 times, creates 14 threads
	threadObj = threading.Thread(target=downloadXkcd, args=(i, i+99))
	downloadThreads.append(threadObj)
	threadObj.start()




# Wait for all threads to end.
for i in downloadThreads:
	i.join()
print('Done.')





