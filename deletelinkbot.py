import praw
import time

# Using semantic versioning MAJOR.MINOR.PATCH
ua = "LinkDeleter 0.1.0 by /u/jonwhobot"
r = praw.Reddit(user_agent = ua)

# Read user and pass from file
f = open('creds', 'r')
username = f.readline().split('=')[-1].rstrip()
password = f.readline().split('=')[-1].rstrip()
f.close()

# Prompts you for username and password in terminal
r.login(username = username, password = password)

# Retrieve link you want to check against
check_link = raw_input("Enter link you want to check: ")
print 'Will check for duplicates of this link: ' + check_link

# Use exact string matching first
# If comment contains the string, delete comment?
# Or replace string with something else?
# To block against smarter users who break url up
# Strip whitespace and make one long string and check for substring contains
# Are there ways around this with capitalization?
# Users can also alias a URL with a name so need to validate alias as well

# Version 1
# Better explained here
# Go through all the comments in a thread
# Make a set of links (meaning no duplicates)
# If comment already in set then delete that entire comment
# Reset the URL set when entering a new thread?

# Version 2
# Target specific threads only by title

# Version 3
# Notify mods of users that send the same link
# Notify mods of multiple users sending the same link

# Have to be careful about rate limit here
# Put in time.sleep between calls or something to make sure
# a single thread doesn't just keep running delete API calls
# For the the more advanced way URLs can be broken up or what not
# don't care about that for now, do the simple case of building
# a set and checking against the set

def run_bot():
  print("Grabbing subreddit...")
  subreddit = r.get_subreddit("myezpzbottester")
  print("Grabbing comments...")
  comments = subreddit.get_comments(limit=1)
  for comment in comments:
    comment_text = comment.body
    # decide on a strategy for checking duplicates
  print("Comments loop finished, time to sleep")

while True:
  run_bot()
  # Run bot every 10 seconds
  time.sleep(10)
