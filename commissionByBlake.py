# Assignment 1
# Connor Blake
# ID: 101199247


def print_summary(salesLst, paymentLst):
    total_sales = 0
    total_payment = 0
    for sTotal in salesLst:
        total_sales += sTotal
    for pTotal in paymentLst:
        total_payment += pTotal
        
    print ("***********************")
    print("      Hank & Son ")
    print(" Monthly sales summary ")
    print("***********************")
    print(f"Store total monthly sales is ${total_sales}")
    print(f"Store total monthly payment is ${total_payment}")
    if total_sales - total_payment > 0:
        print(f"The store profit is ${total_sales - total_payment}")    
    if total_sales - total_payment < 0:
        print(f"The store loss is ${total_sales - total_payment}")
    if total_sales - total_payment == 0:
        print("Break-even")

def main():
    commissionTable = {
            "Tier1/ $0 - $9,999.99": {"Admin Fee":100, "Commision Rate":0.1},
            "Tier2/ $10,000 – $14,999.99": {"Admin Fee":125, "Commision Rate":0.12},
            "Tier3/ $15,000 – $17,999.99": {"Admin Fee":150, "Commision Rate":0.15},
            "Tier4/ $18,000 – $21,999.99": {"Admin Fee":175, "Commision Rate":0.17},
            "Tier5/ $22,000 - $100,000.00": {"Admin Fee":200, "Commision Rate":0.2}
            }

    another = True
    
    salesLst = []
    paymentLst = []
    
    while another == True:
        
        # making sure user input is as wanted 
    
        while True:
            monthly_sales = input("Please enter the salesperson's monthly sales: ")

            try:
                monthly_sales = int(monthly_sales)
                if monthly_sales > 0 and monthly_sales <= 100000:
                    break
                elif monthly_sales <= 0:
                    print("Invalid input. Please enter a number greater than 0 and try again.")
                else:
                    print("Invalid input. Please enter a number not bigger than 100000 and try again.")
                
            except ValueError:
                print("Invalid value. Try again. Enter a number")
                
        while True:
            advanced_pay =  input("Please enter the salesperson's advanced pay: ")

            try:
                advanced_pay = int(advanced_pay)
                if advanced_pay > 0 and advanced_pay <= 100000:
                    break
                elif advanced_pay <= 0:
                    print("Invalid input. Please enter a number greater than 0 and try again.")
                else:
                    print("Invalid input. Please enter a number not bigger than 100000 and try again.")
                
            except ValueError:
                print("Invalid value. Try again. Enter a number")

                                
                
        if 0 < monthly_sales < 10000:
            pay = (monthly_sales * commissionTable["Tier1/ $0 - $9,999.99"]["Commision Rate"]) - advanced_pay - commissionTable["Tier1/ $0 - $9,999.99"]["Admin Fee"]
            
            if pay > 0:
                print(f"The monthly pay is ${pay}")
            if pay < 0: 
                print (f"The amount owing is ${abs(pay)}")
               
            salesLst.append(monthly_sales)
            paymentLst.append(pay + advanced_pay)
                    
        if 10000 <= monthly_sales < 15000:
            pay = (monthly_sales * commissionTable["Tier2/ $10,000 – $14,999.99"]["Commision Rate"]) - advanced_pay - commissionTable["Tier2/ $10,000 – $14,999.99"]["Admin Fee"]
            if pay > 0:
                print(f"The monthly pay is ${pay}")
            if pay < 0: 
                print (f"The amount owing is ${abs(pay)}")
               
            salesLst.append(monthly_sales)
            paymentLst.append(pay + advanced_pay)
            
        if 15000 <= monthly_sales < 18000:
            pay = (monthly_sales * commissionTable["Tier3/ $15,000 – $17,999.99"]["Commision Rate"]) - advanced_pay - commissionTable["Tier3/ $15,000 – $17,999.99"]["Admin Fee"]
            if pay > 0:
                print(f"The monthly pay is ${pay}")
            if pay < 0: 
                print (f"The amount owing is ${abs(pay)}")
                
            salesLst.append(monthly_sales)
            paymentLst.append(pay + advanced_pay)
            
        if 18000 <= monthly_sales < 22000:
            pay = (monthly_sales * commissionTable["Tier4/ $18,000 – $21,999.99"]["Commision Rate"]) - advanced_pay - commissionTable["Tier4/ $18,000 – $21,999.99"]["Admin Fee"]
            #(monthly_sales - commissionTable["Tier4/ $18,000 – $21,999.99"]["Admin Fee"] - advanced_pay) * commissionTable["Tier4/ $18,000 – $21,999.99"]["Commision Rate"]
            if pay > 0:
                print(f"The monthly pay is ${pay}")
            if pay < 0: 
                print (f"The amount owing is ${abs(pay)}")
                
            salesLst.append(monthly_sales)
            paymentLst.append(pay + advanced_pay)

        if 22000 <= monthly_sales < 100000:
            pay = (monthly_sales * commissionTable["Tier5/ $22,000 - $100,000.00"]["Commision Rate"]) - advanced_pay - commissionTable["Tier5/ $22,000 - $100,000.00"]["Admin Fee"]
            if pay > 0:
                print(f"The monthly pay is ${pay}")
            if pay < 0: 
                print (f"The amount owing is ${abs(pay)}")
        
            salesLst.append(monthly_sales)
            paymentLst.append(pay + advanced_pay)

        while True:
            anotha1 = input("Are there more sales person? (Y/N) ")
            try: 
                if anotha1.upper() == "N":
                    another = False
                    break
                elif anotha1.upper() == "Y":
                     break               
                else:
                    print("Invalid input. Enter either 'Y' or 'N' ")   
                    
            except ValueError:
                print("Invalid value. Try again. Enter either 'Y' or 'N' ")
                    
                
    print_summary(salesLst, paymentLst)   
              


if __name__ == "__main__":
    main()