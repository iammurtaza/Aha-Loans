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
	args=sys.argv[1:]
	print(args)
	for item in args:
		value=json.loads(item.replace('\/','/'),strict=False)
		sys.stdout.write(json.dumps(value["user"]["email"]))



if __name__ == '__main__':
		main()	



