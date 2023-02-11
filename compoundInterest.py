def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundInterest()
# This first 3 lines are provided for you
    def calculate_ci(principal, rate, time):
        amount = principal * ( 1 + rate/100) ** time
        print("Compound Interest: "+str(round(amount - principal,2)))
    
    def client_entry():
        client_principal = float(input("Principle (amount): "))
        client_time =      float(input("Time:               "))
        client_rate =      float(input("Rate:               "))
        return  client_principal, client_time, client_rate
    
    def calculateCompoundInterest():
        client_principal1, client_time1, client_rate1 = client_entry()
        calculate_ci(client_principal1, client_time1, client_rate1)
        print("---")
       
        client_principal2, client_time2, client_rate2 = client_entry()
        calculate_ci(client_principal2, client_time2, client_rate2)
        print("---")
        
        client_principal3, client_time3, client_rate3 = client_entry()
        calculate_ci( client_principal3, client_time3, client_rate3)
        print("---")


    #A = client_one_principal( 1 + client_one_rate/100)^client_one_time
    #CI = A - client_one_principal
    #print("Compound Interest: "+str(CI))

    #client_two_principal = float(input("Principle (amount): "))
    #client_two_time =      float(input("Time:               "))
    #client_two_rate =      float(input("Rate:               "))

    #client_three_principal = float(input("Principle (amount): "))
    #client_three_time =      float(input("Time:               "))
    #client_three_rate =      float(input("Rate:               "))
 #print("Compound Interest: "+str(intrest))

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
