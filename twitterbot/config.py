import twitter


# generate your own API from https://developer.twitter.com/en/apps tokens
# and replace HERE with the respective tokens
def getApi():
    return twitter.Api(consumer_key='HERE',
                        consumer_secret='HERE',
                        access_token_key='HERE',
                        access_token_secret='HERE')
