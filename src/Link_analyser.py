import requests
from ip2geotools.databases.noncommercial import DbIpCity


def analyse_link(link):
    pass


'''
get_ip_from(link:str)
    try to get the ip address from the url
    return :
        - ip address (if it can determine it)
        - None (if it can't determine it)
'''
def get_ip_from(link):
    try:
        with requests.get(link, stream=True) as r:
            ip = r.raw._original_response.fp.raw._sock.getpeername()[0]
            return ip
    except Exception as e:
        print(e)
        return None


'''
find_details(ip: str)
    determine the country where are located the server
    return :
        - json {"ip_address" : str, "city": str, "region": str, "country": str, "latitude": float, "longitude": float} (if JSON = True)
        - object with the same attributes (if JSON = False)
'''
def find_details(ip, JSON = False):
    response = DbIpCity.get(ip, api_key='free')
    if JSON:
        return response.to_json()
    elif JSON == False :
        return response

def analyse_link_from(links):
    pass


ip = get_ip_from('https://trustme.ovh/')
print(find_details(ip).country)
