import re,os,json

args1='{"token":"EAAWI8wxzZBC4BABZCS70DwrvDZCXuDvnInXCoJDpFw75nOyyARZBryy0ZCpteQwaUgGYud3XLIbEWLLnSxB0n59yjSWdM1Q530YdUZC0fa5jogm86XRP7ou9B8U2y2AQ8Aw402MflCk1I8Ce1xwG4aoSEoRKZBNWbNZCo8uDfxORSAZDZD","refreshToken":null,"expiresIn":5183865,"id":"1684994381542693","nickname":null,"name":"Suneel Rajpoot","email":"suneel.indiamart@gmail.com","avatar":"https:\/\/graph.facebook.com\/v2.10\/1684994381542693\/picture?type=normal","user":{"name":"Suneel Rajpoot","email":"suneel.indiamart@gmail.com","id":"1684994381542693"},"avatar_original":"https:\/\/graph.facebook.com\/v2.10\/1684994381542693\/picture?width=1920","profileUrl":null}'
args2='{"token":"EAAWI8wxzZBC4BAOpC9mKuJm4SxPkKEYqRpJ249WUeEkJUD9Whhtiq8c8EvAxzwEL6vyRT39X5VpsPuPRjexSzmZCb7dRGWtACxE7Curq6u5ZCd8Fp3v6uQkfjDzhp8dE9bblGsPMUJ6cBDKvZB5er6LYLn9en5IlBhrxZCYTW2AZDZD","refreshToken":null,"expiresIn":5178523,"id":"1730828933650713","nickname":null,"name":"Sunny Yasser","email":"sunnyyasser@gmail.com","avatar":"https:\/\/graph.facebook.com\/v2.10\/1730828933650713\/picture?type=normal","user":{"name":"Sunny Yasser","email":"sunnyyasser@gmail.com","gender":"male","verified":true,"link":"https:\/\/www.facebook.com\/app_scoped_user_id\/YXNpZADpBWEdhek1nY0syLVlJZA0FVRjB0T0pwUHZAKRmVtR29yWTlhSUtLRWpJZAWpWTlFBOTVvMWYzTUU0amE0T3RCUlpzQlVfNjRZAY3MzTm5yT1RPcUh1TldjVzJWaXdqOHZASZAHkxWl9Hc0tsU3BHOFNxWHZAvRncZD\/","id":"1730828933650713"},"avatar_original":"https:\/\/graph.facebook.com\/v2.10\/1730828933650713\/picture?width=1920","profileUrl":"https:\/\/www.facebook.com\/app_scoped_user_id\/YXNpZADpBWEdhek1nY0syLVlJZA0FVRjB0T0pwUHZAKRmVtR29yWTlhSUtLRWpJZAWpWTlFBOTVvMWYzTUU0amE0T3RCUlpzQlVfNjRZAY3MzTm5yT1RPcUh1TldjVzJWaXdqOHZASZAHkxWl9Hc0tsU3BHOFNxWHZAvRncZD\/"}'
args3='{"token":"EAAWI8wxzZBC4BAJsWEDXggQPrL76B9kKZCCM0VcqhqqJc5ZBUR4rdHXpxM22MlI4Pq0hmJn5vOgAfEmlS4LtaimjO3h9VmWnIcxQZAzqPqsCUV9jEpRqpjZCDnVLijpy86uytg31HYXpxsLSL28FBallZBzIyVNezCHF5NZCNlEJAZDZD","refreshToken":null,"expiresIn":5183998,"id":"2102376263110359","nickname":null,"name":"Murtaza Hasan","email":"murtazaygenius@gmail.com","avatar":"https:\/\/graph.facebook.com\/v2.10\/2102376263110359\/picture?type=normal","user":{"name":"Murtaza Hasan","email":"murtazaygenius@gmail.com","gender":"male","verified":true,"link":"https:\/\/www.facebook.com\/app_scoped_user_id\/YXNpZADpBWEVQY1FhUkJDTVR4OWx4UThHUU5aYXFxd2poNGdXZAW1DbFNfODFNUXBWX0NGQU1FeGFNVlVkWXdJV0FYdVI4bUw2UGRha09MWnhoQzJ4QWR0UXJoRTdlVFlKb0lHems4WXZAzZAWlmM1BFaWw1OWY5V1EZD\/","id":"2102376263110359"},"avatar_original":"https:\/\/graph.facebook.com\/v2.10\/2102376263110359\/picture?width=1920","profileUrl":"https:\/\/www.facebook.com\/app_scoped_user_id\/YXNpZADpBWEVQY1FhUkJDTVR4OWx4UThHUU5aYXFxd2poNGdXZAW1DbFNfODFNUXBWX0NGQU1FeGFNVlVkWXdJV0FYdVI4bUw2UGRha09MWnhoQzJ4QWR0UXJoRTdlVFlKb0lHems4WXZAzZAWlmM1BFaWw1OWY5V1EZD\/"}'
args4='{"token":"EAAWI8wxzZBC4BAGGJ0WsGgeZB1NZB7qpxTHN22RH4u7fgkDizYsCVuM4vzRwTqy0P4dRpA8h7IUunifZAKQZAMPNfdAzTFGXZCghZAbODOtkpLJNEYhH8VmSRW4WPIkma0nfhDDlsZBusCWDvFVI4fR5x8QWn0fNRfnbzm33p6ozFAZDZD","refreshToken":null,"expiresIn":5183998,"id":"1628721273866352","nickname":null,"name":"Akbar Ali","email":"akbarrizvi2000@yahoo.co.in","avatar":"https:\/\/graph.facebook.com\/v2.10\/1628721273866352\/picture?type=normal","user":{"name":"Akbar Ali","email":"akbarrizvi2000@yahoo.co.in","gender":"male","verified":true,"link":"https:\/\/www.facebook.com\/app_scoped_user_id\/YXNpZADpBWEU0MEVpZAjNnclVROExCcUpJNUk4V2JIOFRXSlBRTXUtbVljUnZAxUFpHNG5kX3VUOC1ReTVIT3BhTi10Y045VWJCemtlMjNWMFlfUnFQQzdMb3FyMWdKdWRNVFZAPM2tUaU5qMmZAVMEFISktlOEFfOHcZD\/","id":"1628721273866352"},"avatar_original":"https:\/\/graph.facebook.com\/v2.10\/1628721273866352\/picture?width=1920","profileUrl":"https:\/\/www.facebook.com\/app_scoped_user_id\/YXNpZADpBWEU0MEVpZAjNnclVROExCcUpJNUk4V2JIOFRXSlBRTXUtbVljUnZAxUFpHNG5kX3VUOC1ReTVIT3BhTi10Y045VWJCemtlMjNWMFlfUnFQQzdMb3FyMWdKdWRNVFZAPM2tUaU5qMmZAVMEFISktlOEFfOHcZD\/"}'

value=json.loads(val,strict=False)

totalScore=0

try:
    value=json.loads(val,strict=False)
    email=value['email']
    try:
        firstName=value['name'].split(" ")[0]
        containsfirst=re.compile(firstName.lower())
        if(containsfirst.search(email)):totalScore+=25
    except:
        pass
    try:
        lastName=value['name'].split(" ")[-1]
        containslast=re.compile(lastName.lower())
        if(containslast.search(email)):totalScore+=25
    except:
        pass
except:
    pass
        
try:
    verify=value['user']['verified']
    if(verify):totalScore+=30
    else:pass
except:
    pass