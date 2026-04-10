maxsulotlar = [
    {
        "id": 1,
        "name": "s22",
        "price": 450,
        "quantity": 3,
    },
    {
        "id": 2,
        "name": "s23",
        "price": 550,
        "quantity": 2,
    },
    {
        "id": 3,
        "name": "s24",
        "price": 650,
        "quantity": 8,
    }
]

<<<<<<< HEAD
def jami_qiymat(maxsulotlar: list[dict[str, int | str]]) -> float | int:
    jami = 0
    for tovar in maxsulotlar:
        jami +=tovar['price'] * tovar['quantity']

    return jami


def qimmqti_maxsulot(maxsulotlar: list[dict[str, int | str]]) -> dict[str, int | str]:
    if not maxsulotlar:
        return None

    nor_narxi = maxsulotlar[0]
    for tovar in maxsulotlar:
        if tovar['price'] > nor_narxi['price']:
            nor_narxi = tovar

    return nor_narxi


def urtacha_narx(maxsulotlar: list[dict[str, int | str]]) -> float | int:
    jami= 0
    for tovar in maxsulotlar:
        jami += tovar['price']

    urtacha = jami / len(maxsulotlar)
    return urtacha
urtacha = urtacha_narx(maxsulotlar)
nor_narxi = qimmqti_maxsulot(maxsulotlar)
jami = jami_qiymat(maxsulotlar)
print(nor_narxi)
print(jami)
print(urtacha)
=======
# 1. Jami qiymat
def total_amount(products: list[dict[str, int | str]]) -> float | int:
    total = 0
    for product in products:
        total += product['price'] * product['quantity']

    return total

# 2. Eng qimmat product
def get_max_product(products: list[dict[str, int | str]]) -> dict[str, int | str] | None:
    if not products:
        return None
    
    max_product = products[0]
    for product in products:
        if product['price'] > max_product['price']:
            max_product = product

    return max_product

# 3. O'rtacha narx
def get_avg_price(products: list[dict[str, int | str]]) -> float | int:
    total = 0
    for product in products:
        total += product['price']

    avg = total / len(products)
    return avg

avg = get_avg_price(products)
print(avg)
>>>>>>> f1ec0e16fb6300d6060b4e6069e137ee50972ec9
