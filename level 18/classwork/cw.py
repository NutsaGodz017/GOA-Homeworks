#1) შექმენით while ციკლი რომელიც გამოიტანს კენტ რიცხვებს 100-იდან 300-მდე

i = 100
while i <= 300:
    i += 3
    print(i)

#2) მოხმარებელს შემოატანინეთ თავისი გამოცდის ქულა, შემდეგ პირობითი განხცადების საშვალებით შეამოწმეთ ეს ქულა მეტია თუ 50-ზე, თუ მეტია დაუბეჭდეთ რომ გამოცდა ჩააბარა

score = int(input("whats your test grade?: "))

if score > 50:
    print("good job!")

else:
    print("try harder...")