PRODUCTS = [
    {}
]
def get_product_by_name_or_return_none(product_name):
    global PRODUCTS
    for i in PRODUCTS:
        if i["name"] == product_name:
            return i
    return None

def buy(product_name, product_count):
    global PRODUCTS
    if product_name in PRODUCTS and PRODUCTS[product_name]["count"] >= product_count:
        PRODUCTS[product_name]["count"] -= product_count
        PRODUCTS[product_name]["price"] *= 1.10
        print(f"{product_count}add {product_name} kharidari shod")
    else:
        print(f"mahsol {product_name}dar anbar mojod nist ")
        
        
def add(product_name, product_count,product_price):
    global PRODUCTS
    if product_name in PRODUCTS:
        PRODUCTS[product_name]["count"] += product_count
    else: 
        PRODUCTS[product_name] ={"price":product_price , "count":product_count}
    print(f"{product_count}add{product_name}  ba qeymat {product_price} toman be anbar ezafe shod")


def delete(product_name):
    global PRODUCTS
    
    if product_name in PRODUCTS:
        del PRODUCTS[product_name]
        return True
    else:
        return False
    
    
def change(product_name, new_product_count, new_product_price):
    global PRODUCTS
    if product_name in PRODUCTS:
        PRODUCTS[product_name]["price"]=new_product_price
        PRODUCTS[product_name]["count"]=new_product_count
        print(f" etelaat {product_name} beroz shod")
    else:
        print(f"mahsol {product_name} dar anbar vojod nadard")
def main():
    if not PRODUCTS:
        print("anbar khali hast")
    else:
        print(f"mahsol: {product_name},qeymat:{product_price}, {product_count}")
for _ in range(10):
    amaliyat = input("amaliyat mord nazar vared konid").strip().lower()
    if amaliyat == "add":
        product_name = input("product name:").strip()
        product_price = float(input("product price:")).strip()
        product_count= int(input("product count:")).strip()
        add(product_name,product_price,product_count)
    elif amaliyat =="buy":
        product_name = input("product name:").strip()
        product_count= int(input("product count:")).strip()
        buy(product_name,product_count)
    elif amaliyat == "delete":
        product_name = input("product name:").strip()
        delete(product_name)
    elif amaliyat == "change":
        product_name = input("product name:").strip()
        new_product_price =float(input("qeymat jadid mahsol :"))
        new_product_count= int(input("new product_count :"))
        change(product_name,new_product_price,new_product_count)
    else :
        print("namotabar")
print("amojodi anbar:")
main()

if __name__ == "__main__main" :
    main()