import csv
import pycountry

async def get_bin_details(cc):
    fbin = cc[:6]

    def get_bin_info_from_csv(fbin, csv_file='FILES/bins_all.csv'):
        try:
            with open(csv_file, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == fbin:
                        return {
                            "bin": row[0],
                            "country": row[1],
                            "flag": row[2],
                            "brand": row[3],
                            "type": row[4],
                            "level": row[5],
                            "bank": row[6]
                        }
        except Exception as e:
            print(f"Error reading CSV: {e}")
        return {}

    try:
        bin_info = get_bin_info_from_csv(fbin)

        if not bin_info:
            return "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"

        brand = bin_info.get("brand", "N/A").upper()
        card_type = bin_info.get("type", "N/A").upper()
        level = bin_info.get("level", "N/A").upper()
        bank = bin_info.get("bank", "N/A").upper()
        country_code = bin_info.get("country", "N/A").upper()
        flag = bin_info.get("flag", "N/A").upper()
        country_name = "N/A"
        currency = "N/A"

        if country_code != "N/A":
            country = pycountry.countries.get(alpha_2=country_code)
            if country:
                country_name = country.name
                currency = pycountry.currencies.get(numeric=country.numeric)
                if currency:
                    currency = currency.alpha_3

        if country_name == "N/A":
            country_name = bin_info.get("country", "N/A").upper()

        return brand, card_type, level, bank, country_name, flag, currency

    except Exception as e:
        print(f"Error processing BIN details: {e}")
        return "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"
