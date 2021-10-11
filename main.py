def printMenu():
    print ('1. Citire date')
    print ('2. Determinare cea mai lungă subsecvență in care toate numerele sunt pare')
    print ('3. Determinare cea mai lungă subsecvență in care media numerelor nu depășește o valoare citită')
    print ('4. Determinare cea mai lungă subsecvență in care toate numerele sunt divizibile cu un numar')
    print ('5. Iesire')

def citireLista ():
    lst = []
    n = int(input('Dati nr de elemente: '))
    for i in range(n):
        lst.append(int(input('L[' + str(i) + '] =')))
    return lst

def ToateElemSuntPare(lst):
    '''
    determina daca o lista are toate elementele nr pare
    :param lst: lista de nr intregi
    :return: True, daca toate elem din lista sunt nr pare sau False, in caz contrar
    '''
    for i in lst:
        if i % 2 !=0:
            return False
    return True

def test_ToateElemSuntPare(lst):
    assert ToateElemSuntPare([1,2,3]) is False
    assert ToateElemSuntPare([4,6,78,0]) is True
    assert ToateElemSuntPare([17,9,11,5,31,4]) is False

def get_longest_all_even (lst):
    '''
    determina cea mai lunga subsecventa in care toate elementele sunt numere pare
    :param lst: lista de numere intregi
    :return: cea mai lunga subsecventa in care toate elementele sunt numere pare din lst
    '''
    test_ToateElemSuntPare(lst)
    subsecventaMax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if ToateElemSuntPare(lst[i:j+1]) and len(subsecventaMax) < len(lst[i:j+1]):
                subsecventaMax = lst[i:j+1]
    return subsecventaMax

def test_get_longest_all_even ():
    assert get_longest_all_even([1,3]) == []
    assert get_longest_all_even([2,4,12]) == [2,4,12]
    assert get_longest_all_even([5,90,20,71,10]) == [90,20]


def mediaElem (lst):
    '''
    calculeaza media aritmedia a tuturor elementelor din lista
    :param lst: lista de nr intregi
    :return: media aritmetica a elementelor listei
    '''
    sumaNrLista = 0
    for i in lst:
        sumaNrLista = sumaNrLista + i
    medie = sumaNrLista / len(lst)
    return medie

def test_mediaElem ():
    assert mediaElem([1,2,3]) == 2
    assert mediaElem([40]) == 40
    assert mediaElem([-3,6,-19,5]) == -2.75

def get_longest_average_below (lst , average):
    '''
    determina cea mai lunga subsecventa in care toate elementele eu media mai mica decat o valoare citita
    :param lst: lista de nr intregi
    :param average: valoarea citita pentru a putea fi comparata media
    :return: cea mai lunga subsecventa in care toate elementele din lista au media mai mica decat o valoare citita
    '''
    test_mediaElem()
    subsecventaMax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if mediaElem(lst[i:j + 1]) < average and len(subsecventaMax) < len(lst[i:j + 1]):
                subsecventaMax = lst[i:j + 1]
    return subsecventaMax

def test_get_longest_average_below ():
    assert get_longest_average_below([30,1,2,3,56,0],4) == [1,2,3]
    assert get_longest_average_below([34],10) == []
    assert get_longest_average_below([3,5,7,4],6) == [3,5,7,4]

def EsteDivizibilcuK (lst,k):
    '''
    determina daca o lista are toate elementele divizibile cu k
    :param lst: lista de nr intregi
    :param k: nr intreg
    :return: True, daca toate elementele sunt divizibile cu k sau False, in caz contrar
    '''
    for i in lst:
        if i % k != 0:
            return False
    return True

def get_longest_div_k (lst , k):
    '''
    determina cea mai lunga subsecventa in care toate elementele sunt divizibile cu un nr k
    :param lst: lista de nr intregi
    :param k: nr intreg
    :return: cea mai lunga subsecventa in care toate elementele sunt divizibile cu un nr k
    '''
    subsecventaMax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if EsteDivizibilcuK(lst[i:j + 1], k) is True and len(subsecventaMax) < len(lst[i:j + 1]):
                subsecventaMax = lst[i:j + 1]
    return subsecventaMax

def test_get_longest_div_k ():
    assert get_longest_div_k([2,4,6],2) == [2,4,6]
    assert get_longest_div_k([2,1,4],13) == []

def main():
    test_get_longest_div_k()
    test_get_longest_all_even()
    test_get_longest_average_below()
    lst=[]
    while True:
        printMenu()
        optiune = input('Dati optiunea: ')
        if optiune == "1":
            lst=citireLista()
        elif optiune == "2":
            print(get_longest_all_even(lst))
        elif optiune == "3":
            average = int(input("Dati valoarea pentru a compara media: "))
            print (get_longest_average_below((lst) , average))
        elif optiune == "4":
            k = int(input("Dati valoarea cu care doriti sa fie divizibile numerele: "))
            print (get_longest_div_k((lst),k))
        elif optiune == '5':
            break
        else:
            print("Optiune gresita! Reincercati!")


main()