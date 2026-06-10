from scrapers.google_finance_beta_scraper import GoogleFinanceBetaScraper
from scrapers.google_finance_classic_scraper import GoogleFinanceClassicScraper
from interfaces.finance_repository_interface import IFinanceRepository

class FinanceRepository(IFinanceRepository):

    def __init__(self):

        self.beta_scraper = GoogleFinanceBetaScraper()
        self.classic_scraper = GoogleFinanceClassicScraper()

    def fetch_google_data(self, ticker: str):

        try:
            return self.beta_scraper.fetch(ticker)

        except Exception as e:

            print("Erro no Beta:", e)

            return self.classic_scraper.fetch(ticker)