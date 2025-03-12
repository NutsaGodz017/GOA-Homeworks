box = "apples"
minutes = 15
P = 3.14

print(type(box))
print(type(minutes))
print(type(P))

#2) მომხმარებელს შემოატანინეთ თავისი სიმაღლე, შემდეგ შემოატანინეთ წლების რაოდენობა, მიღებული ინფორმაცია შეინახეთ ცვლადში და გამოუთვალეთ მომხმარებელს სავაურდო სიმაღლე იმ წლების შემდეგ რაც მან შემოიტანა თუ დაუშვათ ყოველ წელს სიმაღლე იზრდება 0.5-ით

#simaglis floatshi chawera
heigh = float(input("what is your heigh? "))
years = int(input("how many years passed after? "))
print((years * 0.5) + heigh)
