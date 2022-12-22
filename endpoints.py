from facebook_business.adobjects.campaign import Campaign
import requests
from rich import print, pretty
from dotenv import dotenv_values
from enum import Enum

config = dotenv_values("secrets.env") 
pretty.install()

MAT_USER_ID = 37377012865

#Meta
META_API_VERSION = 'v15.0'
META_API_URL = 'https://graph.facebook.com/{}'.format(META_API_VERSION)

#Meta Endpoints
INSTAGRAM_POSTS_ENDPOINT = '/{IG_USER_ID}/media'
#To be used AFTER authentication
PERSONAL_INSTAGRAM_POSTS_ENDPOINT = '/me/media?fields={FIELDS}&access_token={ACCESS_TOKEN}'
    
# Get user feed from Instagram
def getInstagramPosts(userID):
    endpoint = INSTAGRAM_POSTS_ENDPOINT.format(IG_USER_ID = userID)
    res = requests.get(META_API_URL+endpoint)
    return res.json()


# Post media to Instagram
# Docs: https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#get-media
def createInstagramPost(userID, imageUrl, isCarouselItem, caption, locationID, userTags, productTags):
    endpoint = INSTAGRAM_POSTS_ENDPOINT.format(IG_USER_ID = userID)
    params = {
        'image_url': imageUrl,
        'is_carousel_item': isCarouselItem,
        'caption': caption,
        'location_id': locationID,
        'user_tags': userTags,
        'product_tags': productTags,
        'access_token': config['META_ACCESS_TOKEN'],
    }
    res = requests.post(f'{META_API_URL}/{endpoint}', data=params)
    return res.json()


#TODO: Get a valid ad account ID with marketing campaigns to test this function.
def getMetaMarketingCampaings(ad_account_ids:list[str]):
    campaigns:list(Campaign) = []
    for ID in ad_account_ids:
        endpoint = '/act_{AD_ACCOUNT_ID}/campaigns'.format(AD_ACCOUNT_ID = ID)
        res = requests.get(META_API_URL + endpoint)
        campaigns.append(res.json())
    return campaigns



