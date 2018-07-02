a = 100
b = 200

if a == b:
    print('same')
    print('{}는 {}와 같다'.format(a, b))
else:
    print('different')
    print('{}는 {}와 다르다'.format(a, b))
    if a>b:
        print('{} > {}'.format(a,b))
    else:
        print('{} < {}'.format(a,b))

print('Finished')