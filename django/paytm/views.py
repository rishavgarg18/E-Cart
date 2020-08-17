import requests
import json

from paytmchecksum import PaytmChecksum

def initiate(orderid,amount,customerid):
    paytmParams = dict()

    paytmParams["body"] = {
        "requestType"   : "Payment",
        "mid"           : "MvhSMh12903239445983",
        "websiteName"   : "WEBSTAGING",
        "orderId"       : orderid,
        "callbackUrl"   : "https://merchant.com/callback",
        "txnAmount"     : {
            "value"     : amount,
            "currency"  : "INR",
        },
        "userInfo"      : {
            "custId"    : customerid,
        },
    }

    # Generate checksum by parameters we have in body
    # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
    checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), "neDJV6QZxIuTVBR")

    paytmParams["head"] = {
        "signature"	: checksum
    }

    post_data = json.dumps(paytmParams)

    # for Staging
    url = "https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction?mid=YOUR_MID_HERE&orderId=ORDERID_98765"

    # for Production
    # url = "https://securegw.paytm.in/theia/api/v1/initiateTransaction?mid=YOUR_MID_HERE&orderId=ORDERID_98765"
    response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
    print(response)



# Generate Checksum via Hash/Array
# initialize an Hash/Array
def test(request):
    
    paytmParams = {}

    paytmParams["MID"] = "MvhSMh12903239445983"
    paytmParams["ORDERID"] = "1"

    # Generate checksum by parameters we have
    # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
    paytmChecksum = PaytmChecksum.generateSignature(paytmParams, "@neDJV6QZxIuTVBR")
    verifyChecksum = PaytmChecksum.verifySignature(paytmParams, "@neDJV6QZxIuTVBR",paytmChecksum)

    print("generateSignature Returns:" + str(paytmChecksum))
    print("verifySignature Returns:" + str(verifyChecksum))

# Generate Checksum via String
# initialize JSON String
# body = "{\"mid\":\"YOUR_MID_HERE\",\"orderId\":\"YOUR_ORDER_ID_HERE\"}"

# # Generate checksum by parameters we have
# # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
# paytmChecksum = PaytmChecksum.generateSignature(body, "YOUR_MERCHANT_KEY")
# verifyChecksum = PaytmChecksum.verifySignature(body, "YOUR_MERCHANT_KEY", paytmChecksum)

# print("generateSignature Returns:" + str(paytmChecksum))
# print("verifySignature Returns:" + str(verifyChecksum))