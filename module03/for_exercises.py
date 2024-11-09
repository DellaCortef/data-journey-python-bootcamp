# exercise 06
text = "The Master's Degree in the Postgraduate Program in Applied Computing develops research activities on various topics in Computer Science training and qualifying professionals teachers and researchers from different areas of exact and technological sciences The faculty is interdisciplinary in nature and has active researchers nationally and internationally Currently we carry out projects with several companies and development agencies working hard for regional and national development Topics such as Artificial Intelligence Computer Vision Software Engineering Smart Cities Internet of Things Cloud and Fog Computing E-Health Augmented and Virtual Reality and 5G Mobile Communication are some topics covered in the Master's course"
words = text.split()
words_count = {}

for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
    
print(words_count)


# exercise 07
number_list = [10, 20, 30, 40, 50]
number_norm = min(number_list) + max(number_list)

number_list_norm = [(x / number_norm) for x in number_list]

print(number_list_norm)


# exercise 08
users = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": ""},
    {"name": "Carol", "email": "carol@example.com"},
    {"name": "", "email": "don@example.com"}
]

valid_email_users = [user for user in users if user["email"]]
valid_name_users = [user for user in users if user["name"]]

print(valid_email_users, valid_name_users)


# exercise 09
number_list = range(1, 11)

# True/False for the math
even = [number % 2 == 0 for number in number_list]

# number that match the condition
even = [number for number in number_list if number % 2 == 0]

print(even)


# exercise 10
sales = [
    {"category": "house", "amount": 1200},
    {"category": "books", "amount": 200},
    {"category": "house", "amount": 800},
    {"category": "books", "amount": 3000}
]

total_category = {}
for sale in sales:
    category = sale["category"]
    amount   = sale["amount"]
    if category in total_category:
        total_category[category] += amount
    else:
        total_category[category] = amount

print(total_category)