def is_valid_isbn(isbn):
    """ISBN validator: see http://en.wikipedia.org/wiki/International_Standard_Book_Number"""
    import re
    import operator
    isbn = re.sub("\D","X",re.sub("\W","",isbn))
    if len(isbn) == 10:
        """check used: d_10 = 1*d_1 + ... + 9*d_9 mod 11 (d_i: i'th digit of ISBN)"""
        Map={}
        res = map(lambda a: Map.update({re.sub('10','X',str(a)):a}),range(11))
        v = [Map[i] for i in isbn.upper() if Map.has_key(i)]
        return reduce(operator.add, map(operator.mul, v[:-1], range(1,len(v)))) % len(Map) == v[-1]
    elif len(isbn) == 13:
        d = list(isbn)
        e = map(lambda i: int(d[i]),filter(lambda j: j%2==0,range(13)))
        o = map(lambda i: 3*int(d[i]),filter(lambda j: j%2==1,range(13)))
        return sum(e+o)%10 == 0
    else:
        return False
    