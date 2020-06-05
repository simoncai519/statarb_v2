from enum import Enum, unique


@unique
class Tickers(Enum): pass


# in case we want to add functionality later
# and so functions can accept Snp and Etf ticekrs

class SnpTickers(Tickers):
    A = 'A'
    AAL = 'AAL'
    AAP = 'AAP'
    AAPL = 'AAPL'
    ABBV = 'ABBV'
    ABC = 'ABC'
    ABMD = 'ABMD'
    ABT = 'ABT'
    ACN = 'ACN'
    ADBE = 'ADBE'
    ADI = 'ADI'
    ADM = 'ADM'
    ADP = 'ADP'
    ADS = 'ADS'
    ADSK = 'ADSK'
    AEE = 'AEE'
    AEP = 'AEP'
    AES = 'AES'
    AFL = 'AFL'
    AGN = 'AGN'
    AIG = 'AIG'
    AIV = 'AIV'
    AIZ = 'AIZ'
    AJG = 'AJG'
    AKAM = 'AKAM'
    ALB = 'ALB'
    ALGN = 'ALGN'
    ALK = 'ALK'
    ALL = 'ALL'
    ALLE = 'ALLE'
    ALXN = 'ALXN'
    AMAT = 'AMAT'
    AMCR = 'AMCR'
    AMD = 'AMD'
    AME = 'AME'
    AMGN = 'AMGN'
    AMP = 'AMP'
    AMT = 'AMT'
    AMZN = 'AMZN'
    ANET = 'ANET'
    ANSS = 'ANSS'
    ANTM = 'ANTM'
    AON = 'AON'
    AOS = 'AOS'
    APA = 'APA'
    APD = 'APD'
    APH = 'APH'
    APTV = 'APTV'
    ARE = 'ARE'
    ARNC = 'ARNC'
    ATO = 'ATO'
    ATVI = 'ATVI'
    AVB = 'AVB'
    AVGO = 'AVGO'
    AVY = 'AVY'
    AWK = 'AWK'
    AXP = 'AXP'
    AZO = 'AZO'
    BA = 'BA'
    BAC = 'BAC'
    BAX = 'BAX'
    BBY = 'BBY'
    BDX = 'BDX'
    BEN = 'BEN'
    BIIB = 'BIIB'
    BK = 'BK'
    BKNG = 'BKNG'
    BKR = 'BKR'
    BLK = 'BLK'
    BLL = 'BLL'
    BMY = 'BMY'
    BR = 'BR'
    BSX = 'BSX'
    BWA = 'BWA'
    BXP = 'BXP'
    C = 'C'
    CAG = 'CAG'
    CAH = 'CAH'
    CAT = 'CAT'
    CB = 'CB'
    CBOE = 'CBOE'
    CBRE = 'CBRE'
    CCI = 'CCI'
    CCL = 'CCL'
    CDNS = 'CDNS'
    CDW = 'CDW'
    CE = 'CE'
    CERN = 'CERN'
    CF = 'CF'
    CFG = 'CFG'
    CHD = 'CHD'
    CHRW = 'CHRW'
    CHTR = 'CHTR'
    CI = 'CI'
    CINF = 'CINF'
    CL = 'CL'
    CLX = 'CLX'
    CMA = 'CMA'
    CMCSA = 'CMCSA'
    CME = 'CME'
    CMG = 'CMG'
    CMI = 'CMI'
    CMS = 'CMS'
    CNC = 'CNC'
    CNP = 'CNP'
    COF = 'COF'
    COG = 'COG'
    COO = 'COO'
    COP = 'COP'
    COST = 'COST'
    COTY = 'COTY'
    CPB = 'CPB'
    CPRI = 'CPRI'
    CPRT = 'CPRT'
    CRM = 'CRM'
    CSCO = 'CSCO'
    CSX = 'CSX'
    CTAS = 'CTAS'
    CTL = 'CTL'
    CTSH = 'CTSH'
    CTVA = 'CTVA'
    CTXS = 'CTXS'
    CVS = 'CVS'
    CVX = 'CVX'
    CXO = 'CXO'
    D = 'D'
    DAL = 'DAL'
    DD = 'DD'
    DE = 'DE'
    DFS = 'DFS'
    DG = 'DG'
    DGX = 'DGX'
    DHI = 'DHI'
    DHR = 'DHR'
    DIS = 'DIS'
    DISCA = 'DISCA'
    DISCK = 'DISCK'
    DISH = 'DISH'
    DLR = 'DLR'
    DLTR = 'DLTR'
    DOV = 'DOV'
    DOW = 'DOW'
    DRE = 'DRE'
    DRI = 'DRI'
    DTE = 'DTE'
    DUK = 'DUK'
    DVA = 'DVA'
    DVN = 'DVN'
    DXC = 'DXC'
    EA = 'EA'
    EBAY = 'EBAY'
    ECL = 'ECL'
    ED = 'ED'
    EFX = 'EFX'
    EIX = 'EIX'
    EL = 'EL'
    EMN = 'EMN'
    EMR = 'EMR'
    EOG = 'EOG'
    EQIX = 'EQIX'
    EQR = 'EQR'
    ES = 'ES'
    ESS = 'ESS'
    ETFC = 'ETFC'
    ETN = 'ETN'
    ETR = 'ETR'
    EVRG = 'EVRG'
    EW = 'EW'
    EXC = 'EXC'
    EXPD = 'EXPD'
    EXPE = 'EXPE'
    EXR = 'EXR'
    F = 'F'
    FANG = 'FANG'
    FAST = 'FAST'
    FB = 'FB'
    FBHS = 'FBHS'
    FCX = 'FCX'
    FDX = 'FDX'
    FE = 'FE'
    FFIV = 'FFIV'
    FIS = 'FIS'
    FISV = 'FISV'
    FITB = 'FITB'
    FLIR = 'FLIR'
    FLS = 'FLS'
    FLT = 'FLT'
    FMC = 'FMC'
    FOX = 'FOX'
    FOXA = 'FOXA'
    FRC = 'FRC'
    FRT = 'FRT'
    FTI = 'FTI'
    FTNT = 'FTNT'
    FTV = 'FTV'
    GD = 'GD'
    GE = 'GE'
    GILD = 'GILD'
    GIS = 'GIS'
    GL = 'GL'
    GLW = 'GLW'
    GM = 'GM'
    GOOG = 'GOOG'
    GOOGL = 'GOOGL'
    GPC = 'GPC'
    GPN = 'GPN'
    GPS = 'GPS'
    GRMN = 'GRMN'
    GS = 'GS'
    GWW = 'GWW'
    HAL = 'HAL'
    HAS = 'HAS'
    HBAN = 'HBAN'
    HBI = 'HBI'
    HCA = 'HCA'
    HD = 'HD'
    HES = 'HES'
    HFC = 'HFC'
    HIG = 'HIG'
    HII = 'HII'
    HLT = 'HLT'
    HOG = 'HOG'
    HOLX = 'HOLX'
    HON = 'HON'
    HP = 'HP'
    HPE = 'HPE'
    HPQ = 'HPQ'
    HRB = 'HRB'
    HRL = 'HRL'
    HSIC = 'HSIC'
    HST = 'HST'
    HSY = 'HSY'
    HUM = 'HUM'
    IBM = 'IBM'
    ICE = 'ICE'
    IDXX = 'IDXX'
    IEX = 'IEX'
    IFF = 'IFF'
    ILMN = 'ILMN'
    INCY = 'INCY'
    INFO = 'INFO'
    INTC = 'INTC'
    INTU = 'INTU'
    IP = 'IP'
    IPG = 'IPG'
    IPGP = 'IPGP'
    IQV = 'IQV'
    IR = 'IR'
    IRM = 'IRM'
    ISRG = 'ISRG'
    IT = 'IT'
    ITW = 'ITW'
    IVZ = 'IVZ'
    J = 'J'
    JBHT = 'JBHT'
    JCI = 'JCI'
    JKHY = 'JKHY'
    JNJ = 'JNJ'
    JNPR = 'JNPR'
    JPM = 'JPM'
    JWN = 'JWN'
    K = 'K'
    KEY = 'KEY'
    KEYS = 'KEYS'
    KHC = 'KHC'
    KIM = 'KIM'
    KLAC = 'KLAC'
    KMB = 'KMB'
    KMI = 'KMI'
    KMX = 'KMX'
    KO = 'KO'
    KR = 'KR'
    KSS = 'KSS'
    KSU = 'KSU'
    L = 'L'
    LB = 'LB'
    LDOS = 'LDOS'
    LEG = 'LEG'
    LEN = 'LEN'
    LH = 'LH'
    LHX = 'LHX'
    LIN = 'LIN'
    LKQ = 'LKQ'
    LLY = 'LLY'
    LMT = 'LMT'
    LNC = 'LNC'
    LNT = 'LNT'
    LOW = 'LOW'
    LRCX = 'LRCX'
    LUV = 'LUV'
    LVS = 'LVS'
    LW = 'LW'
    LYB = 'LYB'
    LYV = 'LYV'
    M = 'M'
    MA = 'MA'
    MAA = 'MAA'
    MAR = 'MAR'
    MAS = 'MAS'
    MCD = 'MCD'
    MCHP = 'MCHP'
    MCK = 'MCK'
    MCO = 'MCO'
    MDLZ = 'MDLZ'
    MDT = 'MDT'
    MET = 'MET'
    MGM = 'MGM'
    MHK = 'MHK'
    MKC = 'MKC'
    MKTX = 'MKTX'
    MLM = 'MLM'
    MMC = 'MMC'
    MMM = 'MMM'
    MNST = 'MNST'
    MO = 'MO'
    MOS = 'MOS'
    MPC = 'MPC'
    MRK = 'MRK'
    MRO = 'MRO'
    MS = 'MS'
    MSCI = 'MSCI'
    MSFT = 'MSFT'
    MSI = 'MSI'
    MTB = 'MTB'
    MTD = 'MTD'
    MU = 'MU'
    MXIM = 'MXIM'
    MYL = 'MYL'
    NBL = 'NBL'
    NCLH = 'NCLH'
    NDAQ = 'NDAQ'
    NEE = 'NEE'
    NEM = 'NEM'
    NFLX = 'NFLX'
    NI = 'NI'
    NKE = 'NKE'
    NLOK = 'NLOK'
    NLSN = 'NLSN'
    NOC = 'NOC'
    NOV = 'NOV'
    NOW = 'NOW'
    NRG = 'NRG'
    NSC = 'NSC'
    NTAP = 'NTAP'
    NTRS = 'NTRS'
    NUE = 'NUE'
    NVDA = 'NVDA'
    NVR = 'NVR'
    NWL = 'NWL'
    NWS = 'NWS'
    NWSA = 'NWSA'
    O = 'O'
    ODFL = 'ODFL'
    OKE = 'OKE'
    OMC = 'OMC'
    ORCL = 'ORCL'
    ORLY = 'ORLY'
    OXY = 'OXY'
    PAYX = 'PAYX'
    PBCT = 'PBCT'
    PCAR = 'PCAR'
    PEAK = 'PEAK'
    PEG = 'PEG'
    PEP = 'PEP'
    PFE = 'PFE'
    PFG = 'PFG'
    PG = 'PG'
    PGR = 'PGR'
    PH = 'PH'
    PHM = 'PHM'
    PKG = 'PKG'
    PKI = 'PKI'
    PLD = 'PLD'
    PM = 'PM'
    PNC = 'PNC'
    PNR = 'PNR'
    PNW = 'PNW'
    PPG = 'PPG'
    PPL = 'PPL'
    PRGO = 'PRGO'
    PRU = 'PRU'
    PSA = 'PSA'
    PSX = 'PSX'
    PVH = 'PVH'
    PWR = 'PWR'
    PXD = 'PXD'
    PYPL = 'PYPL'
    QCOM = 'QCOM'
    QRVO = 'QRVO'
    RCL = 'RCL'
    RE = 'RE'
    REG = 'REG'
    REGN = 'REGN'
    RF = 'RF'
    RHI = 'RHI'
    RJF = 'RJF'
    RL = 'RL'
    RMD = 'RMD'
    ROK = 'ROK'
    ROL = 'ROL'
    ROP = 'ROP'
    ROST = 'ROST'
    RSG = 'RSG'
    RTN = 'RTN'
    SBAC = 'SBAC'
    SBUX = 'SBUX'
    SCHW = 'SCHW'
    SEE = 'SEE'
    SHW = 'SHW'
    SIVB = 'SIVB'
    SJM = 'SJM'
    SLB = 'SLB'
    SLG = 'SLG'
    SNA = 'SNA'
    SNPS = 'SNPS'
    SO = 'SO'
    SPG = 'SPG'
    SPGI = 'SPGI'
    SRE = 'SRE'
    STE = 'STE'
    STT = 'STT'
    STX = 'STX'
    STZ = 'STZ'
    SWK = 'SWK'
    SWKS = 'SWKS'
    SYF = 'SYF'
    SYK = 'SYK'
    SYY = 'SYY'
    T = 'T'
    TAP = 'TAP'
    TDG = 'TDG'
    TEL = 'TEL'
    TFC = 'TFC'
    TFX = 'TFX'
    TGT = 'TGT'
    TIF = 'TIF'
    TJX = 'TJX'
    TMO = 'TMO'
    TMUS = 'TMUS'
    TPR = 'TPR'
    TROW = 'TROW'
    TRV = 'TRV'
    TSCO = 'TSCO'
    TSN = 'TSN'
    TTWO = 'TTWO'
    TWTR = 'TWTR'
    TXN = 'TXN'
    TXT = 'TXT'
    UA = 'UA'
    UAA = 'UAA'
    UAL = 'UAL'
    UDR = 'UDR'
    UHS = 'UHS'
    ULTA = 'ULTA'
    UNH = 'UNH'
    UNM = 'UNM'
    UNP = 'UNP'
    UPS = 'UPS'
    URI = 'URI'
    USB = 'USB'
    UTX = 'UTX'
    V = 'V'
    VAR = 'VAR'
    VFC = 'VFC'
    VIAC = 'VIAC'
    VLO = 'VLO'
    VMC = 'VMC'
    VNO = 'VNO'
    VRSK = 'VRSK'
    VRSN = 'VRSN'
    VRTX = 'VRTX'
    VTR = 'VTR'
    VZ = 'VZ'
    WAB = 'WAB'
    WAT = 'WAT'
    WBA = 'WBA'
    WCG = 'WCG'
    WDC = 'WDC'
    WEC = 'WEC'
    WELL = 'WELL'
    WFC = 'WFC'
    WHR = 'WHR'
    WLTW = 'WLTW'
    WM = 'WM'
    WMB = 'WMB'
    WMT = 'WMT'
    WRB = 'WRB'
    WRK = 'WRK'
    WU = 'WU'
    WY = 'WY'
    WYNN = 'WYNN'
    XEC = 'XEC'
    XEL = 'XEL'
    XLNX = 'XLNX'
    XOM = 'XOM'
    XRAY = 'XRAY'
    XRX = 'XRX'
    XYL = 'XYL'
    YUM = 'YUM'
    ZBH = 'ZBH'
    ZBRA = 'ZBRA'
    ZION = 'ZION'
    ZTS = 'ZTS'


class EtfTickers(Tickers):
    ACES = 'ACES'
    ACT = 'ACT'
    AIQ = 'AIQ'
    AIRR = 'AIRR'
    AMJ = 'AMJ'
    AMJL = 'AMJL'
    AMLP = 'AMLP'
    AMU = 'AMU'
    AMUB = 'AMUB'
    AMZA = 'AMZA'
    ARKG = 'ARKG'
    ARKK = 'ARKK'
    ARKW = 'ARKW'
    ATMP = 'ATMP'
    BATT = 'BATT'
    BBC = 'BBC'
    BBH = 'BBH'
    BBP = 'BBP'
    BBRE = 'BBRE'
    BDCL = 'BDCL'
    BDCS = 'BDCS'
    BDCZ = 'BDCZ'
    BDRY = 'BDRY'
    BFIT = 'BFIT'
    BIB = 'BIB'
    BIS = 'BIS'
    BIZD = 'BIZD'
    BJK = 'BJK'
    BLCN = 'BLCN'
    BLOK = 'BLOK'
    BMLP = 'BMLP'
    BNKD = 'BNKD'
    BNKO = 'BNKO'
    BNKU = 'BNKU'
    BNKZ = 'BNKZ'
    BTEC = 'BTEC'
    BUG = 'BUG'
    BUYN = 'BUYN'
    CARZ = 'CARZ'
    CGW = 'CGW'
    CHIE = 'CHIE'
    CHIH = 'CHIH'
    CHII = 'CHII'
    CHIK = 'CHIK'
    CHIM = 'CHIM'
    CHIQ = 'CHIQ'
    CHIR = 'CHIR'
    CHIS = 'CHIS'
    CHIU = 'CHIU'
    CHIX = 'CHIX'
    CHNA = 'CHNA'
    CIBR = 'CIBR'
    CLIX = 'CLIX'
    CLOU = 'CLOU'
    CNBS = 'CNBS'
    CNCR = 'CNCR'
    CNRG = 'CNRG'
    COPX = 'COPX'
    CQQQ = 'CQQQ'
    CRAK = 'CRAK'
    CROP = 'CROP'
    CURE = 'CURE'
    CUT = 'CUT'
    CWEB = 'CWEB'
    DDG = 'DDG'
    DFEN = 'DFEN'
    DFNL = 'DFNL'
    DIET = 'DIET'
    DIG = 'DIG'
    DPST = 'DPST'
    DRIP = 'DRIP'
    DRN = 'DRN'
    DRV = 'DRV'
    DRW = 'DRW'
    DUG = 'DUG'
    DUSL = 'DUSL'
    DUST = 'DUST'
    EBIZ = 'EBIZ'
    ECLN = 'ECLN'
    ECON = 'ECON'
    EMCG = 'EMCG'
    EMIF = 'EMIF'
    EMLP = 'EMLP'
    EMQQ = 'EMQQ'
    EMTY = 'EMTY'
    ENFR = 'ENFR'
    ERUS = 'ERUS'
    ERX = 'ERX'
    ERY = 'ERY'
    ESPO = 'ESPO'
    EUFL = 'EUFL'
    EUFN = 'EUFN'
    EVX = 'EVX'
    EWRE = 'EWRE'
    EXI = 'EXI'
    FAN = 'FAN'
    FAS = 'FAS'
    FAZ = 'FAZ'
    FBT = 'FBT'
    FCG = 'FCG'
    FCOM = 'FCOM'
    FDIS = 'FDIS'
    FDN = 'FDN'
    FENY = 'FENY'
    FFR = 'FFR'
    FIDU = 'FIDU'
    FILL = 'FILL'
    FINU = 'FINU'
    FINX = 'FINX'
    FINZ = 'FINZ'
    FITE = 'FITE'
    FIVG = 'FIVG'
    FIW = 'FIW'
    FLM = 'FLM'
    FMAT = 'FMAT'
    FNCL = 'FNCL'
    FRAK = 'FRAK'
    FREL = 'FREL'
    FRI = 'FRI'
    FSTA = 'FSTA'
    FTAG = 'FTAG'
    FTEC = 'FTEC'
    FTRI = 'FTRI'
    FTXD = 'FTXD'
    FTXG = 'FTXG'
    FTXH = 'FTXH'
    FTXL = 'FTXL'
    FTXN = 'FTXN'
    FTXO = 'FTXO'
    FTXR = 'FTXR'
    FUTY = 'FUTY'
    FXD = 'FXD'
    FXG = 'FXG'
    FXH = 'FXH'
    FXL = 'FXL'
    FXN = 'FXN'
    FXO = 'FXO'
    FXR = 'FXR'
    FXU = 'FXU'
    FXZ = 'FXZ'
    GAMR = 'GAMR'
    GASL = 'GASL'
    GASX = 'GASX'
    GDAT = 'GDAT'
    GDNA = 'GDNA'
    GDX = 'GDX'
    GDXJ = 'GDXJ'
    GII = 'GII'
    GLIF = 'GLIF'
    GNOM = 'GNOM'
    GNR = 'GNR'
    GOAU = 'GOAU'
    GOEX = 'GOEX'
    GQRE = 'GQRE'
    GREK = 'GREK'
    GRES = 'GRES'
    GRID = 'GRID'
    GUNR = 'GUNR'
    GUSH = 'GUSH'
    HACK = 'HACK'
    HAIL = 'HAIL'
    HAP = 'HAP'
    HAUZ = 'HAUZ'
    HDGE = 'HDGE'
    HII = 'HII'
    HMT = 'HMT'
    HOML = 'HOML'
    HOMZ = 'HOMZ'
    HTEC = 'HTEC'
    IAI = 'IAI'
    IAK = 'IAK'
    IAT = 'IAT'
    IBB = 'IBB'
    IBUY = 'IBUY'
    ICF = 'ICF'
    ICLN = 'ICLN'
    IDNA = 'IDNA'
    IDU = 'IDU'
    IECS = 'IECS'
    IEDI = 'IEDI'
    IEFN = 'IEFN'
    IEHS = 'IEHS'
    IEIH = 'IEIH'
    IEME = 'IEME'
    IEO = 'IEO'
    IETC = 'IETC'
    IEUS = 'IEUS'
    IEV = 'IEV'
    IEZ = 'IEZ'
    IFEU = 'IFEU'
    IFGL = 'IFGL'
    IFRA = 'IFRA'
    IGE = 'IGE'
    IGF = 'IGF'
    IGM = 'IGM'
    IGN = 'IGN'
    IGV = 'IGV'
    IHAK = 'IHAK'
    IHE = 'IHE'
    IHF = 'IHF'
    IHI = 'IHI'
    IMLP = 'IMLP'
    INCO = 'INCO'
    INDS = 'INDS'
    INFR = 'INFR'
    IPAY = 'IPAY'
    IRBO = 'IRBO'
    ISRA = 'ISRA'
    ITA = 'ITA'
    ITB = 'ITB'
    ITEQ = 'ITEQ'
    IXC = 'IXC'
    IXG = 'IXG'
    IXJ = 'IXJ'
    IXN = 'IXN'
    IXP = 'IXP'
    IYC = 'IYC'
    IYE = 'IYE'
    IYF = 'IYF'
    IYG = 'IYG'
    IYH = 'IYH'
    IYJ = 'IYJ'
    IYK = 'IYK'
    IYM = 'IYM'
    IYR = 'IYR'
    IYT = 'IYT'
    IYW = 'IYW'
    IYZ = 'IYZ'
    IZRL = 'IZRL'
    JDST = 'JDST'
    JETS = 'JETS'
    JHMA = 'JHMA'
    JHMC = 'JHMC'
    JHME = 'JHME'
    JHMF = 'JHMF'
    JHMH = 'JHMH'
    JHMI = 'JHMI'
    JHMS = 'JHMS'
    JHMU = 'JHMU'
    JNUG = 'JNUG'
    JXI = 'JXI'
    KBE = 'KBE'
    KBWB = 'KBWB'
    KBWD = 'KBWD'
    KBWP = 'KBWP'
    KBWR = 'KBWR'
    KBWY = 'KBWY'
    KCE = 'KCE'
    KIE = 'KIE'
    KMED = 'KMED'
    KNAB = 'KNAB'
    KOIN = 'KOIN'
    KOL = 'KOL'
    KRE = 'KRE'
    KURE = 'KURE'
    KWEB = 'KWEB'
    KXI = 'KXI'
    LABD = 'LABD'
    LABU = 'LABU'
    LACK = 'LACK'
    LBDC = 'LBDC'
    LEGR = 'LEGR'
    LEND = 'LEND'
    LIT = 'LIT'
    LMLP = 'LMLP'
    LNGR = 'LNGR'
    LOUP = 'LOUP'
    LRET = 'LRET'
    LTL = 'LTL'
    MLPA = 'MLPA'
    MLPB = 'MLPB'
    MLPC = 'MLPC'
    MLPE = 'MLPE'
    MLPG = 'MLPG'
    MLPI = 'MLPI'
    MLPO = 'MLPO'
    MLPQ = 'MLPQ'
    MLPX = 'MLPX'
    MLPY = 'MLPY'
    MLPZ = 'MLPZ'
    MOO = 'MOO'
    MORL = 'MORL'
    MORT = 'MORT'
    MRRL = 'MRRL'
    MXI = 'MXI'
    NAIL = 'NAIL'
    NANR = 'NANR'
    NEED = 'NEED'
    NERD = 'NERD'
    NETL = 'NETL'
    NFRA = 'NFRA'
    NLR = 'NLR'
    NRGD = 'NRGD'
    NRGO = 'NRGO'
    NRGU = 'NRGU'
    NRGZ = 'NRGZ'
    NUGT = 'NUGT'
    NURE = 'NURE'
    NXTG = 'NXTG'
    OGIG = 'OGIG'
    OIH = 'OIH'
    OLD = 'OLD'
    ONLN = 'ONLN'
    ORG = 'ORG'
    PASS = 'PASS'
    PAVE = 'PAVE'
    PBD = 'PBD'
    PBE = 'PBE'
    PBJ = 'PBJ'
    PBS = 'PBS'
    PBW = 'PBW'
    PEJ = 'PEJ'
    PEX = 'PEX'
    PEZ = 'PEZ'
    PFI = 'PFI'
    PHDG = 'PHDG'
    PHO = 'PHO'
    PICK = 'PICK'
    PILL = 'PILL'
    PIO = 'PIO'
    PJP = 'PJP'
    PKB = 'PKB'
    PMR = 'PMR'
    PNQI = 'PNQI'
    POTX = 'POTX'
    PPA = 'PPA'
    PPH = 'PPH'
    PPLN = 'PPLN'
    PPTY = 'PPTY'
    PRN = 'PRN'
    PRNT = 'PRNT'
    PSCC = 'PSCC'
    PSCD = 'PSCD'
    PSCE = 'PSCE'
    PSCF = 'PSCF'
    PSCH = 'PSCH'
    PSCI = 'PSCI'
    PSCM = 'PSCM'
    PSCT = 'PSCT'
    PSCU = 'PSCU'
    PSI = 'PSI'
    PSJ = 'PSJ'
    PSL = 'PSL'
    PSP = 'PSP'
    PSR = 'PSR'
    PTF = 'PTF'
    PTH = 'PTH'
    PUI = 'PUI'
    PXE = 'PXE'
    PXI = 'PXI'
    PXJ = 'PXJ'
    PXQ = 'PXQ'
    PYPE = 'PYPE'
    PYZ = 'PYZ'
    PZD = 'PZD'
    QABA = 'QABA'
    QCLN = 'QCLN'
    QQQ = 'QQQ'
    QTEC = 'QTEC'
    QTUM = 'QTUM'
    RCD = 'RCD'
    REET = 'REET'
    REK = 'REK'
    REM = 'REM'
    REML = 'REML'
    REMX = 'REMX'
    RETL = 'RETL'
    REW = 'REW'
    REZ = 'REZ'
    RFEU = 'RFEU'
    RGI = 'RGI'
    RHS = 'RHS'
    RING = 'RING'
    ROBO = 'ROBO'
    ROKT = 'ROKT'
    ROM = 'ROM'
    ROOF = 'ROOF'
    RORE = 'RORE'
    RTH = 'RTH'
    RTL = 'RTL'
    RTM = 'RTM'
    RWO = 'RWO'
    RWR = 'RWR'
    RWW = 'RWW'
    RWX = 'RWX'
    RXD = 'RXD'
    RXI = 'RXI'
    RXL = 'RXL'
    RYE = 'RYE'
    RYF = 'RYF'
    RYH = 'RYH'
    RYT = 'RYT'
    RYU = 'RYU'
    SBIO = 'SBIO'
    SBM = 'SBM'
    SCC = 'SCC'
    SCHH = 'SCHH'
    SCID = 'SCID'
    SDP = 'SDP'
    SEA = 'SEA'
    SEF = 'SEF'
    SGDJ = 'SGDJ'
    SGDM = 'SGDM'
    SIJ = 'SIJ'
    SIL = 'SIL'
    SILJ = 'SILJ'
    SIMS = 'SIMS'
    SKF = 'SKF'
    SKYY = 'SKYY'
    SLIM = 'SLIM'
    SLVP = 'SLVP'
    SLX = 'SLX'
    SMH = 'SMH'
    SMN = 'SMN'
    SMOG = 'SMOG'
    SNSR = 'SNSR'
    SOCL = 'SOCL'
    SOIL = 'SOIL'
    SOXL = 'SOXL'
    SOXS = 'SOXS'
    SOXX = 'SOXX'
    SRET = 'SRET'
    SRS = 'SRS'
    SRVR = 'SRVR'
    SSG = 'SSG'
    SZK = 'SZK'
    TAN = 'TAN'
    TAO = 'TAO'
    TAWK = 'TAWK'
    TBLU = 'TBLU'
    TCLD = 'TCLD'
    TDIV = 'TDIV'
    TDV = 'TDV'
    TECL = 'TECL'
    TECS = 'TECS'
    TOLZ = 'TOLZ'
    TPAY = 'TPAY'
    TPOR = 'TPOR'
    TPYP = 'TPYP'
    UBIO = 'UBIO'
    UCC = 'UCC'
    UGE = 'UGE'
    UPW = 'UPW'
    URA = 'URA'
    URE = 'URE'
    USAI = 'USAI'
    USD = 'USD'
    USRT = 'USRT'
    UTES = 'UTES'
    UTSL = 'UTSL'
    UXI = 'UXI'
    UYG = 'UYG'
    UYM = 'UYM'
    VAW = 'VAW'
    VCR = 'VCR'
    VDC = 'VDC'
    VDE = 'VDE'
    VEGI = 'VEGI'
    VFH = 'VFH'
    VGT = 'VGT'
    VHT = 'VHT'
    VIDG = 'VIDG'
    VIS = 'VIS'
    VMOT = 'VMOT'
    VNQ = 'VNQ'
    VNQI = 'VNQI'
    VOX = 'VOX'
    VPC = 'VPC'
    VPU = 'VPU'
    VQT = 'VQT'
    VRAI = 'VRAI'
    WANT = 'WANT'
    WBIE = 'WBIE'
    WBIF = 'WBIF'
    WBIL = 'WBIL'
    WCLD = 'WCLD'
    WDRW = 'WDRW'
    WOOD = 'WOOD'
    WPS = 'WPS'
    XAR = 'XAR'
    XBI = 'XBI'
    XBUY = 'XBUY'
    XES = 'XES'
    XHB = 'XHB'
    XHE = 'XHE'
    XHS = 'XHS'
    XITK = 'XITK'
    XLB = 'XLB'
    XLC = 'XLC'
    XLE = 'XLE'
    XLEY = 'XLEY'
    XLF = 'XLF'
    XLI = 'XLI'
    XLK = 'XLK'
    XLP = 'XLP'
    XLRE = 'XLRE'
    XLTY = 'XLTY'
    XLU = 'XLU'
    XLUY = 'XLUY'
    XLV = 'XLV'
    XLY = 'XLY'
    XME = 'XME'
    XNTK = 'XNTK'
    XOP = 'XOP'
    XPH = 'XPH'
    XRT = 'XRT'
    XSD = 'XSD'
    XSW = 'XSW'
    XT = 'XT'
    XTH = 'XTH'
    XTL = 'XTL'
    XTN = 'XTN'
    XWEB = 'XWEB'
    YGRN = 'YGRN'
    YLCO = 'YLCO'
    YOLO = 'YOLO'
    ZBIO = 'ZBIO'
    ZIG = 'ZIG'
    ZMLP = 'ZMLP'