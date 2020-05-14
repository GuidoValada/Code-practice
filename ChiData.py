import csv

f = open('Food_Inspections.csv')
restaurants= list(csv.DictReader(f))


restaurants = [restaurant for restaurant in restaurants if restaurant['Results'] == 'Fail'][:1]
print(restaurants)