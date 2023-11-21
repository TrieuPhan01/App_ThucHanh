def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile',
    }, {
        'id': 2,
        'name': 'Tablet'

    }]


def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'phone 13',
        'price': 500000,
        'image': 'https://didongviet.vn/dchannel/wp-content/uploads/2023/07/hinh-anh-iphone-15-pro-max-mau-hong-didongviet-2.jpg'
    }, {
        'id': 2,
        'name': 'phone 15',
        'price': 900000,
        'image': 'https://didongviet.vn/dchannel/wp-content/uploads/2023/07/hinh-anh-iphone-15-pro-max-mau-hong-didongviet-2.jpg'
    }, {
        'id': 3,
        'name': 'samsum',
        'price': 200000,
        'image': 'https://didongviet.vn/dchannel/wp-content/uploads/2023/07/hinh-anh-iphone-15-pro-max-mau-hong-didongviet-2.jpg'
    }, {
        'id': 4,
        'name': 'phone X',
        'price': 700000,
        'image': 'https://didongviet.vn/dchannel/wp-content/uploads/2023/07/hinh-anh-iphone-15-pro-max-mau-hong-didongviet-2.jpg'
    }, {
        'id': 5,
        'name': 'May tinh bang',
        'price': 300000,
        'image': 'https://didongviet.vn/dchannel/wp-content/uploads/2023/07/hinh-anh-iphone-15-pro-max-mau-hong-didongviet-2.jpg'

    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products
