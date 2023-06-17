import os
import csv
import locale

locale.setlocale(locale.LC_ALL, 'en_AU')

budget_path = os.path.join('PyBank','Resources', 'budget_data.csv')

date = []
amount = []

with open(budget_path) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter = ",")
    print (budget_reader)
    budget_data = next(budget_reader)
    print(f"Budget Header: {budget_data}")
    for data_row in budget_reader:
        date.append(data_row [0])
        amount.append(float(data_row[1]))
    #print (date)

#how many months?
unique_dates = set (date)
total_dates = len(unique_dates)
print (total_dates)

#sum total amount 

Total_amount = sum(amount)
print (Total_amount)

#here we go looping again - remember corrections from VBA!!!

Ttl_chg_amnt = []
init_amnt = amount[0]
Sum_Ttl_chg_amnt = 0
init_amnt = amount[0]
Ttl_chg_count = enumerate(Ttl_chg_amnt)

for amnt in amount[1:]:
    chg_amnt = amnt - init_amnt
    Sum_Ttl_chg_amnt += chg_amnt
    init_amnt = amnt

Avg_chg_amount = Sum_Ttl_chg_amnt / (total_dates - 1)    
print (Avg_chg_amount)

#find greatest inrease and decrease

Sum_Ttl_chg_amount = 0
init_amount = [0]
max_inc = 0
max_inc_date = ""
min_inc = 0
min_inc_date = ""

for i in range(1, len(amount)):
    chg_amnt = amount[i] - init_amnt
    Sum_Ttl_chg_amnt += chg_amnt
    init_amnt = amount[i]
    if chg_amnt > max_inc:
        max_inc = chg_amnt
        max_inc_date = date[i]
    elif chg_amnt < min_inc:
        min_inc = chg_amnt
        min_inc_date= date[i]
    

with open("PBmain_Print_Result.txt", 'w') as f:

    print ("Financial Analysis", file=f)
    print("-------------------------------------", file=f)
    print (f"Total months:  {total_dates}", file=f)
    print ("Total: ${:.0f}" .format(Total_amount), file=f)
    print ("Average change:  ${:.2f}" .format(Avg_chg_amount), file=f)
    print ("Greatest increase in profits:  " + (max_inc_date) + "  (${:.0f})" .format(max_inc), file=f)
    print ("Greatest decrease in profits:  " + (min_inc_date) + "  (${:.0f})" .format(min_inc), file=f)

#export results to .txt file

