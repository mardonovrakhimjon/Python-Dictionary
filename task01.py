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