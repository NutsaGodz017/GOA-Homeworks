#1) შექმენით sum ცვლადი რომელშიც შეინახავთ 1-იდან 20-მდე რიცხვების ჯამს, ამისთვის გამოიყენეთ for ციკლი და range ინსტრუქცია, საბოლოოდ ერთხელ დაბეჭედეთ ჯამი

sum = 1
for num in range(1,20):
    sum += num
print(sum)

#2) მომხმარებელს შემოატანინეთ 2 რიცხვი, შემდეგ კი პირველი რიცხვიდან მეორეს ჩათვლით არსებული ყველა რიცხვი დაბეჭდეთ

num1 = int(input("first number: "))
num2 = int(input("second number: "))

for num in range(num1, num2, +1):
    print(num)
    


#3) შექმენით პროგრამა რომელიც მოხმარებელს შეეკითხება პაროლს სანამ სწორად არ ჩაწერს

Password = "ABC"
anonimus = ""

while anonimus != Password:
    anonimus = input("Password: ")