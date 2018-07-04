import requests
import json
import flask
endpoint = "http://uat.ahaloans.com/api/v1/bankstatementanalyzer"
data={

    "body":

    {

        "bank_id":"1",

        "stmtURL":"https://gullakh.s3-us-west-2.amazonaws.com/AxisBank.pdf"

    }

}
data_dump=json.dumps(data)

headers = {"Authorization":"Bearer 51bafe89-c2cd-4590-9532-4424e647cb9b"}

ans=requests.post(endpoint,data=data_dump,headers=headers)
print(json.loads(ans.text))
