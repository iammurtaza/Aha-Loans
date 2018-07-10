import json
import sys
import datetime
import re

def main():
	accnt=sys.argv[1]
	args=sys.argv[2:]
	

	for item in args:
		item=item.replace('!','\!')
		value=json.loads(item.replace('\/','/'),strict=False)
		
	print("******************************************************************************\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	if(accnt == "twitter"):print(twitterScore(value))
	else:print("NO")


def twitterScore(value):

	total_score=0

	if(value['user']['statuses_count']):tweets=value['user']['statuses_count']
	else:tweets=0

	if(value['user']['followers_count']):followers=value['user']['followers_count']
	else:followers=0
	
	if(value['user']['friends_count']):following=value['user']['friends_count']
	else:following=0
	
	if(value['user']['favourites_count']):likes=value['user']['favourites_count']
	else:likes=0
	
	score1=tweets+0.5*following+1.2*followers+0.8*likes

	if(score1>250):total_score+=250
	else:total_score+=score1

	#print("%%%%%%",total_score)


	if(value['user']['created_at']):
		year_created=value['user']['created_at'][-4:]
		now=datetime.datetime.now()
		life_time_of_accnt=now.year-int(year_created)
		time_score=dict([(14,30),(13,30),(12,30),(11,30),(10,30),(9,30),(8,30),(7,30),(6,30),(5,30),(4,20),(3,20),(2,10),(1,10),(0,0)])

		total_score+=time_score[life_time_of_accnt]

	else:pass

	#print("&&&&&&&&&",total_score)
	


	if(value['name'] and value['email']):
		first_name=value['name'].split()[0]
		last_name=value['name'].split()[1]
		email=value['email'].lower()
		contains_first=re.compile(first_name.lower())
		contains_last=re.compile(last_name.lower())

		if(contains_first.search(email)):total_score+=2.5
		if(contains_last.search(email)):total_score+=2.5
	else:pass	

	#print("###################",total_score)



	if(value['user']['statuses_count']):
		if(value['user']['status']):
			months={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
			last_tweet_year=int(value['user']['status']['created_at'][-4:])
			last_tweet_month=value['user']['status']['created_at'].split()[1]
			if(now.year-last_tweet_year is 0):
				difference_month=now.month-months[last_tweet_month]
				if(difference_month <= 2):
					total_score+=60
				elif(difference_month<=3 and difference_month>2):
					total_score+=50	
				elif(difference_month<=4 and difference_month>3):
					total_score+=40
				elif(difference_month<=5 and difference_month>4):
					total_score+=30
				else:total_score+=20		
			else:
				total_score+=10
		else:pass			

	else:pass
	#print("###################",total_score)

	if(value['user']['verified']):
		if(value['user']['verified']=='true'):total_score+=50
		else:pass
	else:pass
	#print("###################",total_score)


	if(value['user']['suspended']):
		if(value['user']['suspended']=='false'):total_score+=50
		else:pass
	else:pass
	#print("###################",total_score)

	return(total_score)




if __name__ == '__main__':
	main()




#total score=510



