def python_to_c(a):
    b=''
    for i in repr(a):
        if i=='[':
            b=b+'{'
        elif i==']':
            b=b+'}'
        else:
            b=b+i
    return b