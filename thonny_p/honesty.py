#Honesty calculator of storage comapnies
advertised_value = input("Enter advertised storage: ").strip().lower()
storage_type = advertised_value[-2:]
numerical_adv_value = advertised_value[:-2].strip()

if storage_type == "tb":
    discrepancy = (10**12)/(1024**4)
    
    print("Real capacity is",int(numerical_adv_value)*discrepancy,"tb")
elif storage_type == "gb":
    discrepancy = (10**9)/(1024**3)
    print("Real capacity is",int(numerical_adv_value)*discrepancy,"gb")
else :
    print("Enter valid storage type")