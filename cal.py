def acc(tp, sum):
    return 100.0*tp/sum

def pre(tp,fp):
    return tp*100.0/(tp+fp) 

def rec(tp,fn):
    return tp*100.0/(tp+fn)

def meanCal(a,sum):
    mean=0.0 
    for i in range(len(a)):
        mean+=a[i]*20
    return mean/sum

def f1(pre,rec):
    return 2*pre*rec/(pre+rec)