from django.shortcuts import render,HttpResponse
def greetings(request):
    # var=request.GET['var']
    res=render(request,'index.html')
    return res

def calculator(request):
    if request.method == "POST":
        v = request.POST['values']
        z=v+'='
        a = [1]
        sum = 0
        v = v.replace('+', ' +')
        v = v.replace('-', ' -')
        lst = v.split(' ')

        def mf(x):
            ss = 1
            l2 = x.split('x')
            for i in range(len(l2)):
                if '/' in l2[i]:
                    l2[i] = df(l2[i])
            for i in range(len(l2)):
                ss *= float(l2[i])
            return ss

        def df(x):
            l3 = x.split('/')
            s = float(l3[0])
            for i in range(1, len(l3)):
                s /= float(l3[i])
            return s

        for i in range(len(lst)):
            if '+' in lst[i]:
                a.append(1)
                lst[i] = lst[i][1:]
            elif '-' in lst[i]:
                a.append(-1)
                lst[i] = lst[i][1:]
        for i in range(len(lst)):
            if 'x' in lst[i]:
                lst[i] = mf(lst[i])
            elif '/' in lst[i]:
                lst[i] = df(lst[i])
            else:
                lst[i] = float(lst[i])
        for i in range(len(lst)):
            sum += (lst[i] * a[i])
            answer=z+str(sum)
        res = render(request, 'index.html', {'result':answer})
        return res



