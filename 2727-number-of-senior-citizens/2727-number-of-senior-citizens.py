class Solution:
    def countSeniors(self, details: list[str]) -> int:
        old_age_passengers = 0
        for passenger in details:
            if int(passenger[11:13]) > 60:
                old_age_passengers +=1
                
        return old_age_passengers