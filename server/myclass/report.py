from reportlab.platypus import Paragraph, Frame, Table, TableStyle, BaseDocTemplate, NextPageTemplate, PageTemplate, PageBreak, FrameBreak, Image, Flowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch, mm, cm
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.enums import TA_LEFT,TA_CENTER, TA_RIGHT ,TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib import utils
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.lib.formatters import DecimalFormatter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics import shapes
from reportlab.graphics.charts.textlabels import Label

import os
import datetime
import pandas as pd
from dateutil import parser
from .tools.utils import max_min_tick
from .mycolor import COLOR
from io import BytesIO

class ROUND_TITLE(Flowable):
    """
    RoundRect flowable --- draws a Round rect in a flowable
    """
 
    #----------------------------------------------------------------------
    def __init__(self, x, y, width, height, radius, texte,bg_color = colors.Color(red=(0/255),green=(32/255),blue=(96/255)), text_color = colors.Color(red=(255/255),green=(255/255),blue=(255/255)),   stroke=1, fill=0, ):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius = radius 
        self.stroke = stroke
        self.fill = fill
        self.texte = texte
        self.bg_color = bg_color
        self.text_color = text_color
        #pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
        #pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))
    #----------------------------------------------------------------------
    def draw(self):
        """
        draw the line
        """
        self.canv.setFillColor(self.bg_color)
        self.canv.roundRect(self.x, self.y, self.width, self.height, self.radius, self.stroke, self.fill)
        self.canv.setFillColor(self.text_color)
        self.canv.setFont("Helvetica",12)
        self.canv.drawString(self.x +2*mm,self.y+2.5*mm, self.texte)



class REPORT(COLOR):
    def __init__(self, data):
        """class initialization"""
        super().__init__()
        self.data = data
        self.buffer = BytesIO()
        self.logo_path = os.path.abspath(os.path.join(os.path.dirname( '__file__' ),'static/media', "logo-transparent.png"))
        self.today = datetime.datetime.today()
        

    def __del__(self):
        """class destruction"""
        self.buffer.close()
        pass


    def background(self,canv,doc):
        """backgroud of all pages"""
        company_logo = ImageReader(self.logo_path)
        canv.drawImage(company_logo, 155*mm,275*mm,width= 55*mm, height = 22*mm, mask = 'auto')
        #canv.drawString(155*mm,275*mm,"Hello World")


    def create_doc(self):
        """create doc"""
        #0 hide border, 1 show border
        show_bound = 0
        #padding of frame
        frame_padding = 0*mm

        #frame page 1

        #frame logo 

        frame_big_logo = Frame(20*mm,200*mm,170*mm,68*mm, showBoundary=show_bound, id ='frame_big_logo',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)
        #frame title
        frame_main_title = Frame(20*mm,170*mm,170*mm,20*mm, showBoundary=show_bound, id ='frame_main_title',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame title
        frame_date = Frame(20*mm,140*mm,170*mm,20*mm, showBoundary=show_bound, id ='frame_main_title',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)


        #frame title
        frame_title = Frame(5*mm,275*mm,140*mm,20*mm, showBoundary=show_bound, id ='frame_title',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame objective management title
        frame_objective_managament_title = Frame(5*mm,264*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_objective_managament_title',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame objective management
        frame_objective_managament = Frame(5*mm,232*mm,200*mm,30*mm, showBoundary=show_bound, id ='frame_objective_managament_',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame characteristic title
        frame_characteristic_title = Frame(5*mm,221*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_characteristic_title',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame characteristic
        frame_characteristic = Frame(5*mm,189*mm,200*mm,30*mm, showBoundary=show_bound, id ='frame_characteristic',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame cumulative performance title
        frame_cumulative_performance_title = Frame(5*mm,178*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_cumulative_performance_title',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame cumulative performance
        frame_cumulative_performance = Frame(5*mm,158*mm,200*mm,18*mm, showBoundary=show_bound, id ='frame_cumulative_performance',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame annual performance title
        frame_annual_performance_title = Frame(5*mm,147*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_annual_performance_title',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame annual performance
        frame_annual_performance = Frame(5*mm,125*mm,200*mm,20*mm, showBoundary=show_bound, id ='frame_annual_performance',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame fees title
        frame_fees_title = Frame(5*mm,114*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_fees_title',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame fees
        frame_fees = Frame(5*mm,94*mm,200*mm,18*mm, showBoundary=show_bound, id ='frame_fees',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame style title
        frame_style_title = Frame(5*mm,83*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_style_title',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame style
        frame_style = Frame(5*mm,51*mm,200*mm,30*mm, showBoundary=show_bound, id ='frame_style',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame style bis title
        frame_style_bis_title = Frame(5*mm,40*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_style_bis_title',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame style bis
        frame_style_bis = Frame(5*mm,18*mm,200*mm,20*mm, showBoundary=show_bound, id ='frame_style_bis',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)


        #frame disclaimer
        frame_disclaimer = Frame(5*mm,2*mm,200*mm,14*mm, showBoundary=show_bound, id ='frame_disclaimer',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        # frame title position
        frame_title_position = Frame(5*mm,264*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_title_position',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)
        #frame date position
        frame_date_position = Frame(110*mm,264*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_date_position',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=2*mm)
        #frame position
        frame_position = Frame(5*mm,182*mm,200*mm,80*mm, showBoundary=show_bound, id ='frame_position',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame title chart 1
        frame_title_chart_1 = Frame(5*mm,171*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_title_chart_1',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame title chart 2
        frame_title_chart_2 = Frame(110*mm,171*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_title_chart_2',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame chart 1
        frame_chart_1 = Frame(5*mm,111*mm,95*mm,58*mm, showBoundary=show_bound, id ='frame_chart_1',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame chart 2
        frame_chart_2 = Frame(110*mm,111*mm,95*mm,58*mm, showBoundary=show_bound, id ='frame_chart_2',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame title carbon
        frame_title_carbon = Frame(5*mm,100*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_title_carbon',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)
        #frame carbon
        frame_carbon = Frame(5*mm,82*mm,200*mm,16*mm, showBoundary=show_bound, id ='frame_carbon',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame durability score title
        frame_title_durability = Frame(5*mm,71*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_title_durability',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)
        #frame durability
        frame_durability = Frame(5*mm,53*mm,200*mm,16*mm, showBoundary=show_bound, id ='frame_durability',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame esg score title
        frame_title_esg = Frame(5*mm,42*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_title_esg',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame esg
        frame_esg = Frame(5*mm,22*mm,200*mm,18*mm, showBoundary=show_bound, id ='frame_esg',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)


        #frame commitment title
        frame_commitment_title = Frame(5*mm,264*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_commitment_title',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)
        #frame commitment
        frame_commitment = Frame(5*mm,171*mm,200*mm,91*mm, showBoundary=show_bound, id ='frame_commitment',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)

        #frame exclusion title
        frame_exclusion_title = Frame(5*mm,160*mm,95*mm,8*mm, showBoundary=show_bound, id ='frame_exclusion_title',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)
        #frame exclusion
        frame_exclusion = Frame(5*mm,22*mm,200*mm,136*mm, showBoundary=show_bound, id ='frame_exclusion',
                                leftPadding=frame_padding, bottomPadding=frame_padding,
                                rightPadding=frame_padding, topPadding=frame_padding)
        


        #frame page 1
        frame_page_0 = [frame_big_logo, frame_main_title,frame_date, frame_disclaimer]
        #list of frames for one asset
        frame_page_one_asset = [ frame_title, frame_objective_managament_title, 
        frame_objective_managament,frame_characteristic_title, frame_characteristic,
        frame_cumulative_performance_title, frame_cumulative_performance,
        frame_annual_performance_title, frame_annual_performance,
        frame_fees_title, frame_fees, frame_style_title, frame_style, frame_disclaimer ]

        #list of frames for multiple assets
        frame_page_multiple_asset = [ frame_title, frame_objective_managament_title, 
        frame_objective_managament,frame_characteristic_title, frame_characteristic,
        frame_cumulative_performance_title, frame_cumulative_performance,
        frame_annual_performance_title, frame_annual_performance,
        frame_fees_title, frame_fees, frame_style_title, frame_style, frame_style_bis_title, frame_style_bis,
        frame_disclaimer]

        #frames page chart
        frame_page_chart = [frame_title, frame_title_position, frame_date_position, frame_position,
        frame_title_chart_1,  frame_chart_1, frame_title_chart_2, frame_chart_2,
        frame_title_carbon, frame_carbon, frame_title_durability, frame_durability,
        frame_title_esg, frame_esg, frame_disclaimer]

        #frames page chart
        frame_page_esg = [frame_title,frame_commitment_title,frame_commitment,
        frame_exclusion_title, frame_exclusion, frame_disclaimer]



        page_0 = PageTemplate(id = 'page_0',frames = frame_page_0,pagesize=A4, )
        #page one asset
        page_one_asset = PageTemplate(id = 'page_one_asset',frames = frame_page_one_asset,pagesize=A4, onPage=self.background)
        # page multiple asset
        page_multiple_asset = PageTemplate(id = 'page_multiple_asset',frames = frame_page_multiple_asset,pagesize=A4, onPage=self.background)

        #page graph
        page_chart = PageTemplate(id = 'page_chart',frames = frame_page_chart ,pagesize=A4, onPage=self.background)

        #page esg
        page_esg = PageTemplate(id = 'page_esg',frames = frame_page_esg,pagesize=A4, onPage=self.background)
        #doc
        #outputFile = os.path.abspath(os.path.join(os.path.dirname( '__file__' ),'static/media', "report.pdf"))
        #print(outputFile)
        doc = BaseDocTemplate(self.buffer, pagesize=landscape(A4), pageTemplates =[page_0, page_one_asset, page_multiple_asset, page_chart, page_esg],
                                rightMargin=2, leftMargin= 2, topMargin=2, bottomMargin=2)

        doc.title = 'Albertine - Analyse de portefeuille'
        return doc
    def create_story(self,doc):
        """add flowable to doc"""
        #logo Albertine
        logo_albertine = Image(self.logo_path,170*mm,68*mm)
        #title management objective
        management_objective_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                  "Objectif de gestion",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)
        #title characteristic
        characteristic_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "Caractéristiques",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)
        #title cumulative performance
        cumulative_performance_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "Performances cumulées (en %)",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)
        #title cumulative performance
        annual_performance_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "Performances annuelles",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)
        #title fees
        fees_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "Frais",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)
        #title equity style
        equity_style_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "Style actions",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)
        #title bonds style
        bond_style_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "Style obligations",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)
        #title chart marketCap
        marketCap_chart_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "Répartition par taille de capitalisation",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)
        #title chart marketCap
        sector_chart_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "Répartition par secteurs",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)
        # title bond type
        bond_type_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "Répartition par types d'obligations",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)
        #rating title
        rating_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "Répartition par notations",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)
        #carbon title
        carbon_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "Score carbone",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)
        #position title
        position_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "10 premières positions",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)

        #durability title
        durability_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "Score de durabilité",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)

        #esg title
        esg_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "Répartition ESG*",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)

        #commitment title
        commitment_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "Engagement",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)

        #exclusion title
        exclusion_title = ROUND_TITLE(0*mm, 0*mm, 95*mm, 8*mm, 3*mm, 
                                                 "Politique d'exclusion",bg_color = self.main_color, text_color=self.white, stroke=0, fill=1)

        #initialize list of flowables
        story = []

        #page 1
        story.append(logo_albertine)
        story.append(FrameBreak())
        story.append(self.paragraph_presentation('Analyse de portefeuilles'))
        story.append(FrameBreak())
        story.append(self.paragraph_title_date())
        story.append(FrameBreak())
        story.append(self.paragraph_disclaimer())

        
        
       
        #loop throught all data
        for data in self.data:
            #page 1
            #if allocation
            if data['marketCap']['assetType'] == 'ALLOCATION':
                story.append(NextPageTemplate('page_multiple_asset'))
            else:
                story.append(NextPageTemplate('page_one_asset'))

            story.append(PageBreak())
            #title
            story.append(self.paragraph_title(data['infos']['LegalName']))
            story.append(FrameBreak())
            #title management objective
            story.append(management_objective_title)
            story.append(FrameBreak())
            #management objective
            story.append(self.adapt_text_size(200*mm,30*mm,data['pages']['objective'],11))
            story.append(FrameBreak())
            #title characteristic
            story.append(characteristic_title)
            story.append(FrameBreak())
            #table characteristic
            story.append(self.table_characteristic(data,200*mm, 30*mm))
            story.append(FrameBreak())
            #title cumulative performance
            story.append(cumulative_performance_title)
            story.append(FrameBreak())
            #table cumulative performance
            story.append(self.table_cumulative_performance(data,200*mm, 18*mm))
            story.append(FrameBreak())
            #title annual performance
            story.append(annual_performance_title)
            story.append(FrameBreak())
            #table annual performance
            story.append(self.table_annual_performance(data,200*mm, 20*mm))
            story.append(FrameBreak())
            #title fees
            story.append(fees_title)
            story.append(FrameBreak())
            #table fees
            story.append(self.table_fees(data,200*mm, 18*mm))
            story.append(FrameBreak())
            #title equity style
            if data['marketCap']['assetType'] in ['ALLOCATION', 'EQUITY']:
                story.append(equity_style_title)
                story.append(FrameBreak())
                story.append(self.table_equity_style(data,200*mm, 30*mm))
            #title bond style
            else:
                story.append(bond_style_title)
                story.append(FrameBreak())
                story.append(self.table_bond_style(data,200*mm, 30*mm))
            if data['marketCap']['assetType'] in ['ALLOCATION']:
                story.append(bond_style_title)
                story.append(FrameBreak())
                story.append(self.table_bond_style(data,200*mm, 20*mm))
            #disclaimer page 1
            story.append(FrameBreak())
            story.append(self.paragraph_disclaimer())
            
            #page 2
            story.append(NextPageTemplate('page_chart'))
            story.append(FrameBreak())
            #title
            story.append(self.paragraph_title(data['infos']['LegalName']))
            story.append(FrameBreak())

            #position title
            story.append(position_title)
            story.append(FrameBreak())
            #fund date
            if 'holdingSummary' in data['positions']:

                story.append(self.paragraph_date(parser.parse(data['positions']['holdingSummary']['portfolioDate'])))
                story.append(FrameBreak())
            else:

                story.append(FrameBreak())
            #positions
            if 'boldHoldingPage' in data['positions']:
                story.append(self.table_position(data,200*mm,80*mm))
                story.append(FrameBreak())
            else:
                story.append(FrameBreak())
            

            #charts
            #if equity
            if data['marketCap']['assetType'] in ['EQUITY']:
                
                #chart marketCap 
                story.append(marketCap_chart_title)
                story.append(FrameBreak())
                story.append(self.marketCap_chart(data,95*mm, 58*mm))
                story.append(FrameBreak())
                #chart sector
                story.append(sector_chart_title)
                story.append(FrameBreak())
                story.append(self.sector_chart(data,95*mm, 58*mm))
            #if fixed income
            elif data['marketCap']['assetType'] in ['FIXEDINCOME']:
                
                #chart bond type
                story.append(bond_type_title)
                story.append(FrameBreak())
                story.append(self.bond_type_chart(data,95*mm, 58*mm))
                story.append(FrameBreak())
                #chart rating
                story.append(rating_title)
                story.append(FrameBreak())
                story.append(self.rating_chart(data,95*mm, 58*mm))
            #if allocation and bond and equity
            elif data['marketCap']['assetType'] in ['ALLOCATION'] and data['numberOfBondHolding'] > 0 and data['numberOfEquityHolding'] > 0:
                
                #chart bond type
                story.append(bond_type_title)
                story.append(FrameBreak())
                story.append(self.bond_type_chart(data,95*mm, 58*mm))
                story.append(FrameBreak())
                #chart sector
                story.append(sector_chart_title)
                story.append(FrameBreak())
                story.append(self.sector_chart(data,95*mm, 58*mm))
            #if allocation and equity
            elif data['marketCap']['assetType'] in ['ALLOCATION'] and data['numberOfBondHolding'] > 0:
                
                #chart marketCap 
                story.append(marketCap_chart_title)
                story.append(FrameBreak())
                story.append(self.marketCap_chart(data,95*mm, 58*mm))
                story.append(FrameBreak())
                #chart sector
                story.append(sector_chart_title)
                story.append(FrameBreak())
                story.append(self.sector_chart(data,95*mm, 58*mm))
            #if allocation and bond
            elif data['marketCap']['assetType'] in ['ALLOCATION'] and data['numberOfBondHolding'] > 0:
                
                #chart bond type
                story.append(bond_type_title)
                story.append(FrameBreak())
                story.append(self.bond_type_chart(data,95*mm, 58*mm))
                story.append(FrameBreak())
                #chart rating
                story.append(rating_title)
                story.append(FrameBreak())
                story.append(self.rating_chart(data,95*mm, 58*mm))
            else:
                
                #chart marketCap 
                story.append(marketCap_chart_title)
                story.append(FrameBreak())
                
                story.append(FrameBreak())
                #chart sector
                story.append(sector_chart_title)
                story.append(FrameBreak())

            #carbon
            story.append(FrameBreak())
            story.append(carbon_title)
            story.append(FrameBreak())
            story.append(self.table_carbon(data,200*mm,16*mm))
            #durability
            story.append(FrameBreak())
            story.append(durability_title)
            story.append(FrameBreak())
            story.append(self.table_durability(data,200*mm,16*mm))
            #esg
            story.append(FrameBreak())
            story.append(esg_title)
            story.append(FrameBreak())
            story.append(self.table_esg(data,200*mm,18*mm))
            #disclaimer page 2
            story.append(FrameBreak())
            story.append(self.paragraph_disclaimer())
            #page 3 esg
            
            story.append(NextPageTemplate('page_esg'))
            story.append(FrameBreak())
            #title
            story.append(self.paragraph_title(data['infos']['LegalName']))
            story.append(FrameBreak())
            #commitment title
            story.append(commitment_title)
            story.append(FrameBreak())
            #commitment
            story.append(self.table_commitment(data,200*mm, 91*mm))
            story.append(FrameBreak())
            #exclusion title
            story.append(exclusion_title)
            story.append(FrameBreak())
            #exclusion
            story.append(self.table_exclusion(data,200*mm, 136*mm))
            story.append(FrameBreak())
            #disclaimer page 3
            story.append(self.paragraph_disclaimer())

        #story = []
        #story.append(FrameBreak())
            
        doc.build(story)
        return self.buffer

    def table_exclusion(self, obj, w, h):
        """table exclusion"""
        excludesAbortionStemCells = obj['esgData']['sustainabilityIntentionality']['excludesAbortionStemCells']
        if excludesAbortionStemCells == True:
            TFexcludesAbortionStemCells = 'Oui'
            TFexcludesAbortionStemCellsColor = self.green
        elif excludesAbortionStemCells == False:
            TFexcludesAbortionStemCells = 'Non'
            TFexcludesAbortionStemCellsColor = self.red
        else:
            TFexcludesAbortionStemCells = '-'
            TFexcludesAbortionStemCellsColor = self.black


        excludesAdultEntertainment = obj['esgData']['sustainabilityIntentionality']['excludesAdultEntertainment']
        if excludesAdultEntertainment == True:
            TFexcludesAdultEntertainment = 'Oui'
            TFexcludesAdultEntertainmentColor = self.green
        elif excludesAdultEntertainment == False:
            TFexcludesAdultEntertainment = 'Non'
            TFexcludesAdultEntertainmentColor = self.red
        else:
            TFexcludesAdultEntertainment = '-'
            TFexcludesAdultEntertainmentColor = self.black

        excludesAlcohol = obj['esgData']['sustainabilityIntentionality']['excludesAlcohol']
        if excludesAlcohol == True:
            TFexcludesAlcohol = 'Oui'
            TFexcludesAlcoholColor = self.green
        elif excludesAlcohol == False:
            TFexcludesAlcohol = 'Non'
            TFexcludesAlcoholColor = self.red
        else:
            TFexcludesAlcohol = '-'
            TFexcludesAlcoholColor = self.black


        excludesAnimalTesting = obj['esgData']['sustainabilityIntentionality']['excludesAnimalTesting']
        if excludesAnimalTesting == True:
            TFexcludesAnimalTesting = 'Oui'
            TFexcludesAnimalTestingColor = self.green
        elif excludesAnimalTesting == False:
            TFexcludesAnimalTesting = 'Non'
            TFexcludesAnimalTestingColor = self.red
        else:
            TFexcludesAnimalTesting = '-'
            TFexcludesAnimalTestingColor = self.black


        excludesControversialWeapons = obj['esgData']['sustainabilityIntentionality']['excludesControversialWeapons']
        if excludesControversialWeapons == True:
            TFexcludesControversialWeapons = 'Oui'
            TFexcludesControversialWeaponsColor = self.green
        elif excludesControversialWeapons == False:
            TFexcludesControversialWeapons = 'Non'
            TFexcludesControversialWeaponsColor = self.red
        else:
            TFexcludesControversialWeapons = '-'
            TFexcludesControversialWeaponsColor = self.black

        excludesFurSpecialtyLeather = obj['esgData']['sustainabilityIntentionality']['excludesFurSpecialtyLeather']
        if excludesFurSpecialtyLeather == True:
            TFexcludesFurSpecialtyLeather = 'Oui'
            TFexcludesFurSpecialtyLeatherColor = self.green
        elif excludesFurSpecialtyLeather == False:
            TFexcludesFurSpecialtyLeather = 'Non'
            TFexcludesFurSpecialtyLeatherColor = self.red
        else:
            TFexcludesFurSpecialtyLeather = '-'
            TFexcludesFurSpecialtyLeatherColor = self.black


        excludesGambling = obj['esgData']['sustainabilityIntentionality']['excludesGambling']
        if excludesGambling == True:
            TFexcludesGambling = 'Oui'
            TFexcludesGamblingColor = self.green
        elif excludesGambling == False:
            TFexcludesGambling = 'Non'
            TFexcludesGamblingColor = self.red
        else:
            TFexcludesGambling = '-'
            TFexcludesGamblingColor = self.black


        excludesGMOs = obj['esgData']['sustainabilityIntentionality']['excludesGMOs']
        if excludesGMOs == True:
            TFexcludesGMOs = 'Oui'
            TFexcludesGMOsColor = self.green
        elif excludesGMOs == False:
            TFexcludesGMOs = 'Non'
            TFexcludesGMOsColor = self.red
        else:
            TFexcludesGMOs = '-'
            TFexcludesGMOsColor = self.black


        excludesMilitaryContracting = obj['esgData']['sustainabilityIntentionality']['excludesMilitaryContracting']
        if excludesMilitaryContracting == True:
            TFexcludesMilitaryContracting = 'Oui'
            TFexcludesMilitaryContractingColor = self.green
        elif excludesMilitaryContracting == False:
            TFexcludesMilitaryContracting = 'Non'
            TFexcludesMilitaryContractingColor = self.red
        else:
            TFexcludesMilitaryContracting = '-'
            TFexcludesMilitaryContractingColor = self.black

        excludesNuclear = obj['esgData']['sustainabilityIntentionality']['excludesNuclear']
        if excludesNuclear == True:
            TFexcludesNuclear = 'Oui'
            TFexcludesNuclearColor = self.green
        elif excludesNuclear == False:
            TFexcludesNuclear = 'Non'
            TFexcludesNuclearColor = self.red
        else:
            TFexcludesNuclear = '-'
            TFexcludesNuclearColor = self.black


        excludesPalmOil = obj['esgData']['sustainabilityIntentionality']['excludesPalmOil']
        if excludesPalmOil == True:
            TFexcludesPalmOil = 'Oui'
            TFexcludesPalmOilColor = self.green
        elif excludesPalmOil == False:
            TFexcludesPalmOil = 'Non'
            TFexcludesPalmOilColor = self.red
        else:
            TFexcludesPalmOil = '-'
            TFexcludesPalmOilColor = self.black

        excludesPesticides = obj['esgData']['sustainabilityIntentionality']['excludesPesticides']
        if excludesPesticides == True:
            TFexcludesPesticides = 'Oui'
            TFexcludesPesticidesColor = self.green
        elif excludesPesticides == False:
            TFexcludesPesticides = 'Non'
            TFexcludesPesticidesColor = self.red
        else:
            TFexcludesPesticides = '-'
            TFexcludesPesticidesColor = self.black


        excludesSmallArms = obj['esgData']['sustainabilityIntentionality']['excludesSmallArms']
        if excludesSmallArms == True:
            TFexcludesSmallArms = 'Oui'
            TFexcludesSmallArmsColor = self.green
        elif excludesSmallArms == False:
            TFexcludesSmallArms = 'Non'
            TFexcludesSmallArmsColor = self.red
        else:
            TFexcludesSmallArms = '-'
            TFexcludesSmallArmsColor = self.black

        excludesThermalCoal = obj['esgData']['sustainabilityIntentionality']['excludesThermalCoal']
        if excludesThermalCoal == True:
            TFexcludesThermalCoal = 'Oui'
            TFexcludesThermalCoalColor = self.green
        elif excludesThermalCoal == False:
            TFexcludesThermalCoal = 'Non'
            TFexcludesThermalCoalColor = self.red
        else:
            TFexcludesThermalCoal = '-'
            TFexcludesThermalCoalColor = self.black

        excludesTobacco = obj['esgData']['sustainabilityIntentionality']['excludesTobacco']
        if excludesTobacco == True:
            TFexcludesTobacco = 'Oui'
            TFexcludesTobaccoColor = self.green
        elif excludesTobacco == False:
            TFexcludesTobacco = 'Non'
            TFexcludesTobaccoColor = self.red
        else:
            TFexcludesTobacco = '-'
            TFexcludesTobaccoColor = self.black



        data = [
            ["Exclusion des Cellules souches d'avortement",TFexcludesAbortionStemCells ],
            ["Exclusion du divertissement pour adulte", TFexcludesAdultEntertainment],
            ["Exclusion de l'alcool", TFexcludesAlcohol],
            ["Exclusion de test animal", TFexcludesAnimalTesting],
            ["Exclusion des armes controversées", TFexcludesControversialWeapons],
            ["Exclusion de la fourrure", TFexcludesFurSpecialtyLeather],
            ["Exclusion des jeux d'argent", TFexcludesGambling],
            ["Exclusion des OGM", TFexcludesGMOs],
            ["Exclusion des contrats militaires", TFexcludesMilitaryContracting],
            ["Exclusion du nucléaire", TFexcludesNuclear],
            ["Exclusion de l'huile de Palme", TFexcludesPalmOil],
            ["Exclusion des pesticides", TFexcludesPesticides],
            ["Exclusion des petites armes", TFexcludesSmallArms ],
            ["Exclusion des centrales à charbon", TFexcludesThermalCoal],
            ["Exclusion du tabac", TFexcludesTobacco],


        ]
        #0 column, 1 row
        style = [
                                ('FONTNAME', (0,0),(-1,-1),self.text_n),
                                #('FONTNAME', (0,0),(-1,0),self.text_b),
                                ('FONTSIZE', (0,0),(-1,-1), 10),
                                ('TEXTCOLOR', (0,1),(-1,-1),self.black),
                                ('TEXTCOLOR', (1,0),(1,0),TFexcludesAbortionStemCellsColor),
                                ('TEXTCOLOR', (1,1),(1,1),TFexcludesAdultEntertainmentColor),
                                ('TEXTCOLOR', (1,2),(1,2),TFexcludesAlcoholColor),
                                ('TEXTCOLOR', (1,3),(1,3),TFexcludesAnimalTestingColor),
                                ('TEXTCOLOR', (1,4),(1,4),TFexcludesControversialWeaponsColor),
                                ('TEXTCOLOR', (1,5),(1,5),TFexcludesFurSpecialtyLeatherColor),
                                ('TEXTCOLOR', (1,6),(1,6),TFexcludesGamblingColor),

                                ('TEXTCOLOR', (1,7),(1,7),TFexcludesGMOsColor),
                                ('TEXTCOLOR', (1,8),(1,8),TFexcludesMilitaryContractingColor),
                                ('TEXTCOLOR', (1,9),(1,9),TFexcludesNuclearColor),
                                ('TEXTCOLOR', (1,10),(1,10),TFexcludesPalmOilColor),
                                ('TEXTCOLOR', (1,11),(1,11),TFexcludesPesticidesColor),
                                ('TEXTCOLOR', (1,12),(1,12),TFexcludesSmallArmsColor),
                                ('TEXTCOLOR', (1,13),(1,13),TFexcludesThermalCoalColor),
                                ('TEXTCOLOR', (1,14),(1,14),TFexcludesTobaccoColor),

                                ('ALIGN', (0,0),(-1,-1),'CENTER'),
                                ('ALIGN', (0,0),(0,-1),'LEFT'),
                                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                                ('TOPPADDING',(0,0),(-1,-1),0),
                                ('BOTTOMPADDING',(0,0),(-1,-1),0),
                                ('LEFTPADDING',(0,0),(-1,-1),6),
                                ('RIGHTPADDING',(0,0),(-1,-1),6)]

        

        table_style = TableStyle(style)

        table = Table(data, colWidths =[w*0.5, w*0.5],
                        rowHeights = [h/len(data)]*len(data), style = table_style)

        return table


    def table_commitment(self, obj, w,h):
        """table commitment"""
        
        eSGIncorporation = obj['esgData']['sustainabilityIntentionality']['eSGIncorporation']
        if eSGIncorporation == True:
            TFeSGIncorporation = 'Oui'
            TFeSGIncorporationColor = self.green
        elif eSGIncorporation == False:
            TFeSGIncorporation = 'Non'
            TFeSGIncorporationColor = self.red
        else:
            TFeSGIncorporation = '-'
            TFeSGIncorporationColor = self.black

        eSGEngagement = obj['esgData']['sustainabilityIntentionality']['eSGEngagement']
        if eSGEngagement == True:
            TFeSGEngagement = 'Oui'
            TFeSGEngagementColor = self.green
        elif eSGEngagement == False:
            TFeSGEngagement = 'Non'
            TFeSGEngagementColor = self.red
        else:
            TFeSGEngagement = '-'
            TFeSGEngagementColor = self.black

        genderDiversity = obj['esgData']['sustainabilityIntentionality']['genderDiversity']
        if genderDiversity == True:
            TFgenderDiversity = 'Oui'
            TFgenderDiversityColor = self.green
        elif genderDiversity == False:
            TFgenderDiversity = 'Non'
            TFgenderDiversityColor = self.red
        else:
            TFgenderDiversity = '-'
            TFgenderDiversityColor = self.black

        communityDevelopment = obj['esgData']['sustainabilityIntentionality']['communityDevelopment']
        if communityDevelopment == True:
            TFcommunityDevelopment = 'Oui'
            TFcommunityDevelopmentColor = self.green
        elif communityDevelopment == False:
            TFcommunityDevelopment = 'Non'
            TFcommunityDevelopmentColor = self.red
        else:
            TFcommunityDevelopment = '-'
            TFcommunityDevelopmentColor = self.black

        lowCarbonFossilFuelFree = obj['esgData']['sustainabilityIntentionality']['lowCarbonFossilFuelFree']
        if lowCarbonFossilFuelFree == True:
            TFlowCarbonFossilFuelFree = 'Oui'
            TFlowCarbonFossilFuelFreeColor = self.green
        elif lowCarbonFossilFuelFree == False:
            TFlowCarbonFossilFuelFree = 'Non'
            TFlowCarbonFossilFuelFreeColor = self.red
        else:
            TFlowCarbonFossilFuelFree = '-'
            TFlowCarbonFossilFuelFreeColor = self.black


        renewableEnergy = obj['esgData']['sustainabilityIntentionality']['renewableEnergy']
        if renewableEnergy == True:
            TFrenewableEnergy = 'Oui'
            TFrenewableEnergyColor = self.green
        elif renewableEnergy == False:
            TFrenewableEnergy = 'Non'
            TFrenewableEnergyColor = self.red
        else:
            TFrenewableEnergy = '-'
            TFrenewableEnergyColor = self.black


        waterFocused = obj['esgData']['sustainabilityIntentionality']['waterFocused']
        if waterFocused == True:
            TFwaterFocused = 'Oui'
            TFwaterFocusedColor = self.green
        elif waterFocused == False:
            TFwaterFocused = 'Non'
            TFwaterFocusedColor = self.red
        else:
            TFwaterFocused = '-'
            TFwaterFocusedColor = self.black


        generalEnvironmentalSector = obj['esgData']['sustainabilityIntentionality']['generalEnvironmentalSector']
        if generalEnvironmentalSector == True:
            TFgeneralEnvironmentalSector = 'Oui'
            TFgeneralEnvironmentalSectorColor = self.green
        elif generalEnvironmentalSector == False:
            TFgeneralEnvironmentalSector = 'Non'
            TFgeneralEnvironmentalSectorColor = self.red
        else:
            TFgeneralEnvironmentalSector = '-'
            TFgeneralEnvironmentalSectorColor = self.black


        sustainableInvestmentOverall = obj['esgData']['sustainabilityIntentionality']['sustainableInvestmentOverall']
        if sustainableInvestmentOverall == True:
            TFsustainableInvestmentOverall = 'Oui'
            TFsustainableInvestmentOverallColor = self.green
        elif sustainableInvestmentOverall == False:
            TFsustainableInvestmentOverall = 'Non'
            TFsustainableInvestmentOverallColor = self.red
        else:
            TFsustainableInvestmentOverall = '-'
            TFsustainableInvestmentOverallColor = self.black


        impactFundOverall = obj['esgData']['sustainabilityIntentionality']['impactFundOverall']
        if impactFundOverall == True:
            TFimpactFundOverall = 'Oui'
            TFimpactFundOverallColor = self.green
        elif impactFundOverall == False:
            TFimpactFundOverall = 'Non'
            TFimpactFundOverallColor = self.red
        else:
            TFimpactFundOverall = '-'
            TFimpactFundOverallColor = self.black



        data = [
            ['Critères ESG inclus dans la gestion', TFeSGIncorporation],
            ["Engagement ESG", TFeSGEngagement],
            ["Engagement pour la parité Homme/Femme", TFgenderDiversity],
            ["Engagement pour le développement de la communauté",TFcommunityDevelopment],
            ["Engagement dans la réduction des émissions CO2",TFlowCarbonFossilFuelFree],
            ["Engagement dans l'énergie renouvelable", TFrenewableEnergy],
            ["Investissement focalisé dans l'eau", TFwaterFocused],
            ["Investissement global dans le secteur environnemental", TFgeneralEnvironmentalSector],
            ["Fonds à investissement durable", TFsustainableInvestmentOverall],
            ["Fonds à impact", TFimpactFundOverall],
            ]


        #0 column, 1 row
        style = [
                                ('FONTNAME', (0,0),(-1,-1),self.text_n),
                                #('FONTNAME', (0,0),(-1,0),self.text_b),
                                ('FONTSIZE', (0,0),(-1,-1), 10),
                                ('TEXTCOLOR', (0,1),(-1,-1),self.black),
                                ('TEXTCOLOR', (1,0),(1,0),TFeSGIncorporationColor),
                                ('TEXTCOLOR', (1,1),(1,1),TFeSGEngagementColor),
                                ('TEXTCOLOR', (1,2),(1,2),TFgenderDiversityColor),
                                ('TEXTCOLOR', (1,3),(1,3),TFcommunityDevelopmentColor),
                                ('TEXTCOLOR', (1,4),(1,4),TFlowCarbonFossilFuelFreeColor),
                                ('TEXTCOLOR', (1,5),(1,5),TFrenewableEnergyColor),
                                ('TEXTCOLOR', (1,6),(1,6),TFwaterFocusedColor),
                                ('TEXTCOLOR', (1,7),(1,7),TFgeneralEnvironmentalSectorColor),
                                ('TEXTCOLOR', (1,8),(1,8),TFsustainableInvestmentOverallColor),
                                ('TEXTCOLOR', (1,9),(1,9),TFimpactFundOverallColor),
                                ('ALIGN', (0,0),(-1,-1),'CENTER'),
                                ('ALIGN', (0,0),(0,-1),'LEFT'),
                                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                                ('TOPPADDING',(0,0),(-1,-1),0),
                                ('BOTTOMPADDING',(0,0),(-1,-1),0),
                                ('LEFTPADDING',(0,0),(-1,-1),6),
                                ('RIGHTPADDING',(0,0),(-1,-1),6)]

        

        table_style = TableStyle(style)

        table = Table(data, colWidths =[w*0.5, w*0.5],
                        rowHeights = [h/len(data)]*len(data), style = table_style)

        return table

    def table_esg(self, obj,w, h):
        """table esg"""

        if obj['esgData']['esgScoreCalculation']['environmentalScore'] == None:
            environmentalScore = None
        else:
             environmentalScore = str(obj['esgData']['esgScoreCalculation']['environmentalScore']).replace('.',',')

        if obj['esgData']['esgScoreCalculation']['socialScore'] == None:
            socialScore = None
        else:
             socialScore = str(obj['esgData']['esgScoreCalculation']['socialScore']).replace('.',',')

        if obj['esgData']['esgScoreCalculation']['governanceScore'] == None:
            governanceScore = None
        else:
             governanceScore = str(obj['esgData']['esgScoreCalculation']['governanceScore']).replace('.',',')

        if obj['esgData']['esgScoreCalculation']['portfolioUnallocatedEsgRiskScore'] == None:
            portfolioUnallocatedEsgRiskScore = None
        else:
            portfolioUnallocatedEsgRiskScore = str(obj['esgData']['esgScoreCalculation']['portfolioUnallocatedEsgRiskScore']).replace('.',',')


        data = [
            ["Environnement",	"Social","Gouvernance","Non-alloué"],
            [
                environmentalScore ,
                socialScore,
                governanceScore,
                portfolioUnallocatedEsgRiskScore,
            ], 
            ["*(scores plus faibles = risque plus faible)"]
            ]
        #0 column, 1 row
        style = [
                                ('FONTNAME', (0,0),(-1,-1),self.text_n),
                                ('FONTNAME', (0,0),(-1,0),self.text_b),
                                ('FONTSIZE', (0,0),(-1,-1), 10),
                                ('TEXTCOLOR', (0,1),(-1,-1),self.black),
                                ('ALIGN', (0,0),(-1,-1),'CENTER'),
                                ('ALIGN', (0,-1),(-1,-1),'LEFT'),
                                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                                ('TOPPADDING',(0,0),(-1,-1),0),
                                ('BOTTOMPADDING',(0,0),(-1,-1),0),
                                ('LEFTPADDING',(0,0),(-1,-1),6),
                                ('RIGHTPADDING',(0,0),(-1,-1),6)]

        

        table_style = TableStyle(style)

        table = Table(data, colWidths =[w/4]*4,
                        rowHeights = [h/len(data)]*len(data), style = table_style)

        return table
    def table_durability(self, obj,w,h):
        """table durability"""


        #0 column, 1 row
        style = [
                                ('FONTNAME', (0,0),(-1,-1),self.text_n),
                                ('FONTNAME', (0,0),(-1,0),self.text_b),
                                ('FONTSIZE', (0,0),(-1,-1), 10),
                                ('TEXTCOLOR', (0,1),(-1,-1),self.black),
                                ('ALIGN', (0,0),(-1,-1),'CENTER'),
                                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                                ('TOPPADDING',(0,0),(-1,-1),0),
                                ('BOTTOMPADDING',(0,0),(-1,-1),0),
                                ('LEFTPADDING',(0,0),(-1,-1),6),
                                ('RIGHTPADDING',(0,0),(-1,-1),6)]

        if obj['esgData']['esgData']['fundSustainabilityScore'] == None:
            fundSustainabilityScore = None
        else:
            if obj['esgData']['esgData']['fundSustainabilityScore'] > 30:
                style.append(('TEXTCOLOR', (0,1),(0,1),self.red))
            elif obj['esgData']['esgData']['fundSustainabilityScore'] > 20:
                style.append(('TEXTCOLOR', (0,1),(0,1),self.orange))
            elif obj['esgData']['esgData']['fundSustainabilityScore'] > 10:
                style.append(('TEXTCOLOR', (0,1),(0,1),self.yellow))
            else:
                style.append(('TEXTCOLOR', (0,1),(0,1),self.green))

            fundSustainabilityScore = "{:.2f}".format(obj['esgData']['esgData']['fundSustainabilityScore']).replace('.', ',')

        if obj['esgData']['esgData']['sustainabilityRatingCorporateContributionPercent'] == None:
            sustainabilityRatingCorporateContributionPercent = None
        else:
            sustainabilityRatingCorporateContributionPercent = "{:.2f}".format(obj['esgData']['esgData']['sustainabilityRatingCorporateContributionPercent']).replace('.', ',') + '%'
        if obj['esgData']['esgData']['portfolioSovereignsustainabilityscore'] == None:
            portfolioSovereignsustainabilityscore = None
        else:
            if obj['esgData']['esgData']['portfolioSovereignsustainabilityscore'] > 30:
                style.append(('TEXTCOLOR', (2,1),(2,1),self.red))
            elif obj['esgData']['esgData']['portfolioSovereignsustainabilityscore'] > 20:
                style.append(('TEXTCOLOR', (2,1),(2,1),self.orange))
            elif obj['esgData']['esgData']['portfolioSovereignsustainabilityscore'] > 10:
                style.append(('TEXTCOLOR', (2,1),(2,1),self.yellow))
            else:
                style.append(('TEXTCOLOR', (2,1),(2,1),self.green))

            portfolioSovereignsustainabilityscore = "{:.2f}".format(obj['esgData']['esgData']['portfolioSovereignsustainabilityscore']).replace('.', ',') 
        if obj['esgData']['esgData']['sustainabilityRatingSovereignContributionPercent'] == None:
            sustainabilityRatingSovereignContributionPercent = None
        else:
            sustainabilityRatingSovereignContributionPercent = "{:.2f}".format(obj['esgData']['esgData']['sustainabilityRatingSovereignContributionPercent']).replace('.', ',')  + '%'

        data = [
            ["Score entreprises","Contribution entreprises","Score souverains","Contribution souverains"],
            [fundSustainabilityScore, 
            sustainabilityRatingCorporateContributionPercent,
            portfolioSovereignsustainabilityscore,
            sustainabilityRatingSovereignContributionPercent,
            
            ],
            ]
       

        table_style = TableStyle(style)

        table = Table(data, colWidths =[w/4]*4,
                        rowHeights = [h/len(data)]*len(data), style = table_style)

        return table
    def table_position(self, obj,w, h):
        """table position"""
        data = [['Nom', 'Poids', 'Description']]
        #all securities in a Dataframe
        df = pd.DataFrame(obj['positions']['boldHoldingPage']['holdingList'] +
             obj['positions']['equityHoldingPage']['holdingList']+
             obj['positions']['otherHoldingPage']['holdingList'])

        #sort by weight
        df = df.sort_values(by=['weighting'], ascending=False)
        df = df.loc[df["secondarySectorName"] != "Cash"]
        df['secondarySectorName'] = df['secondarySectorName'].fillna(df['sector'])
        df = df.reset_index(drop = True)
        total = 0
        for index, row in df.iterrows():
            if index == 10:
                break
            data.append([row['securityName'], "{:.2f}".format(row['weighting']).replace('.', ','), row['secondarySectorName']])
            total += row['weighting']
        data.append(['total', "{:.2f}".format(total).replace('.', ',')])
        #0 column, 1 row
        style = [
                                ('FONTNAME', (0,0),(-1,-1),self.text_n),
                                ('FONTNAME', (0,0),(-1,0),self.text_b),
                                ('FONTNAME', (0,-1),(-1,-1),self.text_b),
                                ('FONTSIZE', (0,0),(-1,-1), 10),
                                ('TEXTCOLOR', (0,1),(-1,-1),self.black),
                                ('TEXTCOLOR', (0,-1),(-1,-1),self.main_color),
                                ('ALIGN', (0,0),(-1,-1),'CENTER'),
                                ('ALIGN', (0,0),(0,-1),'LEFT'),
                                ('ALIGN', (2,0),(2,-1),'LEFT'),
                                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                                ('TOPPADDING',(0,0),(-1,-1),0),
                                ('BOTTOMPADDING',(0,0),(-1,-1),0),
                                ('LEFTPADDING',(0,0),(-1,-1),6),
                                ('RIGHTPADDING',(0,0),(-1,-1),6)]

        table_style = TableStyle(style)
        
        table = Table(data, colWidths =[w*0.4, w*0.2, w*0.4],
                        rowHeights = [h/len(data)]*len(data), style = table_style)

        return table
        

    def table_carbon(self, obj,w,h):
        """table carbon"""
  
        if obj['carbonMetrics']['isLowCarbon'] == "true":
            isLowCarbon = 'Oui'
            isLowCarbonColor = self.green
        elif obj['carbonMetrics']['isLowCarbon'] == "false":
            isLowCarbon = 'Non'
            isLowCarbonColor = self.red
        else:
            isLowCarbon = ''
            isLowCarbonColor = self.black

        if obj['carbonMetrics']['carbonRiskScore'] == None:
            carbonPortfolioCoveragePct = None
        else:
            carbonPortfolioCoveragePct = obj['carbonMetrics']['carbonPortfolioCoveragePct']
          
        data = [["Score risque carbone",	"% portefeuille couvert",
        	"Faible teneur \nen carbone",	"% Impliqué dans des \ncombustibles fossiles"],
            [obj['carbonMetrics']['carbonRiskScore'],
            carbonPortfolioCoveragePct,
             isLowCarbon,
            obj['carbonMetrics']['fossilFuelInvolvementPct']
            ]
            ]

        #0 column, 1 row
        style = [
                                ('FONTNAME', (0,0),(-1,-1),self.text_n),
                                ('FONTNAME', (0,0),(-1,0),self.text_b),
                                ('FONTSIZE', (0,0),(-1,-1), 10),
                                ('TEXTCOLOR', (0,1),(-1,-1),self.black),
                                ('ALIGN', (0,0),(-1,-1),'CENTER'),
                                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                                ('TOPPADDING',(0,0),(-1,-1),0),
                                ('BOTTOMPADDING',(0,0),(-1,-1),0),
                                ('LEFTPADDING',(0,0),(-1,-1),6),
                                ('RIGHTPADDING',(0,0),(-1,-1),6)]

        style.append(('TEXTCOLOR', (2,1),(2,1),isLowCarbonColor))

        table_style = TableStyle(style)

        table = Table(data, colWidths =[w/4]*4,
                        rowHeights = [h/len(data)]*len(data), style = table_style)

        return table

    def rating_chart(self, obj, w, h):
        """Vertical Chart rating"""
        drawing = Drawing(w,h)
        lc = VerticalBarChart()

        
        if obj['creditQuality']['fund']["creditQualityBelowB"] != None:
            creditQualityBelowB = float(obj['creditQuality']['fund']["creditQualityBelowB"])
        else:
            creditQualityBelowB = None

        if obj['creditQuality']['fund']["creditQualityAAA"] != None:
            creditQualityAAA= float(obj['creditQuality']['fund']["creditQualityAAA"])
        else:
            creditQualityAAA = None

        if obj['creditQuality']['fund']["creditQualityAA"] != None:
            creditQualityAA= float(obj['creditQuality']['fund']["creditQualityAA"])
        else:
            creditQualityAA = None

        if obj['creditQuality']['fund']["creditQualityA"] != None:
            creditQualityA= float(obj['creditQuality']['fund']["creditQualityA"])
        else:
            creditQualityA = None

        if obj['creditQuality']['fund']["creditQualityBBB"] != None:
            creditQualityBBB = float(obj['creditQuality']['fund']["creditQualityBBB"])
        else:
            creditQualityBBB = None

        if obj['creditQuality']['fund']["creditQualityBB"] != None:
            creditQualityBB = float(obj['creditQuality']['fund']["creditQualityBB"])
        else:
            creditQualityBB = None
        if obj['creditQuality']['fund']["creditQualityB"] != None:
            creditQualityB = float(obj['creditQuality']['fund']["creditQualityB"])
        else:
            creditQualityB = None

        if obj['creditQuality']['fund']["creditQualityNotRated"] != None:
            creditQualityNotRated = float(obj['creditQuality']['fund']["creditQualityNotRated"])
        else:
            creditQualityNotRated = None
        data = [
            [
                creditQualityAAA,
                creditQualityAA,
                creditQualityA,
                creditQualityBBB,
                creditQualityBB,
                creditQualityB,
                creditQualityBelowB,
                creditQualityNotRated
        ]
        ]


        categories = ["AAA",
        "AA",
        "A",
        "BBB",
        "BB",
        "B",
        "< B",
        "Non noté",

        ]



        max_v, min_v, tick = max_min_tick(data,5)
                
            
        lc.groupSpacing = 15

        lc.data = data
        lc.x = 0
        lc.y = 55
        lc.height = h*0.5
        lc.width = w
        lc.barWidth = 30
        lc.barSpacing = 4
        lc.strokeWidth = 0
        lc.categoryAxis.categoryNames = categories
        lc.categoryAxis.visibleTicks = 0
        lc.categoryAxis.strokeColor = self.black
        lc.categoryAxis.strokeWidth = 0.1

        lc.categoryAxis.labels.fontName = self.text_n
        lc.categoryAxis.labels.fontSize = 7
        lc.categoryAxis.labels.fillColor = self.black
        lc.categoryAxis.labels.angle = 45
        lc.categoryAxis.labels.dx = -8
        lc.categoryAxis.labels.dy = -30
        lc.categoryAxis.visibleLabels = 1

        lc.valueAxis.valueMin = min_v
        lc.valueAxis.valueMax = max_v
        lc.valueAxis.valueStep = tick
        lc.valueAxis.visible = 0

        lc.bars[0].fillColor = self.main_color
        lc.bars[0].strokeColor = None

        lc.barLabelFormat = DecimalFormatter(places = 1, suffix='%',decimalSep = '.')

        lc.barLabels[0].visible = 1
        lc.barLabels.nudge = 5
        lc.barLabels.width = 0.01
        lc.barLabels.maxWidth = 0.5
        lc.barLabels[0].dx = 2

        lc.barLabels.fontName = self.text_n
        lc.barLabels.fontSize = 7
        lc.barLabels[0].fillColor = self.black
        lc.barLabels.boxTarget = 'hi'
        drawing.add(lc)
        return drawing
    
    def bond_type_chart(self, obj, w, h,):
        """Vertical Chart bond type"""
        drawing = Drawing(w,h)
        lc = VerticalBarChart()

        data = [
            [
                obj['sector']['FIXEDINCOME']["fundPortfolio"]['government'],
                obj['sector']['FIXEDINCOME']["fundPortfolio"]['municipal'],
                obj['sector']['FIXEDINCOME']["fundPortfolio"]['corporate'],
                obj['sector']['FIXEDINCOME']["fundPortfolio"]['securitized'],
                obj['sector']['FIXEDINCOME']["fundPortfolio"]['cashAndEquivalents'],
                obj['sector']['FIXEDINCOME']["fundPortfolio"]['derivative'],



        ]
        ]

        categories = ["Gouvernement",
        "Municipalité",
        "Entreprise",
        "Titrisé",
        "Cash",
        "Dérivés"

        ]


        max_v, min_v, tick = max_min_tick(data,5)
                
            
        lc.groupSpacing = 15

        lc.data = data
        lc.x = 0
        lc.y = 55
        lc.height = h*0.5
        lc.width = w
        lc.barWidth = 30
        lc.barSpacing = 4
        lc.strokeWidth = 0
        lc.categoryAxis.categoryNames = categories
        lc.categoryAxis.visibleTicks = 0
        lc.categoryAxis.strokeColor = self.black
        lc.categoryAxis.strokeWidth = 0.1

        lc.categoryAxis.labels.fontName = self.text_n
        lc.categoryAxis.labels.fontSize = 7
        lc.categoryAxis.labels.fillColor = self.black
        lc.categoryAxis.labels.angle = 90
        lc.categoryAxis.labels.dx = -8
        lc.categoryAxis.labels.dy = -30
        lc.categoryAxis.visibleLabels = 1

        lc.valueAxis.valueMin = min_v
        lc.valueAxis.valueMax = max_v
        lc.valueAxis.valueStep = tick
        lc.valueAxis.visible = 0

        lc.bars[0].fillColor = self.main_color
        lc.bars[0].strokeColor = None

        lc.barLabelFormat = DecimalFormatter(places = 1, suffix='%',decimalSep = '.')

        lc.barLabels[0].visible = 1
        lc.barLabels.nudge = 5
        lc.barLabels.width = 0.01
        lc.barLabels.maxWidth = 0.5
        lc.barLabels[0].dx = 2

        lc.barLabels.fontName = self.text_n
        lc.barLabels.fontSize = 7
        lc.barLabels[0].fillColor = self.black
        lc.barLabels.boxTarget = 'hi'
        drawing.add(lc)
        return drawing
    def marketCap_chart(self, obj, w, h,):
        """Vertical Chart marketCap"""
        drawing = Drawing(w,h)
        lc = VerticalBarChart()

        data = [
            [
                obj['marketCap']['fund']['giant'],
                obj['marketCap']['fund']['large'],
                obj['marketCap']['fund']['medium'],
                obj['marketCap']['fund']['small'],
                obj['marketCap']['fund']['micro']


        ]
        ]

        categories = ["géantes", "grandes", "moyenne","petite", "micro"]

        

        max_v, min_v, tick = max_min_tick(data,5)
                
            
        lc.groupSpacing = 15

        lc.data = data
        lc.x = 0
        lc.y = 55
        lc.height = h*0.5
        lc.width = w
        lc.barWidth = 30
        lc.barSpacing = 4
        lc.strokeWidth = 0
        lc.categoryAxis.categoryNames = categories
        lc.categoryAxis.visibleTicks = 0
        lc.categoryAxis.strokeColor = self.black
        lc.categoryAxis.strokeWidth = 0.1

        lc.categoryAxis.labels.fontName = self.text_n
        lc.categoryAxis.labels.fontSize = 7
        lc.categoryAxis.labels.fillColor = self.black
        lc.categoryAxis.labels.angle = 45
        lc.categoryAxis.labels.dx = -8
        lc.categoryAxis.labels.dy = -20
        lc.categoryAxis.visibleLabels = 1

        lc.valueAxis.valueMin = min_v
        lc.valueAxis.valueMax = max_v
        lc.valueAxis.valueStep = tick
        lc.valueAxis.visible = 0

        lc.bars[0].fillColor = self.main_color
        lc.bars[0].strokeColor = None

        lc.barLabelFormat = DecimalFormatter(places = 1, suffix='%',decimalSep = '.')

        lc.barLabels[0].visible = 1
        lc.barLabels.nudge = 5
        lc.barLabels.width = 0.01
        lc.barLabels.maxWidth = 0.5
        lc.barLabels[0].dx = 2

        lc.barLabels.fontName = self.text_n
        lc.barLabels.fontSize = 7
        lc.barLabels[0].fillColor = self.black
        lc.barLabels.boxTarget = 'hi'
        drawing.add(lc)
        return drawing



    def sector_chart(self, obj, w, h,):
        """Vertical Chart sector"""
        drawing = Drawing(w,h)
        lc = VerticalBarChart()

        data = [
            [
                obj['sector']['EQUITY']["fundPortfolio"]['consumerCyclical'],
                obj['sector']['EQUITY']["fundPortfolio"]['consumerDefensive'],
                obj['sector']['EQUITY']["fundPortfolio"]['energy'],
                obj['sector']['EQUITY']["fundPortfolio"]['financialServices'],
                obj['sector']['EQUITY']["fundPortfolio"]['realEstate'],
                obj['sector']['EQUITY']["fundPortfolio"]['industrials'],
                obj['sector']['EQUITY']["fundPortfolio"]['basicMaterials'],
                obj['sector']['EQUITY']["fundPortfolio"]['healthcare'],
                obj['sector']['EQUITY']["fundPortfolio"]['technology'],
                obj['sector']['EQUITY']["fundPortfolio"]['communicationServices'],
                obj['sector']['EQUITY']["fundPortfolio"]['utilities'],

        ]
        ]
        categories = ["Conso. \ndiscrétionnaire",
        "Conso. \nde base", "Energie", "Finance",
        "Immobilier", "Industrie", 'Matériaux',
         "Santé",  "Technologies",
         "Télécom",  "Utilities"
        ]

        

        max_v, min_v, tick = max_min_tick(data,5)
                
            
        lc.groupSpacing = 15

        lc.data = data
        lc.x = 0
        lc.y = 55
        lc.height = h*0.5
        lc.width = w
        lc.barWidth = 30
        lc.barSpacing = 4
        lc.strokeWidth = 0
        lc.categoryAxis.categoryNames = categories
        lc.categoryAxis.visibleTicks = 0
        lc.categoryAxis.strokeColor = self.black
        lc.categoryAxis.strokeWidth = 0.1

        lc.categoryAxis.labels.fontName = self.text_n
        lc.categoryAxis.labels.fontSize = 7
        lc.categoryAxis.labels.fillColor = self.black
        lc.categoryAxis.labels.angle = 90
        lc.categoryAxis.labels.dx = -8
        lc.categoryAxis.labels.dy = -30
        lc.categoryAxis.visibleLabels = 1

        lc.valueAxis.valueMin = min_v
        lc.valueAxis.valueMax = max_v
        lc.valueAxis.valueStep = tick
        lc.valueAxis.visible = 0

        lc.bars[0].fillColor = self.main_color
        lc.bars[0].strokeColor = None

        lc.barLabelFormat = DecimalFormatter(places = 1, suffix='%',decimalSep = '.')

        lc.barLabels[0].visible = 1
        lc.barLabels.nudge = 5
        lc.barLabels.width = 0.01
        lc.barLabels.maxWidth = 0.5
        lc.barLabels[0].dx = 2

        lc.barLabels.fontName = self.text_n
        lc.barLabels.fontSize = 7
        lc.barLabels[0].fillColor = self.black
        lc.barLabels.boxTarget = 'hi'
        drawing.add(lc)
        return drawing






    def paragraph_disclaimer(self):
        """paragraph for disclaimer"""
        disclaimer = """Ce document a été élaboré dans le but de présenter des caractéristiques des fonds dans une volonté de transparence et pour donner facilement à tous, l'accès à de l'information publique. 
        Il ne présente pas une recommandation, un conseil en investissement ou une offre d'achat.
        Les données sont extraites depuis internet à l'aide d'un programme automatisé, elles n'ont pas été vérifées. Ce document ne peut pas être vendu. Il est issu d'un travail gratuit, libre et indépendant.
        Toutes réclamantions peuvent être adréssées à Albertine SASU par courriel à l'adresse albertine@albertine.io
        """
        style_para = ParagraphStyle(name = 'style_para', 
                                    fontName=self.text_i,
                                    fontSize=8.5,
                                    leading = 8,
                                    textColor = self.black,
                                    alignment = TA_JUSTIFY,
                                    )
        return Paragraph(disclaimer,style = style_para)


    def table_bond_style(self, obj,w,h):
        """table bond style"""

        if obj['bondStyle']["fund"]["avgEffectiveDuration"] != None:
            duration ="{:.2f}".format(obj['bondStyle']["fund"]["avgEffectiveDuration"]).replace('.', ',')
        else:
            duration = None

        if obj['bondStyle']["fund"]["avgEffectiveMaturity"] != None:
            maturity ="{:.2f}".format(obj['bondStyle']["fund"]["avgEffectiveMaturity"]).replace('.', ',')
        else:
            maturity = None

        if obj['bondStyle']["fund"]["modifiedDuration"] != None:
            modified_duration ="{:.2f}".format(obj['bondStyle']["fund"]["modifiedDuration"]).replace('.', ',')
        else:
            modified_duration = None

        if obj['bondStyle']["fund"]["avgPrice"] != None:
            price ="{:.2f}".format(obj['bondStyle']["fund"]["avgPrice"]).replace('.', ',')
        else:
            price = None

        if obj['bondStyle']["fund"]["avgCoupon"] != None:
            coupon ="{:.2f}".format(obj['bondStyle']["fund"]["avgCoupon"]).replace('.', ',')
        else:
            coupon = None

        if obj['bondStyle']["fund"]["yieldToMaturity"] != None:
            ytm ="{:.2f}".format(obj['bondStyle']["fund"]["yieldToMaturity"]).replace('.', ',')
        else:
            ytm = None

        

        data = [["Duration","Duration \nmodifiée","Maturité \nmoyenne","Qualité \ndu crédit",
    	"Notation \nmoyenne",	"Coupon \nmoyen",	"Prix \nmoyen","Rendement \nà maturité"],
        [duration, modified_duration,
        maturity,
        obj['bondStyle']["fund"]["avgCreditQualityName"],
        obj['bondStyle']["fund"]["calculatedAverageCreditRating"],
        coupon,
        price,
        ytm,
               
        ],
        ]

        #0 column, 1 row
        table_style = TableStyle([
                                ('FONTNAME', (0,0),(-1,-1),self.text_n),
                                ('FONTNAME', (0,0),(-1,0),self.text_b),
                                ('FONTSIZE', (0,0),(-1,-1), 10),
                                ('TEXTCOLOR', (0,1),(-1,-1),self.black),
                                ('ALIGN', (0,0),(-1,-1),'CENTER'),
                                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                                ('TOPPADDING',(0,0),(-1,-1),0),
                                ('BOTTOMPADDING',(0,0),(-1,-1),0),
                                ('LEFTPADDING',(0,0),(-1,-1),6),
                                ('RIGHTPADDING',(0,0),(-1,-1),6)])

        table = Table(data, colWidths =[w/8]*8,
                        rowHeights = [h/len(data)]*len(data), style = table_style)

        return table

    def table_equity_style(self, obj,w,h):
        """table equity style"""

        if obj['stockStyle']["fund"]["prospectiveEarningsYield"] != None:
            prospectiveEarningsYield = "{:.2f}".format(obj['stockStyle']["fund"]["prospectiveEarningsYield"]).replace('.', ',')
        else:
            prospectiveEarningsYield = None


        if obj['stockStyle']["fund"]["prospectiveBookValueYield"] != None:
            prospectiveBookValueYield = "{:.2f}".format(obj['stockStyle']["fund"]["prospectiveBookValueYield"]).replace('.', ',')
        else:
            prospectiveBookValueYield = None

        if obj['stockStyle']["fund"]["prospectiveRevenueYield"] != None:
            prospectiveRevenueYield = "{:.2f}".format(obj['stockStyle']["fund"]["prospectiveRevenueYield"]).replace('.', ',')
        else:
            prospectiveRevenueYield = None

        if obj['stockStyle']["fund"]["prospectiveCashFlowYield"] != None:
            prospectiveCashFlowYield = "{:.2f}".format(obj['stockStyle']["fund"]["prospectiveCashFlowYield"]).replace('.', ',')
        else:
            prospectiveCashFlowYield = None

        if obj['stockStyle']["fund"]["prospectiveDividendYield"] != None:
            prospectiveDividendYield = "{:.2f}".format(obj['stockStyle']["fund"]["prospectiveDividendYield"]).replace('.', ',')
        else:
            prospectiveDividendYield = None

        if obj['stockStyle']["fund"]["forecasted5YearEarningsGrowth"] != None:
            forecasted5YearEarningsGrowth = "{:.2f}".format(obj['stockStyle']["fund"]["forecasted5YearEarningsGrowth"]).replace('.', ',')
        else:
            forecasted5YearEarningsGrowth = None


        if obj['stockStyle']["fund"]["forecastedEarningsGrowth"] != None:
            forecastedEarningsGrowth = "{:.2f}".format(obj['stockStyle']["fund"]["forecastedEarningsGrowth"]).replace('.', ',')
        else:
            forecastedEarningsGrowth = None


        if obj['stockStyle']["fund"]["forecastedBookValueGrowth"] != None:
            forecastedBookValueGrowth = "{:.2f}".format(obj['stockStyle']["fund"]["forecastedBookValueGrowth"]).replace('.', ',')
        else:
            forecastedBookValueGrowth = None

        if obj['stockStyle']["fund"]["forecastedRevenueGrowth"] != None:
            forecastedRevenueGrowth = "{:.2f}".format(obj['stockStyle']["fund"]["forecastedRevenueGrowth"]).replace('.', ',')
        else:
            forecastedRevenueGrowth = None

        if obj['stockStyle']["fund"]["forecastedCashFlowGrowth"] != None:
            forecastedCashFlowGrowth = "{:.2f}".format(obj['stockStyle']["fund"]["forecastedCashFlowGrowth"]).replace('.', ',')
        else:
            forecastedCashFlowGrowth = None

        



        data = [["Rendement \nbénéfices",
        "Rendement \nvaleur comptable","Rendement \nchiffre d'affaires",
        "Rendement \ncash flow",	"Taux \ndividende",
       ],
        [prospectiveEarningsYield,
        prospectiveBookValueYield,
        prospectiveRevenueYield,
        prospectiveCashFlowYield,
        prospectiveDividendYield,

        ], [
        "Croissance \nbénéfices 5 ans",	
        "Croissance \nbénéfices",	"Croissance \nvaleur comptable",
        "Croissance \nchiffre d'affaires",	"Croissance \ncash flow"
        ], [
        forecasted5YearEarningsGrowth,
        forecastedEarningsGrowth,
        forecastedBookValueGrowth,
        forecastedRevenueGrowth,
        forecastedCashFlowGrowth

        ]
        ]

            #0 column, 1 row
        style = [
                                ('FONTNAME', (0,0),(-1,-1),self.text_n),
                                ('FONTNAME', (0,0),(-1,0),self.text_b),
                                ('FONTNAME', (0,2),(-1,2),self.text_b),
                                ('FONTSIZE', (0,0),(-1,-1), 10),
                                ('TEXTCOLOR', (0,1),(-1,-1),self.black),
                                ('ALIGN', (0,0),(-1,-1),'CENTER'),
                                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                                ('TOPPADDING',(0,0),(-1,-1),0),
                                ('BOTTOMPADDING',(0,0),(-1,-1),0),
                                ('LEFTPADDING',(0,0),(-1,-1),6),
                                ('RIGHTPADDING',(0,0),(-1,-1),6)]
        if prospectiveEarningsYield != None: 
            if obj['stockStyle']["fund"]["prospectiveEarningsYield"] < 0:
                    style.append(('TEXTCOLOR', (0,1),(0,1),self.red))
            else:
                    style.append(('TEXTCOLOR', (0,1),(0,1),self.green))

        if prospectiveBookValueYield != None: 
            if obj['stockStyle']["fund"]["prospectiveBookValueYield"] < 0:
                    style.append(('TEXTCOLOR', (1,1),(1,1),self.red))
            else:
                    style.append(('TEXTCOLOR', (1,1),(1,1),self.green))

        if prospectiveRevenueYield != None:
            if obj['stockStyle']["fund"]["prospectiveRevenueYield"] < 0:
                    style.append(('TEXTCOLOR', (2,1),(2,1),self.red))
            else:
                    style.append(('TEXTCOLOR', (2,1),(2,1),self.green))


        if prospectiveCashFlowYield != None:
            if obj['stockStyle']["fund"]["prospectiveCashFlowYield"] < 0:
                    style.append(('TEXTCOLOR', (3,1),(3,1),self.red))
            else:
                    style.append(('TEXTCOLOR', (3,1),(3,1),self.green))

        if prospectiveDividendYield != None:
            if obj['stockStyle']["fund"]["prospectiveDividendYield"] < 0:
                    style.append(('TEXTCOLOR', (4,1),(4,1),self.red))
            else:
                    style.append(('TEXTCOLOR', (4,1),(4,1),self.green))


        if forecasted5YearEarningsGrowth != None:
            if obj['stockStyle']["fund"]["forecasted5YearEarningsGrowth"] < 0:
                    style.append(('TEXTCOLOR', (0,3),(0,3),self.red))
            else:
                    style.append(('TEXTCOLOR', (0,3),(0,3),self.green))

        if forecastedEarningsGrowth != None:
            if obj['stockStyle']["fund"]["forecastedEarningsGrowth"] < 0:
                    style.append(('TEXTCOLOR', (1,3),(1,3),self.red))
            else:
                    style.append(('TEXTCOLOR', (1,3),(1,3),self.green))

        if forecastedBookValueGrowth != None:
            if obj['stockStyle']["fund"]["forecastedBookValueGrowth"] < 0:
                    style.append(('TEXTCOLOR', (2,3),(2,3),self.red))
            else:
                    style.append(('TEXTCOLOR', (2,3),(2,3),self.green))

        if forecastedRevenueGrowth != None:
            if obj['stockStyle']["fund"]["forecastedRevenueGrowth"] < 0:
                    style.append(('TEXTCOLOR', (3,3),(3,3),self.red))
            else:
                    style.append(('TEXTCOLOR', (3,3),(3,3),self.green))

        if forecastedCashFlowGrowth !=None:
            if obj['stockStyle']["fund"]["forecastedCashFlowGrowth"] < 0:
                    style.append(('TEXTCOLOR', (4,3),(4,3),self.red))
            else:
                    style.append(('TEXTCOLOR', (4,3),(4,3),self.green))

        table_style = TableStyle(style)

        table = Table(data, colWidths =[w/5]*5,
                        rowHeights = [h*0.3, h*0.2, h*0.3, h*0.2], style = table_style)

        return table

    def table_fees(self, obj, w,h):
        """tables fees"""
        data = [["Frais de souscription \nmaximum",	"Frais de rachat \nmaximum",
        	"Frais de gestion \nannuels maximum",	"Frais courants",	"Frais de conversion"],
            [obj['pages']['Frais de souscription max'], obj['pages']['Frais de rachat max.'],
            obj['pages']['Frais de gestion annuels maximum'], obj['pages']['Frais courants'],
            obj['pages']['Frais de conversion']]
            ]

        #0 column, 1 row
        table_style = TableStyle([
                                ('FONTNAME', (0,0),(-1,-1),self.text_n),
                                ('FONTNAME', (0,0),(-1,0),self.text_b),
                                ('FONTSIZE', (0,0),(-1,-1), 10),
                                ('TEXTCOLOR', (0,1),(-1,-1),self.black),
                                ('ALIGN', (0,0),(-1,-1),'CENTER'),
                                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                                ('TOPPADDING',(0,0),(-1,-1),0),
                                ('BOTTOMPADDING',(0,0),(-1,-1),0),
                                ('LEFTPADDING',(0,0),(-1,-1),6),
                                ('RIGHTPADDING',(0,0),(-1,-1),6)])

        table = Table(data, colWidths =[w/5]*5,
                        rowHeights = [h/len(data)]*len(data), style = table_style)

        return table

        


    def table_annual_performance(self, obj,w,h):
        """table annual performance"""
        data = []
        
        #0 column, 1 row
        style = [
                ('FONTNAME', (0,0),(-1,-1),self.text_n),
                ('FONTNAME', (0,0),(-1,0),self.text_b),
                
                ('FONTSIZE', (0,0),(-1,-1), 10),
                ('TEXTCOLOR', (0,1),(-1,-1),self.black),
                ('ALIGN', (0,0),(-1,-1),'CENTER'),
                ('ALIGN', (0,0),(0,-1),'LEFT'),
                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                ('TOPPADDING',(0,0),(-1,-1),0),
                ('BOTTOMPADDING',(0,0),(-1,-1),0),
                ('LEFTPADDING',(0,0),(-1,-1),6),
                ('RIGHTPADDING',(0,0),(-1,-1),6)]

        date_arr = ['']
        performance = ['Performance (en %)']
        rank = ['Classement (centile)']
        col = 0
        for y in range(7,0,-1):
            col +=1
            date_arr.append(self.today.year - y)
            if "%s_funds_performance" % (self.today.year -y) in obj["pages"]:
                performance.append(obj['pages']["%s_funds_performance" % (self.today.year -y)])
                if obj['pages']["%s_funds_performance" % (self.today.year -y)][:1]  =='-':
                    style.append(('TEXTCOLOR', (col,1),(col,1),self.red))
                else:
                    style.append(('TEXTCOLOR', (col,1),(col,1),self.green))

            else:
                performance.append('')

            if "%s_rank" % (self.today.year -y) in obj["pages"]:
                rank.append(obj['pages']["%s_rank" % (self.today.year -y)])
                try:
                    if int(obj['pages']["%s_rank" % (self.today.year -y)]) > 75:
                        style.append(('TEXTCOLOR', (col,2),(col,2),self.red))
                    elif int(obj['pages']["%s_rank" % (self.today.year -y)]) > 50:
                        style.append(('TEXTCOLOR', (col,2),(col,2),self.orange))
                    elif int(obj['pages']["%s_rank" % (self.today.year -y)]) > 25:
                        style.append(('TEXTCOLOR', (col,2),(col,2),self.yellow))
                    else:
                        style.append(('TEXTCOLOR', (col,2),(col,2),self.green))
                except:
                    pass


            else:
                rank.append('')


        date_arr.append(self.today.year)
        performance.append(obj['pages']["fund_cumulative_performance_Début d'année"])
        if obj['pages']["fund_cumulative_performance_Début d'année"][:1]  =='-':
            style.append(('TEXTCOLOR', (8,1),(8,1),self.red))
        else:
            style.append(('TEXTCOLOR', (8,1),(8,1),self.green))

        if obj['pages']["current_rank"] == '-':
            rank.append('')
        else:
            rank.append(obj['pages']["current_rank"])
        try:
            if int(obj['pages']["current_rank"]) > 75:
                style.append(('TEXTCOLOR', (8,2),(8,2),self.red))
            elif int(obj['pages']["current_rank"]) > 50:
                style.append(('TEXTCOLOR', (8,2),(8,2),self.orange))
            elif int(obj['pages']["current_rank"]) > 25:
                style.append(('TEXTCOLOR', (8,2),(8,2),self.yellow))
            else:
                style.append(('TEXTCOLOR', (8,2),(8,2),self.green))
            
        except:
            pass

        
        data.append(date_arr)
        data.append(performance)
        data.append(rank)


        table_style = TableStyle(style)

        table = Table(data, colWidths =[w*0.18] + [w*0.82/8]*9,
                        rowHeights = [h/len(data)]*len(data), style = table_style)

        return table

    def table_cumulative_performance(self,obj,w,h):
        """table cumulative performance"""

        #10 years
        if "fund_cumulative_performance_10 ans (annualisée)"  in obj['pages']:
            ann_10Y = obj['pages']["fund_cumulative_performance_10 ans (annualisée)"]
        else:
            ann_10Y = "-"

        #5 years
        if "fund_cumulative_performance_5 ans (annualisée)"  in obj['pages']:
            ann_5Y = obj['pages']["fund_cumulative_performance_5 ans (annualisée)"]
        else:
            ann_5Y = "-"

        #3 years
        if "fund_cumulative_performance_3 ans (annualisée)"  in obj['pages']:
            ann_3Y = obj['pages']["fund_cumulative_performance_3 ans (annualisée)"]
        else:
            ann_3Y = "-"

        data = [["Début \nde l'année",	"1 jour",	"1 semaine",	"1 mois",	"3 mois",	"6 mois",	"1 an",	"3 ans \nannualisé",	"5 ans \nannualisé",	"10 ans \nannualisé"],
        [obj['pages']["fund_cumulative_performance_Début d'année"],obj['pages']["fund_cumulative_performance_1 jour"],
        obj['pages']["fund_cumulative_performance_1 semaine"],obj['pages']["fund_cumulative_performance_1 mois"],
        obj['pages']["fund_cumulative_performance_3 mois"], obj['pages']["fund_cumulative_performance_6 mois"],
        obj['pages']["fund_cumulative_performance_1 an"], ann_3Y,
        ann_5Y, ann_10Y
        ]
        ]
        #0 column, 1 row
        style = [
                                ('FONTNAME', (0,0),(-1,-1),self.text_n),
                                ('FONTNAME', (0,0),(-1,0),self.text_b),
                                
                                ('FONTSIZE', (0,0),(-1,-1), 10),
                                ('TEXTCOLOR', (0,1),(-1,-1),self.black),
                                ('ALIGN', (0,0),(-1,-1),'CENTER'),
                                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                                ('TOPPADDING',(0,0),(-1,-1),0),
                                ('BOTTOMPADDING',(0,0),(-1,-1),0),
                                ('LEFTPADDING',(0,0),(-1,-1),6),
                                ('RIGHTPADDING',(0,0),(-1,-1),6)]

        if obj['pages']["fund_cumulative_performance_Début d'année"] == '-':
            style.append(('TEXTCOLOR', (0,1),(0,1),self.black))
        elif obj['pages']["fund_cumulative_performance_Début d'année"][:1]  =='-':
            style.append(('TEXTCOLOR', (0,1),(0,1),self.red))
        else:
            style.append(('TEXTCOLOR', (0,1),(0,1),self.green))

        if obj['pages']["fund_cumulative_performance_1 jour"] == '-':
            style.append(('TEXTCOLOR', (1,1),(1,1),self.black))
        elif obj['pages']["fund_cumulative_performance_1 jour"][:1]  =='-':
            style.append(('TEXTCOLOR', (1,1),(1,1),self.red))
        else:
            style.append(('TEXTCOLOR', (1,1),(1,1),self.green))

        if obj['pages']["fund_cumulative_performance_1 semaine"] == '-':
            style.append(('TEXTCOLOR', (2,1),(2,1),self.black))
        elif obj['pages']["fund_cumulative_performance_1 semaine"][:1]  =='-':
            style.append(('TEXTCOLOR', (2,1),(2,1),self.red))
        else:
            style.append(('TEXTCOLOR', (2,1),(2,1),self.green))

        if obj['pages']["fund_cumulative_performance_1 mois"] == '-':
            style.append(('TEXTCOLOR', (3,1),(3,1),self.black))
        elif obj['pages']["fund_cumulative_performance_1 mois"][:1]  =='-':
            style.append(('TEXTCOLOR', (3,1),(3,1),self.red))
        else:
            style.append(('TEXTCOLOR', (3,1),(3,1),self.green))

        if obj['pages']["fund_cumulative_performance_3 mois"] == '-':
            style.append(('TEXTCOLOR', (4,1),(4,1),self.black))
        elif obj['pages']["fund_cumulative_performance_3 mois"][:1]  =='-':
            style.append(('TEXTCOLOR', (4,1),(4,1),self.red))
        else:
            style.append(('TEXTCOLOR', (4,1),(4,1),self.green))

        if obj['pages']["fund_cumulative_performance_6 mois"] == '-':
            style.append(('TEXTCOLOR', (5,1),(5,1),self.black))
        elif obj['pages']["fund_cumulative_performance_6 mois"][:1]  =='-':
            style.append(('TEXTCOLOR', (5,1),(5,1),self.red))
        else:
            style.append(('TEXTCOLOR', (5,1),(5,1),self.green))

        if obj['pages']["fund_cumulative_performance_1 an"] == '-':
            style.append(('TEXTCOLOR', (6,1),(6,1),self.black))
        elif obj['pages']["fund_cumulative_performance_1 an"][:1]  =='-':
            style.append(('TEXTCOLOR', (6,1),(6,1),self.red))
        else:
            style.append(('TEXTCOLOR', (6,1),(6,1),self.green))

        if ann_3Y == '-':
            style.append(('TEXTCOLOR', (7,1),(7,1),self.black))
        elif ann_3Y  =='-':
            style.append(('TEXTCOLOR', (7,1),(7,1),self.red))
        else:
            style.append(('TEXTCOLOR', (7,1),(7,1),self.green))

        if ann_5Y == '-':
            style.append(('TEXTCOLOR', (8,1),(8,1),self.black))
        elif ann_5Y  =='-':
            style.append(('TEXTCOLOR', (8,1),(8,1),self.red))
        else:
            style.append(('TEXTCOLOR', (8,1),(8,1),self.green))

        if ann_10Y == '-':
            style.append(('TEXTCOLOR', (9,1),(9,1),self.black))
        elif ann_10Y  =='-':
            style.append(('TEXTCOLOR', (9,1),(9,1),self.red))
        else:
            style.append(('TEXTCOLOR', (9,1),(9,1),self.green))


        table_style = TableStyle(style)

        table = Table(data, colWidths =[w/10]*10,
                        rowHeights = [h/len(data)]*len(data), style = table_style)

        return table

    def table_characteristic(self, obj, w, h):
        """table characteristic"""


        data = [['ISIN',obj['pages']['ISIN'], "Actif net", "{:.2f}".format(obj['infos']['FundTNAV']/1000000).replace('.', ',') + ' M ' + obj['infos']['PriceCurrency'],'Valeur liquidative', str(obj['infos']['ClosePrice']).replace('.', ',') + ' ' + obj['infos']['PriceCurrency'] ],
                ["Devise", obj['infos']['PriceCurrency'],'Eligible PEA', obj['pages']['PEA'],'Eligible PME PEA', obj['pages']['PEAPME'], ],
                ["Structure légale", obj['pages']['Structure légale'],"UCITS", obj['pages']['UCITS'], '', ''],
                
                ["Société de gestion", obj['pages']['Société de gestion'][:30], "Site internet", obj['pages']['Site Internet'], '', '']
        ]



        #0 column, 1 row
        table_style = TableStyle([
                                ('FONTNAME', (0,0),(-1,-1),self.text_n),
                                ('FONTNAME', (0,0),(0,-1),self.text_b),
                                ('FONTNAME', (2,0),(2,-1),self.text_b),
                                ('FONTNAME', (4,0),(4,-1),self.text_b),
                                ('FONTNAME', (2,0),(2,-1),self.text_b),
                                ('FONTSIZE', (0,0),(-1,-1), 10),
                                ('TEXTCOLOR', (0,1),(-1,-1),self.black),
                                ('ALIGN', (0,0),(-1,-1),'LEFT'),
                                ('VALIGN', (0,0),(-1,-1),'MIDDLE'),
                                ('TOPPADDING',(0,0),(-1,-1),0),
                                ('BOTTOMPADDING',(0,0),(-1,-1),0),
                                ('LEFTPADDING',(0,0),(-1,-1),6),
                                ('RIGHTPADDING',(0,0),(-1,-1),6)])

        table = Table(data, colWidths =[w*0.17, w*0.27, w*0.13, w*0.13, w*0.17, w*0.13],
                        rowHeights = [h/len(data)]*len(data), style = table_style)

        return table
    def paragraph_text(self, text):
        """paragraph for text"""
        style_para = ParagraphStyle(name = 'style_para', 
                                    fontName=self.text_n,
                                    fontSize=12,
                                    leading = 12,
                                    textColor = self.black,
                                    alignment = TA_JUSTIFY,
                                    )
        return Paragraph(text,style = style_para)


    def paragraph_date(self, target_date):
        """title of the document"""
        style_para = ParagraphStyle(name = 'style_para', 
                                    fontName=self.text_b,
                                    fontSize=12,
                                    leading = 12,
                                    textColor = self.main_color,
                                    alignment = TA_LEFT,
                                    )
        return Paragraph('Portefeuille au %s' %(target_date.strftime('%d/%m/%Y')),style = style_para)
    def paragraph_title(self, title):
        """title of the document"""
        style_para = ParagraphStyle(name = 'style_para', 
                                    fontName=self.text_b,
                                    fontSize=20,
                                    leading = 20,
                                    textColor = self.main_color,
                                    alignment = TA_LEFT,
                                    )
        return Paragraph(title,style = style_para)
        
    def paragraph_title_date(self):
        """title date of the document"""
        style_para = ParagraphStyle(name = 'style_para', 
                                    fontName=self.text_n,
                                    fontSize=16,
                                    leading = 20,
                                    textColor = self.main_color,
                                    alignment = TA_CENTER,
                                    )
        return Paragraph("Rapport créé le \n %s" % (self.today.strftime('%d/%m/%Y')),style = style_para)

    def paragraph_presentation(self, title):
        """title of the document"""
        style_para = ParagraphStyle(name = 'style_para', 
                                    fontName=self.text_b,
                                    fontSize=25,
                                    leading = 20,
                                    textColor = self.main_color,
                                    alignment = TA_CENTER,
                                    )
        return Paragraph(title,style = style_para)

    def adapt_text_size(self,w,h,text, font_size, leading = 14):
        """reecriture du texte"""

        table_style = TableStyle([('ALIGN', (0,0),(-1,-1),'LEFT'),
                                ('VALIGN', (0,0),(-1,-1),'TOP'),
                                ('TOPPADDING',(0,0),(-1,-1),1),
                                ('BOTTOMPADDING',(0,0),(-1,-1),1),
                                ('LEFTPADDING',(0,0),(-1,-1),6),
                                ('RIGHTPADDING',(0,0),(-1,-1),6)
                                 ])

        style_paragraph = ParagraphStyle(name = 'style_paragraph', 
                            fontName=self.text_n,
                            fontSize=12,
                            leading=leading,
                            textColor = self.black,
                            alignment = TA_JUSTIFY,
                            spaceShrinkage = 0.05,
                            borderPadding = 0,
                            wordWrap = None,)

        # largeur et hauteur disponible du cadre commentaire
        #copie le style texte
        fontsize = font_size
        leading_size = leading
        Aw = w + 1*mm
        Ah = h + 1*mm
        while Aw >= w and Ah >= h:
            fontsize -= 1
            if leading_size >= fontsize:
                leading_size = fontsize + 1
            style_paragraph.fontSize = fontsize
            style_paragraph.leading = leading_size
            target_paragraph = Paragraph(text,style_paragraph)
            Aw,Ah = target_paragraph.wrap(w,h)
        table = Table([[target_paragraph]], colWidths = [w], rowHeights = [h], style =  table_style)
        return table

