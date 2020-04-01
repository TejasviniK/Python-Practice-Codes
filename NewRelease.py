days_since_release = 14
original_price = 60
greatest_hits = True

weak = int(days_since_release/7)
if greatest_hits :
    price_lost = weak
else : 
    price_lost = weak * 2

new_price = original_price - price_lost
if(new_price < 20) :
    print("$20")
else :
    print("$"+str(new_price))