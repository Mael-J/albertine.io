from flask import Blueprint, jsonify, request, send_file
from pandas.core.frame import DataFrame
from calculation.ms_scraping import fund_info, get_bearer_token, scrape_page, get_position, get_marketCap, get_sector, get_creditQuality, get_stockStyle, get_fixedIncomeStyle, get_esgData, get_carbonMetrics
from myclass.report import REPORT, REPORTCANVA, REPORTCANVA2
from investpy.utils.extra import random_user_agent
import requests
import json
import pandas as pd
from io import BytesIO
import os


# prefix of the route
prefix = "/api/funds"

funds = Blueprint('funds',__name__)

proxy_dict = {
                'https': "http://10.118.4.13:8086",
                'http': "http://10.118.4.13:8086",
                  
                  }
@funds.route("%s/test" % (prefix), methods = ["GET"])
def test_api():
  return jsonify({"HELLO" : "world"}), 200

@funds.route("%s/download/pdf" % (prefix), methods = ["POST"])
def download_pdf():
    """download file as pdf"""

    data = request.json
    cla = REPORT(data)
    doc = cla.create_doc()
    pdf = cla.create_story(doc)
    del cla
    # cla = REPORTCANVA2()
    # pdf = cla.create_pdf()
    # del cla
    pdf.seek(0)
    
    return send_file(pdf, attachment_filename='output.pdf', as_attachment=True, mimetype='application/pdf', cache_timeout=0)

@funds.route("%s/download/excel" % (prefix), methods = ['POST'])
def download_excel():
    """download file as excel"""
    #data from post
    data = request.json
    #reset list
    idx = []
    core = []
    #bond style data
    for d in data:
      #funds id
      idx.append(d["infos"]['SecId'])
      core.append(d["bondStyle"]['fund'])
      #category id
      idx.append(d["infos"]['categoryId'])
      core.append(d["bondStyle"]['categoryAverage'])
    #bondsStyle DataFrame
    df_bonds = pd.DataFrame(core, index = idx).reset_index(drop = False)
    #reset list
    idx = []
    core = []
    #carbon data
    for d in data:
      #funds id
      idx.append(d["infos"]['SecId'])
      core.append(d["carbonMetrics"])
    #carbon DataFrame
    df_carbon = pd.DataFrame(core, index = idx).reset_index(drop = False)
    #reset list
    idx = []
    core = []

    #credit quality data
    for d in data:
      #funds id
      idx.append(d["infos"]['SecId'])
      core.append(d["creditQuality"]['fund'])
      #category id
      idx.append(d["infos"]['categoryId'])
      core.append(d["creditQuality"]['category'])
      #index name
      idx.append(d["creditQuality"]['indexName'])
      core.append(d["creditQuality"]['index'])
    #credit quality DataFrame
    df_creditQuality = pd.DataFrame(core, index = idx).reset_index(drop = False)

    #reset list
    idx = []
    core = []
    #esg Data
    for d in data:
      #funds id
      idx.append(d["infos"]['SecId'])
      core.append(d['esgData']['esgData'])
    df_esgData = pd.DataFrame(core, index = idx).reset_index(drop = False)
    #reset list
    idx = []
    core = []
    #esg calculation data
    for d in data:
      #funds id
      idx.append(d["infos"]['SecId'])
      core.append(d['esgData']['esgScoreCalculation'])
    df_esgScoreCalculation= pd.DataFrame(core, index = idx).reset_index(drop = False)
    #reset list
    idx = []
    core = []
    #sustainabilityIntentionality data
    for d in data:
      #funds id
      idx.append(d["infos"]['SecId'])
      core.append(d['esgData']['sustainabilityIntentionality'])
    df_sustainabilityIntentionality= pd.DataFrame(core, index = idx).reset_index(drop = False)
    #reset list
    idx = []
    core = []
    #fund characteristics data
    for d in data:
      #funds id
      idx.append(d["infos"]['SecId'])
      core.append(d['infos'])
    #funds characteristic DataFrame
    df_infos= pd.DataFrame(core, index = idx).reset_index(drop = False)
    #reset list
    idx = []
    core = []

    #market cap data
    for d in data:
      #funds id
      idx.append(d["infos"]['SecId'])
      core.append(d["marketCap"]['fund'])
      #category id
      idx.append(d["infos"]['categoryId'])
      core.append(d["marketCap"]['category'])
      #index name
      idx.append(d["marketCap"]['index']['name'])
      core.append(d["marketCap"]['index'])
    #market cap DataFrame
    df_marketCap = pd.DataFrame(core, index = idx).reset_index(drop = False)
    #reset list
    idx = []
    core = []
    #fund metrics data
    for d in data:
      #funds id
      idx.append(d["infos"]['SecId'])
      core.append(d['pages'])
    #funds metric DataFrame
    df_page= pd.DataFrame(core, index = idx).reset_index(drop = False)
    #reset list
    idx = []
    core = []
    #equity sector data
    for d in data:
      #funds id
      idx.append(d["infos"]['SecId'])
      core.append(d['sector']['EQUITY']["fundPortfolio"])
      #category id
      idx.append(d["infos"]['categoryId'])
      core.append(d['sector']['EQUITY']["categoryPortfolio"])
      #index name
      idx.append(d['sector']['EQUITY']['indexName'])
      core.append(d['sector']['EQUITY']['indexPortfolio'])
    #equitSector DataFrame
    df_equitySector = pd.DataFrame(core, index = idx).reset_index(drop = False)
    #reset list
    idx = []
    core = []
    #bonds sector data
    for d in data:
      #funds id
      idx.append(d["infos"]['SecId'])
      core.append(d['sector']['FIXEDINCOME']["fundPortfolio"])
      #category id
      idx.append(d["infos"]['categoryId'])
      core.append(d['sector']['FIXEDINCOME']["categoryPortfolio"])
      #index name
      idx.append(d['sector']['FIXEDINCOME']['indexName'])
      core.append(d['sector']['FIXEDINCOME']['indexPortfolio'])
    #bond sector DataFrame
    df_bondSector = pd.DataFrame(core, index = idx).reset_index(drop = False)
    #reset list
    idx = []
    core = []
    #stock syle data
    for d in data:
      #funds id
      idx.append(d["infos"]['SecId'])
      core.append(d['stockStyle']['fund'])
      #category id
      idx.append(d["infos"]['categoryId'])
      core.append(d['stockStyle']['categoryAverage'])
      #index name
      idx.append(d['sector']['FIXEDINCOME']['indexName'])
      core.append(d['stockStyle']['indexAverage'])
    #stock style DataFrame
    df_stockStyle = pd.DataFrame(core, index = idx).reset_index(drop = False)


    #holdings data
    df_holdings = pd.DataFrame()
    for d in data:
        df_buffer = pd.DataFrame()
        #equity holdings
        if 'equityHoldingPage' in d['positions']:
          df_equityHoldings = pd.DataFrame(d['positions']['equityHoldingPage']['holdingList'])
        else:
          df_equityHoldings = pd.DataFrame()
        #bond holdings
        if 'boldHoldingPage' in d['positions']:
          df_bondHoldings = pd.DataFrame(d['positions']['boldHoldingPage']['holdingList'])
        else:
          df_bondHoldings = pd.DataFrame()
        #other holdings
        if 'otherHoldingPage' in d['positions']:
          df_otherHoldings = pd.DataFrame(d['positions']['otherHoldingPage']['holdingList'])
        else:
          df_otherHoldings = pd.DataFrame()
        
        df_buffer = pd.concat([df_buffer, df_equityHoldings, df_bondHoldings, df_otherHoldings])
        df_buffer['portfolioId'] = d["infos"]['SecId']
        df_buffer['portfolioName'] = d["infos"]['LegalName']
        df_holdings = pd.concat([df_buffer, df_holdings])

    #blob
    # output =os.path.abspath(os.path.join(os.path.dirname( '__file__' ),'static/media', "albertine_letempsretrouve.xlsx"))
    # print(output)
    output = BytesIO()
    #to excel
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    #funds characteristics page
    df_infos.to_excel(writer, sheet_name='fundsCharacteristics', index = False)
    ##funds metrics page
    df_page.to_excel(writer, sheet_name='fundsMetrics', index = False)
    #bond Style page
    df_bonds.to_excel(writer, sheet_name='bondStyle', index = False)
    #carbon page
    df_carbon.to_excel(writer, sheet_name='carbonMetrics', index = False)
    #credit quality page
    df_creditQuality.to_excel(writer, sheet_name='creditQuality', index = False)
    #esg data page
    df_esgData.to_excel(writer, sheet_name='esgData', index = False)
    #esg calculation page
    df_esgScoreCalculation.to_excel(writer, sheet_name='esgScoreCalculation', index = False)
    #sustainabilityIntentionality page
    df_sustainabilityIntentionality.to_excel(writer, sheet_name='sustainabilityIntentionality', index = False)
    #marketCapitalization page
    df_marketCap.to_excel(writer, sheet_name='marketCapitalization', index = False)
    #holdings page
    df_holdings.to_excel(writer, sheet_name='holdings', index = False)
    #equity sector page
    df_equitySector.to_excel(writer, sheet_name='equitySector', index = False)
    #bonds sector page
    df_bondSector.to_excel(writer, sheet_name='bondSector', index = False)
    #stock style page
    df_stockStyle.to_excel(writer, sheet_name='stockStyle', index = False)

    #save update
    writer.save()
    output.seek(0)
    return send_file(output, attachment_filename='output.xlsx', as_attachment=True)



@funds.route("%s/info/<code>" % (prefix), methods = ['GET'])
def get_info(code):
    """get info about funds"""
    #get bearer token for authorization
    bearer = get_bearer_token(code, proxy_dict = proxy_dict)

    #all info from screener
    infos = fund_info(code,proxy_dict = proxy_dict)
    #info from pages
    pages = scrape_page(code, proxy_dict = proxy_dict)
    #position of the funds
    positions= get_position(code,bearer, proxy_dict = proxy_dict)
    #market cap
    marketCap = get_marketCap(code,bearer, proxy_dict = proxy_dict)
    #sector
    sector = get_sector(code,bearer, proxy_dict = proxy_dict)
    #credit Quality
    creditQuality = get_creditQuality(code,bearer, proxy_dict = proxy_dict)
    #stock style
    stockStyle = get_stockStyle(code,bearer, proxy_dict = proxy_dict)
    #bonds style
    bondStyle = get_fixedIncomeStyle(code,bearer, proxy_dict = proxy_dict)
    #esg data
    esgData = get_esgData(code,bearer, proxy_dict = proxy_dict)

    #carbon metrics
    carbonMetrics = get_carbonMetrics(code,bearer, proxy_dict = proxy_dict)

    #number of bonds
    if 'numberOfBondHolding' in positions:
      numberOfBondHolding = positions["numberOfBondHolding"]
    else:
      numberOfBondHolding = 0

    #number of equities
    if 'numberOfEquityHolding' in positions:
      numberOfEquityHolding = positions["numberOfEquityHolding"]
    else:
      numberOfEquityHolding = 0

    #number of other holdings
    if 'numberOfOtherHolding' in positions:
      numberOfOtherHolding = positions["numberOfOtherHolding"]
    else:
      numberOfOtherHolding = 0
    

    result = {'infos': infos, 'pages' : pages, 'positions': positions, 
              'marketCap': marketCap,'sector' : sector,
              'creditQuality' : creditQuality,'stockStyle' : stockStyle, 'bondStyle' : bondStyle,
              'esgData' : esgData, 'carbonMetrics' : carbonMetrics, 'numberOfBondHolding' : numberOfBondHolding,
              'numberOfEquityHolding': numberOfEquityHolding, 'numberOfOtherHolding': numberOfOtherHolding
              }
  
    return jsonify(result), 200


@funds.route("%s/fundlist/<term>" % (prefix), methods = ['GET'])
def get_fund_list(term):
    """get list of funds based on user input"""


    #url
    url = "https://tools.morningstar.co.uk/api/rest.svc/klr5zyak8x/security/screener"
  
    params = {
    'page' : 1,
    'pageSize' : 10,
    'sortOrder' : 'LegalName asc',
    'outputType' : 'json',
    'version' : 1,
    'languageId' : 'fr-FR',
    'currencyId' : 'EUR',
    'universeIds' : 'FOFRA$$ALL',
    'securityDataPoints' : 'SecId|TenforeId|LegalName',
    'term' : term,
    }

    #headers
    headers = {
                'user-agent': random_user_agent(),
                }   

    response = requests.get(url,params=params, headers=headers, proxies=proxy_dict)
    if response.status_code == 200:
      result =json.loads(response.content.decode())
      if result:
        rows = result['rows']
        #rows to df
        df = pd.DataFrame(rows)
        #correction isin code
        df['TenforeId'] =df['TenforeId'].str[-12:]
        #label is name + isin
        df['label'] = df['LegalName'] + ' : ' + df['TenforeId']
        #value is secid
        df = df.rename(columns={'SecId' : 'value'})
        #keep only value and label
        df = df[['value', 'label']]
        #convert DataFrame to json
        result = df.to_json(orient='records')
      else:
        result = {}
        
    else:
      print(response)
      result = {}
    return result

