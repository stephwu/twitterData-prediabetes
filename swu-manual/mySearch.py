#!/usr/bin/env python
import twitter
import argparse

#Setting up Twitter API
api = twitter.Api(
 consumer_key='hzgVOcyf2JcmzF41b21FHkhY3',
 consumer_secret='#',
 access_token_key='209327360-B5ux9W7ocj2EmAJTBJqRu6TtY6M9nl3vrIT5TxgP',
 access_token_secret='#'
 )

#Parsing the commands
#Top Level
parser = argparse.ArgumentParser(prog='stwitter', description='Custom search of Twitter')
parser.add_argument('-c', '--count', metavar='num', default=100, type=int, help='The total number of tweets to return (before filters)')
parser.add_argument('-f', '--removefilters', action='store_true', help='Removes the tweet filters')
parser.add_argument('-d', '--removedirect', action='store_true', help='Filters direct tweets to our account')
sp = parser.add_subparsers(dest='command')
#prediabetes Sub
sp_prediabetes = sp.add_parser('prediabetes', help='%(prog)s searches for prediabetes')
#MyHob Sub
sp_diabetes = sp.add_parser('diabetes', help='%(prog)s searches for diabetes')
#Keyword Sub
sp_keyword = sp.add_parser('search', help='%(prog)s searches using a custom query')
sp_keyword.add_argument('term', type=str, help='A query for searching Twitter; must be in quotes')

#Parse the Args
args = parser.parse_args()
if args.command != '':
#Custom looping so we can search more than 100 tweets
 tweetID = ''
 i = int(round(args.count -51, -2)) / 100 + 1
 for x in range (0, i):

 #Perform Find
 if args.command == 'prediabetes':
 print '------Searching Tweets about prediabetes ' + str(x * 100) + '/' + str(args.count) + '------'
 search = api.GetSearch(term='"prediabetes" OR "blood sugar" OR "blood glucose" OR "diabets"', lang='en', result_type='recent', count=(args.count - 100 * x), max_id=tweetID)

 elif args.command == 'sp_diabetes':
 print '------Searching Tweets about my diabetes ' + str(x * 100) + '/' + str(args.count) + '------'
 search = api.GetSearch(term='"diabetes" OR "blood sugar" OR "blood glucose" OR "disease"', lang='en', result_type='recent', count=(args.count - 100 * x), max_id=tweetID)

 elif args.command == 'search':
 print '------Searching Tweets using \"' + args.term + '\"' + str(x * 100) + '/' + str(args.count) + '------'
 search = api.GetSearch(term=args.term, lang='en', result_type='recent', count=(args.count - 100 * x), max_id=tweetID)

 #Filter Results
 for t in search:
 #Filter the results by default
 if args.removefilters == False:
 if (
 #Filters Twitter Account
 t.user.screen_name != 'jerkface' and
 t.user.screen_name != 'notniceguy' and
 t.user.screen_name != 'spambot' and
 t.user.screen_name != 'junkbot' and
 #Filter Retweets
 'RT @' not in t.text and
 #Filter Direct Tweets
 (args.removedirect == False or '@mytwittername' not in t.text) and
 #Filter out words
 'sex' not in t.text):
 print ''
 print t.user.screen_name + ' (' + t.created_at + ')'
 #Add the .encode to force encoding
 print t.text.encode('utf-8')
 print ''

 else:
 print ''
 print t.user.screen_name
 print t.created_at
 print t.text.encode('utf-8')
 print ''
#Save the this tweet ID
 tweetID = t.id


