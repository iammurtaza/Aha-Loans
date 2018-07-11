import json
import sys
import datetime
import re

def main():
	#accnt=sys.argv[1]
	#args=sys.argv[2:]

	args1='{"token":"935426607220629504-YMpxqgZv5EViljATeuU3Xwuj875nvrM","tokenSecret":"tw5YPyEXLqduUFFTCn67vH2TyFGj0mH0wUoaAp3iH9oM1","id":"935426607220629504","nickname":"mhzTweets","name":"Murtaza Hasan","email":"murtaza.hasan.zaidi@gmail.com","avatar":"http:\/\/abs.twimg.com\/sticky\/default_profile_images\/default_profile_normal.png","user":{"id_str":"935426607220629504","entities":{"description":{"urls":[]}},"protected":false,"followers_count":5,"friends_count":71,"listed_count":0,"created_at":"Tue Nov 28 08:34:17 +0000 2017","favourites_count":0,"utc_offset":null,"time_zone":null,"geo_enabled":false,"verified":false,"statuses_count":0,"lang":"en","contributors_enabled":false,"is_translator":false,"is_translation_enabled":false,"profile_background_color":"F5F8FA","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"has_extended_profile":false,"default_profile":true,"default_profile_image":true,"following":false,"follow_request_sent":false,"notifications":false,"translator_type":"none","suspended":false,"needs_phone_verification":false,"url":null,"profile_background_image_url":null,"profile_background_image_url_https":null,"profile_image_url":"http:\/\/abs.twimg.com\/sticky\/default_profile_images\/default_profile_normal.png","profile_image_url_https":"https:\/\/abs.twimg.com\/sticky\/default_profile_images\/default_profile_normal.png","location":"","description":""},"avatar_original":"http:\/\/abs.twimg.com\/sticky\/default_profile_images\/default_profile.png"}'
	args2='{"token":"2893967203-dOE22LzIdWCe3CPtNZ9A8Ln294ECNM2zHGERnAe","tokenSecret":"Ru45pT4i1ZgMMGlJ9T8E4EusHNpHRrMv2SOWeMAUFEvMt","id":"2893967203","nickname":"SunnyYasser","name":"Sunny Yasser","email":"sunnyyasser@gmail.com","avatar":"http:\/\/pbs.twimg.com\/profile_images\/531118150880735232\/mt-lTYJf_normal.jpeg","user":{"id_str":"2893967203","entities":{"description":{"urls":[]}},"protected":false,"followers_count":1,"friends_count":39,"listed_count":0,"created_at":"Sat Nov 08 16:10:33 +0000 2014","favourites_count":0,"utc_offset":null,"time_zone":null,"geo_enabled":false,"verified":false,"statuses_count":0,"lang":"en","contributors_enabled":false,"is_translator":false,"is_translation_enabled":false,"profile_background_color":"C0DEED","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"has_extended_profile":false,"default_profile":true,"default_profile_image":false,"following":false,"follow_request_sent":false,"notifications":false,"translator_type":"none","suspended":false,"needs_phone_verification":false,"url":null,"profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/531118150880735232\/mt-lTYJf_normal.jpeg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/531118150880735232\/mt-lTYJf_normal.jpeg","location":"","description":""},"avatar_original":"http:\/\/pbs.twimg.com\/profile_images\/531118150880735232\/mt-lTYJf.jpeg"}'
	args3='{"token":"439097118-haVqJ96QY6kggmHc1qQVE8CaYqBw4uTc6G1hf1Fh","tokenSecret":"hYJa4aQk912zstScfVNIoJXv5Z9BpugHKeImFxUjNA4hf","id":"439097118","nickname":"suneelweb","name":"Suneel Kumar Rajpoot","email":null,"avatar":"http:\/\/pbs.twimg.com\/profile_images\/425281075791671296\/fZw94RG1_normal.jpeg","user":{"id_str":"439097118","entities":{"url":{"urls":[{"url":"http:\/\/t.co\/14VCfEDmBO","expanded_url":"http:\/\/www.webtechnologiesindia.com","display_url":"webtechnologiesindia.com","indices":[0,22]}]},"description":{"urls":[]}},"protected":false,"followers_count":10,"friends_count":229,"listed_count":0,"created_at":"Sat Dec 17 10:56:13 +0000 2011","favourites_count":2,"utc_offset":null,"time_zone":null,"geo_enabled":true,"verified":false,"statuses_count":6,"lang":"en","status":{"created_at":"Mon Mar 26 05:56:23 +0000 2018","id":978148638290599936,"id_str":"978148638290599936","text":"@HDFCBank_Cares Although Im a software coder but still fail to understand the codes used by Hdfc bank in the narra\u2026 https:\/\/t.co\/0awbfJvckV","truncated":true,"entities":{"hashtags":[],"symbols":[],"user_mentions":[{"screen_name":"HDFCBank_Cares","name":"HDFC Bank","id":145931959,"id_str":"145931959","indices":[0,15]}],"urls":[{"url":"https:\/\/t.co\/0awbfJvckV","expanded_url":"https:\/\/twitter.com\/i\/web\/status\/978148638290599936","display_url":"twitter.com\/i\/web\/status\/9\u2026","indices":[117,140]}]},"source":"\u003Ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003ETwitter for Android\u003C\/a\u003E","in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":145931959,"in_reply_to_user_id_str":"145931959","in_reply_to_screen_name":"HDFCBank_Cares","geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"retweet_count":0,"favorite_count":0,"favorited":false,"retweeted":false,"lang":"en"},"contributors_enabled":false,"is_translator":false,"is_translation_enabled":false,"profile_background_color":"C0DEED","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"has_extended_profile":true,"default_profile":true,"default_profile_image":false,"following":false,"follow_request_sent":false,"notifications":false,"translator_type":"none","suspended":false,"needs_phone_verification":false,"url":"http:\/\/t.co\/14VCfEDmBO","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/425281075791671296\/fZw94RG1_normal.jpeg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/425281075791671296\/fZw94RG1_normal.jpeg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/439097118\/1515488543","location":"India","description":"PHP,OOPS, MySQL,Laravel Framework , OpenCart,  Ajax, Javascript, jQuery,LAMP, AWS"},"avatar_original":"http:\/\/pbs.twimg.com\/profile_images\/425281075791671296\/fZw94RG1.jpeg"}'
	args4='{"token":"3316267201-YgkvjS3ZgrgGOCgqV9hFG9XCOPWl5s2Tz5kMEy3","tokenSecret":"sFZHWSELwvBREwwyxWeXNW8RMvDzaPBKoI5JJ6YSG3GlG","id":"3316267201","nickname":"akbar_alirizvi","name":"Akbar Ali","email":"ikki0702@icloud.com","avatar":"http:\/\/pbs.twimg.com\/profile_images\/915832581395853313\/RMq-YvvC_normal.jpg","user":{"id_str":"3316267201","entities":{"url":{"urls":[{"url":"https:\/\/t.co\/RP9oe97sYY","expanded_url":"https:\/\/www.gullakh.com","display_url":"gullakh.com","indices":[0,23]}]},"description":{"urls":[]}},"protected":false,"followers_count":97,"friends_count":108,"listed_count":1,"created_at":"Sat Aug 15 19:53:25 +0000 2015","favourites_count":91,"utc_offset":null,"time_zone":null,"geo_enabled":false,"verified":false,"statuses_count":111,"lang":"en","status":{"created_at":"Wed Jun 20 08:54:36 +0000 2018","id":1009358843904655360,"id_str":"1009358843904655360","text":"@DoC_GoI @sureshpprabhu @narendramodi Tar, nictone and carbon monoxide content shud be made mandatory on packets of\u2026 https:\/\/t.co\/DtFSLL93oc","truncated":true,"entities":{"hashtags":[],"symbols":[],"user_mentions":[{"screen_name":"DoC_GoI","name":"DoC","id":719814610686255105,"id_str":"719814610686255105","indices":[0,8]},{"screen_name":"sureshpprabhu","name":"Suresh Prabhu","id":141208596,"id_str":"141208596","indices":[9,23]},{"screen_name":"narendramodi","name":"Narendra Modi","id":18839785,"id_str":"18839785","indices":[24,37]}],"urls":[{"url":"https:\/\/t.co\/DtFSLL93oc","expanded_url":"https:\/\/twitter.com\/i\/web\/status\/1009358843904655360","display_url":"twitter.com\/i\/web\/status\/1\u2026","indices":[117,140]}]},"source":"\u003Ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003ETwitter for Android\u003C\/a\u003E","in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":719814610686255105,"in_reply_to_user_id_str":"719814610686255105","in_reply_to_screen_name":"DoC_GoI","geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"retweet_count":0,"favorite_count":0,"favorited":false,"retweeted":false,"lang":"en"},"contributors_enabled":false,"is_translator":false,"is_translation_enabled":false,"profile_background_color":"C0DEED","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"has_extended_profile":true,"default_profile":true,"default_profile_image":false,"following":false,"follow_request_sent":false,"notifications":false,"translator_type":"none","suspended":false,"needs_phone_verification":false,"url":"https:\/\/t.co\/RP9oe97sYY","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/915832581395853313\/RMq-YvvC_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/915832581395853313\/RMq-YvvC_normal.jpg","location":"New Delhi, India","description":"Co-Founder"},"avatar_original":"http:\/\/pbs.twimg.com\/profile_images\/915832581395853313\/RMq-YvvC.jpg"}'
	# for item in args:
	# 	item=item.replace('!','\!')

	value=json.loads(args2,strict=False)
	

	print("******************************************************************************\n\n\n")
	print(twitterScore(value))

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
		time_score=dict([(16,50),(15,50),(14,50),(13,50),(12,50),(11,50),(10,50),(9,50),(8,50),(7,50),(6,50),(5,50),(4,30),(3,20),(2,10),(1,10),(0,0)])

		total_score+=time_score[life_time_of_accnt]

	else:pass

	#print("&&&&&&&&&",total_score)
	


	if(value['name'] and value['email']):
		first_name=value['name'].split()[0]
		last_name=value['name'].split()[1]
		email=value['email'].lower()
		contains_first=re.compile(first_name.lower())
		contains_last=re.compile(last_name.lower())

		if(contains_first.search(email)):total_score+=25
		if(contains_last.search(email)):total_score+=25
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
					total_score+=70
				elif(difference_month<=3 and difference_month>2):
					total_score+=60	
				elif(difference_month<=4 and difference_month>3):
					total_score+=50
				elif(difference_month<=5 and difference_month>4):
					total_score+=20
				else:total_score+=10		
			else:
				total_score+=10
		else:pass			

	else:pass
	#print("###################",total_score)

	if(value['user']['verified']):
		if(value['user']['verified']=='true'):total_score+=20
		else:pass
	else:pass
	#print("###################",total_score)


	if(value['user']['suspended']):
		if(value['user']['suspended']=='false'):total_score+=50
		else:pass
	else:pass
	#print("###################",total_score)


	if(value['user']['geo_enabled']):
		if(value['user']['geo_enabled']=='true'):total_score+=10
		else:pass
	else:pass
	#print("###################",total_score)


	return(int(total_score))


if __name__ == '__main__':
	main()