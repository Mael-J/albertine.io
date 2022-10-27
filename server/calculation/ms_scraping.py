import datetime
from investpy.utils.extra import random_user_agent
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
import re
from mstarpy import Funds, search_funds
import numpy as np




def get_carbonMetrics(code, bearerToken, proxy_dict = None):
    """Get carbon metrics"""

    
    #url of API
    url = """https://www.us-api.morningstar.com/sal/sal-service/fund/esg/carbonMetrics/%s/data""" % (code)

    #params
    params = {
            "languageId": "en-GB",
            "locale": "en-GB",
            "clientId": "MDC_intl",
            "benchmarkId": "mstarorcat",
            "component": "sal-components-mip-carbon-metrics",
            "version": "3.60.0"
    }

    #headers
    headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': 'Bearer %s' % (bearerToken),
                'credentials': 'omit',
                'origin': 'https://www.morningstar.co.uk',
                'referer': 'https://www.morningstar.co.uk/',
                'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': random_user_agent(),
                'X-API-RequestId': '6c20ob56-8055-aa34-9632-5f5a0dbbvboi',
                'X-SAL-ContentType': 'e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU='
                }    
    response = requests.get(url,params=params, headers=headers, proxies=proxy_dict)
    if response.status_code == 200:
         
        result =json.loads(response.content.decode()) 
    else:
        print("get_carbonMetrics",response)
        result = {}
    return result

def get_esgData(code, bearerToken, proxy_dict = None):
    """Get ESG"""

    
    #url of API
    url = """https://www.us-api.morningstar.com/sal/sal-service/fund/esg/v1/%s/data""" % (code)

    #params
    params = {
            "languageId": "en-GB",
            "locale": "en-GB",
            "clientId": "MDC_intl",
            "benchmarkId": "mstarorcat",
            "component": "sal-components-sustainability",
            "version": "3.60.0"
    }

    #headers
    headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': 'Bearer %s' % (bearerToken),
                'credentials': 'omit',
                'origin': 'https://www.morningstar.co.uk',
                'referer': 'https://www.morningstar.co.uk/',
                'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': random_user_agent(),
                'X-API-RequestId': '6c20ob56-8055-aa34-9632-5f5a0dbbvboi',
                'X-SAL-ContentType': 'e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU='
                }    
    response = requests.get(url,params=params, headers=headers, proxies=proxy_dict)
    if response.status_code == 200:
         
        result =json.loads(response.content.decode()) 
    else:
        print("get_esgData",response)
        result = {}
    return result

def get_creditQuality(code, bearerToken, proxy_dict = None):
    """Get credit quality"""


    #url of API
    url = """https://www.us-api.morningstar.com/sal/sal-service/fund/portfolio/creditQuality/%s/data""" % (code)

    #params
    params = {
            "languageId": "en-GB",
            "locale": "en-GB",
            "clientId": "MDC_intl",
            "benchmarkId": "mstarorcat",
            "component": "sal-components-mip-credit-quality",
            "version": "3.60.0"
    }

    #headers
    headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': 'Bearer %s' % (bearerToken),
                'credentials': 'omit',
                'origin': 'https://www.morningstar.co.uk',
                'referer': 'https://www.morningstar.co.uk/',
                'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': random_user_agent(),
                'X-API-RequestId': '6c20ob56-8055-aa34-9632-5f5a0dbbvboi',
                'X-SAL-ContentType': 'e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU='
                }    
    response = requests.get(url,params=params, headers=headers, proxies=proxy_dict)
    if response.status_code == 200:
         
        result =json.loads(response.content.decode()) 
    else:
        print("get_creditQuality", response)
        result = {}
    return result

def get_fixedIncomeStyle(code, bearerToken, proxy_dict = None):
    """Get Fixed Income Style"""

    
    #url of API
    url = """https://www.us-api.morningstar.com/sal/sal-service/fund/process/fixedIncomeStyle/%s/data""" % (code)

    #params
    params = {
            "languageId": "en-GB",
            "locale": "en-GB",
            "clientId": "MDC_intl",
            "benchmarkId": "mstarorcat",
            "component": "sal-components-mip-fixed-income-style",
            "version": "3.60.0"
    }

    #headers
    headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': 'Bearer %s' % (bearerToken),
                'credentials': 'omit',
                'origin': 'https://www.morningstar.co.uk',
                'referer': 'https://www.morningstar.co.uk/',
                'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': random_user_agent(),
                'X-API-RequestId': '6c20ob56-8055-aa34-9632-5f5a0dbbvboi',
                'X-SAL-ContentType': 'e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU='
                }    
    response = requests.get(url,params=params, headers=headers, proxies=proxy_dict)
    if response.status_code == 200:
         
        result =json.loads(response.content.decode()) 
    else:
        print("get_fixedIncomeStyle", response)
        result = {}
    return result
def get_sector(code, bearerToken, proxy_dict = None):
    """Get sector"""

    #url of API
    url = """https://www.us-api.morningstar.com/sal/sal-service/fund/portfolio/v2/sector/%s/data""" % (code)

    #params
    params = {
            "languageId": "en-GB",
            "locale": "en-GB",
            "clientId": "MDC_intl",
            "benchmarkId": "mstarorcat",
            "component": "sal-components-mip-sector-exposure",
            "version": "3.60.0"
    }

    #headers
    headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': 'Bearer %s' % (bearerToken),
                'credentials': 'omit',
                'origin': 'https://www.morningstar.co.uk',
                'referer': 'https://www.morningstar.co.uk/',
                'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': random_user_agent(),
                'X-API-RequestId': '6c20ob56-8055-aa34-9632-5f5a0dbbvboi',
                'X-SAL-ContentType': 'e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU='
                }    
    response = requests.get(url,params=params, headers=headers, proxies=proxy_dict)
    if response.status_code == 200:
         
        result =json.loads(response.content.decode()) 
    else:
        print("get_sector",response)
        result = {}
    return result
def get_financialMetrics(code, bearerToken, proxy_dict = None):
    """Get financial metrics"""

    
    #url of API
    url = """https://www.us-api.morningstar.com/sal/sal-service/fund/process/financialMetrics/%s/data""" % (code)

    #params
    params = {
            "languageId": "en-GB",
            "locale": "en-GB",
            "clientId": "MDC_intl",
            "benchmarkId": "mstarorcat",
            "component": "sal-components-mip-financial-metrics",
            "version": "3.60.0"
    }

    #headers
    headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': 'Bearer %s' % (bearerToken),
                'credentials': 'omit',
                'origin': 'https://www.morningstar.co.uk',
                'referer': 'https://www.morningstar.co.uk/',
                'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': random_user_agent(),
                'X-API-RequestId': '6c20ob56-8055-aa34-9632-5f5a0dbbvboi',
                'X-SAL-ContentType': 'e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU='
                }    
    response = requests.get(url,params=params, headers=headers, proxies=proxy_dict)
    if response.status_code == 200:
         
        result =json.loads(response.content.decode()) 
    else:
        print("get_financialMetrics",response)
        result = {}
    return result
def get_marketCap(code, bearerToken, proxy_dict = None):
    """Get market Cap"""

    #url of API
    url = """https://www.us-api.morningstar.com/sal/sal-service/fund/process/marketCap/%s/data""" % (code)

    #params
    params = {
            "languageId": "en-GB",
            "locale": "en-GB",
            "clientId": "MDC_intl",
            "benchmarkId": "mstarorcat",
            "component": "sal-components-mip-market-cap",
            "version": "3.60.0"
    }

    #headers
    headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': 'Bearer %s' % (bearerToken),
                'credentials': 'omit',
                'origin': 'https://www.morningstar.co.uk',
                'referer': 'https://www.morningstar.co.uk/',
                'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': random_user_agent(),
                'X-API-RequestId': '6c20ob56-8055-aa34-9632-5f5a0dbbvboi',
                'X-SAL-ContentType': 'e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU='
                }    
    response = requests.get(url,params=params, headers=headers, proxies=proxy_dict)
    if response.status_code == 200:
     
        result =json.loads(response.content.decode()) 
    else:
        print("get_marketCap", response)
        result = {}
    return result

def get_stockStyle(code, bearerToken, proxy_dict = None):
    """Get stock Style"""
    #url of API
    url = """https://www.us-api.morningstar.com/sal/sal-service/fund/process/stockStyle/v2/%s/data""" % (code)

    #params
    params = {
            "languageId": "en-GB",
            "locale": "en-GB",
            "clientId": "MDC_intl",
            "benchmarkId": "mstarorcat",
            "component": "sal-components-mip-measures",
            "version": "3.60.0"
    }

    #headers
    headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': 'Bearer %s' % (bearerToken),
                'credentials': 'omit',
                'origin': 'https://www.morningstar.co.uk',
                'referer': 'https://www.morningstar.co.uk/',
                'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': random_user_agent(),
                'X-API-RequestId': '6c20ob56-8055-aa34-9632-5f5a0dbbvboi',
                'X-SAL-ContentType': 'e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU='
                }    
    response = requests.get(url,params=params, headers=headers, proxies=proxy_dict)
    if response.status_code == 200:
     
        result =json.loads(response.content.decode()) 
    else:
        print("get_stockStyle", response)
        result = {}
    return result
def get_factorProfile(code, bearerToken, proxy_dict = None):
    """Get factor Profile"""
    
    #url of API
    url = """https://www.us-api.morningstar.com/sal/sal-service/fund/factorProfile/%s/data""" % (code)

    #params
    params = {
            "languageId": "en-GB",
            "locale": "en-GB",
            "clientId": "MDC_intl",
            "benchmarkId": "mstarorcat",
            "component": "sal-components-mip-factor-profile",
            "version": "3.60.0"
    }

    #headers
    headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': 'Bearer %s' % (bearerToken),
                'credentials': 'omit',
                'origin': 'https://www.morningstar.co.uk',
                'referer': 'https://www.morningstar.co.uk/',
                'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': random_user_agent(),
                'X-API-RequestId': '6c20ob56-8055-aa34-9632-5f5a0dbbvboi',
                'X-SAL-ContentType': 'e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU='
                }    
    response = requests.get(url,params=params, headers=headers, proxies=proxy_dict)
    if response.status_code == 200:
     
        result = json.loads(response.content.decode()) 
    else:
        print("get_factorProfile", response)
        result = {}
    return result
def get_ownershipZone(code, bearerToken, proxy_dict = None):
    """Get ownershipZone"""
    #url of API
    url = """https://www.us-api.morningstar.com/sal/sal-service/fund/process/ownershipZone/%s/data""" % (code)

    #params
    params = {
            "languageId": "en-GB",
            "locale": "en-GB",
            "clientId": "MDC_intl",
            "benchmarkId": "mstarorcat",
            "component": "sal-components-mip-stock-style",
            "version": "3.60.0"
    }

    #headers
    headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': 'Bearer %s' % (bearerToken),
                'credentials': 'omit',
                'origin': 'https://www.morningstar.co.uk',
                'referer': 'https://www.morningstar.co.uk/',
                'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': random_user_agent(),
                'X-API-RequestId': '6c20ob56-8055-aa34-9632-5f5a0dbbvboi',
                'X-SAL-ContentType': 'e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU='
                }    
    response = requests.get(url,params=params, headers=headers, proxies=proxy_dict)
    if response.status_code == 200:
     
        result =json.loads(response.content.decode())
    else:
        print("get_ownershipZone", response)
        result = {}
    return result
def get_asset(code, bearerToken):
    """Get asset allocation"""

    #url of API
    url = """https://www.us-api.morningstar.com/sal/sal-service/fund/process/asset/v2/%s/data""" % (code)

    #params
    params = {
            "languageId": "en-GB",
            "locale": "en-GB",
            "clientId": "MDC_intl",
            "benchmarkId": "mstarorcat",
            "component": "sal-components-mip-asset-allocation",
            "version": "3.60.0"
    }

    #headers
    headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': 'Bearer %s' % (bearerToken),
                'credentials': 'omit',
                'origin': 'https://www.morningstar.co.uk',
                'referer': 'https://www.morningstar.co.uk/',
                'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': random_user_agent(),
                'X-API-RequestId': '6c20ob56-8055-aa34-9632-5f5a0dbbvboi',
                'X-SAL-ContentType': 'e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU='
                }    
    response = requests.get(url,params=params, headers=headers, proxies=proxy_dict)
    if response.status_code == 200:
        result = json.loads(response.content.decode())
    else:
        print("get_asset", response)
        result = {}
    return result

def get_position(code, bearerToken, proxy_dict = None):
    """Get All positions of the Funds"""

    
    #url of API
    url = """https://www.us-api.morningstar.com/sal/sal-service/fund/portfolio/holding/v2/%s/data""" % (code)

    #params
    params = {
        'premiumNum': '1000',
        'freeNum': '1000',
        'languageId': 'en-GB',
        'locale': 'en-GB',
        'clientId': 'MDC_intl',
        'benchmarkId': 'category',
        'component': 'sal-components-mip-holdings',
        'version': '3.40.1'
        }

    #headers
    headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': 'Bearer %s' % (bearerToken),
                'credentials': 'omit',
                'origin': 'https://www.morningstar.co.uk',
                'referer': 'https://www.morningstar.co.uk/',
                'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': random_user_agent(),
                'X-API-RequestId': '6c20ob56-8055-aa34-9632-5f5a0dbbvboi',
                'X-SAL-ContentType': 'e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU='
                }    
    response = requests.get(url,params=params, headers=headers, proxies=proxy_dict)
    if response.status_code == 200:
        result =json.loads(response.content.decode())
        
    else:
        print("get_position", response)
        result = {}
    return result


def historicalData(loaded_funds):
    """get historical data of loaded funds"""
    data =loaded_funds.historicalData()
    df = pd.DataFrame(data["graphData"]["fund"])
    #df["date"] =pd.to_datetime(df["date"])
    df["pct"] = (df["value"]/df["value"].shift(1)-1).fillna(0)
    df["base_100"] = 100*np.cumprod(1+df["pct"])
    df = df.set_index("date")
    return df["base_100"].to_dict()

def scrape_page(funds_code):
    """retrieve info from pages overview, performance, risk, management, fees"""
    #dictionary of result
    result = {}
    #headers random agent
    headers = {'user-agent' : random_user_agent()}
    #Page 1 - overview
    #url page overview
    url = 'https://www.morningstar.fr/fr/funds/snapshot/snapshot.aspx?id=%s' % (funds_code)
    #get HTML page overview
    response = requests.get(url, headers=headers)
    #if page non found
    
    if response.status_code == 404:
        return result
    if "Le fonds demandé n'est pas enregistré à la vente dans le pays suivant" in response.text:
        return result
    else:
        #html page as soup
        soup = BeautifulSoup(response.text, 'html.parser')
        #investment objective funds
        result['objective'] = soup.find(id='overviewObjectiveDiv').find('td', {"class": "value text"}).text
        #benchmark and category
        benchmark = soup.find(id='overviewBenchmarkDiv2Cols').find_all('td', {"class": "value text"})
        result['benchmark'] = benchmark[0].text
        result['category'] = benchmark[1].text

        result['ISIN'] = soup.find(id='overviewQuickstatsDiv').find_all('td', {"class": "line text"})[2].text

        #page 1 - performance
        url = 'https://www.morningstar.fr/fr/funds/snapshot/snapshot.aspx?id=%s&tab=1' % (funds_code)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        #annual performance
        #report date annual performance
        annual_performance_date = soup.find(id='returnsCalenderYearDiv').find('td', {"class": "titleBarNote"}).text
        result['annual_performance_date'] = annual_performance_date 
        #label are dates
        regex = re.compile('.*heading number')
        label_list = soup.find(id='returnsCalenderYearDiv').find_all('td', {"class": regex})
        #funds performance, category performance, index performance, rank in category
        regex = re.compile('.*value number')
        #values
        value_list = soup.find(id='returnsCalenderYearDiv').find_all('td', {"class": regex})
        #loop on category
        count = 0
        for cat in ['funds_performance','category_performance', 'index_performance', 'rank']:
            #first col is nothing
            for i in range(1, len(label_list)):
                label = label_list[i].text
                #if today
                if '/' in label:
                    label = 'current'
                #add category to label
                if label:
                    label += '_'+ cat
                    result[label] = value_list[i+(count)*(len(label_list)-1)-1].text
            #next category
            count += 1
        #cumulative performance
        cumulative_performance_date = soup.find(id='returnsTrailingDiv').find('td', {"class": "titleBarNote"}).text
        result['cumulative_performance_date'] = cumulative_performance_date 
        #days
        regex = re.compile('.*label')
        label_list = soup.find(id='returnsTrailingDiv').find_all('td', {"class": regex})
        #performance fund
        regex = re.compile('.*col2 value number')
        value_list_funds = soup.find(id='returnsTrailingDiv').find_all('td', {"class": regex})
        #performance category
        regex = re.compile('.*col3 value number')
        value_list_category = soup.find(id='returnsTrailingDiv').find_all('td', {"class": regex})
        #performance index
        regex = re.compile('.*col4 value number')
        value_list_index  = soup.find(id='returnsTrailingDiv').find_all('td', {"class": regex})
        #loop on label
        for i in range(0, len(label_list)):
            #label
            label = label_list[i].text
            #perf funds
            result['fund_cumulative_performance_' + label] = re.sub('[^0-9,-]','',value_list_funds[i].text)
            #perf category
            result['category_cumulative_performance_' + label] = re.sub('[^0-9,-]','',value_list_category [i].text)
            #perf index
            result['index_cumulative_performance_' + label] = re.sub('[^0-9,-]','',value_list_index[i].text)

        #quarterly performance
        quarterly_performance_date = soup.find(id='returnsQuarterlyDiv').find('td', {"class": "titleBarNote"}).text
        result['quarterly_performance_date'] = cumulative_performance_date 

        #quarter label
        regex = re.compile('.*heading number')
        quarter_list = soup.find(id='returnsQuarterlyDiv').find_all('td', {"class": regex})
        #year label
        regex = re.compile('.*label')
        year_list =soup.find(id='returnsQuarterlyDiv').find_all('td', {"class": regex})
        #1st Quarter 
        regex = re.compile('.*col2 value number')
        quarter_1_list = soup.find(id='returnsQuarterlyDiv').find_all('td', {"class": regex})
        #2nd Quarter
        regex = re.compile('.*col3 value number')
        quarter_2_list = soup.find(id='returnsQuarterlyDiv').find_all('td', {"class": regex})
        #3rd Quarter
        regex = re.compile('.*col4 value number')
        quarter_3_list = soup.find(id='returnsQuarterlyDiv').find_all('td', {"class": regex})
        #4th Quarter
        regex = re.compile('.*col5 value number')
        quarter_4_list = soup.find(id='returnsQuarterlyDiv').find_all('td', {"class": regex})
        #loop on year
        for i in range(0, len(year_list)):
            label = 'performance_%s_' % (year_list[i].text)
            result[label + 'quarter_1'] = quarter_1_list[i].text
            result[label + 'quarter_2'] = quarter_2_list[i].text
            result[label + 'quarter_3'] = quarter_3_list[i].text
            result[label + 'quarter_4'] = quarter_4_list[i].text

        #page 2 - Risk
        url = 'https://www.morningstar.fr/fr/funds/snapshot/snapshot.aspx?id=%s&tab=2' % (funds_code)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        #report date quarter performance
        risk_date = soup.find(id='ratingRiskDiv').find('td', {"class": "titleBarNote"}).text
        result['risk_date'] = risk_date
        #volatility and average performance
        label_list =soup.find(id='ratingRiskLeftDiv').find_all('td', {"class": 'label'})
        value_list = soup.find(id='ratingRiskLeftDiv').find_all('td', {"class": 'value number'})
        #loop on label
        for i in range(0, len(value_list)):
            #label
            label = label_list[i].text
            result[label] = value_list[i].text

        #sharpe 3 years
        sharpe_3Y = soup.find(id='ratingRiskRightDiv').find('td', {"class": 'value'}).text
        result['sharpe_3Y'] = sharpe_3Y

        

        #page 4 - info about found
        url = 'https://www.morningstar.fr/fr/funds/snapshot/snapshot.aspx?id=%s&tab=4' % (funds_code)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        #label
        label_list = soup.find(id='managementManagementDiv').find_all('td', {"class": "col1 label"})
        #value
        value_list = soup.find(id='managementManagementDiv').find_all('td', {"class": "col2 value number"})
        for i in range(0, len(value_list)):
            label = label_list[i].text
            
            result[label] = value_list[i].text
        #page 5 - fees
        url = 'https://www.morningstar.fr/fr/funds/snapshot/snapshot.aspx?id=%s&tab=5' % (funds_code)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        #label
        label_list =soup.find(id='managementFeesDiv').find_all('td', {"class": "label"})
        #value
        value_list = soup.find(id='managementFeesDiv').find_all('td', {"class": "value number"}) + soup.find(id='managementFeesDiv').find_all('td', {"class": "value number jdpa"})
        for i in range(0, len(value_list)):
            label = label_list[i].text
            result[label] = re.sub('(\\n +)|(\\n)','',value_list[i].text)

    return result




def get_bearer_token(funds_code, proxy_dict = None):
        """get the Bearer Token"""
        url = 'https://www.morningstar.fr/Common/funds/snapshot/PortfolioSAL.aspx'
        
        headers = {'user-agent' : random_user_agent()}

        payload = {
        'Site': 'fr',
        'FC': funds_code,
        'IT': 'FO',
        'LANG': 'fr-FR'}




        response = requests.get(url, headers=headers, params=payload, proxies=proxy_dict)
        soup = BeautifulSoup(response.text, 'html.parser')
        script = soup.find('script', {'type':'text/javascript'})
        bearerToken = str(script).split('tokenMaaS:')[-1].split('}')[0].replace('"','').strip()
        return bearerToken

def fund_info(funds_code, proxy_dict = None):
    """Get info about fund"""
    #list of funds
    url_funds = 'https://tools.morningstar.co.uk/api/rest.svc/klr5zyak8x/security/screener'
    #old
    #url_funds ='https://lt.morningstar.com/api/rest.svc/klr5zyak8x/security/screener'
    #empty DataFrame
    df_funds = pd.DataFrame()

        
    params = {
            'page': 1,
            'pageSize':10,
            'sortOrder': 'LegalName asc',
            'outputType': 'json',
            'version' : 1,
            'languageId' : 'fr-FR',
            'currencyId': 'EUR',
            'universeIds':'FOFRA$$ALL',
            'securityDataPoints':"""SecId|Name|PriceCurrency|TenforeId|LegalName|ClosePrice|StarRatingM255|SustainabilityRank|QuantitativeRating|AnalystRatingScale|CategoryName|Yield_M12|GBRReturnD1|GBRReturnW1|GBRReturnM1|GBRReturnM3|GBRReturnM6|GBRReturnM0|GBRReturnM12|GBRReturnM36|GBRReturnM60|GBRReturnM120|MaxFrontEndLoad|OngoingCostActual|PerformanceFeeActual|TransactionFeeActual|MaximumExitCostAcquired|FeeLevel|ManagerTenure|MaxDeferredLoad|InitialPurchase|FundTNAV|EquityStyleBox|BondStyleBox|AverageMarketCapital|AverageCreditQualityCode|EffectiveDuration|MorningstarRiskM255|AlphaM36|BetaM36|R2M36|StandardDeviationM36|SharpeM36|InvestorTypeRetail|InvestorTypeProfessional|InvestorTypeEligibleCounterparty|ExpertiseBasic|ExpertiseAdvanced|ExpertiseInformed|ReturnProfilePreservation|ReturnProfileGrowth|ReturnProfileIncome|ReturnProfileHedging|ReturnProfileOther|TrackRecordExtension|investmentObjective|investmentExpertise|investorType|investment|instrumentName|largestSector|globalAssetClassId|brandingCompanyId|categoryId|distribution|equityStyle|administratorCompanyId|fundSize|fundStyle|umbrellaCompanyId|geoRegion|globalCategoryId|investmentExpertise|managementStyle|ongoingCharge|riskSrri|shareClassType|starRating|sustainabilityRating|yieldPercent|totalReturnTimeFrame|totalReturn|iMASectorId|ReturnD1|ReturnW1|ReturnM1|ReturnM3|ReturnM6|ReturnM0|ReturnM12|ReturnM36|ReturnM60|ReturnM120""",
            
            'filters' : '',   
            'term' : funds_code,
            'subUniverseId' : '',

        }
    headers = {'user-agent' : random_user_agent()}



    response = requests.get(url_funds, headers=headers,params=params,proxies=proxy_dict)
    if response.status_code == 200:
        result =json.loads(response.content.decode())
        if result:
            return result['rows'][0]
        else:
            print("fund_info", response)
            return {}
    else:
        return {}
        
        


if __name__ == '__main__':
    #d = get_bearer_token('F00000WUZO')
    proxy_dict = {
                'https': "http://10.118.4.13:8086",
                'http': "http://10.118.4.13:8086",
                  
                  }
    data = fund_info('F00000ZZZB', proxy_dict = proxy_dict )
    print(data)

    