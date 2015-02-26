"""
Created on Sun Feb 22 13:41 2015

@author: Franton Lin

"""

"""
	NEWS variables:
	- url     : the URL of the referred web content,
	- title   : the title of the content at the URL,
	- text    : the content text,
	- language: the content language,
	- author  : for news items and images, the author,
	- date    : for news items, the publication date.
"""

import re
import cPickle
from pattern.web import Facebook, NEWS, COMMENTS, LIKES, FRIENDS
import csv
import matplotlib.pyplot as plt
import numpy as np

# removed my key
def fetch_data(data="facebook.pickle", friends_count=1000, news_count=100, key='REMOVED MY KEY'):
	""" Fetches link data from given key for the specified number 
		of friends and the specified number of posts and saves it
		to a facebook.pickle file

		data: name of data file to save to (default: facebook.pickle)
		friends_count: number of friends to search through (default: 1000)
		news_count: number of each friends' posts to search through (default: 100)
		key: the key for pattern to access Facebook
	"""
	print "Fetching data..."

	# Get the data
	fb = Facebook(license=key)
	me = fb.profile()
	print me
	counter = 1;

	link_counts = {"num_posts":0, "num_links":0, "num_texts":0}

	my_friends = fb.search(me[0], type=FRIENDS, count=friends_count)
	for friend in my_friends:
		print counter
		counter += 1
		friend_news = fb.search(friend.id, type=NEWS, count=news_count)
		for news in friend_news:
			link_counts["num_posts"] += 1
			if news.url:	
				link_counts["num_links"] += 1
				if news.url in link_counts:
					link_counts[news.url][0] += 1
					link_counts[news.url][1] += news.likes
				else:
					link_counts[news.url] = [1, news.likes]

	# Save the data to a file
	f = open(data,'w')
	cPickle.dump(link_counts,f)
	f.close()

def process_data(data='facebook.pickle'):
	""" Processes link data from given .pickle file by calculating 
		frequencies and cumulative likes

		data: the .pickle file name to process (default: facebook.pickle)
	"""
	print "Processing data...\n"

	# Load the data from a file
	input_file = open(data,'r')
	link_counts = cPickle.load(input_file)

	# Process the data
	short_counts = {"num_posts":link_counts["num_posts"], "num_links":link_counts["num_links"]}
	for url in link_counts:
		#	print url
		if url != "num_posts" and url != "num_links" and re.match('http',url):	# not a post counter and is a valid URL
			if "facebook" in url:			# most cases of Facebook related URLs
				if "video.php" in url:		# shared video
					short_url = re.search('//[^\t\n\r\f\v]*video.php', url).group()[2:]
				elif "/photos/" in url:		# shared photo
					short_url = re.search('//[^\t\n\r\f\v]*photos', url).group()[6:]
				elif "posts" in url:		# link to post
					short_url = re.search('//[^\t\n\r\f\v]*posts', url).group()[2:]
				elif re.match('https*://www.facebook.com/[^\t\n\r\f\v/]*',url):	# profile
					short_url = re.search('//[^\t\n\r\f\v]*', url).group()[2:]
				else:						# other mystery case
					short_url = re.search('//[^\t\n\r\f\v/]*/', url).group()[2:-1]
			else:
				if "fbcdn-" in url:			# one instance of Facebook photos
					list_url = list(re.search('//[^\t\n\r\f\v/]*/', url).group()[2:-1])
					list_url[14] = '*'
					list_url[16] = '*'
					short_url = "".join(list_url)
				elif "scontent.xx.fbcdn.net" in url:	# another instance of Facebook photos (combining them)
					short_url = "fbcdn-sphotos-*-*.akamaihd.net"
				elif "youtu" in url:		# youtube
					short_url = "youtube.com"
				elif "imgur" in url:		# imgur
					short_url = "imgur.com"
				elif "//t." in url:			# twitter
					short_url = "twitter.com"
				elif re.search('flic.?kr', url):	# flickr nyti.ms vs mytimes.com, es.pn vs espn.go.com
					short_url = "flickr.com"
				elif "//m." in url:			# mobile links
					short_url = re.search('//[^\t\n\r\f\v/]*/', url).group()[4:-1]
				elif url[-1] != "/" and "/" not in re.search('//[^\t\n\r\f\v]*', url).group()[2:-1]:	# url without '/' at end
					short_url = re.search('//[^\t\n\r\f\v/]*', url).group()[2:]
				else:						# every other case
					if "//www2" in url:		# remove www.
						short_url = re.search('//[^\t\n\r\f\v/]*/', url).group()[7:-1]
					elif "//www" in url:
						short_url = re.search('//[^\t\n\r\f\v/]*/', url).group()[6:-1]
					else:
						short_url = re.search('//[^\t\n\r\f\v/]*/', url).group()[2:-1]

			# update the counter dictionary
			if short_url in short_counts:
				short_counts[short_url][0] += link_counts[url][0]
				short_counts[short_url][1] += link_counts[url][1]
			else:
				short_counts[short_url] = link_counts[url]

	sort_list = [(k, v[0], v[1]) for k, v in short_counts.iteritems() if k != "num_posts" and k != "num_links"]
	num_entries = 50

	# Sort from highest to lowest number of posts
	sort_list.sort(key=lambda tup: tup[1], reverse = True)
	# Plot number of posts
	plot_bar_graph([tup[0] for tup in sort_list[:num_entries]], "URL",
		[tup[1] for tup in sort_list[:num_entries]], "Number of Posts",
		num_entries, "URLs with Highest Number of Posts")	

	# Sort from highest to lowest cumulative likes
	sort_list.sort(key=lambda tup: tup[2], reverse = True)
	# Plot cumulative likes
	plot_bar_graph([tup[0] for tup in sort_list[:num_entries]], "URL",
		[tup[2] for tup in sort_list[:num_entries]], "Cumulative Likes",
		num_entries, "URLs with Highest Cumulative Likes")

	# Sort from highest to lowest average likes per post
	sort_list.sort(key=lambda tup: float(tup[2])/tup[1], reverse = True)
	# Plot average likes per post
	plot_bar_graph([tup[0] for tup in sort_list[:num_entries]], "URL",
		[float(tup[2])/tup[1] for tup in sort_list[:num_entries]], "Rounded Average Likes per Post",
		num_entries, "URLs with Highest Average Likes per Post")

	# Save the results
	#save_to_csv(sort_list, data[:-6] + "csv")

	# Print the results
	#for item in sort_list:
	# 	print (item[0] + ":").ljust(65) + str(item[1]) + " posts, " + str(item[2]) + " likes"

	print "num_posts: " + str(short_counts["num_posts"])
	print "num_links: " + str(short_counts["num_links"])

def plot_bar_graph(x_data, x_label, y_data, y_label, num_entries, title):
	fig = plt.figure(figsize=(20, 10))
	ax = plt.subplot(111)


	index = np.arange(num_entries)
	bar_width = 0.7

	rects =ax.bar(index, y_data, bar_width, color='b')

	plt.xlabel(x_label, fontsize=18)
	plt.ylabel(y_label, fontsize=18)
	plt.title(title, fontsize=24)
	plt.tick_params(axis='both', which='major', labelsize=14)
	plt.xticks(index + bar_width / 2.0, x_data, rotation=90)
	plt.ylim([0, max(y_data)+max(y_data)%(10**(len("%.f"%max(y_data))-1))/2])
	print 10**len("%.f"%max(y_data))

	# Value labels on top
	for i, rect in enumerate(rects):
		height = rect.get_height()
		plt.text(rect.get_x()+bar_width/2, height + len("%.f"%max(y_data)), "%.f" % (y_data[i]),
			fontsize=9, ha='center', va='bottom')

	plt.tight_layout()
	plt.show()


def save_to_csv(data, filename):
	""" Writes given data in list of tuples to a .csv file with the given filename
			data: the list of tuples to write to a .csv
		filename: the name of the .csv to write
	"""
	with open(filename, "w") as f:
		writer = csv.writer(f)
		writer.writerow(['URL', 'num_posts', 'num_likes'])	
		for row in data:
			writer.writerow(row)

#fetch_data()
process_data('facebook_1000_250.pickle')

#print "Text:\t" + (news.text).encode('utf-8')