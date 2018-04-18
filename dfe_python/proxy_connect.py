# -*- coding: utf-8 -*-
# module for connecting to a proxy
# use Python naming convention
# https://www.python.org/dev/peps/pep-0008/#naming-conventions

def connect_to_proxy(username,pword_filepath):
    import requests #For sending requests from Python
    from requests.auth import HTTPProxyAuth #For proxy authentification
    #e.g. username = 'cstaff'
    pword = open(pword_filepath,'r')#example 'misc/my_password.txt'
    password = pword.read()
    pword.close()
    #Proxy IP and port; Note that the HTTP proxy (lonbloxx01) will be decommissioned towards the end of the year
    proxy_string_http = 'http://192.168.2.40:8080'
    proxy_string_https = 'https://10.20.18.3:9090'
        
    #Create a http session
    session_http = requests.Session()
    #Whether or not to trust the environment for proxy configuration
    session_http.trust_env=False
    #Details proxies for different types of requests
    session_http.proxies = {"http": proxy_string_http}
    #Provides the authentication details (DfE login details)
    session_http.auth = HTTPProxyAuth("ad\\" + username,
                           password)
    
    #Create a https session
    session_https = requests.Session()
    #Whether or not to trust the environment for proxy configuration
    session_https.trust_env=False
    #Details proxies for different types of requests
    session_https.proxies = {"https": proxy_string_https}
    #Provides the authentication details (DfE login details)
    session_https.auth = HTTPProxyAuth("ad\\" + username,
                           password)
    #Detail URL
    url_http = "http://www.bbc.co.uk"
    
    #Send GET request
    request_http = session_http.get(url_http, verify=False)
    
    #Get status of request
    return request_http.status_code

    