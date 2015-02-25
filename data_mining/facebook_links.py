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

import  re
import cPickle
from pattern.web import Facebook, NEWS, COMMENTS, LIKES, FRIENDS
import matplotlib.pyplot as plt

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
		#print url
		if url != "num_posts" and url != "num_links" and re.match('http',url):	# not a post counter and is a valid URL
			if "facebook" in url:		# most cases of Facebook related URLs
				if "video.php" in url:	# shared video
					short_url = re.search('//[^\t\n\r\f\v]*video.php', url).group()[2:]
				elif "/photos/" in url:	# shared photo
					short_url = re.search('//[^\t\n\r\f\v]*photos', url).group()[6:]
				elif "posts" in url:	# link to post
					short_url = re.search('//[^\t\n\r\f\v]*posts', url).group()[2:]
				elif re.match('https*://www.facebook.com/[^\t\n\r\f\v/]*',url): # profile
					short_url = re.search('//[^\t\n\r\f\v]*', url).group()[2:]
				else:					# other mystery case
					short_url = re.search('//[^\t\n\r\f\v/]*/', url).group()[2:-1]
			else:
				if "fbcdn-" in url:		# one instance of Facebook photos
					list_url = list(re.search('//[^\t\n\r\f\v/]*/', url).group()[2:-1])
					list_url[14] = '*'
					list_url[16] = '*'
					short_url = "".join(list_url)
				elif "youtu" in url:	# youtube
					short_url = "youtube.com"
				elif "imgur" in url:	# imgur
					short_url = "imgur.com"
				elif "//t." in url:
					short_url = "twitter.com"
				elif "//m." in url:		# mobile links
					short_url = re.search('//[^\t\n\r\f\v/]*/', url).group()[4:-1]
				elif url[-1] != "/" and "/" not in re.search('//[^\t\n\r\f\v]*', url).group()[2:-1]:	# url without '/' at end
					short_url = re.search('//[^\t\n\r\f\v/]*', url).group()[2:]
				else:					# every other case
					if "//www2" in url:	# remove www.
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

	# Print the results

	#sort_list = [(k, v[0], v[1]) for k, v in short_counts.iteritems() if k != "num_posts" and k != "num_links"]
	#sort_list.sort(key=lambda tup: tup[2])#, reverse = True)
	#for item in sort_list:
	# 	print (item[0] + ":").ljust(65) + str(item[1]) + " posts, " + str(item[2]) + " likes"

	print "num_posts: " + str(short_counts["num_posts"])
	print "num_links: " + str(short_counts["num_links"])

#fetch_data()
process_data('facebook_1000_250.pickle')

#print "Text:\t" + (news.text).encode('utf-8')