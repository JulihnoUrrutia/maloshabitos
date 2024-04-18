
def AreaRec(a, b):
    result = a * b
    return result


def AreaTria(largo, ancho):
    r = 0.5 * largo * ancho
    return r

def Principal():
    x = 4
    y= 6
    rect_area = AreaRec(x, y)
    print("Área del rectángulo:", AreaRec(x, y))

    l = 5
    a= 8
    tri_area = AreaTria(l, a)
    print("Área del triángulo:", AreaTria(l, a))



Principal()
