def 畫星星(t,n=20,x=144,angle=18):
    '''
    :param t: 小龜物件
    :param n: number of stars
    :param x: exterior angle of each star
    :param angle: angle of rotation for the spiral
    :return: None
    '''
    import random

    # loop for number of stars
    for i in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        t.pencolor(r, g, b)
        t.fillcolor(r, g, b)

        t.begin_fill()
        # loop for drawing each star
        for j in range(5):
            t.forward(5 * n - 5 * i)
            t.right(x)
            t.forward(5 * n - 5 * i)
            t.right(72 - x)
        t.end_fill()
        t.rt(angle)


def 畫正方形(t,x,y,size,rgb_tuple):
    '''
    繪製 正方形
    :param t: 小龜物件
    :param x: x座標
    :param y: y座標
    :param size: 邊長
    :param rgb_tuple: (R,G,B)顏色
    :return: 沒有回傳
    '''
    t.hideturtle()
    t.speed(0)
    t.pencolor(rgb_tuple)
    t.fillcolor(rgb_tuple)

    t.penup()
    t.goto(x + size/2, y - size/2)
    t.setheading(90)
    t.pendown()

    t.begin_fill()
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.end_fill()

def 畫矩形(t,x,y,w,h,colors):
    '''
    繪製 矩形
    :param t: 小龜物件
    :param x: x座標
    :param y: y座標
    :param w: 寬
    :param h: 高
    :param rgb_tuple: (R,G,B)顏色  'red' 顏色字串也可以
    :return: 沒有回傳
    '''
    t.hideturtle()
    t.speed(0)
    t.pencolor(colors)
    t.fillcolor(colors)

    t.penup()
    t.goto(x + w/2, y - h/2)
    t.setheading(90)
    t.pendown()

    t.begin_fill()
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.end_fill()

def logo(t,x,y,s,pencolor_str,fillcolor_str):
    '''
    繪製 Android Logo
    :param t: 小龜物件
    :param x: x座標
    :param y: y座標
    :param s: 大小比例
    :param pencolor_str: 筆的顏色(用顏色字串)
    :param fillcolor_str: 填滿的顏色(用顏色字串)
    :return: 沒有回傳
    '''
    t.hideturtle()
    t.speed(0)
    t.fillcolor( fillcolor_str )
    t.pencolor( pencolor_str )

    # -----頭-----
    t.penup()  # 提起筆
    t.goto(x+100*s, y+100*s)

    t.pendown()  # 下筆
    t.begin_fill()
    t.seth(90)
    t.circle(100*s, 180)  # 半球 半徑為100
    t.lt(90)
    t.fd(200*s)
    t.end_fill()

    # -----眼睛-----
    t.penup()
    t.goto(x-50*s, y+150*s)  # 左眼
    t.pendown()  # 下筆
    t.dot(23*s, "white")

    t.penup()
    t.goto(x+50*s, y+150*s)  # 右眼
    t.pendown()  # 下筆
    t.dot(23*s, "white")

    # -----天線-----
    t.pensize(5 * s)  # 筆粗

    t.penup()
    t.goto(x-40*s, y+180*s)  # 左線
    t.seth(120)  # 調角度
    t.pendown()  # 下筆
    t.fd(50*s)

    t.penup()
    t.goto(x+40*s, y+180*s)
    t.seth(60)
    t.pendown()
    t.fd(50*s)

    t.pensize(1)  # 筆粗

    # ------身體------
    t.penup()
    t.goto(x-100*s, y+80*s)  # 起始位置
    t.seth(270)  # 角度
    t.pendown()
    t.begin_fill()  # 開始填色
    t.fd(160*s)
    t.circle(20*s, 90)
    t.fd(160*s)
    t.circle(20*s, 90)
    t.fd(160*s)
    t.lt(90)
    t.fd(200*s)
    t.end_fill()  # 結束填色

    # -----手-----
    t.pensize(40*s)

    t.penup()
    t.goto(x-130*s, y+50*s)
    t.seth(250)
    t.pendown()
    t.fd(85*s)

    t.penup()
    t.goto(x+130*s, y+50*s)
    t.seth(70)
    t.pendown()
    t.fd(85*s)

    # ------腳------

    t.penup()
    t.goto(x-50*s, y-80*s)
    t.seth(270)
    t.pendown()
    t.fd(65*s)

    t.penup()
    t.goto(x+50*s, y-80*s)
    t.seth(300)
    t.pendown()
    t.fd(70*s)

    t.pensize(1)

    return None

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
          'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
          'thistle', 'snow2', 'snow3',
          'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
          'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
          'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
          'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
          'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
          'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
          'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
          'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
          'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
          'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
          'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
          'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
          'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
          'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
          'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
          'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
          'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
          'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
          'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
          'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
          'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
          'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
          'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
          'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
          'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
          'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
          'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
          'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
          'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
          'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
          'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
          'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
          'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
          'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
          'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
          'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
          'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
          'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
          'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
          'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
          'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
          'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
          'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
          'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
          'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
          'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
          'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
          'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
          'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
          'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
          'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
          'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
          'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
          'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
          'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
          'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
          'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

STUDENTS = ['梁若庠','張昱誠','吳敬熙','范振榮',
            '林哲彥','林怡君','陳盈君','葉利穔',
            '鍾靜怡','洪姿珺','黃俊鑫','鄭楷諭',
            '范姜葶','王敬','吳冠誼','徐郁欣',
            '蔡承達',' 許慶宏','陳長春 ','林宥辰',
            '唐承捷',' 陳俊瑋','黃彥瀚','許菁怡',
            '王士誠','鄭仕傳','徐政華','吳孟儒',' 陳沛汝','陳裕東']

MYFONTS = ['System', '@System', 'Terminal', '@Terminal', 'Fixedsys',  #  Tkinter 用
           '@Fixedsys', 'Modern', 'Roman', 'Script', 'Courier',
           'MS Serif', 'MS Sans Serif', 'Small Fonts', 'Adobe 黑体 Std R',
           '@Adobe 黑体 Std R', 'Adobe 明體 Std L', '@Adobe 明體 Std L',
           'Adobe Myungjo Std M', '@Adobe Myungjo Std M', 'Adobe Pi Std',
           'Adobe 宋体 Std L', '@Adobe 宋体 Std L', 'Courier Std',
           'Kozuka Gothic Pr6N M', '@Kozuka Gothic Pr6N M', 'Kozuka Mincho Pr6N R',
           '@Kozuka Mincho Pr6N R', 'Myriad CAD', 'Adobe Caslon Pro Bold',
           'Adobe Caslon Pro', 'Adobe 仿宋 Std R', '@Adobe 仿宋 Std R',
           'Adobe 繁黑體 Std B', '@Adobe 繁黑體 Std B', 'Adobe Gothic Std B',
           '@Adobe Gothic Std B', 'Adobe 楷体 Std R', '@Adobe 楷体 Std R',
           'Adobe Naskh Medium', 'Adobe Garamond Pro Bold', 'Adobe Garamond Pro',
           'Birch Std', 'Blackoak Std', 'Brush Script Std', 'Chaparral Pro',
           'Chaparral Pro Light', 'Charlemagne Std', 'Cooper Std Black',
           'Giddyup Std', 'Hobo Std', 'Kozuka Gothic Pro B', '@Kozuka Gothic Pro B',
           'Kozuka Gothic Pro EL', '@Kozuka Gothic Pro EL', 'Kozuka Gothic Pro H',
           '@Kozuka Gothic Pro H', 'Kozuka Gothic Pro L', '@Kozuka Gothic Pro L',
           'Kozuka Gothic Pro M', '@Kozuka Gothic Pro M', 'Kozuka Gothic Pro R',
           '@Kozuka Gothic Pro R', 'Kozuka Mincho Pro B', '@Kozuka Mincho Pro B',
           'Kozuka Mincho Pro EL', '@Kozuka Mincho Pro EL', 'Kozuka Mincho Pro H',
           '@Kozuka Mincho Pro H', 'Kozuka Mincho Pro L', '@Kozuka Mincho Pro L',
           'Kozuka Mincho Pro M', '@Kozuka Mincho Pro M', 'Kozuka Mincho Pro R',
           '@Kozuka Mincho Pro R', 'Lithos Pro Regular', 'Mesquite Std', 'Minion Pro Cond',
           'Minion Pro Med', 'Minion Pro SmBd', 'Myriad Arabic', 'Nueva Std',
           'Nueva Std Cond', 'OCR A Std', 'Orator Std', 'Poplar Std', 'Prestige Elite Std',
           'Rosewood Std Regular', 'Stencil Std', 'Tekton Pro', 'Tekton Pro Cond',
           'Tekton Pro Ext', 'Trajan Pro', 'Adobe Arabic', 'Adobe Devanagari',
           'Adobe Hebrew', 'Kozuka Gothic Pr6N B', '@Kozuka Gothic Pr6N B',
           'Kozuka Gothic Pr6N EL', '@Kozuka Gothic Pr6N EL', 'Kozuka Gothic Pr6N H',
           '@Kozuka Gothic Pr6N H', 'Kozuka Gothic Pr6N L', '@Kozuka Gothic Pr6N L',
           'Kozuka Gothic Pr6N R', '@Kozuka Gothic Pr6N R', 'Kozuka Mincho Pr6N B',
           '@Kozuka Mincho Pr6N B', 'Kozuka Mincho Pr6N EL', '@Kozuka Mincho Pr6N EL',
           'Kozuka Mincho Pr6N H', '@Kozuka Mincho Pr6N H', 'Kozuka Mincho Pr6N L',
           '@Kozuka Mincho Pr6N L', 'Kozuka Mincho Pr6N M', '@Kozuka Mincho Pr6N M',
           'Letter Gothic Std', 'Minion Pro', 'Myriad Hebrew', 'Myriad Pro',
           'Myriad Pro Cond', 'Myriad Pro Light', 'Marlett', 'Arial',
           'Arabic Transparent', 'Arial Baltic', 'Arial CE', 'Arial CYR',
           'Arial Greek', 'Arial TUR', 'Arial Black', 'Bahnschrift Light',
           'Bahnschrift SemiLight', 'Bahnschrift', 'Bahnschrift SemiBold',
           'Bahnschrift Light SemiCondensed', 'Bahnschrift SemiLight SemiConde',
           'Bahnschrift SemiCondensed', 'Bahnschrift SemiBold SemiConden',
           'Bahnschrift Light Condensed', 'Bahnschrift SemiLight Condensed',
           'Bahnschrift Condensed', 'Bahnschrift SemiBold Condensed', 'Calibri',
           'Calibri Light', 'Cambria', 'Cambria Math', 'Candara', 'Candara Light',
           'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Corbel Light',
           'Courier New', 'Courier New Baltic', 'Courier New CE', 'Courier New CYR',
           'Courier New Greek', 'Courier New TUR', 'Ebrima', 'Franklin Gothic Medium',
           'Gabriola', 'Gadugi', 'Georgia', 'Impact', 'Ink Free', 'Javanese Text',
           'Leelawadee UI', 'Leelawadee UI Semilight', 'Lucida Console', 'Lucida Sans Unicode',
           'Malgun Gothic', '@Malgun Gothic', 'Malgun Gothic Semilight', '@Malgun Gothic Semilight',
           'Microsoft Himalaya', '微軟正黑體', '@微軟正黑體', 'Microsoft JhengHei UI',
           '@Microsoft JhengHei UI', '微軟正黑體 Light', '@微軟正黑體 Light',
           'Microsoft JhengHei UI Light', '@Microsoft JhengHei UI Light',
           'Microsoft New Tai Lue', 'Microsoft PhagsPa', 'Microsoft Sans Serif',
           'Microsoft Tai Le', 'Microsoft YaHei', '@Microsoft YaHei', 'Microsoft YaHei UI',
           '@Microsoft YaHei UI', 'Microsoft YaHei Light', '@Microsoft YaHei Light',
           'Microsoft YaHei UI Light', '@Microsoft YaHei UI Light', 'Microsoft Yi Baiti',
           '細明體-ExtB', '@細明體-ExtB', '新細明體-ExtB', '@新細明體-ExtB', '細明體_HKSCS-ExtB',
           '@細明體_HKSCS-ExtB', 'Mongolian Baiti', 'MS Gothic', '@MS Gothic',
           'MS UI Gothic', '@MS UI Gothic', 'MS PGothic', '@MS PGothic', 'MV Boli',
           'Myanmar Text', 'Nirmala UI', 'Nirmala UI Semilight', 'Palatino Linotype',
           'Segoe MDL2 Assets', 'Segoe Print', 'Segoe Script', 'Segoe UI',
           'Segoe UI Black', 'Segoe UI Emoji', 'Segoe UI Historic', 'Segoe UI Light',
           'Segoe UI Semibold', 'Segoe UI Semilight', 'Segoe UI Symbol',
           'SimSun', '@SimSun', 'NSimSun', '@NSimSun', 'SimSun-ExtB', '@SimSun-ExtB',
           'Sitka Small', 'Sitka Text', 'Sitka Subheading', 'Sitka Heading',
           'Sitka Display', 'Sitka Banner', 'Sylfaen', 'Symbol', 'Tahoma',
           'Times New Roman', 'Times New Roman Baltic', 'Times New Roman CE',
           'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR',
           'Trebuchet MS', 'Verdana', 'Webdings', 'Wingdings', 'Yu Gothic',
           '@Yu Gothic', 'Yu Gothic UI', '@Yu Gothic UI', 'Yu Gothic UI Semibold',
           '@Yu Gothic UI Semibold', 'Yu Gothic Light', '@Yu Gothic Light',
           'Yu Gothic UI Light', '@Yu Gothic UI Light', 'Yu Gothic Medium',
           '@Yu Gothic Medium', 'Yu Gothic UI Semilight', '@Yu Gothic UI Semilight',
           '標楷體', '@標楷體', '細明體', '@細明體', '新細明體', '@新細明體', '細明體_HKSCS',
           '@細明體_HKSCS', 'HoloLens MDL2 Assets', 'AcadEref', 'AIGDT', 'AmdtSymbols',
           'GENISO', 'AMGDT', 'BankGothic Lt BT', 'BankGothic Md BT', 'CityBlueprint',
           'CommercialPi BT', 'CommercialScript BT', 'CountryBlueprint', 'Dutch801 Rm BT',
           'Dutch801 XBd BT', 'EuroRoman', 'ISOCPEUR', 'ISOCTEUR', 'Monospac821 BT',
           'PanRoman', 'Romantic', 'RomanS', 'SansSerif', 'Stylus BT', 'SuperFrench',
           'Swis721 BT', 'Swis721 BdOul BT', 'Swis721 Cn BT', 'Swis721 BdCnOul BT',
           'Swis721 BlkCn BT', 'Swis721 LtCn BT', 'Swis721 Ex BT', 'Swis721 BlkEx BT',
           'Swis721 LtEx BT', 'Swis721 Blk BT', 'Swis721 BlkOul BT', 'Swis721 Lt BT',
           'TechnicBold', 'TechnicLite', 'Technic', 'UniversalMath1 BT', 'Vineta BT',
           'AMGDT_IV25', 'AMGDT_IV50', 'Complex_IV25', 'Complex_IV50', 'GDT_IV25',
           'GDT_IV50', 'GOST Common', 'GreekC_IV25', 'GreekC_IV50', 'GreekS_IV25',
           'GreekS_IV50', 'ISOCP_IV25', 'ISOCP_IV50', 'ISOCP2_IV25', 'ISOCP2_IV50',
           'ISOCP3_IV25', 'ISOCP3_IV50', 'ISOCT_IV25', 'ISOCT_IV50', 'ISOCT2_IV25',
           'ISOCT2_IV50', 'ISOCT3_IV25', 'ISOCT3_IV50', 'Italic_IV25', 'Italic_IV50',
           'Monotxt_IV25', 'Monotxt_IV50', 'RomanS_IV25', 'RomanS_IV50', 'ScriptS_IV25',
           'ScriptS_IV50', 'Simplex_IV25', 'Simplex_IV50', 'Syastro_IV25', 'Syastro_IV50',
           'Symap_IV25', 'Symap_IV50', 'Symath_IV25', 'Symath_IV50', 'Symeteo_IV25',
           'Symeteo_IV50', 'Symusic_IV25', 'Symusic_IV50', 'Txt_IV25', 'Txt_IV50',
           'Arial Unicode MS', '@Arial Unicode MS', 'Century', 'Wingdings 2',
           'Wingdings 3', 'Tempus Sans ITC', 'Pristina', 'Papyrus', 'Mistral',
           'Lucida Handwriting', 'Kristen ITC', 'Juice ITC', 'French Script MT',
           'Freestyle Script', 'Bradley Hand ITC', 'Book Antiqua', 'Garamond',
           'Monotype Corsiva', 'Century Gothic', 'Algerian', 'Baskerville Old Face',
           'Bauhaus 93', 'Bell MT', 'Berlin Sans FB', 'Bernard MT Condensed',
           'Bodoni MT Poster Compressed', 'Britannic Bold', 'Broadway', 'Brush Script MT',
           'Californian FB', 'Centaur', 'Chiller', 'Colonna MT', 'Cooper Black',
           'Footlight MT Light', 'Harlow Solid Italic', 'Harrington', 'High Tower Text',
           'Jokerman', 'Kunstler Script', 'Lucida Bright', 'Lucida Calligraphy',
           'Lucida Fax', 'Magneto', 'Matura MT Script Capitals', 'Modern No. 20',
           'Niagara Engraved', 'Niagara Solid', 'Old English Text MT', 'Onyx',
           'Parchment', 'Playbill', 'Poor Richard', 'Ravie', 'Informal Roman',
           'Showcard Gothic', 'Snap ITC', 'Stencil', 'Viner Hand ITC', 'Vivaldi',
           'Vladimir Script', 'Wide Latin', 'Tw Cen MT', 'Tw Cen MT Condensed',
           'Script MT Bold', 'Rockwell Extra Bold', 'Rockwell Condensed', 'Rockwell',
           'Rage Italic', 'Perpetua Titling MT', 'Perpetua', 'Palace Script MT',
           'OCR A Extended', 'Maiandra GD', 'Lucida Sans Typewriter', 'Lucida Sans',
           'Imprint MT Shadow', 'Haettenschweiler', 'Goudy Stout', 'Goudy Old Style',
           'Gloucester MT Extra Condensed', 'Gill Sans Ultra Bold Condensed',
           'Gill Sans Ultra Bold', 'Gill Sans MT Condensed', 'Gill Sans MT',
           'Gill Sans MT Ext Condensed Bold', 'Gigi', 'Franklin Gothic Medium Cond',
           'Franklin Gothic Heavy', 'Franklin Gothic Demi Cond', 'Franklin Gothic Demi',
           'Franklin Gothic Book', 'Forte', 'Felix Titling', 'Eras Medium ITC',
           'Eras Light ITC', 'Eras Demi ITC', 'Eras Bold ITC', 'Engravers MT', 'Elephant',
           'Edwardian Script ITC', 'Curlz MT', 'Copperplate Gothic Light',
           'Copperplate Gothic Bold', 'Century Schoolbook', 'Castellar', 'Calisto MT',
           'Bookman Old Style', 'Bodoni MT Condensed', 'Bodoni MT Black', 'Bodoni MT',
           'Blackadder ITC', 'Arial Rounded MT Bold', 'Agency FB', 'Berlin Sans FB Demi',
           'Tw Cen MT Condensed Extra Bold', 'HYSWLongFangSong', '@HYSWLongFangSong',
           'SWAstro', 'OLF SimpleSansOC', 'SWComp', 'SWGothe', 'SWGothg', 'SWGothi',
           'SWGrekc', 'SWGreks', 'SWIsop1', 'SWIsop2', 'SWIsop3', 'SWIsot1', 'SWIsot2',
           'SWIsot3', 'SWItal', 'SWItalc', 'SWItalt', 'SWMap', 'SWMath', 'SWMeteo', 'SWMono',
           'SWMusic', 'SWRomnc', 'SWRomnd', 'SWRomns', 'SWRomnt', 'SWScrpc', 'SWScrps',
           'SWSimp', 'SWTxt', 'SWGDT', 'SWLink', 'SOLIDWORKS GDT', 'INSPECTIONXPERT GDT FRAMES',
           'INSPECTIONXPERT GDT NOFRMS', 'Arial Narrow', 'Bodoni Bd BT',
           'Bodoni Bk BT', 'CentSchbkCyrill BT', 'Century725 Cn BT', 'Century751 BT',
           'Century751 No2 BT', 'Century751 SeBd BT', 'Clarendon Blk BT',
           'Clarendon BT', 'Clarendon Lt BT', 'DeVinne Txt BT', 'DFGothic-EB',
           '@DFGothic-EB', 'ＤＦ中太楷書体', '@ＤＦ中太楷書体', 'DFMincho-SU', '@DFMincho-SU',
           'DFMincho-UB', '@DFMincho-UB', 'ＤＦ明朝体W5', '@ＤＦ明朝体W5', 'DFPOP1-W9',
           '@DFPOP1-W9', 'Embassy BT', 'EngraversGothic BT', 'Exotc350 Bd BT',
           'Exotc350 DmBd BT', 'Freehand521 BT', 'Futura Bk BT', 'Futura Md BT',
           'Geometr212 BkCn BT', 'Geometr415 Blk BT', 'Geometr706 BlkCn BT',
           'GeoSlab703 Md BT', 'GeoSlab703 MdCn BT', 'Humanst521 BT', 'Humanst521 Lt BT',
           'Humnst777 Blk BT', 'Humnst777 BlkCn BT', 'Humnst777 BT', 'Humnst777 Cn BT',
           'Humnst777 Lt BT', 'Kaufmann BT', 'News701 BT', 'News706 BT', 'NewsGoth BT',
           'NewsGoth Lt BT', 'OCR-A BT', 'OCR-B 10 BT', 'Schadow BT', 'Square721 BT',
           'Square721 Cn BT', 'Swis721 Hv BT', 'Swis721 WGL4 BT', 'TypoUpright BT',
           'Bookshelf Symbol 7', 'MS Outlook', 'MS Reference Sans Serif',
           'MS Reference Specialty', 'MT Extra', 'ZWAdobeF', 'Dubai', 'Dubai Light',
           'Dubai Medium', 'Leelawadee', 'Microsoft Uighur', 'Complex', 'GDT',
           'GothicE', 'GothicG', 'GothicI', 'GreekC', 'GreekS', 'ISOCP2', 'ISOCP3',
           'ISOCP', 'ISOCT2', 'ISOCT3', 'ISOCT', 'ItalicC', 'ItalicT', 'Italic',
           'Monotxt', 'Proxy 1', 'Proxy 2', 'Proxy 3', 'Proxy 4', 'Proxy 5', 'Proxy 6',
           'Proxy 7', 'Proxy 8', 'Proxy 9', 'RomanC', 'RomanD', 'RomanT', 'ScriptC',
           'ScriptS', 'Simplex', 'Syastro', 'Symap', 'Symath', 'Symeteo', 'Symusic',
           'Txt', 'Artifakt Element', 'DengXian', '@DengXian', 'DengXian Light',
           '@DengXian Light', 'FangSong', '@FangSong', 'KaiTi', '@KaiTi', 'SimHei', '@SimHei']