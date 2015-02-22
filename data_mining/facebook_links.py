"""
Created on Sun Feb 22 13:41 2015

@author: Franton Lin

"""

import  re
import cPickle
from pattern.web import Facebook, NEWS, COMMENTS, LIKES, FRIENDS

def fetch_data():
	print "Fetching data..."

	# Get the data
	fb = Facebook(license='key') # removed my key
	me = fb.profile()
	print me
	counter = 1;

	link_counts = {"num_posts":0, "num_links":0}

	my_friends = fb.search(me[0], type=FRIENDS, count=1000)
	for friend in my_friends:
		print counter
		counter += 1
		friend_news = fb.search(friend.id, type=NEWS, count=250)
		for news in friend_news:
			link_counts["num_posts"] += 1
			if news.url:	
				link_counts["num_links"] += 1
				if news.url in link_counts:
					link_counts[news.url][0] += 1
					link_counts[news.url][1] += news.likes
				else:
					link_counts[news.url] = [1, news.likes]

	#for url in link_counts:
	#	print url + ": " + str(link_counts[url])

	# Save the data to a file
	f = open('facebook.pickle','w')
	cPickle.dump(link_counts,f)
	f.close()

def process_data():
	print "Processing data...\n"

	# Load the data from a file
	input_file = open('facebook.pickle','r')
	link_counts = cPickle.load(input_file)

	# Process the data
	short_counts = {"num_posts":link_counts["num_posts"], "num_links":link_counts["num_links"]}
	for url in link_counts:
		#print url
		if url != "num_posts" and url != "num_links" and re.match('http',url):
			if "facebook" in url:
				if "video.php" in url:	# videos
					short_url = re.search('//[^\t\n\r\f\v]*video.php', url).group()[2:]
				elif "photos" in url:	# photos
					short_url = re.search('//[^\t\n\r\f\v]*photos', url).group()[2:]
				elif "posts" in url:	# posts
					short_url = re.search('//[^\t\n\r\f\v]*posts', url).group()[2:]
				elif re.match('https*://www.facebook.com/[^\t\n\r\f\v/]*',url): # profile
					short_url = re.search('//[^\t\n\r\f\v]*', url).group()[2:]
				else:	# other mystery case
					short_url = re.search('//[^\t\n\r\f\v/]*/', url).group()[2:-1]
			else:
				if url[-1] != "/" and "/" not in re.search('//[^\t\n\r\f\v]*', url).group()[2:-1]:	# url without '/' at end
					short_url = re.search('//[^\t\n\r\f\v/]*', url).group()[2:]
				else:	# every other case
					short_url = re.search('//[^\t\n\r\f\v/]*/', url).group()[2:-1]

			if short_url in short_counts:
				short_counts[short_url][0] += link_counts[url][0]
				short_counts[short_url][1] += link_counts[url][1]
			else:
				short_counts[short_url] = link_counts[url]

	# Print the results
	print "num_posts: " + str(short_counts["num_posts"])
	print "num_links: " + str(short_counts["num_links"])

	sort_list = [(k, v[0], v[1]) for k, v in short_counts.iteritems() if k != "num_posts" and k != "num_links"]
	sort_list.sort(key=lambda tup: tup[2])#, reverse = True)
	for item in sort_list:
	 	print (item[0] + ":").ljust(65) + str(item[1]) + " posts, " + str(item[2]) + " likes"

#fetch_data()
process_data()