
from TwitterAPI import TwitterAPI

CONSUMER_KEY = 'bv7PJU4xT5rE2P2HwBLrJBmHE' 
CONSUMER_SECRET = 'AOpsl1kX7RddcAjJapquqYdFwm012HwWYaYRB6ZhFoOivVl7Wg'
ACCESS_TOKEN_KEY = '2184016926-19oyeVCq0P3hwpIkTnekFLBbT1iUre5vM7P6OBx'
ACCESS_TOKEN_SECRET = 'vMnGh2dfQPzFmhyMsWcvoFQbHxDrbCpVORWbOCLqhKmTG'

api = TwitterAPI(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_SECRET)
COUNT = 100
r = api.request("search/tweets",{"q":"Apple Cars","count":COUNT})


c = 0
with open("AppleCars.txt","a") as csvfile2:         
        for item in r.get_iterator():
          try:
               c+=1
               print c
               csvfile2.write(str(item))
          except UnicodeEncodeError:
                contine
           
          try:
              
              if 'text' in item:
                  text= item['text']
              if 'retweet_count' in item:
                  comments_count = item['retweet_count']
              if 'created_at' in item:
                  created_at = item['created_at']
              if 'user' in item:
                  user = item['user']
                  screen_name = user["screen_name"]
                  location = user["location"]

             
              


              print text, '\t',created_at, '\t',comments_count,'\t',screen_name,'\t',location
              
              csvfile2.write(str(text)+'\t'+str(created_at)+'\t'+str(comments_count)+'\t'+str(screen_name)+'\t'+str(location)+'\t'+str(created_at)+'\n')
          except UnicodeEncodeError:
               continue
