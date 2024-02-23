import locale

def currency_to_locale(currency: str):
    if currency == 'USD':
        return 'en_US.UTF-8'
    elif currency == 'EUR':
        return 'de_DE.UTF-8'
    elif currency == 'GBP':
        return 'en_GB.UTF-8'
    elif currency == 'JPY':
        return 'ja_JP.UTF-8'
    elif currency == 'KRW':
        return 'ko_KR.UTF-8'
    # implement other currencies if needed
    else:
        return 'en_US.UTF-8'

def format_currency(value: float, currency: str):
    locale.setlocale(locale.LC_ALL, currency_to_locale(currency))
    return locale.currency(value, symbol=True, grouping=True)
