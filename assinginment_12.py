#Q1
#what is access token
#an object token is an object that describes the security context of a process or thread
#how to generate your access token for any API
#sign in to developer account
#create a new api
#under that go to keys and access token
#generate access token

#Q2
#google ip address= 216.58.210.14
#facebook ip address=157.240.23.39

#Q3
from key import consumer_key,Consumer_Secret,Access_Token,Access_Secret
import tweepy
oauth = tweepy.OAuthHandler(consumer_key,Consumer_Secret)
oauth.set_access_token(Access_Token,Access_Secret)
api = tweepy.API(oauth)
print(api.search("#salman khan"))


#Q4

#    Difference between a library and an API
#API is a part of library which defines how an application communicates with external code

#API can be written in any language.
#Library is written in same language which is a collection of all the functionalities required for the use case.
#For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
#For further reading : https://stackoverflow.com/questions/3678665/is-there-still-a-difference-between-a-library-
#We can create our own APIs using Python Framework like Django and Flask which can be used in websites.
#You can follow documentation of Django in order to create your own website with Python. Check this out:
#https://docs.djangoproject.com/en/2.0/

 #Q5


from key import consumer_key,Consumer_Secret,Access_Token,Access_Secret
import tweepy
oauth = tweepy.OAuthHandler(consumer_key,Consumer_Secret)
oauth.set_access_token(Access_Token,Access_Secret)
api = tweepy.API(oauth)
print(api.search("#modi"))
print(api.get_user("@karwalVikramjit"))
user = api.get_user("@karwalVikramjit")
print(user.screen_name)
print(user.followers_count)
print(user.friends_count)
