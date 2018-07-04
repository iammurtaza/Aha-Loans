import fb
import json

oauth_access_token='EAACEdEose0cBAGk2ZBeiz4JfApAjTs9SogB3F97UpDTo2UK24JVzjvwCjAqajcpvMnLjEop206BZB8df5SCTTDmoHa6aaKpvZCmyHB9DqcZCiW87MZAZAPEIDFAczR7dcTykh3BKMpQWcIraLqZC39SAbnzI7IVgSZAgZBbPOOzbkXruoIIYZA6vgZBbS36Nlm78f19DGsxMP03SwZDZD'

def pp(o):
	print(json.dumps(o, indent=1))

graph = fb.graph.api(oauth_access_token)
profile = graph.get_object(cat="single")
friends = graph.get_object(cat="single",id = "me", fields=["id","name","email","birthday","gender","age_range","tagged_place"])

pp(friends)