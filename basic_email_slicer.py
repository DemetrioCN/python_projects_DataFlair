
print("\n")
print(10*"-", "Email Slicer", 10*"_")
print("\n")

email = input("Introduce your email: ").strip()

user_name = email[:email.index('@')]

domain = email[email.index('@')+1:]

output = f'Your usernam is {user_name} and your domain name is {domain}'

print(output)
print('\n')

