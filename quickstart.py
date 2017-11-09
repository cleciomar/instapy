from instapy import InstaPy

insta_username = 'insanitravel'
insta_password = 'macbookpro'

# if you want to run this script on a server, 
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password)
session.login()

# For 50% of the 30 newly followed, move to their profile
# and randomly choose 5 pictures to be liked.
# Take into account the other set options like the comment rate
# and the filtering for inappropriate words or users
while True:
	session.set_user_interact(amount=5, random=True, percentage=50, media='Photo')
	session.follow_user_followers(['campeveryday', 'folkscenery', 'folkgreen'], amount=2, random=False, interact=True)

# end the bot session
session.end()
