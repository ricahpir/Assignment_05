#------------------------------------------#
# Title: CDInventory_Starter.py
# Desc: Edited script to 
# Change Log: (Who, When, What)
# ricahpir, 2021-02-13, Updated File:
# Imported CSV
# Added functionality to load data from txt file
# Added functionality to delete dic from list of dics
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # Replaced list of lists with list of dicts
dicRow = {}  # dic of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

import csv #ricahpir added: import csv, so program can save data to CDInventory.txt doc OR load data from it  

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allows the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. User can exit program if they so choose
        break
    if strChoice == 'l':
        # 6. ricahpir added: Functionality of loading existing data from a txt file
        with open('CDInventory.txt') as csvfile:
            for i in csv.reader(csvfile):
                print(', '.join(i)) 
        print(' ')
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Data can be added to the table (2d-list) each time the user wants 
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {"ID": intID, "title": strTitle, "artist": strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. The current data can be display to the user, each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
    elif strChoice == 'd':
        # 7. ricahpir added: Functionality to delete dictionary from lstTbl using ID key  
        for row in lstTbl:
            print('{}\t{} (by:{}'.format(*row.values()))
        print()
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        rowNr = -1
        for row in lstTbl:
            rowNr += 1
            if row['ID'] == intIDDel:
               del lstTbl[rowNr]
               break      
        pass
    elif strChoice == 's':
        # 4. The user can save the data to a text file CDInventory.txt if they so choose
        objFile = open(strFileName, 'a') 
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

