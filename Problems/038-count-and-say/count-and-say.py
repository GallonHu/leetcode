class Solution:
    def countAndSay(self, n: int) -> str:
        pre_person = '1'
        
        for i in range(1,n):
            next_person, num, count = '', pre_person[0], 1
            for j in range(1,len(pre_person)):
                if(pre_person[j]==num):
                    count = count + 1
                else:
                    next_person += str(count) + num
                    num = pre_person[j]
                    count = 1
            next_person +=str(count) + num
            pre_person = next_person                 
        return pre_person