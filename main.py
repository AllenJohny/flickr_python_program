import requests

api_key = u'418b41e60d44ab4a8488fcc2f5bf6b79'
api_secret = u'7ccc9bb5a890e188'
access_token = u'72157720905634064-b51bc0c1ece259d6'
token_secret = u'6600870aa2f3f405'


def get_popular_photos():
    url = f'https://www.flickr.com/services/rest?method=flickr.photos.getPopular&oauth_consumer_key={api_key}&oauth_token={access_token}&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1704463021&oauth_nonce=wTruodfKEa1&oauth_version=1.0&oauth_callback=http%3A%2F%2Fexample.com&oauth_verifier=561978901e2ae1fc&oauth_signature=Gen51DiUPcN2iW1PK2IM4pjumyU%3D'
    response = requests.get(url)

    if response.status_code != 200 or response.headers["Content-Type"] != 'text/xml; charset=utf-8':
        return "Invalid"

    return "valid"


print(get_popular_photos())
