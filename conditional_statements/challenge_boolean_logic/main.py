seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100
overstock_risk = True
discount_eligible = False
make_discount = False

if seasonal == True and current_stock > high_stock_threshold:
    overstock_risk = True
if not selling_well and not on_sale:
    discount_eligible = True

if overstock_risk == True or discount_eligible == True:
    make_discount = True

print ('Should the item be discounted?', make_discount)