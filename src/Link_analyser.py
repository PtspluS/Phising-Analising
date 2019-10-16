import requests
import re
from ip2geotools.databases.noncommercial import DbIpCity


'''
key_dic(key : obj, dic : {obj, obj}
    test if key are in dic 
    return :
        - True if key are inside
        - False if key are not inside
'''
def key_dic(key, dic):
    if key in dic:
        return True
    else:
        return False


'''
analyse_link(link : str)
    try to determine the concordance of the link
    return : 
        - ratio of the link who point on the same information
'''
def analyse_link(link):
    starter = re.findall("(https|http)", link)[0]+':/'
    regex_path = re.findall("\/?[\w\.\-]+\/", link)

    weight = 1/len(regex_path)           # use to determine the concordance

    country_list = {}                    # use to determined if the country was already present
    ip_list = {}                         # use to determined if the ip was already present
    latitude_list = {}                   # use to determined if the latitude was already present
    longitude_list = {}                  # use to determined if the longitude was already present

    url = starter
    for i in range(0,len(regex_path)):
        url += regex_path[i]
        ip = get_ip_from(url)
        details = find_details(ip)

        # test if the country are already check. If not, add the country to the list and give it a weight
        if(key_dic(details.country, country_list)):
            country_list[details.country] += weight
        else:
            country_list[details.country] = weight

        # test if ip is already check. If not, add the ip to the list and give it a weight
        if(key_dic(details.ip_address, ip_list)):
            ip_list[details.ip_address] += weight
        else:
            ip_list[details.ip_address] = weight

        # test if positions are already check. If not, add them to the list and give them weight
        if(key_dic(details.latitude, latitude_list)):
            latitude_list[details.latitude] += weight
        else:
            latitude_list[details.latitude] = weight

        # test if positions are already check. If not, add them to the list and give them weight
        if (key_dic(details.longitude, longitude_list)):
            longitude_list[details.longitude] += weight
        else:
            longitude_list[details.longitude] = weight




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
    elif not JSON:
        return response


'''
analyse_link_from(links : [str])
    automatise the analyse for all links given in param (typically links from documents)
    return : 
        - 
'''
def analyse_link_from(links):
    annalyse = {}
    for l in links:
        an = analyse_link(l)
        annalyse[l] = an

    pass


link = 'https://www.geeksforgeeks.org/python-program-find-ip-address/'
analyse_link(link)
