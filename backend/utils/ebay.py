import requests
import json
from django.conf import settings
import urllib, base64
import redis
from datetime import datetime, timedelta
from django.utils import timezone
import os
from user_alerts.models import UserAlerts, EbayItems

class Ebay:

    def __init__(self):
        self.app_id = os.environ.get("EBAY_APP_ID")
        self.cert_id = os.environ.get("EBAY_CERT_ID")
        self.ru_name = os.environ.get("EBAY_REDIRECT_URL_NAME")
        self.r = redis.Redis(host='redis', port=6379, db=0)
        self.token = self.r.get('ebay_token')

    def getAuthToken(self):
        if self.token:
            return self.token
        else:
            AppSettings = {
                'client_id': self.app_id,
                'client_secret': self.cert_id,
                'ruName': self.ru_name}
            authHeaderData = AppSettings['client_id'] + ':' + AppSettings['client_secret']
            encodedAuthHeader = base64.b64encode(str.encode(authHeaderData))
            encodedAuthHeader = str(encodedAuthHeader)[2:len(str(encodedAuthHeader)) - 1]
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": "Basic " + str(encodedAuthHeader)
            }
            body = {
                "grant_type": "client_credentials",
                "scope": "https://api.ebay.com/oauth/api_scope"
            }
            data = urllib.parse.urlencode(body)
            tokenURL = "https://api.ebay.com/identity/v1/oauth2/token"
            response = requests.post(tokenURL, headers=headers, data=data)
            if response.status_code == 200:
                res_json = response.json()
                self.r.setex('ebay_token', int(res_json['expires_in']), json.dumps(res_json['access_token']))
                return res_json['access_token']
            return None

    def search(self, keywords, limit: int = 20, offset: int = 0, sort: str = 'price'):
        url = 'https://api.ebay.com/buy/browse/v1/item_summary/search?' \
              '&q={keywords}' \
              '&limit={limit}' \
              '&offset={offset}' \
              '&sort={sort}'.format(
                keywords = keywords,
                limit = str(limit),
                offset = str(offset),
                sort=str(sort),
            )
        token = self.getAuthToken()
        headers = {
            "Authorization": "Bearer " + str(token)
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            return response_json['itemSummaries']
        return None

    def getItem(self, item_id, fieldgroups: str = 'PRODUCT'):
        url = 'https://api.ebay.com/buy/browse/v1/item/{item_id}?fieldgroups={fieldgroups}'\
            .format(item_id= item_id, fieldgroups = fieldgroups)
        token = self.getAuthToken()
        headers = {
            "Authorization": "Bearer " + str(token)
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            return response_json
        return None

