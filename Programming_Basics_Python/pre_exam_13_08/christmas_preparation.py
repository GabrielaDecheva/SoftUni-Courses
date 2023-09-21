count_paper = int(input())
count_fabric = int(input())
litres_glue = float(input())
discount_percent = int(input())

total_paper_price = count_paper * 5.8
total_fabric_price = count_fabric * 7.2
total_glue_price = litres_glue * 1.2
all_materials = total_paper_price + total_fabric_price + total_glue_price
all_with_discount = all_materials - (all_materials * discount_percent / 100)
print(f'{all_with_discount:.3f}')