# https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics

import os
from urllib.request import urlretrieve
import tarfile
import zipfile
import sys
import csv

def get_data(data):

	if data == "dummy":
		return "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
	elif data == "subset":
		maybe_download_and_extract("subset")
	elif data == "380000":
		data_set = []

		with open('./data_set/lyrics.csv') as csvfile:
			csv_reader = csv.reader(csvfile)
			# print(csv_reader.shape)
			for i,row in enumerate(csv_reader):
				if(i == 0):
					continue
				data_set.append((row[5],row[4],row[2]))
		return data_set



def maybe_download_and_extract(data):

	main_directory = "./data_set/"


	url = ""

	if not os.path.exists(main_directory):
		os.makedirs(main_directory)
		if data == "subset":
			url = "http://static.echonest.com/millionsongsubset_full.tar.gz"

		filename = url.split('/')[-1]
		file_path = os.path.join(main_directory, filename)
		ziped = file_path
		file_path, _ = urlretrieve(url=url, filename=file_path, reporthook=_print_download_progress)

		print()
		print("Download finished. Extracting files.")
		if file_path.endswith(".zip"):
		    zipfile.ZipFile(file=file_path, mode="r").extractall(main_directory)
		elif file_path.endswith((".tar.gz", ".tgz")):
		    tarfile.open(name=file_path, mode="r:gz").extractall(main_directory)
		print("Done.")

		os.remove(ziped)

def _print_download_progress(count, block_size, total_size):
	pct_complete = float(count * block_size) / total_size
	msg = "\r- Download progress: {0:.1%}".format(pct_complete)
	sys.stdout.write(msg)
	sys.stdout.flush()