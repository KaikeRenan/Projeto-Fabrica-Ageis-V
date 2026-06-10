from interfaces.financeHealth_interface import IFinancialHealthAnalyzer


class FinancialHealthAnalyzer(IFinancialHealthAnalyzer):

    def extrair_numero(self, texto):
        """
        Converte strings financeiras para float.
        Base utilizada:
        T = Trilhões
        B = Bilhões
        M = Milhões
        """

        if not texto:
            return 0.0

        texto = str(texto)

        if texto == "—" or "Sem dados" in texto:
            return 0.0

        texto_limpo = (
            texto.replace("R$", "")
            .replace("$", "")
            .replace("%", "")
            .replace("BRL", "")
            .replace("USD", "")
            .replace(",", "")
            .strip()
        )

        multiplicador = 1.0

        if texto_limpo.endswith("T"):
            multiplicador = 1000.0
            texto_limpo = texto_limpo[:-1]

        elif texto_limpo.endswith("B"):
            multiplicador = 1.0
            texto_limpo = texto_limpo[:-1]

        elif texto_limpo.endswith("M"):
            multiplicador = 0.001
            texto_limpo = texto_limpo[:-1]

        try:
            return float(texto_limpo) * multiplicador
        except ValueError:
            return 0.0

    def evaluate(self, data: dict) -> dict:
        """
        Score universal de saúde financeira (0-10)
        """

        print("\n===== HEALTH ANALYZER =====")
        print(data)
        print("===========================\n")

        mercado = data.get("mercado", {})
        financeiro = data.get("financeiro", {})

        nota = 0
        auditoria = []

        # 1. P/E Ratio
        pl = self.extrair_numero(
            mercado.get("P/E ratio", "0")
        )

        if 0 < pl <= 15:
            nota += 1
            auditoria.append(
                f"[+] P/L saudável ({pl})"
            )

        # 2. Price to Book
        pvp = self.extrair_numero(
            financeiro.get("Price to book", {})
            .get("valor", "0")
        )

        if 0 < pvp <= 2:
            nota += 1
            auditoria.append(
                f"[+] P/VP atrativo ({pvp})"
            )

        # 3. Lucro
        lucro = self.extrair_numero(
            financeiro.get("Net income", {})
            .get("valor", "0")
        )

        if lucro > 0:
            nota += 1
            auditoria.append(
                f"[+] Empresa dá lucro ({lucro} bi)"
            )

        # 4. Crescimento do lucro
        var_lucro = self.extrair_numero(
            financeiro.get("Net income", {})
            .get("variacao", "0")
        )

        if var_lucro > 0:
            nota += 1
            auditoria.append(
                f"[+] Lucro em expansão ({var_lucro}%)"
            )

        # 5. Margem líquida
        margem = self.extrair_numero(
            financeiro.get("Net profit margin", {})
            .get("valor", "0")
        )

        if margem > 10:
            nota += 1
            auditoria.append(
                f"[+] Margem líquida forte ({margem}%)"
            )

        # 6. Crescimento da receita
        var_receita = self.extrair_numero(
            financeiro.get("Revenue", {})
            .get("variacao", "0")
        )

        if var_receita > 0:
            nota += 1
            auditoria.append(
                f"[+] Receita crescendo ({var_receita}%)"
            )

        # 7. Eficiência operacional
        var_custos = self.extrair_numero(
            financeiro.get("Operating expense", {})
            .get("variacao", "0")
        )

        if var_receita > var_custos and var_receita != 0:
            nota += 1
            auditoria.append(
                "[+] Ganho de eficiência (Receita subiu mais que Custos)"
            )

        # 8. Solvência
        ativos = self.extrair_numero(
            financeiro.get("Total assets", {})
            .get("valor", "0")
        )

        passivos = self.extrair_numero(
            financeiro.get("Total liabilities", {})
            .get("valor", "0")
        )

        if ativos > passivos and ativos != 0:
            nota += 1
            auditoria.append(
                "[+] Solvente: Ativos cobrem Passivos"
            )

        # 9. ROA
        roa = self.extrair_numero(
            financeiro.get("Return on assets", {})
            .get("valor", "0")
        )

        if roa > 0:
            nota += 1
            auditoria.append(
                f"[+] Retorno sobre ativos positivo ({roa}%)"
            )

        # 10. Dividend Yield
        dy = self.extrair_numero(
            mercado.get("Dividend yield", "0")
        )

        if dy >= 4:
            nota += 1
            auditoria.append(
                f"[+] Bom pagamento de dividendos ({dy}%)"
            )

        return {
            "ticker": data.get("ticker"),
            "Nota": nota,
            "auditoria": auditoria
        }