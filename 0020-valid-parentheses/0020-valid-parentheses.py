class Solution:
    def isValid(self, s: str) -> bool:
        # Using counter for diffrent brackets
        curl:int=0#{}
        circular:int=0#()
        square:int=0#[]
        list_for_check=[]
        for any_bracket in s:
            if len(list_for_check)>=2:
                if (ord(list_for_check[-1])-ord(list_for_check[-2])) in [-82,85,-30,34,53,-50]:
                    return False
                elif (ord(list_for_check[-1])-ord(list_for_check[-2])) in [2,1]:  
                    list_for_check.pop()
                    list_for_check.pop()    
            if (curl or circular or square)<0:
                return False
            elif any_bracket=='{':
                list_for_check.append(any_bracket)
                curl+=1
            elif any_bracket=='}':
                list_for_check.append(any_bracket)
                curl-=1
            elif any_bracket=='(':
                list_for_check.append(any_bracket)
                circular+=1
            elif any_bracket==')':
                list_for_check.append(any_bracket)
                circular-=1             
            elif any_bracket=='[':
                list_for_check.append(any_bracket)
                square+=1    
            elif any_bracket==']':
                list_for_check.append(any_bracket)
                square-=1   
                
        if (curl==0 and circular==0 and square==0): 
            return True
        else :
            return False
    