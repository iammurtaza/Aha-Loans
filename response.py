import requests
import json
import flask
endpoint = "http://uat.ahaloans.com/api/v1/bankstatementanalyzer/results"
data={

    "body":

    {

        "bankID":"1",

        "documentId":"baa5b94fe978398594aef80c73656449"

    }

}
data_dump=json.dumps(data)

headers = {"Authorization":"Bearer 51bafe89-c2cd-4590-9532-4424e647cb9b"}

ans=requests.post(endpoint,data=data_dump,headers=headers)
print(json.loads(ans.text))

#baa5b94fe978398594aef80c73656449
