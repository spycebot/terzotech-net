# /usr/bin/env/python3
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def datestamp() -> str:
	"""Pass back a date stamp string
	appropriately formatted for appending
	onto a file name."""
	dstring = datetime.now().strftime("%Y%m%d_%H%M%S")
	return dstring

def list_to_string(tlist) -> str:
	"""Convert list of page text into text
	file ready string"""
	tstring = ""
	for clv in tlist:
		tstring += (clv + "\n")
	return tstring

def site_stamp(r_url = 'http://www.terzotech.net') -> str:
	"""Produce site name stamp from site URL for save file name."""
	# print(r_url[:7])
	# Typical use case with lots of forward slash
	#r_url = "https://www.dw.com/en/top-stories/s-9097"
	if r_url[:8] == "https://":
		r_url = r_url[8:]
	if r_url[:7] == "http://":
		r_url = r_url[7:]
	if r_url[:4] == "www.":
		r_url = r_url[4:]
	# print(r_url)
	sstamp = r_url.replace("/", "_")
	return sstamp

def length_to_list_of_strings(t_length: int) -> list:
	"""Based on the input target length, return a list
	populated with strings from zero to target integer"""
	out = []
	for clv in range(t_length):
		out.append(str(clv))
	return out

def main_old() -> None:
	"""Coordinating function"""

	site_url = "http://terzotech.net"

	print("Site:", site_url)

	print("[Enter] to acept, [X] to exit, or enter new URL")

	# User URL
	u_url = input()

	print("u_url:",  str(u_url))

	if u_url.lower() in ["x", "exit"]:
		exit()

	if u_url == "":
		response = requests.get(site_url)
	else:
		response = requests.get(u_url)

	# response = requests.get("https://www.dw.com/en/top-stories/s-9097")

	soup = BeautifulSoup(response.text, 'html.parser')

	# print(soup.prettify())

	print_list = []
	tag_list = soup.find_all()

	"""Iterate through tag list, selecting
	image alt text and tag strings,
	while skipping duplicates
	ctag is Current Tag
	1. Acquire candidate string from current tag
	2. Split cstring and check for length
	3. Check whether cstring is already in list
	4. Append cstring to list
	"""
	for ctag in tag_list:
	# 	print(ctag)
		if ctag.get("alt") and (ctag["alt"] not in print_list):
			print_list.append(ctag["alt"])
		if ctag.get("title") and (ctag["title"] not in print_list):
			print_list.append(ctag["title"])
		if ctag.name in ['p', 'a', "blockquote"] and ctag.string and (ctag.string not in print_list):
			print_list.append(ctag.string)

	print("Finally:")

	for citem in print_list:
		print(citem)

	with open(f"../text/{datestamp()}_{site_stamp()}.txt", "w") as fhandler:
			fhandler.write(list_to_string(print_list))

def fetch_text(t_url: str) -> bool:
	"""Capture web page text and save to disk"""
	print("Menu option fetch text")
	response = requests.get(t_url)
	soup = BeautifulSoup(response.text, 'html.parser')
	print_list = []
	tag_list = soup.find_all()

	"""Iterate through tag list, selecting
	image alt text and tag strings,
	while skipping duplicates
	ctag is Current Tag
	1. Acquire candidate string from current tag
	2. Split cstring and check for length
	3. Check whether cstring is already in list
	4. Append cstring to list
	"""
	for ctag in tag_list:
		if ctag.get("alt") and (ctag["alt"] not in print_list):
			print_list.append(ctag["alt"])
		if ctag.get("title") and (ctag["title"] not in print_list):
			print_list.append(ctag["title"])
		if ctag.name in ['p', 'a', "blockquote"] and ctag.string and (ctag.string not in print_list):
			print_list.append(ctag.string)

	with open(f"../text/{datestamp()}_{site_stamp(t_url)}.txt", "w") as fhandler:
			fhandler.write(list_to_string(print_list))
	return True

def fetch_code(t_url: str) -> bool:
	"""Capture web page code (HTML) and save to disk"""
	print("Menu option fetch code")
	return True

def fetch_text_and_code(t_url: str) -> bool:
	"""Capture web page, save text as text, and save code as code"""
	print("Menu optiom fetch text and code""")
	return True

def main() -> None:
	"""Application menu driven loop"""
	instructions = "Enter site number,\nnew URL, \nor [x] to eXit."
	site_list = [
		"http://terzotech.net",
		"https://www.dw.com/en/top-stories/s-9097",
		"https://www.rte.ie/news/",
		"https://www.nytimes.com/",
		"https://edition.cnn.com/"
	]
	for m_option in range(len(site_list)):
		print(f"[{m_option}] {site_list[m_option]}")
	# print(length_to_list_of_strings(5))
	menu_input_one = ""
	menu_input_two = ""
	# print(range(len(site_list)))

	while menu_input_one.lower() not in ["x", "exit", "q", "quit"]:
		print(instructions)
		menu_input_one = input("[> ")
		if menu_input_one in length_to_list_of_strings(len(site_list)):
			target_url = site_list[int(menu_input_one)]
			print(target_url)
		else:
			print(f"User: {menu_input_one}")
			target_url = menu_input_one
		if menu_input_one.lower() not in ["x", "exit", "q", "quit"]:
			print("[A]udio, [C]ode or [B]oth")
			menu_input_two = input("[> ")
			if menu_input_two.lower() in ["a", "audio", "t", "text"]:
				fetch_text(target_url)
			elif menu_input_two.lower() in ["c", "code"]:
				fetch_code(target_url)
		elif menu_input_two.lower() in ["b", "both"]:
			fetch_text_and_code(target_url)

if __name__ == "__main__":
	main()
	# print(site_stamp())

