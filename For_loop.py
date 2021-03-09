
animals = {'chickens': 30, 'cow': 730, 'pigs': 75, 'horse': 400, 'cockatoo': 47}

shipment = []
shipment_weight = 0
max_weight = 600

for animal, weight in animals.items():
    print(f'Current shipment weight: {shipment_weight}')
    
    if weight + shipment_weight < max_weight:
        print(f"Adding {animal} with weight of {weight}\n")  
        shipment.append(animal)
        shipment_weight += weight
                 
    elif weight + shipment_weight > max_weight:
        print(   f"\nskipping {animal} with weight of {weight}\n")
        continue
        
    else: 
        print("You have passed the weight limit")
        break
    
print(f"\n Final Shipment Weight {shipment_weight}")
print(f" Final Shipment {shipment}")