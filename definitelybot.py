import praw
import time

# Used code sample from this video https://www.youtube.com/watch?v=a5BnJpTQIMM

# API calls per method call to run_bot
# 4 calls per 10 seconds 

# Using semantic versioning MAJOR.MINOR.PATCH
ua = "DefinitelyFixer 0.1.0 by /u/jonwhobot"
r = praw.Reddit(user_agent = ua)

# Read user and pass from file
f = open('creds', 'r')
username = f.readline().split('=')[-1].rstrip()
password = f.readline().split('=')[-1].rstrip()
f.close()

# Prompts you for username and password in terminal
r.login(username = username, password = password)

words_to_match = ['definately', 'defiantly', 'definantly', 'definatly']
cache = []

def run_bot():
  print("Grabbing subreddit...")
  subreddit = r.get_subreddit("myezpzbottester")
  print("Grabbing comments...")
  comments = subreddit.get_comments(limit=1)
  for comment in comments:
    comment_text = comment.body.lower()
    isMatch = any(string in comment_text for string in words_to_match)
    if comment.id not in cache and isMatch:
      print("Match found! Comment ID: " + comment.id)
      comment.reply('I think you meant to say "definitely"')
      print("reply successful!")
      cache.append(comment.id)
  print("Comments loop finished, time to sleep")

while True:
  run_bot()
  # Run bot every 10 seconds
  time.sleep(10)
