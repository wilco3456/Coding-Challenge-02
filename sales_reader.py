### This code was developed and tested using python 2.7.12 ###

import collections
import json

def JSONReader():
    filename = "sales.json"
    
    #Read JSON data into the datastore variable
    if filename:
        with open(filename, 'r') as f:
            datastore = json.load(f)

            #Return the datastore variable
            return datastore

def DictionaryProcess(JSON_dictionary):
    totals = {}
    highest_month = 0

    #Reads each record from the JSON datastore 
    for record in JSON_dictionary:
        date = record.get("date").split("-")
        month = int(date[1])    #Only the month is needed
        agent = record.get("agent")
        amount = record.get("amount")

        #Keeps the highest month in store
        if highest_month < month:
            highest_month = month

        #Creates new record if not already present
        if agent not in totals:
            totals[agent] = [[month, 1, amount]]
        else:
            #Verify if month is present and record its occurence
            flag = False
            val = 0
            for agent_record in totals[agent]:
                if month == agent_record[0]:
                    flag = True
                    break
                val += 1

            #Increments sale number and total amount if the month is present
            if flag:
                totals[agent][val][1] += 1
                totals[agent][val][2] += amount
            else:
                #New month is appended on abscence
                totals[agent].append([month, 1, amount])

    #Sorts the values by month
    for key, item in totals.items():
        totals[key] = sorted(item, key = lambda x: int(x[0]))

    #Sorts the keys by alphabetical order
    totals = collections.OrderedDict(sorted(totals.items()))

    #Return processed dictionary and the highest month
    return totals, highest_month

def TableFormatter(totals, highest_month):
    #Keep store of all the months of the year
    keys = [1,2,3,4,5,6,7,8,9,10,11,12]
    values = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    months = dict(zip(keys, values))

    #Print the table header in 12 space format
    s = '%-12s' % ("Agent")
    for i in range(1, (highest_month+1)):
        month = months[i]
        s = s + '%-12s' % (month + " Sales")
        s = s + '%-12s' % (month + " Total")
    print(s)

    #Print the dictionary records in 12 space format
    for key, val in totals.items():
        s = '%-12s' % (key)
        for record in val:
            s = s + '%-12i' % record[1]
            s = s + '%-12.2f' % (float(record[2])/100)
        print(s)

def main():
    JSON_dictionary = JSONReader()
    totals, highest_month = DictionaryProcess(JSON_dictionary)
    TableFormatter(totals, highest_month)

if __name__ == "__main__":
    main()
