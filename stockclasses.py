class Stock:
    def __init__(self, ticker_info, ticker):
        self.marketCap = ticker_info.info["marketCap"]
        self.name = ticker

    def get_cap(self):
        return self.marketCap

    def get_name(self):
        return self.name


class Index:
    def __init__(self, holdings, divisor):
        self.divisor = divisor

        self.totalMarketCap = 0
        for i in holdings:
            self.totalMarketCap += i.get_cap()

        self.indexValue = 0
        for i in holdings:
            weight = i.get_cap() / self.totalMarketCap
            self.indexValue += weight * i.get_cap()
        self.indexValue = self.indexValue / self.divisor

    def value(self):
        return self.indexValue
