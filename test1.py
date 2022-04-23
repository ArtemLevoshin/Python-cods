def generate_shape(a):
    b = ''
    for x in range(a):
        for y in range(a):
            b+='+'
        print(b)
        b = ''
    return b
print(generate_shape(7))
