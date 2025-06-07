class FindEligibility():
    def Elegible(strGender, strAge):
        strMessage=''
        if  strGender.upper()=='M' and strAge>=21:
            strcriteria="Eligible"
            strGender="Male"
            strMessage = "Your Gender is {} \nYour age is {} \n{}".format(strGender, strAge ,strcriteria)
        elif strGender.upper()=='F' and strAge>=18:
            strcriteria="Eligible"
            strGender="Female"
            strMessage = "Your Gender {} \nYour age is  {} \n{}".format(strGender, strAge ,strcriteria)
        else:
            if strGender.upper()=='M':
                strGender='Male' 
            else: 
                strGender='Female'
                
            strcriteria="NOT Eligible"            
            strMessage = "Your Gender is {} \nYour age is {} \n{}".format(strGender, strAge ,strcriteria)

        return strMessage