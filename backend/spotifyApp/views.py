#used for testing: 
from django.shortcuts import HttpResponse
#used for testing: 
from django.http import JsonResponse

#  think backend works w out having to worry about csrf:
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os
import base64
from requests import post
import json

load_dotenv()

client_id=os.getenv("CLIENT_ID")
client_secret=os.getenv("CLIENT_SECRET")

#gets a new token everytime its called but
#  every token only exists for about an hour

def getToken():
    auth_string=client_id+"+"+client_secret
    auth_bytes=auth_string.encode("utf-8")
    auth_base64=str(base64.b64encode(auth_bytes),"utf-8")

    url="https://accounts.spotify.com/api/token"
    headers={
        "Authorization":"Basic "+auth_base64,
        "Content-Type":"application/x-www-form-urlencoded"
    }
    data={"grant_type":"client_credentials"}
    result=post(url,headers=headers,data=data)
    json_result=json.loads(result.content)
    token=json_result["access_token"]
    return token

def get_auth_header(token):
    return{"Authorization":"Bearer " +token}

@csrf_exempt
def handlePost(request):
    if request.method=='POST':
        #Newtoken=getToken()
        try:
            # Parse JSON data
            data = json.loads(request.body)
            print("JSON Data:", data)
            # Access individual fields if needed
            return JsonResponse({'status': 'success', 'data': data})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return HttpResponse('Send a POST request')




