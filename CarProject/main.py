import time
from lib.functions import CarProjectClient

# extracting the registration no. from car_input.text
num_plates = CarProjectClient().get_num_plates()
print(f'Found vehicle registration {num_plates}')
print(f'\33[92mChecking vehicle identity and comparing it to car_output.txt.........\33[0m')
time.sleep(2)

# Feeding the reg no. to https://cartaxcheck.co.uk/ and comparing the output
# with car_output.txt

for i in range(len(num_plates)):
    veh_info = CarProjectClient().get_veh_details(num_plates[i])
    CarProjectClient().verify_output(veh_info)
