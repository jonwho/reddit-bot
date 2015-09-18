import praw
import time
import os.path

# Using semantic versioning MAJOR.MINOR.PATCH
ua = "LinkDeleter 0.1.0 by /u/jonwhobot"
r = praw.Reddit(user_agent = ua)

# Read user and pass from file
f = open('creds', 'r')
username = f.readline().split('=')[-1].rstrip()
password = f.readline().split('=')[-1].rstrip()
f.close()

# Login with values from file
r.login(username = username, password = password)

# Use exact string matching first
# If comment contains the string, delete comment?
# Or replace string with something else?
# To block against smarter users who break url up
# Strip whitespace and make one long string and check for substring contains
# Are there ways around this with capitalization?
# Users can also alias a URL with a name so need to validate alias as well

# This bot should only run on threads that meet these requirements
# Thread is posted by automoderator
# Title has the keyword referral in it

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

# Some more steps
# Go into subreddit
# Get submissions and write submission.id into file if:
#   submitted by AutoModerator
#   thread title contains referral

# Task: Open file to write and only write to file if thread passes criteria
# f = open('filename', 'w') or something like that
# Task: Open test subreddit and only pick threads made by a certain account
# Task: Read the comments and validate expected hyperlinks
#       Referral hyperlinks most likely have to be the same with https

# Common variables
automoderator = r.get_redditor('AutoModerator')
submissions = automoderator.get_submitted()
myezpzbottester = r.get_subreddit('myezpzbottester')
submission_id_set = set([line.strip() for line in open('submission_ids')])

# this is for appending to the file, does not allow reading
# file_submission_ids = open('submission_ids', 'a')

def run_bot():
  print("Check if thread by AutoModerator is in /r/churning")
  if subreddit
  comments = subreddit.get_comments(limit=1)
  for comment in comments:
    comment_text = comment.body
    # decide on a strategy for checking duplicates
  print("Comments loop finished, time to sleep")

# Perform the moderation task this bot was tasked to do:
# Find duplicate links in comment thread
# On finding a duplicate link remove each comment that contains that link
def moderate():


# Return true if the thread is submitted by AutoModerator and is the
# official churning referral thread. Else false.
# @return Boolean
def submitted_by_automoderator(submission):
  name = submission.author.name.encode('ascii', 'ignore')
  if name == 'AutoModerator':
    return True if 'Referral' in submission.title.encode('ascii', 'ignore')
  return False

def get_user():
  user = 'AutoModerator'
  redditor = r.get_redditor(user)
  print redditor
  #print_attrs(redditor)
  # print_attrs(redditor.get_submitted())
  submissions = redditor.get_submitted()
  submission = submissions.next()
  print submission
  print_attrs(submission)

def get_comments(submission):
  return submission.comments

# Check that the submission is in /r/churning subreddit.
# @return Boolean
def is_churning( submission ):
  return u_to_s(submission.subreddit.display_name) == 'churning'

# Check that the thread is the referral thread.
# @return Boolean
def is_referral_thread( submission ):
  return 'referral' in u_to_s(submission.title).lower()

# Convert unicode to a string and return it.
# @return String
def u_to_s( u_string ):
  return u_string.encode('ascii', 'ignore')

# Iterate over comments
# for comment in comments:
#   print comment

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

# while True:
  # run_bot()
  # # Run bot every 10 seconds
  # time.sleep(10)

get_user()

