class Fact():
    def __init__(self,n):
        self.n=n
    def fa(self,n):
        assert n==int(n),"Write integer value"
        if(n==1):
            return 1
        return n*f.fa((n-1))   
n=5
f=Fact(n)
print(f.fa(n))

