обща_стайна_квадратура_м2 = float(input())
цена_паркет_за_1_м2 = float(input())

колко_метра_первази = float(input())
цена_за_1_метър_первази = float(input())

колко_метра_лайсни = float(input())
цена_за_1_метър_лайсни = float(input())

цена_за_подложка_за_1_м2 = float(input())

цена_труд_за_1_м2 = float(input())
цена_транспорт = float(input())

цена_за_други_консумативи = float(input())

процент_отстъпка = float(input()) 


обща_цена_на_паркет = обща_стайна_квадратура_м2 * цена_паркет_за_1_м2
обща_цена_первази = колко_метра_первази * цена_за_1_метър_первази
обща_цена_лайсни = колко_метра_лайсни + цена_за_1_метър_лайсни
обща_цена_подложка = цена_за_подложка_за_1_м2 * обща_стайна_квадратура_м2
обща_цена_труд = цена_труд_за_1_м2 * обща_стайна_квадратура_м2

обща_цена_без_отстъпка = обща_цена_на_паркет + обща_цена_первази + обща_цена_лайсни + обща_цена_подложка
+ обща_цена_труд + цена_транспорт + цена_за_други_консумативи

обща_цена_с_отстъпка = обща_цена_без_отстъпка - (обща_цена_без_отстъпка * процент_отстъпка/100)

print(f"Цената на паркета за стая с квадратура от {обща_стайна_квадратура_м2} м2 е {обща_цена_на_паркет} лв." 
      f"\n Цената на первазите за {колко_метра_первази} линейни метра е {обща_цена_первази} лв." 
      f"\n Цената на лайсните за {колко_метра_лайсни} линейни метра лайсни е {обща_цена_лайсни} лв."
      f"\n Цената на подложката за цялата стайна квадратура е {обща_цена_подложка} лв."
      f"\n Цената на труда за цялата стайна квадратура е {обща_цена_труд} лв."
      f"\n Цената за транспорт е {цена_транспорт} лв."
      f"\n Цената за други допълнителни консумативи е {цена_за_други_консумативи} лв."
      f"\n Отстъпката е {процент_отстъпка} %./"
      
      f"\n Общата цена с материали, труд и консумативи без отстъпка е {обща_цена_без_отстъпка} лв., а с отстъпката е {обща_цена_с_отстъпка} лв.")

