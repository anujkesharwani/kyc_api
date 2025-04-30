import re

from lib.base import BaseVerifier
from lib.basic_utils import extract_captcha_value
from lib.verifire_utils.payload import pay_load_info


class ChildClass(BaseVerifier):

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
        'Connection': 'keep-alive',
        'Referer': 'https://ird.gov.np/pan-search',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36',
    }

    pre_query_url = "https://ird.gov.np/pan-search"
    query_url = "https://ird.gov.np/statstics/getPanSearch"

    timeout_setting = {
        "timeout": 10
    }


    def __init__(self, proxy=None):
        super().__init__(to_verify=None, proxy=proxy)
        self.pan = None
        self._token = None
        self.captcha = None

    @staticmethod
    def clean_text_with_regex(text):
        return re.sub(r'\s+', ' ', text).strip()

    def pre_query(self):
        response = self.smart_request('GET', self.pre_query_url,headers=self.headers)
        tree =self.get_etree(response)
        self._token = tree.xpath("//input[@type='hidden' and @name='_token']/@value")[0]

        # captcha = self.clean_text_with_regex(' '.join(tree.xpath("//div[@id='mid']//label/text()")))
        captcha = tree.xpath("//div[@id='mid']/label/text()")[0].strip()
        captcha_value = extract_captcha_value(captcha)
        return self.query_info(captcha_value)

    def query_info(self,content):
        payload = pay_load_info(self.pan, self._token, self.captcha)
        response = self.smart_request('POST', self.query_url, data=payload,headers=self.headers)
        return self.extract_info(response)

    def extract_info(self,response):
        data = response.json()
        pan_details_list = data.get('panDetails', [])
        result = pan_details_list[0]
        pan = result['pan']
        trade_name = result['trade_Name_Nep']
        office_names = result['office_Name']
        ward = result['ward_No']
        mobile_number = result['mobile']
        street_name = result['street_Name']

        pan_info = dict()
        pan_info["pan_number"] = pan
        pan_info["trade_name_nep"] = trade_name
        pan_info["office_name"] = office_names
        pan_info["ward_number"] = ward
        pan_info["mobile_number"] = mobile_number
        pan_info["street_name"] = street_name
        # print(pan_info)
        return pan_info


# obj=ChildClass()
# obj.pre_query()
