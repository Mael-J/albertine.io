from reportlab.lib import colors


class COLOR:
    """class for color"""
    def __init__(self):
        """instanciate class """
        
        self.text_n = 'Helvetica'
        self.text_b = 'Helvetica-Bold'
        self.text_i = 'Helvetica-Oblique'
        self.text_ib = 'Helvetica-BoldOblique'
        self.black = colors.Color(red=(0/255),green=(0/255),blue=(0/255))
        self.white = colors.Color(red=(255/255),green=(255/255),blue=(255/255))
        self.grey = colors.Color(red=(170/255),green=(170/255),blue=(170/255))
        self.dark_light_blue = colors.Color(red=(22/255),green=(46/255),blue=(90/255))
        self.light_blue = colors.Color(red=(238/255),green=(244/255),blue=(255/255))
        self.main_color = colors.Color(red=(165/255),green=(159/255),blue=(211/255))
        self.secondary_color = colors.Color(red=(243/255),green=(242/255),blue=(255/255))
        self.main_color_pink = colors.Color(red=(211/255),green=(159/255),blue=(195/255))
        self.green = colors.Color(red=(15/255),green=(179/255),blue=(47/255))
        self.red = colors.Color(red=(255/255),green=(25/255),blue=(36/255))
        self.orange = colors.Color(red=(236/255),green=(114/255),blue=(7/255))
        self.yellow = colors.Color(red=(236/255),green=(211/255),blue=(7/255))