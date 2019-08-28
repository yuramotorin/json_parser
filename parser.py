import json
with open('output.json', 'r') as f:
    dict = json.load(f)     
for key in dict:
    print(key['id'])
print("\n")    
input("Press Enter to continue...")
