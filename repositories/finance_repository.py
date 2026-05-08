import httpx
from bs4 import BeautifulSoup
from interfaces.finance_repository_interface import IFinanceRepository

class FinanceRepository(IFinanceRepository):
    def fetch_google_data(self, ticker: str) -> dict:
        url = f"https://www.google.com/finance/quote/{ticker}?hl=pt"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        
        with httpx.Client(headers=headers, follow_redirects=True) as client:
            response = client.get(url)
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        nome_tag = soup.find("div", {"class": "zzDege"}) or soup.find("div", {"class": "zzDe30"})
        nome_empresa = nome_tag.get_text(strip=True) if nome_tag else "Nome não encontrado"

        dados_limpos = {
            "nome_empresa": nome_empresa,
            "mercado": {},
            "financeiro": {}
        }

        ignorar = ["Sede", "Data da fundação", "Empregados", "Website", "CEO", "Diretor executivo", "Presidente"]
        for row in soup.find_all("div", {"class": "gyFHrc"}):
            label = row.find("div", {"class": "mfs7Fc"})
            value = row.find("div", {"class": "P6K39c"})
            if label and value:
                txt_label = label.get_text(strip=True)
                if txt_label not in ignorar:
                    dados_limpos["mercado"][txt_label] = value.get_text(strip=True).replace('\xa0', ' ')

        for tabela in soup.find_all("table", {"class": "slpEwd"}):
            for row in tabela.find_all("tr", {"class": "roXhBd"}):
                label_div = row.find("div", {"class": "rsPbEe"})
                value_td = row.find("td", {"class": "QXDnM"})
                var_td = row.find("td", {"class": "gEUVJe"})

                if label_div and value_td:
                    txt_label = label_div.get_text(strip=True)
                    txt_value = value_td.get_text(strip=True).replace('\xa0', ' ')
                    txt_var = var_td.get_text(strip=True) if var_td else "Sem dados"
                    
                    dados_limpos["financeiro"][txt_label] = {
                        "valor": txt_value,
                        "variacao": "Sem dados" if txt_var == "—" else txt_var
                    }

        return dados_limpos