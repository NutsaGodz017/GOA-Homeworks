#1) შექმენით პროგრამა, რომელშიც მომხმარებელს შემოატანინებთ სახელსა და გვარს, შემდეგ კი დაუბეჭდავთ ერთად
name = input("what is your name? ")
lastname = input("what is your last name? ")

print(name + ' ' + lastname)

"""2) მომხმარებელს input-ის საშვალებით შემოტანინეთ ორი რიცხვი number1 და number2 შემდეგ კი დაბეჭდეთ მათი ჯამი. ასევე შექმენით level-ის ცვლადი რომელშიც მომხამრებელს შემოაყვანინებთ მათ ამჟამინდელ level-ს, შეეცადეთ level-ის მნიშვნელობას დაუმატოთ ერთი და ისე დაბეჭდოთ. მიღებული შედეგებით გამოიტანეთ დასკვნა და დაწერეთ კომენტარებით"""
num1 = input("first number: ")
num2 = input("second number: ")

print(num1 + num2)

your_lvl = input("your current lvl: ")
print(your_lvl + 1)