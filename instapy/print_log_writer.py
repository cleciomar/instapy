"""Module only used to log the number of followers to a file"""
from datetime import datetime
from .util import log_remotely

def log_follower_num(browser, username, previous_followers_num):
    """Prints and logs the current number of followers to  seperate file"""
    browser.get('https://www.instagram.com/' + username)
    followed_by = browser.execute_script("return window._sharedData.entry_data.ProfilePage[0].user.followed_by.count")
    delta = int(followed_by)-int(previous_followers_num)
    delta_str = ''
    if delta > 0:
      delta_str = '+'
    delta_str +=str(delta)
    following = browser.execute_script("return window._sharedData.entry_data.ProfilePage[0].user.follows.count")
    losg_str='{:%Y-%m-%d %H:%M} Followers: {} ({}), Following: {}\n'.format(datetime.now(), delta_str, followed_by or 0, following or 0)
    
    log_remotely(username,"Followers",losg_str) 
    with open('./logs/followerNum.txt', 'a') as numFile:
        numFile.write(losg_str)

    return int(followed_by)

def log_followed_pool(login, followed, logger):
    """Prints and logs the followed to
    a seperate file"""
    try:
        with open('./logs/' + login + '_followedPool.csv', 'a+') as followPool:
            followPool.write(followed + ",\n")
    except BaseException as e:
        logger.error("log_followed_pool error {}".format(str(e)))
