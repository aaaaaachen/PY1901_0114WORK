shop = [
    {"id": 1, "good_name": "西紅柿", "good_price": 10},
    {"id": 2, "good_name": "番茄\t", "good_price": 12},
    {"id": 3, "good_name": "土豆\t", "good_price": 15},
    {"id": 4, "good_name": "黄瓜\t", "good_price": 17},
    {"id": 5, "good_name": "青椒\t", "good_price": 14},
]

for good in shop:
    print("编号:%s 商品  %s 价格  %s"%(good["id"],good["good_name"],good["good_price"]))
