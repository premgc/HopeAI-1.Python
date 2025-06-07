class FindPercentage():   
    def Percent(intSubject1,intSubject2,intSubject3,intSubject4,intSubject5):
        add=intSubject1+intSubject2+intSubject3+intSubject4+intSubject5
        percentage= (add * 100 )/500
        strMessage =   f"Subject: {intSubject1}\nSubject2: {intSubject2}\nSubject3: {intSubject3}\nSubject4: {intSubject4}\nSubject5: {intSubject5} \nTotal: {add} \nPercentage: {percentage}"
    
        return strMessage 