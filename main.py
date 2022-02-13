import json
from config import PRODUCT_DOES_NOT_EXIST_ERROR_MESSAGE


class Solution:

    products_dict = dict()

    def __init__(self):
        self._read_sales_input()

    def _get_dict_containing_price_and_country(self, country, price):
        return {'country': country, 'price': price}

    def _aggregate_products_data(self, products_data):
        for product in products_data:
            if product.get('prod') in self.products_dict:
                country_found_in_current_product = False
                for current_product in self.products_dict.get(product.get('prod')):
                    if product.get('country') == current_product.get('country'):
                        # if country exists, simply add the price
                        current_product['price'] += product.get('price')
                        country_found_in_current_product = True
                        break

                if not country_found_in_current_product:
                    # if country does not exists, append the price and country dict
                    self.products_dict[product.get('prod')].append(
                        self._get_dict_containing_price_and_country(product.get('country'), product.get('price')))
            else:
                self.products_dict[product.get('prod')] = [self._get_dict_containing_price_and_country(
                    product.get('country'), product.get('price'))]

    def _read_sales_input(self):
        # opening JSON file
        file = open('input.json')

        # returns JSON object as a dictionary
        products_data = json.load(file)

        self._aggregate_products_data(products_data.get('sales'))
        file.close()

        print(self.products_dict)

    def _return_maximum_total_sales(self, product_name):
        if product_name not in self.products_dict:
            return None

        current_max_country = None
        current_max_price = -1
        for product in self.products_dict.get(product_name):
            if product.get('price') > current_max_price:
                current_max_country = product.get('country')
                current_max_price = product.get('price')

        return current_max_country


s = Solution()
print('Enter a product name: ')
product_name = input()
country_name = s._return_maximum_total_sales(product_name)

if country_name:
    print('Country with maximum sales: ', country_name)
else:
    print(PRODUCT_DOES_NOT_EXIST_ERROR_MESSAGE)
