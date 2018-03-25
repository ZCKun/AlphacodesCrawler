# https://wall.alphacoders.com/search.php?search=anime+girl

import requests
from bs4 import BeautifulSoup
import os
import sys


url = "https://wall.alphacoders.com/search.php?search=anime+girl&page={}"
headers = {
	"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0",
}


def request(url):
	resp = requests.get(url, headers=headers)
	if resp.status_code != requests.codes.OK:
		print("Request Error. Code: %d" % resp.status_code)
		sys.exit()
	return resp.text


def parser(url):
	resource = request(url)
	soup = BeautifulSoup(resource, "html.parser")

	if os.path.exists("./Alpha/") != True:
		os.mkdir("Alpha/")
	
	# ok i think i need using "findAll"
	thumbs = soup.findAll("div", class_="thumb-container-big")
	for thumb in thumbs:
		boxcaption = thumb.find("div", class_="boxcaption")
		overlay = boxcaption.find("div", class_="overlay")
		download_url = overlay.find("span", class_="download-button")['data-href']
	
		# we need get the id
		# https://initiate.alphacoders.com/download/wallpaper/678388/images2/jpg/0428534225
		id_name = download_url.split("wallpaper/")[1].split("/images")[0]

		# ok start download
		print("Start Download %s" % download_url)
		r = requests.get(download_url)
		if r.status_code != requests.codes.OK:
			print("%s download error.")
			continue

		with open("./Alpha/%s.jpg" % id_name, "wb") as f:
			f.write(r.content)



def main():
	for i in range(1, 100):
		parser(url.format(i))


if __name__ == "__main__":
	main()




