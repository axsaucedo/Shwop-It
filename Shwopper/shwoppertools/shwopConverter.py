#This class will convert a link into an affiliate link if possible,
# otherwise it will return null
from urlparse import urlparse

def convertIntoAffiliate(url):
    url_elements = urlparse(url)[1].split('.')
    # url_elements = ["abcde","co","uk"]

    #Removing the www if present
    www = 0
    if url_elements[0] == "www":
        www = 1
    domain = ''.join(url_elements[www:])

    domain = domain.lower()

    if domain in globals():
        return globals()[domain](url)

    return ""

def amazoncouk(url):
    return "http://" + urlparse(url)[1] + "/DummyAffiliateLink"

def amazoncom(url):
    return "http://" + urlparse(url)[1] + "/DummyAffiliateLink"

def ebaycom(url):
    return "http://" + urlparse(url)[1] + "/DummyAffiliateLink"

def ebaycouk(url):
    return "http://" + urlparse(url)[1] + "/DummyAffiliateLink"

def storeapplecom(url):
    return "http://" + urlparse(url)[1] + "/DummyAffiliateLink"