
animals = {'chickens': 30, 'cow': 730, 'pigs': 75, 'horse': 400, 'cockatoo': 47}

shipment = ' '
shipment_weight = 0
max_weight = 600

for key, value in animals.items():
    
    while True:
        
        if value < max_weight:
            print(f'adding {key} to the shipment')
            key += shipment
            value += shipment_weight
        
        if value > max_weight:
            print('You have reached the weight limit')
            continue 
        