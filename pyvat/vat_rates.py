#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from decimal import Decimal

from .item_type import ItemType

# http://ec.europa.eu/taxation_customs/tic/public/vatRates/vatratesSearch.html
VAT_RATES = {
    'AT': [{
        'valid_from': datetime.date(2002, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('20.0')
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('20.0'),
            ItemType.generic_electronic_service: Decimal('20.0'),
            ItemType.generic_telecommunications_service: Decimal('20.0'),
            ItemType.generic_broadcasting_service: Decimal('20.0'),
            ItemType.prepaid_broadcasting_service: Decimal('10.0'),
            ItemType.ebook: Decimal('20.0'),
            ItemType.enewspaper: Decimal('20.0')
        }
    }],
    'BE': [{
        'valid_from': datetime.date(2002, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('21.0')
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('21.0'),
            ItemType.generic_electronic_service: Decimal('21.0'),
            ItemType.generic_telecommunications_service: Decimal('21.0'),
            ItemType.generic_broadcasting_service: Decimal('21.0'),
            ItemType.prepaid_broadcasting_service: Decimal('21.0'),
            ItemType.ebook: Decimal('21.0'),
            ItemType.enewspaper: Decimal('21.0')
        }
    }],
    'BG': [{
        'valid_from': datetime.date(2002, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('20.0')
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('20.0'),
            ItemType.generic_electronic_service: Decimal('20.0'),
            ItemType.generic_telecommunications_service: Decimal('20.0'),
            ItemType.generic_broadcasting_service: Decimal('20.0'),
            ItemType.prepaid_broadcasting_service: Decimal('20.0'),
            ItemType.ebook: Decimal('20.0'),
            ItemType.enewspaper: Decimal('20.0')
        }
    }],
    'CY': [{
        'valid_from': datetime.date(2014, 1, 13),
        'rates': {
            ItemType.generic_physical_good: Decimal('19.0'),
            ItemType.generic_electronic_service: Decimal('19.0'),
            ItemType.generic_telecommunications_service: Decimal('19.0'),
            ItemType.generic_broadcasting_service: Decimal('19.0'),
            ItemType.prepaid_broadcasting_service: Decimal('19.0'),
            ItemType.ebook: Decimal('19.0'),
            ItemType.enewspaper: Decimal('19.0')
        }
    }],
    'CZ': [{
        'valid_from': datetime.date(2013, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('21.0')
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('21.0'),
            ItemType.generic_electronic_service: Decimal('21.0'),
            ItemType.generic_telecommunications_service: Decimal('21.0'),
            ItemType.generic_broadcasting_service: Decimal('21.0'),
            ItemType.prepaid_broadcasting_service: Decimal('21.0'),
            ItemType.ebook: Decimal('21.0'),
            ItemType.enewspaper: Decimal('21.0')
        }
    }],
    'DE': [{
        'valid_from': datetime.date(2007, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('19.0'),
            ItemType.generic_electronic_service: Decimal('19.0'),
            ItemType.generic_telecommunications_service: Decimal('19.0'),
            ItemType.generic_broadcasting_service: Decimal('19.0'),
            ItemType.prepaid_broadcasting_service: Decimal('19.0'),
            ItemType.ebook: Decimal('19.0'),
            ItemType.enewspaper: Decimal('19.0')
        }
    }],
    'DK': [{
        'valid_from': datetime.date(2002, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('25.0'),
            ItemType.generic_electronic_service: Decimal('25.0'),
            ItemType.generic_telecommunications_service: Decimal('25.0'),
            ItemType.generic_broadcasting_service: Decimal('25.0'),
            ItemType.prepaid_broadcasting_service: Decimal('25.0'),
            ItemType.ebook: Decimal('25.0'),
            ItemType.enewspaper: Decimal('25.0')
        }
    }],
    'EE': [{
        'valid_from': datetime.date(2009, 7, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('20.0'),
            ItemType.generic_electronic_service: Decimal('20.0'),
            ItemType.generic_telecommunications_service: Decimal('20.0'),
            ItemType.generic_broadcasting_service: Decimal('20.0'),
            ItemType.prepaid_broadcasting_service: Decimal('20.0'),
            ItemType.ebook: Decimal('20.0'),
            ItemType.enewspaper: Decimal('20.0')
        }
    }],
    'ES': [{
        'valid_from': datetime.date(2012, 9, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('21.0')
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('21.0'),
            ItemType.generic_electronic_service: Decimal('21.0'),
            ItemType.generic_telecommunications_service: Decimal('21.0'),
            ItemType.generic_broadcasting_service: Decimal('21.0'),
            ItemType.prepaid_broadcasting_service: Decimal('21.0'),
            ItemType.ebook: Decimal('21.0'),
            ItemType.enewspaper: Decimal('21.0')
        }
    }],
    'FI': [{
        'valid_from': datetime.date(2013, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('24.0'),
            ItemType.generic_electronic_service: Decimal('24.0'),
            ItemType.generic_telecommunications_service: Decimal('24.0'),
            ItemType.generic_broadcasting_service: Decimal('24.0'),
            ItemType.prepaid_broadcasting_service: Decimal('24.0'),
            ItemType.ebook: Decimal('24.0'),
            ItemType.enewspaper: Decimal('24.0')
        }
    }],
    'FR': [{
        'valid_from': datetime.date(2014, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('20.0'),
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('20.0'),
            ItemType.generic_electronic_service: Decimal('20.0'),
            ItemType.generic_telecommunications_service: Decimal('20.0'),
            ItemType.ebook: Decimal('5.5'),
            ItemType.enewspaper: Decimal('2.1'),
            ItemType.generic_broadcasting_service: Decimal('10.0'),
            ItemType.prepaid_broadcasting_service: Decimal('10.0'),
        }
    }],
    'GB': [{
        'valid_from': datetime.date(2011, 1, 4),
        'rates': {
            ItemType.generic_physical_good: Decimal('20.0')
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('20.0'),
            ItemType.generic_electronic_service: Decimal('20.0'),
            ItemType.generic_telecommunications_service: Decimal('20.0'),
            ItemType.generic_broadcasting_service: Decimal('20.0'),
            ItemType.prepaid_broadcasting_service: Decimal('20.0'),
            ItemType.ebook: Decimal('20.0'),
            ItemType.enewspaper: Decimal('20.0')
        }
    }],
    'GR': [{
        'valid_from': datetime.date(2010, 7, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('23.0'),
            ItemType.generic_electronic_service: Decimal('23.0'),
            ItemType.generic_telecommunications_service: Decimal('23.0'),
            ItemType.generic_broadcasting_service: Decimal('23.0'),
            ItemType.prepaid_broadcasting_service: Decimal('23.0'),
            ItemType.ebook: Decimal('23.0'),
            ItemType.enewspaper: Decimal('23.0')
        }
    }, {
        'valid_from': datetime.date(2016, 6, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('24.0'),
            ItemType.generic_electronic_service: Decimal('24.0'),
            ItemType.generic_telecommunications_service: Decimal('24.0'),
            ItemType.generic_broadcasting_service: Decimal('24.0'),
            ItemType.prepaid_broadcasting_service: Decimal('24.0'),
            ItemType.ebook: Decimal('24.0'),
            ItemType.enewspaper: Decimal('24.0')
        }
    }],
    'HR': [{
        'valid_from': datetime.date(2012, 3, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('25.0'),
            ItemType.generic_electronic_service: Decimal('25.0'),
            ItemType.generic_telecommunications_service: Decimal('25.0'),
            ItemType.generic_broadcasting_service: Decimal('25.0'),
            ItemType.prepaid_broadcasting_service: Decimal('25.0'),
            ItemType.ebook: Decimal('25.0'),
            ItemType.enewspaper: Decimal('25.0')
        }
    }],
    'HU': [{
        'valid_from': datetime.date(2012, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('27.0'),
            ItemType.generic_electronic_service: Decimal('27.0'),
            ItemType.generic_telecommunications_service: Decimal('27.0'),
            ItemType.generic_broadcasting_service: Decimal('27.0'),
            ItemType.prepaid_broadcasting_service: Decimal('27.0'),
            ItemType.ebook: Decimal('27.0'),
            ItemType.enewspaper: Decimal('27.0')
        }
    }],
    'IE': [{
        'valid_from': datetime.date(2012, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('23.0')
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('23.0'),
            ItemType.generic_electronic_service: Decimal('23.0'),
            ItemType.generic_telecommunications_service: Decimal('23.0'),
            ItemType.generic_broadcasting_service: Decimal('23.0'),
            ItemType.prepaid_broadcasting_service: Decimal('23.0'),
            ItemType.ebook: Decimal('23.0'),
            ItemType.enewspaper: Decimal('23.0')
        }
    }],
    'IT': [{
        'valid_from': datetime.date(2013, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('22.0'),
            ItemType.generic_electronic_service: Decimal('22.0'),
            ItemType.generic_telecommunications_service: Decimal('22.0'),
            ItemType.generic_broadcasting_service: Decimal('22.0'),
            ItemType.prepaid_broadcasting_service: Decimal('22.0'),
            ItemType.ebook: Decimal('22.0'),
            ItemType.enewspaper: Decimal('22.0')
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('22.0'),
            ItemType.generic_electronic_service: Decimal('22.0'),
            ItemType.generic_telecommunications_service: Decimal('22.0'),
            ItemType.generic_broadcasting_service: Decimal('22.0'),
            ItemType.ebook: Decimal('4.0'),
            ItemType.prepaid_broadcasting_service: Decimal('22.0'),
            ItemType.enewspaper: Decimal('22.0')
        }
    }],
    'LT': [{
        'valid_from': datetime.date(2009, 9, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('21.0')
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('21.0'),
            ItemType.generic_electronic_service: Decimal('21.0'),
            ItemType.generic_telecommunications_service: Decimal('21.0'),
            ItemType.generic_broadcasting_service: Decimal('21.0'),
            ItemType.prepaid_broadcasting_service: Decimal('21.0'),
            ItemType.ebook: Decimal('21.0'),
            ItemType.enewspaper: Decimal('21.0')
        }
    }],
    'LU': [{
        'valid_from': datetime.date(2006, 1, 1),
        'rates': {
            ItemType.ebook: Decimal('3.0'),
            ItemType.generic_broadcasting_service: Decimal('3.0'),
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('17.0'),
            ItemType.generic_electronic_service: Decimal('17.0'),
            ItemType.ebook: Decimal('17.0'),
            ItemType.generic_telecommunications_service: Decimal('17.0'),
            ItemType.generic_broadcasting_service: Decimal('3.0'),
            ItemType.prepaid_broadcasting_service: Decimal('3.0'),
            ItemType.ebook: Decimal('17.0'),
            ItemType.enewspaper: Decimal('17.0')
        }
    }],
    'LV': [{
        'valid_from': datetime.date(2012, 7, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('21.0')
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('21.0'),
            ItemType.generic_electronic_service: Decimal('21.0'),
            ItemType.generic_telecommunications_service: Decimal('21.0'),
            ItemType.generic_broadcasting_service: Decimal('21.0'),
            ItemType.prepaid_broadcasting_service: Decimal('21.0'),
            ItemType.ebook: Decimal('21.0'),
            ItemType.enewspaper: Decimal('21.0')
        }
    }],
    'MT': [{
        'valid_from': datetime.date(2002, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('18.0')
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('18.0'),
            ItemType.generic_electronic_service: Decimal('18.0'),
            ItemType.generic_telecommunications_service: Decimal('18.0'),
            ItemType.generic_broadcasting_service: Decimal('18.0'),
            ItemType.prepaid_broadcasting_service: Decimal('18.0'),
            ItemType.ebook: Decimal('18.0'),
            ItemType.enewspaper: Decimal('18.0')
        }
    }],
    'NL': [{
        'valid_from': datetime.date(2012, 10, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('21.0')
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('21.0'),
            ItemType.generic_electronic_service: Decimal('21.0'),
            ItemType.generic_telecommunications_service: Decimal('21.0'),
            ItemType.generic_broadcasting_service: Decimal('21.0'),
            ItemType.prepaid_broadcasting_service: Decimal('21.0'),
            ItemType.ebook: Decimal('21.0'),
            ItemType.enewspaper: Decimal('21.0')
        }
    }],
    'PL': [{
        'valid_from': datetime.date(2011, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('23.0'),
            ItemType.generic_electronic_service: Decimal('23.0'),
            ItemType.generic_telecommunications_service: Decimal('23.0'),
            ItemType.generic_broadcasting_service: Decimal('8.0'),
            ItemType.prepaid_broadcasting_service: Decimal('8.0'),
            ItemType.ebook: Decimal('23.0'),
            ItemType.enewspaper: Decimal('23.0')
        }
    }],
    'PT': [{
        'valid_from': datetime.date(2011, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('23.0')
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('23.0'),
            ItemType.generic_electronic_service: Decimal('23.0'),
            ItemType.generic_telecommunications_service: Decimal('23.0'),
            ItemType.generic_broadcasting_service: Decimal('23.0'),
            ItemType.prepaid_broadcasting_service: Decimal('23.0'),
            ItemType.ebook: Decimal('23.0'),
            ItemType.enewspaper: Decimal('23.0')
        }
    }],
    'RO': [{
        'valid_from': datetime.date(2010, 7, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('24.0'),
            ItemType.generic_electronic_service: Decimal('24.0'),
            ItemType.generic_telecommunications_service: Decimal('24.0'),
            ItemType.generic_broadcasting_service: Decimal('24.0'),
            ItemType.prepaid_broadcasting_service: Decimal('24.0'),
            ItemType.ebook: Decimal('24.0'),
            ItemType.enewspaper: Decimal('24.0')
        }
    }, {
        'valid_from': datetime.date(2016, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('20.0'),
            ItemType.generic_electronic_service: Decimal('20.0'),
            ItemType.generic_telecommunications_service: Decimal('20.0'),
            ItemType.generic_broadcasting_service: Decimal('20.0'),
            ItemType.prepaid_broadcasting_service: Decimal('20.0'),
            ItemType.ebook: Decimal('20.0'),
            ItemType.enewspaper: Decimal('20.0')
        }
    }, {
        'valid_from': datetime.date(2017, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('19.0'),
            ItemType.generic_electronic_service: Decimal('19.0'),
            ItemType.generic_telecommunications_service: Decimal('19.0'),
            ItemType.generic_broadcasting_service: Decimal('19.0'),
            ItemType.prepaid_broadcasting_service: Decimal('19.0'),
            ItemType.ebook: Decimal('19.0'),
            ItemType.enewspaper: Decimal('19.0')
        }
    }],
    'SE': [{
        'valid_from': datetime.date(2002, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('25.0')
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('25.0'),
            ItemType.generic_electronic_service: Decimal('25.0'),
            ItemType.generic_telecommunications_service: Decimal('25.0'),
            ItemType.generic_broadcasting_service: Decimal('25.0'),
            ItemType.prepaid_broadcasting_service: Decimal('25.0'),
            ItemType.ebook: Decimal('25.0'),
            ItemType.enewspaper: Decimal('25.0')
        }
    }],
    'SI': [{
        'valid_from': datetime.date(2013, 7, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('22.0'),
            ItemType.generic_electronic_service: Decimal('22.0'),
            ItemType.generic_telecommunications_service: Decimal('22.0'),
            ItemType.generic_broadcasting_service: Decimal('22.0'),
            ItemType.prepaid_broadcasting_service: Decimal('22.0'),
            ItemType.ebook: Decimal('22.0'),
            ItemType.enewspaper: Decimal('22.0')
        }
    }],
    'SK': [{
        'valid_from': datetime.date(2010, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('20.0')
        }
    }, {
        'valid_from': datetime.date(2015, 1, 1),
        'rates': {
            ItemType.generic_physical_good: Decimal('20.0'),
            ItemType.generic_electronic_service: Decimal('20.0'),
            ItemType.generic_telecommunications_service: Decimal('20.0'),
            ItemType.generic_broadcasting_service: Decimal('20.0'),
            ItemType.prepaid_broadcasting_service: Decimal('20.0'),
            ItemType.ebook: Decimal('20.0'),
            ItemType.enewspaper: Decimal('20.0')
        }
    }]
}
