from facebook_business.adobjects.campaign import Campaign
import requests
from rich import print
from dotenv import dotenv_values
from enum import Enum

config = dotenv_values("secrets.env") 


#Meta
META_API_VERSION = 'v15.0'
INSTAGRAM_POST_API_URL = 'https://graph.facebook.com/{API_VERSION}'.format(META_API_VERSION)
META_MARKETING_API_URL = 'https://graph.facebook.com/{API_VERSION}'.format(META_API_VERSION)


    

# Post media to Instagram
# Docs: https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#get-media

def createInstagramPost(userID, imageUrl, isCarouselItem, caption, locationID, userTags, productTags):
    endpoint = '/{IG_USER_ID}/media'.format(IG_USER_ID = userID)
    params = {
        'image_url': imageUrl,
        'is_carousel_item': isCarouselItem,
        'caption': caption,
        'location_id': locationID,
        'user_tags': userTags,
        'product_tags': productTags,
        'access_token': config['META_ACCESS_TOKEN'],
    }
    res = requests.post(f'{INSTAGRAM_POST_API_URL}/{endpoint}', data=params)
    return res.json()

#TODO: Get a valid ad account ID to test this function.
def getMetaMarketingCampaings(ad_account_ids:list[str]):
    campaigns:list(Campaign) = []
    for ID in ad_account_ids:
        endpoint = '/act_{AD_ACCOUNT_ID}/campaigns'.format(AD_ACCOUNT_ID = ID)
        res = requests.get(META_MARKETING_API_URL + endpoint)
        campaigns.append(res.json())
    return campaigns



