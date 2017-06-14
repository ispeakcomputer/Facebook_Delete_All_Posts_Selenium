# Facebook Cleaner using Selenium and python

This script will delete all of your old posts on Facebook. Take your Facebook back after posting kitten photos or dumb political stuff all these years 
 Keep in mind that if you run into any profile picture updates or you need to expand past years posts into the timeline the script will stop.
 Hide these posts from your timeline are expand the next years posts and restart the script. Fill free to fully automate or add onto the script. It has served
 it purpose for my personal clean up. I hope that it can help some of you.As the script automates the browser on the screen feel free to watch the terminal you ran
  the script in to see how manyy posts where deleted.

# Installation on Linux with Python Installed

1.) If you want a virtualenv go ahead and set one up

2.) run "pip install Selenium"

3.) Install or update Chrome Browser

4.) Go grab the the chromedriver for the version of Chrome you have and stick it in your path. I put it in the /usr/bin file

5.) run the script with it in your path with "python facebook_comments_delete.py"

6.) Have fun getting your Facebook profile cleaned !


# Future Improvements

Catch the "ElementNotVisibleException" exception and then look to hide a post from the time line. If the script fails again
have it expand by clicking the "See more posts in 201?" button and then trying again. That should fully automate this process.
All and all the script worked to remove 7 years worth of posts with not much effort.
