import praw
import time
import os.path
import re

# Using semantic versioning MAJOR.MINOR.PATCH
ua = "LinkDeleter 0.2.0 by /u/jonwhobot"
r = praw.Reddit(user_agent = ua)

# Read user and pass from file
f = open('creds', 'r')
username = f.readline().split('=')[-1].rstrip()
password = f.readline().split('=')[-1].rstrip()
f.close()

# Login with values from file
r.login(username = username, password = password)

# Version 1
# Go through all the comments in a thread
# Make a set of links (meaning no duplicates)
# If comment already in set then delete that entire comment

# Version 2
# Notify mods of users that send the same link
# Notify mods of multiple users sending the same link

# Have to be careful about rate limit here
# Put in time.sleep() between calls or something to make sure
# a single thread doesn't just keep running delete API calls
# For the the more advanced way URLs can be broken up or what not
# don't care about that for now, do the simple case of building
# a set and checking against the set

# Task: Open file to write and only write to file if thread passes criteria
# f = open('filename', 'w') or something like that
# Task: Open test subreddit and only pick threads made by a certain account
# Task: Read the comments and validate expected hyperlinks
#       Referral hyperlinks most likely have to be the same with https

# Common variables
# automoderator = r.get_redditor('AutoModerator')
# submissions = automoderator.get_submitted()
jonwhobot = r.get_redditor('jonwhobot')
submissions = jonwhobot.get_submitted()
myezpzbottester = r.get_subreddit('myezpzbottester') # probably won't need this
# save file writing stuff for next version
# submission_id_set = set([line.strip() for line in open('submission_ids')])

# this is for appending to the file, does not allow reading
# file_submission_ids = open('submission_ids', 'a')

def run_bot():
  print "Check if thread by AutoModerator is in /r/churning"
  for submission in submissions:
    if is_churning( submission ) and is_referral_thread( submission ):
      print "Found referral thread!"
      print "Thread name is: " + u_to_s( submission.title )
      print "Created on: " + str(submission.created_utc)
      moderate( submission )
      print "Done moderating thread! Looking for more..."
  print "All done! Going to sleep now for 10 seconds then repeat actions."

# Perform the moderation task this bot was tasked to do:
# Find duplicate links in comment thread
# On finding a duplicate link remove each comment that contains that link
def moderate( submission ):
  # Each time moderate is called on a thread the set of links should be empty to start.
  links = set()
  comments = get_comments( submission )
  for comment in comments:
    urls = re.findall(r'(https?://[^\s]+)', u_to_s(comment.body))
    for url in urls:
      if url in links:
        print '\tDeleting a comment!'
        comment.remove()
      else:
        links.add(url)

# Just have this method for now to return a string of all comments concatenated.
# @return String
def stupid_concat( llist ):
  s = ''
  for l in llist:
    s += ' ' + u_to_s(l.body)
  return s
    
# Currently not in use.
def get_user():
  user = 'AutoModerator'
  redditor = r.get_redditor(user)
  print redditor
  #print_methods(redditor)
  # print_methods(redditor.get_submitted())
  submissions = redditor.get_submitted()
  submission = submissions.next()
  print submission
  print_methods(submission)

# Returns all the comments for a submitted thread.
# @return List
def get_comments(submission):
  return submission.comments

# Check that the submission is in /r/churning subreddit.
# @return Boolean
def is_churning( submission ):
  return u_to_s(submission.subreddit.display_name).lower() == 'myezpzbottester'
  #return u_to_s(submission.subreddit.display_name).lower() == 'churning'

# Check that the thread is the referral thread.
# @return Boolean
def is_referral_thread( submission ):
  return 'links' in u_to_s(submission.title).lower()
  #return 'referral' in u_to_s(submission.title).lower()

# Convert unicode to a string and return it.
# @return String
def u_to_s( u_string ):
  return u_string.encode('ascii', 'ignore')

# Method to print the methods available to an instance of a class
def print_methods(instance = None):
  if instance:
    methods = [method for method in dir(instance) if callable(getattr(instance, method))]
    for method in methods:
      print method

# Method to print the data fields available to an instance of a class
def print_fields(instance = None):
  if instance:
    fields = [f for f in dir(instance) if not callable(getattr(instance, f)) and not f.startswith('__')]
    for f in fields:
      print f

while True:
  run_bot()
  # Run bot every 10 seconds
  time.sleep(10)
