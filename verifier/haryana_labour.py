import json
import requests
from lxml import html

import re

from lib.util import temp


class HaryanaLabour:
    def __init__(self, vc1, vc2, vc3, vc4):
        self.vc1 = vc1
        self.vc2 = vc2
        self.vc3 = vc3
        self.vc4 = vc4

    def pre_request(self):
        url = "https://hrylabour.gov.in/verify"
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.1.1051981851.1731735935; PHPSESSID=s1b0ecui9nvl487u40ec3qp4k0vd2hifn81iverfiopevs1psn0lioa8j9komjbq22brk0nso64vroee23o4j33kfiuocolcgfr5kvfopk1ej97u9g0v7lkcnjujhslqk2vl23d3790mdebu7g2lhq; _ga_RMM91YWVZ8=GS1.1.1731735935.1.1.1731736395.0.0.0',
            'Referer': 'https://hrylabour.gov.in/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }
        params = temp(self.vc1, self.vc2, self.vc3, self.vc4)
        response = requests.get(url, headers=headers, params=params)

        return self.post_request(response.content)

    @staticmethod
    def clean_text_with_regex(text):
        """Cleans the text by removing unwanted escape sequences and extra spaces using regex."""
        return re.sub(r'\s+', ' ', text).strip()

    def post_request(self, content):
        tree = html.fromstring(content)

        shop_bip_list = tree.xpath('//td[strong[contains(text(), "Shop BIP:")]]/following-sibling::td/text()')
        name_of_the_shop = tree.xpath(
            '//td[strong[contains(text(), "Name of the Shop:")]]/following-sibling::td/text()')
        employer_name = tree.xpath('//td[strong[contains(text(), "Employer Name:")]]/following-sibling::td/text()')
        name_of_the_manager = tree.xpath(
            '//td[strong[contains(text(), "Name of the manager:")]]/following-sibling::td/text()')
        address_of_the_shop = tree.xpath(
            '//td[strong[contains(text(), "Address of the Shop:")]]/following-sibling::td/text()')
        date_of_commencement = tree.xpath(
            '//td[strong[contains(text(), "Date of Commencement:")]]/following-sibling::td/text()')
        shop_license_no = tree.xpath('//td[strong[contains(text(), "Shop License No:")]]/following-sibling::td/text()')
        shop_license_valid_upto = tree.xpath(
            '//td[strong[contains(text(), "Shop License Valid upto:")]]/following-sibling::td/text()')
        shop_license_issued_date = tree.xpath(
            '//td[strong[contains(text(), "Shop License Issued Date:")]]/following-sibling::td/text()')

        shop_license_info = {
            "Shop BIP": HaryanaLabour.clean_text_with_regex(shop_bip_list[0]) if shop_bip_list else "Not found",
            "name_of_the_shop": HaryanaLabour.clean_text_with_regex(
                name_of_the_shop[0]) if name_of_the_shop else "Not found",
            "employer_name": HaryanaLabour.clean_text_with_regex(employer_name[0]) if employer_name else "Not found",
            "name_of_the_manager": HaryanaLabour.clean_text_with_regex(
                name_of_the_manager[0]) if name_of_the_manager else "Not found",
            "Address_of_the_Shop": HaryanaLabour.clean_text_with_regex(
                address_of_the_shop[0]) if address_of_the_shop else "Not found",
            "Date_of_Commencement": HaryanaLabour.clean_text_with_regex(
                date_of_commencement[0]) if date_of_commencement else "Not found",
            "Shop_License_No": HaryanaLabour.clean_text_with_regex(
                shop_license_no[0]) if shop_license_no else "Not found",
            "Shop_License_Valid_upto": HaryanaLabour.clean_text_with_regex(
                shop_license_valid_upto[0]) if shop_license_valid_upto else "Not found",
            "Shop_License_Issued_date": HaryanaLabour.clean_text_with_regex(
                shop_license_issued_date[0]) if shop_license_issued_date else "Not found"
        }

        return json.dumps(shop_license_info, indent=4)

