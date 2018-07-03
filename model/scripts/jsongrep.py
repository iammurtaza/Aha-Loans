import json
import sys
"""jsonstr='{"token":"EAAWI8wxzZBC4BABZCS70DwrvDZCXuDvnInXCoJDpFw75nOyyARZBryy0ZCpteQwaUgGYud3XLIbEWLLnSxB0n59yjSWdM1Q530YdUZC0fa5jogm86XRP7ou9B8U2y2AQ8Aw402MflCk1I8Ce1xwG4aoSEoRKZBNWbNZCo8uDfxORSAZDZD","refreshToken":"null","expiresIn":5183865,"id":"1684994381542693","nickname":"null","name":"Suneel Rajpoot","email":"suneel.indiamart@gmail.com","avatar":"https:\/\/graph.facebook.com\/v2.10\/1684994381542693\/picture?type=normal","user":{"name":"Suneel Rajpoot","email":"suneel.indiamart@gmail.com","id":"1684994381542693"},"avatar_original":"https:\/\/graph.facebook.com\/v2.10\/1684994381542693\/picture?width=1920","profileUrl":"null"}'

print(jsonstr)


value=json.loads(jsonstr.replace('\/','/'))
#sys.stdout.write(json.dumps(value))
print(json.dumps(value))
json must string must be enclosed in quotes

all json values also must be ienclosed in quotes

mustnt contain escape characters
"""
def main():
	accnt=sys.argv[1]
	args=sys.argv[2:]
	print(args)
	for item in args:
		item=item.replace('!','\!')
		value=json.load(item.replace('\/','/'),strict=False)
		#sys.stdout.write(json.dumps(value['user']['statuses_count']))
	


	
	if(accnt == "twitter"):twitterScore(value)
	else:print("NO")
	

	

def twitterScore(value):
	total_score=0

	"""
	tweets=1.0
	following=0.5
	followers=1.2
	likes=0.8
	older than _ years={4:50
						3:40
						2:30
						1:10}
	
	firstname in email:25
	lastname " " "  ":25

	last tweet={}

	suspended = y?0:50
	verified= y?20:0
"""
	tweets=value['user']['statuses_count']
	followers=value['user']['followers_count']
	following=value['user']['friends_count']
	likes=value['user']['favourites_count']
	score1=tweets+0.5*following+1.2*followers+0.8*likes

	if(score1>250):total_score+=250
	else:total_score+=score1


	print(score1)
	
	
						


if __name__ == '__main__':
		main()	



