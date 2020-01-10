dog_years = int(input('Enter "dog" years: '))

if dog_years < 3:
    human_years = dog_years*10.5
else:
    human_years = 21 + (dog_years-2)*4

print(f"Human years: {human_years}")