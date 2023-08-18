#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = input("What is the total of check?\n")
total_float = float(bill)

num_guests = input("How many people ate?\n")
num_guests_int = int(num_guests)

tip = input("What percent do you want to add?\n")
tip_as_int = int(tip)

total_tip_perguest =  (total_float * (tip_as_int / 100)) / num_guests_int
portion_total = total_float / num_guests_int
result = total_tip_perguest + portion_total
result_round = round(result, 2)
print(f"Each guest should pay ${result_round}")
