# Ugly Number 2

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Avoid binary search by keeping pointers to the last accessed block
        last = [0,0,0]
        #Subproblem way of solving
        d=[1]
        if n==0:
            return 0
        
        for i in range(1,n):
            
            a = d[last[0]]*2
            b = d[last[1]]*3
            c = d[last[2]]*5
            #Check which is smaller and make the change
            if a <= b and a<=c:
                # 2*3 = 3*2 i,e multiple way of getting the same val
                if a==b:
                    last[1]+=1
                if a==c:
                    last[2]+=1
                #append to the list
                d.append(a)
                last[0]+=1
            elif b <= c and b<=a:
                if b==c:
                    last[2]+=1
                d.append(b)
                last[1]+=1
            else:
                d.append(c)
                last[2]+=1
        #print d
        return d[-1]