class Solution(object):
    def sumAndMultiply(self, n):
        number=str(n)
        if n==0 :
            return 0
        l1=[]
        for i in number:
            l1.append(int(i))
        c1=l1.count(0)
        j=1
        while j<=c1:
            l1.remove(0)
            j+=1
        sum_num=sum(l1)
        string=""
        for i in l1:
            string+=str(i)
        return int(string)*sum_num