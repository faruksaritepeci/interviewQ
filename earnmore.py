# Author: FARUK SARITEPECİ
# Date: 3.12.2022

# directory'deki örnek "lists.txt" kullanılabilir, veya uygun formatta yeni list oluşturulabilir
filename = input("Enter list file path:")

try:
    f = open(filename, "r")
    
except IOError:
    print("Couldn't open file!")
    quit()

#verilecek olan 3 listeyi tut    
list1 = []
list2 = []
list3 = []

try:
    line = f.readline()
    nums = line.split(",") #virgüllerle ayırılmış sayıları liste ekle
    for num in nums:
        list1.append(int(num))
    
    line = f.readline()
    nums = line.split(",")
    for num in nums:
        list2.append(int(num))
        
    line = f.readline()
    nums = line.split(",")
    for num in nums:
        list3.append(int(num))
        
    del num # ileride muhtemel sorun yaratmaması için temp variable'ları sil
    del nums
        
except IOError:
    print("Invalid format for list! Use comma to seperate elements in the same line \nGive at least 3 lists")
    f.close()
    quit()

def OptimalBuySell(priceList: list) -> list:
    """Calculates best steps to buy and sell the stock

    Args:
        list (priceList): Price history list
        
    Return:
        list (steps):     Returns the time of each transaction and the amount of goods
    """
    t = -1 # loop başında günü ilerleterek başladığı için -1 al
    money = 0 # toplam para (başlangıç parası = ilk ürün alınan gündeki ürün fiyatının 1 adeti)
    bought = 0 # satın alınan ürün sayısı
    steps = [] # (time, amount) verilerini tutan adımları tutar (işlem tarihi, ürün alım/satım ["+" -> alım, "-" -> satım])
    
    for num in priceList:
        t += 1
        if bought == 0 and t+1 < len(priceList): # elinde ürün yoksa (satın almak için uygun mu diye bak)
            if num < priceList[t+1]: # en kötü bir sonraki gün daha pahalıya satabilecek isen
                if money == 0: #ilk satın alım için
                    bought = 1
                    steps.append( (t, 1) )
                    print("Bought", 1, "at day", t+1, "- at", priceList[t],"money each")
                
                else:
                    bought = money // priceList[t] # paranla alabileceğin kadar al
                    money -= bought * priceList[t]
                    steps.append( (t, bought) )
                    print("Bought", bought, "at day", t+1, "- at", priceList[t],"money each")
                    
            else: # daha pahalı olmicaksa, bugünü atla
                continue
        
        elif t+1 < len(priceList): # eğer satılcaksa ve son gün değilse
            if num > priceList[t+1]: # yarın fiyat düşcekse bugün sat
                money += bought * priceList[t]
                print("Sold at day", t+1, "for", priceList[t]*bought, "and made", bought*(priceList[t] - priceList[steps[-1][0]]), "profit")
                steps.append( (t, -bought) )
                bought = 0
                
            else:
                continue # fiyat düşmicekse satma, bugünü atla
            
        else: # son gün için
            if bought == 0: # elinde ürün yoksa loop bitti
                continue
            else: # son günü kar ile sat
                money += bought * priceList[t]
                print("Sold at day", t+1, "for", priceList[t]*bought, "and made", bought*(priceList[t] - priceList[steps[-1][0]]), "profit")
                steps.append( (t, -bought) )
                bought = 0
                
    print("\nFinal money:", money)
    if len(steps) > 0:
        print("Total profit:", money - priceList[steps[0][0]])
        if priceList[steps[0][0]] > 0:
            print("Total ROI:", 100*(money - priceList[steps[0][0]]) / priceList[steps[0][0]], "%")
        else:
            print("ROI incalculable: price of a good cannot be zero or negative")
    else:
        print("No operations done, therefore no profit recorded.")
    print("### Reached end of time for this list.\n")
    return steps
                    
                
# Ben steps listesini kullanmadım bu kodda, fakat başka fonksiyonlar için işe yarayabilir diye uyarladım.
steps1 = OptimalBuySell(list1)

steps2 = OptimalBuySell(list2)

steps3 = OptimalBuySell(list3)

f.close()