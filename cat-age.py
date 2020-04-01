#ask the user for their cat's age
cat_age = input('How old is your cat? ')
#convert to an integer
cat_age = int(cat_age)
#print one messageif it's a ktten, otherwise 
if cat_age >= 0: #we have a live cat?
    if cat_age < 2 and cat_age >=0:
        print('What a cute kitten!')

    elif cat_age >= 0 and (cat_age < 9 or cat_age >100):
        print('What a cute kitten!')

    else:
        print('what a boring cat')


#print = f'nice! she is, {cat_age()}'
#greeting = f'WELCOME, {customer_name.upper()}'


