from flask import Blueprint, jsonify, request, send_file
from calculation.ms_scraping import scrape_page
from myclass.report import REPORT
import json
import pandas as pd
from io import BytesIO
from mstarpy import Funds, search_funds
import numpy as np


# prefix of the route
prefix = "/api/funds"

funds = Blueprint('funds',__name__)


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
    
    return send_file(pdf, download_name='output.pdf', as_attachment=True, mimetype='application/pdf')

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
    return send_file(output, download_name='output.xlsx', as_attachment=True)



@funds.route("%s/historicaldata" % (prefix), methods = ['GET'])
def get_data():
  """get historical data"""
  code_str = request.args.get('code')
  code_list = json.loads(code_str)
  df = pd.DataFrame()
  
  for code in code_list:
    funds = Funds(code["value"])
    data = funds.historicalData()
    df_funds = pd.DataFrame(data["graphData"]["fund"])
    df_funds = df_funds.rename(columns= {"value" : f"{funds.name}"})
    if df.empty:
      df = df_funds
    else:
      if not df_funds.empty:
        df = df.merge(df_funds, how = 'inner', on ='date', )
  if df.empty:
    return jsonify([]), 200
  df = df.set_index("date")
  df = (df/df.shift(1)-1).fillna(0)
  df = round(100*np.cumprod(1+df),2)
  df =df.reset_index()
  
  return df.to_json(orient='records')



@funds.route("%s/currentdata" % (prefix), methods = ['GET'])
def get_currentdata():
  """get info about funds """
  
  
  result_list = []
  code_str = request.args.get('code')
  code_list = json.loads(code_str)

  for code in code_list:
    try:
      funds = Funds(code["value"])
      #all info from screener
      infos_list = funds.dataPoint(['SecId',	'Name',	'PriceCurrency',	'TenforeId',	'LegalName',	'ClosePrice',	'StarRatingM255',	'SustainabilityRank',	'QuantitativeRating',	'AnalystRatingScale',	'CategoryName',	'Yield_M12',	'GBRReturnD1',	'GBRReturnW1',	'GBRReturnM1',	'GBRReturnM3',	'GBRReturnM6',	'GBRReturnM0',	'GBRReturnM12',	'GBRReturnM36',	'GBRReturnM60',	'GBRReturnM120',	'MaxFrontEndLoad',	'OngoingCostActual',	'PerformanceFeeActual',	'TransactionFeeActual',	'MaximumExitCostAcquired',	'FeeLevel',	'ManagerTenure',	'MaxDeferredLoad',	'InitialPurchase',	'FundTNAV',	'EquityStyleBox',	'BondStyleBox',	'AverageMarketCapital',	'AverageCreditQualityCode',	'EffectiveDuration',	'MorningstarRiskM255',	'AlphaM36',	'BetaM36',	'R2M36',	'StandardDeviationM36',	'SharpeM36',	'InvestorTypeRetail',	'InvestorTypeProfessional',	'InvestorTypeEligibleCounterparty',	'ExpertiseBasic',	'ExpertiseAdvanced',	'ExpertiseInformed',	'ReturnProfilePreservation',	'ReturnProfileGrowth',	'ReturnProfileIncome',	'ReturnProfileHedging',	'ReturnProfileOther',	'TrackRecordExtension',	'investmentObjective',	'investmentExpertise',	'investorType',	'investment',	'instrumentName',	'largestSector',	'globalAssetClassId',	'brandingCompanyId',	'categoryId',	'distribution',	'equityStyle',	'administratorCompanyId',	'fundSize',	'fundStyle',	'umbrellaCompanyId',	'geoRegion',	'globalCategoryId',	'investmentExpertise',	'managementStyle',	'ongoingCharge',	'riskSrri',	'shareClassType',	'starRating',	'sustainabilityRating',	'yieldPercent',	'totalReturnTimeFrame',	'totalReturn',	'iMASectorId',	'ReturnD1',	'ReturnW1',	'ReturnM1',	'ReturnM3',	'ReturnM6',	'ReturnM0',	'ReturnM12',	'ReturnM36',	'ReturnM60',	'ReturnM120',])
      if infos_list:
        infos = infos_list[0]
      else:
        infos = {}
      #info from pages
      pages = scrape_page(code["value"])
      #position of the funds
      positions= funds.position()
      #market cap
      marketCap = funds.marketCapitalization()
      #sector
      sector = funds.sector()
      #credit Quality
      creditQuality = funds.creditQuality()
      #stock style
      stockStyle = funds.equityStyle()
      #bonds style
      bondStyle = funds.fixedIncomeStyle()
      #esg data
      esgData = funds.esgData()

      #carbon metrics
      carbonMetrics = funds.carbonMetrics()

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
                'numberOfEquityHolding': numberOfEquityHolding, 'numberOfOtherHolding': numberOfOtherHolding,
                
                }
      result_list.append(result)
    except:
      continue
  if result_list:
    return jsonify(result_list), 200
  else:
    return jsonify([0]), 200

    
    

    

@funds.route("%s/info/<code>" % (prefix), methods = ['GET'])
def get_info(code):
    """get info about funds"""

    funds = Funds(code)

    #all info from screener
    infos_list = funds.dataPoint(['SecId',	'Name',	'PriceCurrency',	'TenforeId',	'LegalName',	'ClosePrice',	'StarRatingM255',	'SustainabilityRank',	'QuantitativeRating',	'AnalystRatingScale',	'CategoryName',	'Yield_M12',	'GBRReturnD1',	'GBRReturnW1',	'GBRReturnM1',	'GBRReturnM3',	'GBRReturnM6',	'GBRReturnM0',	'GBRReturnM12',	'GBRReturnM36',	'GBRReturnM60',	'GBRReturnM120',	'MaxFrontEndLoad',	'OngoingCostActual',	'PerformanceFeeActual',	'TransactionFeeActual',	'MaximumExitCostAcquired',	'FeeLevel',	'ManagerTenure',	'MaxDeferredLoad',	'InitialPurchase',	'FundTNAV',	'EquityStyleBox',	'BondStyleBox',	'AverageMarketCapital',	'AverageCreditQualityCode',	'EffectiveDuration',	'MorningstarRiskM255',	'AlphaM36',	'BetaM36',	'R2M36',	'StandardDeviationM36',	'SharpeM36',	'InvestorTypeRetail',	'InvestorTypeProfessional',	'InvestorTypeEligibleCounterparty',	'ExpertiseBasic',	'ExpertiseAdvanced',	'ExpertiseInformed',	'ReturnProfilePreservation',	'ReturnProfileGrowth',	'ReturnProfileIncome',	'ReturnProfileHedging',	'ReturnProfileOther',	'TrackRecordExtension',	'investmentObjective',	'investmentExpertise',	'investorType',	'investment',	'instrumentName',	'largestSector',	'globalAssetClassId',	'brandingCompanyId',	'categoryId',	'distribution',	'equityStyle',	'administratorCompanyId',	'fundSize',	'fundStyle',	'umbrellaCompanyId',	'geoRegion',	'globalCategoryId',	'investmentExpertise',	'managementStyle',	'ongoingCharge',	'riskSrri',	'shareClassType',	'starRating',	'sustainabilityRating',	'yieldPercent',	'totalReturnTimeFrame',	'totalReturn',	'iMASectorId',	'ReturnD1',	'ReturnW1',	'ReturnM1',	'ReturnM3',	'ReturnM6',	'ReturnM0',	'ReturnM12',	'ReturnM36',	'ReturnM60',	'ReturnM120',])
    if infos_list:
      infos = infos_list[0]
    else:
      infos = {}
    #info from pages
    pages = scrape_page(code)
    #position of the funds
    positions= funds.position()
    #market cap
    marketCap = funds.marketCapitalization()
    #sector
    sector = funds.sector()
    #credit Quality
    creditQuality = funds.creditQuality()
    #stock style
    stockStyle = funds.equityStyle()
    #bonds style
    bondStyle = funds.fixedIncomeStyle()
    #esg data
    esgData = funds.esgData()

    #carbon metrics
    carbonMetrics = funds.carbonMetrics()

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
              'numberOfEquityHolding': numberOfEquityHolding, 'numberOfOtherHolding': numberOfOtherHolding,
              
              }
  
    return jsonify(result), 200


@funds.route("%s/fundlist/<term>" % (prefix), methods = ['GET'])
def get_fund_list(term):
    """get list of funds based on user input"""
    funds_list = search_funds(term,["SecId","TenforeId","LegalName"])
    
    if funds_list :
      #rows to df
      df = pd.DataFrame(funds_list)
      
      #correction isin code
      df['TenforeId'] =df['TenforeId'].str[-12:]
      #label is name + isin 
      df['label'] = df['LegalName'] + ' : ' + df['TenforeId']
      #if TenforeIddoes not exist replace by sec id
      df['label'] = df['label'].fillna(df['LegalName'] + ' : ' + df['SecId'])
      #value is secid
      df = df.rename(columns={'SecId' : 'value'})
      #keep only value and label
      df = df[['value', 'label']]
      #convert DataFrame to json
      result = df.to_json(orient='records')
    else:
      result = [{}]
      
    return result

