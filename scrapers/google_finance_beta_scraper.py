import httpx
from bs4 import BeautifulSoup


class GoogleFinanceBetaScraper:

    BASE_URL = "https://www.google.com/finance/beta/quote"

    def __init__(self):
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36"
            )
        }

    def fetch(self, ticker: str) -> dict:

        overview_data = self._scrape_overview(ticker)

        financials_data = self._scrape_financials(ticker)

        return {
            **overview_data,
            "financeiro": financials_data
        }

    def _get_soup(self, ticker: str, tab: str | None = None):

        if tab:
            url = f"{self.BASE_URL}/{ticker}?tab={tab}"
        else:
            url = f"{self.BASE_URL}/{ticker}"

        with httpx.Client(
            headers=self.headers,
            follow_redirects=True
        ) as client:

            response = client.get(url)

        response.raise_for_status()

        return BeautifulSoup(
            response.text,
            "html.parser"
        )

    def _scrape_overview(self, ticker: str) -> dict:

        soup = self._get_soup(ticker)

        nome_tag = (
            soup.find("div", {"class": "YTGvuc"})
            or
            soup.find("div", {"class": "gO24Ff"})
        )

        nome_empresa = (
            nome_tag.get_text(strip=True)
            if nome_tag
            else "Nome não encontrado"
        )

        dados = {
            "ticker": ticker,
            "nome_empresa": nome_empresa,
            "mercado": {}
        }

        ignorar = [
            "Headquarters",
            "Founded",
            "Employees",
            "Website",
            "CEO"
        ]

        for row in soup.find_all(
            "div",
            {"class": "KxsRFb"}
        ):

            label = row.find(
                "div",
                {"class": "SwQK7"}
            )

            value = row.find(
                "div",
                {"class": "dO6ijd"}
            )

            if not label or not value:
                continue

            txt_label = label.get_text(strip=True)

            if txt_label in ignorar:
                continue

            dados["mercado"][txt_label] = (
                value.get_text(strip=True)
                .replace("\xa0", " ")
            )

        return dados

    def _scrape_financials(self, ticker: str) -> dict:

        soup = self._get_soup(
            ticker,
            "financials"
        )

        financeiro = {}

        for tabela in soup.find_all(
            "table",
            {"class": "IvSrfb"}
        ):

            for row in tabela.find_all(
                "tr",
                {"class": "K5RZUc"}
            ):

                label_div = row.find(
                    "div",
                    {"class": "sp5q4e"}
                )

                value_td = row.find(
                    "td",
                    {"class": "cUfeoc"}
                )

                var_td = row.find(
                    "div",
                    {"class": "CNzF7d"}
                )

                if not label_div or not value_td:
                    continue

                txt_label = label_div.get_text(
                    strip=True
                )

                txt_value = value_td.get_text(
                    strip=True
                )

                txt_var = (
                    var_td.get_text(strip=True)
                    if var_td
                    else "Sem dados"
                )

                financeiro[txt_label] = {
                    "valor": txt_value,
                    "variacao": (
                        "Sem dados"
                        if txt_var == "—"
                        else txt_var
                    )
                }

        return financeiro