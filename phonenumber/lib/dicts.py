#!/usr/bin/env python

phonenumber_types = {
        0:'FIXED_LINE',
        1:'MOBILE',
        2:'FIXED_LINE_OR_MOBILE',
        3:'TOLL_FREE',
        4:'PREMIUM_RATE',
        5:'SHARED_COST',
        6:'VOIP',
        7:'PERSONAL_NUMBER',
        8:'PAGER',
        9:'UAN',
        10:'VOICEMAIL',
        99:'UNKNOWN'
        }

country_iso2to3 = {
    'AS': 'ASM',
    'AI': 'AIA',
    'AG': 'ATG',
    'BS': 'BHS',
    'BB': 'BRB',
    'BM': 'BMU',
    'VG': 'VGB',
    'KY': 'CYM',
    'DM': 'DMA',
    'DO': 'DOM',
    'GD': 'GRD',
    'GU': 'GUM',
    'JM': 'JAM',
    'MS': 'MSR',
    'MP': 'MNP',
    'KN': 'KNA',
    'LC': 'LCA',
    'MF': 'MAF',
    'VC': 'VCT',
    'TT': 'TTO',
    'TC': 'TCA',
    'VI': 'VIR',
    'AL': 'ALB',
    'DZ': 'DZA',
    'AD': 'AND',
    'AO': 'AGO',
    'AQ': 'ATA',
    'AM': 'ARM',
    'AW': 'ABW',
    'AZ': 'AZE',
    'BH': 'BHR',
    'BD': 'BGD',
    'BY': 'BLR',
    'BZ': 'BLZ',
    'BJ': 'BEN',
    'BT': 'BTN',
    'BO': 'BOL',
    'BA': 'BIH',
    'BW': 'BWA',
    'BN': 'BRN',
    'BG': 'BGR',
    'BF': 'BFA',
    'BI': 'BDI',
    'KH': 'KHM',
    'CM': 'CMR',
    'CV': 'CPV',
    'CF': 'CAF',
    'TD': 'TCD',
    'KM': 'COM',
    'CK': 'COK',
    'CR': 'CRC',
    'HR': 'HRV',
    'CY': 'CYP',
    'CZ': 'CZE',
    'CD': 'COD',
    'DJ': 'DJI',
    'EC': 'ECU',
    'SV': 'SLV',
    'GQ': 'GNQ',
    'ER': 'ERI',
    'EE': 'EST',
    'ET': 'ETH',
    'FK': 'FLK',
    'FO': 'FRO',
    'FJ': 'FJI',
    'FI': 'FIN',
    'PF': 'PYF',
    'GA': 'GAB',
    'GM': 'GMB',
    'GE': 'GEO',
    'GH': 'GHA',
    'GI': 'GIB',
    'GL': 'GRL',
    'GT': 'GTM',
    'GN': 'GIN',
    'GW': 'GNB',
    'GY': 'GUY',
    'HT': 'HTI',
    'HN': 'HND',
    'HK': 'HKG',
    'IS': 'IS',
    'IQ': 'IRQ',
    'IE': 'IRL',
    'IL': 'ISR',
    'CI': 'CIV',
    'JO': 'JOR',
    'KE': 'KEN',
    'KI': 'KIR',
    'KW': 'KWT',
    'KG': 'KGZ',
    'LA': 'LAO',
    'LV': 'LVA',
    'LB': 'LBN',
    'LS': 'LSO',
    'LR': 'LBR',
    'LY': 'LBY',
    'LI': 'LIE',
    'LT': 'LTU',
    'LU': 'LUX',
    'MO': 'MAC',
    'MK': 'MKD',
    'MG': 'MDG',
    'MW': 'MWI',
    'MV': 'MDV',
    'ML': 'MLI',
    'MT': 'MLT',
    'MH': 'MHL',
    'MR': 'MRT',
    'MU': 'MUS',
    'YT': 'MYT',
    'FM': 'FSM',
    'MD': 'MDA',
    'MC': 'MCO',
    'MN': 'MNG',
    'ME': 'MNE',
    'MA': 'MAR',
    'MZ': 'MOZ',
    'NA': 'NAM',
    'NR': 'NRU',
    'NP': 'NPL',
    'AN': 'ANT',
    'NC': 'NCL',
    'NI': 'NIC',
    'NE': 'NER',
    'NG': 'NGA',
    'NU': 'NIU',
    'KP': 'PRK',
    'OM': 'OMN',
    'PW': 'PLW',
    'PA': 'PAN',
    'PG': 'PNG',
    'PY': 'PRY',
    'PN': 'PCN',
    'PT': 'PRT',
    'QA': 'QAT',
    'CG': 'COG',
    'RW': 'RWA',
    'BL': 'BLM',
    'SH': 'SHN',
    'PM': 'SPM',
    'WS': 'WSM',
    'SM': 'SMR',
    'ST': 'STP',
    'SA': 'SAU',
    'SN': 'SEN',
    'RS': 'SRB',
    'SC': 'SYC',
    'SL': 'SLE',
    'SK': 'SVK',
    'SI': 'SVN',
    'SB': 'SLB',
    'SO': 'SOM',
    'SD': 'SDN',
    'SR': 'SUR',
    'SZ': 'SWZ',
    'SY': 'SYR',
    'TW': 'TWN',
    'TJ': 'TJK',
    'TZ': 'TZA',
    'TL': 'TLS',
    'TG': 'TGO',
    'TK': 'TKL',
    'TO': 'TON',
    'TN': 'TUN',
    'TM': 'TKM',
    'TV': 'TUV',
    'UG': 'UGA',
    'UA': 'UKR',
    'AE': 'ARE',
    'UY': 'URY',
    'UZ': 'UZB',
    'VU': 'VUT',
    'WF': 'WLF',
    'EH': 'ESH',
    'YE': 'YEM',
    'ZM': 'ZMB',
    'ZW': 'ZWE',
    'AF': 'AFG',
    'AR': 'ARG',
    'AU': 'AUS',
    'AT': 'AUT',
    'BE': 'BEL',
    'BR': 'BRA',
    'MM': 'MMR',
    'CL': 'CHL',
    'CN': 'CHN',
    'CX': 'CXR',
    'CC': 'CCK',
    'CO': 'COL',
    'CU': 'CUB',
    'DK': 'DNK',
    'EG': 'EGY',
    'FR': 'FRA',
    'DE': 'DEU',
    'GR': 'GRC',
    'VA': 'VAT',
    'HU': 'HUN',
    'IN': 'IND',
    'ID': 'IDN',
    'IR': 'IRN',
    'IM': 'IMN',
    'IT': 'ITA',
    'JP': 'JPN',
    'MY': 'MYS',
    'MX': 'MEX',
    'NL': 'NLD',
    'NZ': 'NZL',
    'NO': 'NOR',
    'PK': 'PAK',
    'PE': 'PER',
    'PH': 'PHL',
    'PL': 'POL',
    'RO': 'ROU',
    'SG': 'SGP',
    'ZA': 'ZAF',
    'KR': 'KOR',
    'ES': 'ESP',
    'LK': 'LKA',
    'SE': 'SWE',
    'CH': 'CHE',
    'TH': 'THA',
    'TR': 'TUR',
    'GB': 'GBR',
    'VE': 'VEN',
    'VN': 'VNM',
    'CA': 'CAN',
    'KZ': 'KAZ',
    'PR': 'PRI',
    'RU': 'RUS',
    'US': 'USA'        
        }
    