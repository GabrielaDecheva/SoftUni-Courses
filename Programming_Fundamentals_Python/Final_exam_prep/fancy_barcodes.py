import re


def validate_barcode(regex, barcode):
    product_group = ''
    is_valid = re.findall(regex, barcode)
    if is_valid:
        for element in barcode:
            if element.isdigit():
                product_group += element
        if not product_group:
            product_group = '00'
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')


count_barcodes = int(input())
pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'
for barcode in range(count_barcodes):
    current_barcode = input()
    validate_barcode(pattern, current_barcode)


# def parse_barcode(barcode_data):
#     pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'
#
#     for barcode in barcode_data:
#         match = re.fullmatch(pattern, barcode)
#         if match:
#             product_group = ''.join(re.findall(r'\d', barcode))
#             product_group = product_group if product_group else '00'
#             print(f'Product group: {product_group}')
#         else:
#             print('Invalid barcode')
#
#
# num = int(input())
# data = [input() for _ in range(num)]
# parse_barcode(data)