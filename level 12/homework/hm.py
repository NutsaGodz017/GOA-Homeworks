#2) გააკეთეთ 5-5 მაგალითი თთოეულ შედარების ოპერატორზე (>, >=, <, <=, ==, !=), გვერდზე კომენტარის საშვალებით მიუთითეთ თუ რომელ boolean მნიშვნელობას გამოიტანას, აიღეთ მრავალფეროვანი კომბინაციები, შეეცადეთ გქონდეთ ყველა ვარიანტი

print(5 == 5)
print(7 == 6)
print(3 > 2)
print(3 < 4)
print(7 == 10)
print(15 != 14)
print(16 >= 15)
print(56 <= 77)
print(16 != 66)
print(78 > 99)
print(177 == (100 + 77))
print(19 < (10 - 7))
print(79 != (6 * 16))
print(89 != (34 / 4))

#3) შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ შედარების ოპერაციათა შედეგებს, შედარების ოპერაციას გვერდზე კომენტარის საშვალებით მიუწერეთ მისი შედეგი (boolean მნიშვნელობა) და ახსენით რა განსხვავებაა ოპერატორსა და ოპერაციას შორის

cvladi = 6 > 27 #false
print(bool(cvladi))

cvladi2 = 67 == 60 + 7 #true
print(bool(cvladi2))

cvladi3 = 179 != 155 #true
print(bool(cvladi3))

cvladi4 = 88 < 79 - 16 #false
print(bool(cvladi4))

cvladi5 = 67 >= 55 #true
print(bool(cvladi5))


#4) შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ ლოგიკურ და შედარების ოპერაციათა შედეგებს (უნდა იყოს შედარების და ლოგიკური ოპერატორები ერთად მაგალითად temperature > 30 and not cloudy), გვერდზე კომენტარის საშვალებით მიუწერეთ ეს შედეგი (boolean მნიშვნელობა) აიღეთ მრავალფეროვანი კომბინაციები

temperature = -1
rainy = True
#false
can_go_out = temperature >= 10 and not rainy
print(can_go_out)


distance = 17 
snowy = False
#true
safe_trip = not snowy
print(safe_trip)


temperature = 39.4
sick = True
#false
feel_good = temperature < 38 and not sick
print(feel_good)


temperature = 2
snowy = False
#false
making_snowman = temperature < 0 and snowy is True
print(making_snowman)


distance = 38
rainy = True
#False
safe_trip_with_family = distance < 20 and rainy is False
print(safe_trip_with_family)
#6) Bonus დავალება
#შექმენით პროგრამა, რომელიც განსაზღვრავს productive ცვლადის მნიშვნელობას შემდეგი პირობების მიხედვით:
#read_pages ცვლადში ინახება წაკითხული გვერდების რაოდენობა (მთლიანი რიცხვი).
#free_time ცვლადში ინახება boolean მნიშვნელობა (True/False), რომელიც გვიჩვენებს, ჰქონდა თუ არა თავისუფალი დრო.
#productive ცვლადი იქნება ჭეშმარიტი (True), თუ მოსწავლემ წაიკითხა მინიმუმ 20 გვერდი და თავისუფალი დრო ჰქონდა.

read_pages = 30
free_time = True

productive = read_pages > 20 and free_time is True
print(productive)