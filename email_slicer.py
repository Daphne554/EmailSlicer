emailId = input("Enter your email: ")
username = emailId[0:emailId.index("@")]
domain = emailId[emailId.index("@")+1: ]

print(f"Username - {username}")
print(f"Domain - {domain}")
