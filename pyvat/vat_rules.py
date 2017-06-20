import datetime
from .countries import EU_COUNTRY_CODES
from .vat_charge import VatCharge, VatChargeAction
from .vat_rates import VAT_RATES


JANUARY_1_2015 = datetime.date(2015, 1, 1)


class VatRules(object):
    """Base VAT rules for a country.
    """

    def get_vat_rate(self, item_type):
        """Get the VAT rate for an item type.

        :param item_type: Item type.
        :type item_type: ItemType
        :returns: the VAT rate in percent.
        :rtype: decimal.Decimal
        """

        raise NotImplementedError()

    def get_sale_to_country_vat_charge(self,
                                       date,
                                       item_type,
                                       buyer,
                                       seller):
        """Get the VAT charge for selling an item to a buyer in the country.

        :param date: Sale date.
        :type date: datetime.date
        :param item_type: Type of the item being sold.
        :type item_type: ItemType
        :param buyer: Buyer.
        :type buyer: Party
        :param seller: Seller.
        :type seller: Party
        :rtype: VatCharge
        :raises NotImplementedError:
            if no explicit rules for selling to the given country from the
            given country exist. VAT charge determining falls back to testing
            rules for the country in which the seller resides if this is
            raised.
        """

        raise NotImplementedError()

    def get_sale_from_country_vat_charge(self,
                                         date,
                                         item_type,
                                         buyer,
                                         seller):
        """Get the VAT charge for selling an item as a seller in the country.

        :param date: Sale date.
        :type date: datetime.date
        :param item_type: Type of the item being sold.
        :type item_type: ItemType
        :param buyer: Buyer.
        :type buyer: Party
        :param seller: Seller.
        :type seller: Party
        :rtype: VatCharge
        :raises NotImplementedError:
            if no rules for selling from the given country to the given country
            exist.
        """

        raise NotImplementedError()


class EuVatRulesMixin(object):
    """Mixin for VAT rules in EU countries.
    """

    def get_sale_to_country_vat_charge(self,
                                       date,
                                       item_type,
                                       buyer,
                                       seller):
        # We only support business sellers at this time.
        if not seller.is_business:
            raise NotImplementedError(
                'non-business sellers are currently not supported'
            )

        # If the seller resides in the same country as the buyer, we charge
        # VAT regardless of whether the buyer is a business or not. Similarly,
        # if the buyer is a consumer, we must charge VAT in the buyer's country
        # of residence.
        if seller.country_code == buyer.country_code or \
           (not buyer.is_business and date >= JANUARY_1_2015):
            return VatCharge(VatChargeAction.charge,
                             buyer.country_code,
                             self.get_vat_rate(item_type, date))

        # EU consumers are charged VAT in the seller's country prior to January
        # 1st, 2015.
        if not buyer.is_business:
            # Fall back to the seller's VAT rules for this one.
            raise NotImplementedError()

        # EU businesses will never be charged VAT but must account for the VAT
        # by the reverse-charge mechanism.
        return VatCharge(VatChargeAction.reverse_charge,
                         buyer.country_code,
                         0)

    def get_sale_from_country_vat_charge(self,
                                         date,
                                         item_type,
                                         buyer,
                                         seller):
        # We only support business sellers at this time.
        if not seller.is_business:
            raise NotImplementedError(
                'non-business sellers are currently not supported'
            )

        # If the buyer resides outside the EU, we do not have to charge VAT.
        if buyer.country_code not in EU_COUNTRY_CODES:
            return VatCharge(VatChargeAction.no_charge, buyer.country_code, 0)

        # Both businesses and consumers are charged VAT in the seller's
        # country if both seller and buyer reside in the same country.
        if buyer.country_code == seller.country_code:
            return VatCharge(VatChargeAction.charge,
                             seller.country_code,
                             self.get_vat_rate(item_type, date))

        # Businesses in other EU countries are not charged VAT but are
        # responsible for accounting for the tax through the reverse-charge
        # mechanism.
        if buyer.is_business:
            return VatCharge(VatChargeAction.reverse_charge,
                             buyer.country_code,
                             0)

        # Consumers in other EU countries are charged VAT in their country of
        # residence after January 1st, 2015. Before this date, you charge VAT
        # in the country where the company is located.
        if date >= JANUARY_1_2015:
            buyer_rules = VAT_RULES[buyer.country_code]

            return VatCharge(VatChargeAction.charge,
                             buyer.country_code,
                             buyer_rules.get_vat_rate(item_type, date))
        else:
            return VatCharge(VatChargeAction.charge,
                             seller.country_code,
                             self.get_vat_rate(item_type, date))


class EuVatRateRule(EuVatRulesMixin):
    """VAT rules for a country with a constant VAT rate in the entiry country.
    """

    def __init__(self, vat_rates):
        self.vat_rates = vat_rates

    def get_vat_rate(self, item_type, date):
        rates = None
        for item in self.vat_rates:
            if date >= item['valid_from'] and \
               not rates:
                rates = item
            if date >= item['valid_from'] and \
               rates and rates['valid_from'] < item['valid_from']:
                rates = item
        if not rates:
            raise ValueError('`date` is invalid, date: ', date)
        for category in rates['rates']:
            if category == item_type:
                return rates['rates'][category]
        raise ValueError('`item_type` is invalid, item_type: ', item_type)


# VAT rates are based on the report from January 1st, 2017
# http://ec.europa.eu/taxation_customs/sites/taxation/files/resources/documents/taxation/vat/how_vat_works/rates/vat_rates_en.pdf
VAT_RULES = {}
for country_code in EU_COUNTRY_CODES:
    VAT_RULES[country_code] = EuVatRateRule(VAT_RATES[country_code])


"""VAT rules by country.

Maps an ISO 3316 alpha-2 country code to the VAT rules applicable in the given
country.
"""