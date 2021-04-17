import time
import os

# try:
#     os.system('rm parallel.json')
#     os.system('rm serial.json')
# except Exception:
#     pass

with open("domains.txt",'r') as domains:
    content = domains.readlines()
    for i in content:
        dizin = i.strip('\n').replace('.','_')

        try:
            os.system(f'rm output/serial/{dizin}.json')
        except Exception:
            pass

        command1=f"./testssl.sh --ids-friendly -S -s --fast --jsonfile parallel.json --file {i} --parallel"
        command2=f"./testssl.sh --ids-friendly -S -s --fast --jsonfile output/serial/{dizin}.json {i}"
        print(command2)


        start = time.time()
        os.system(command2)
        end=time.time()

        print(f"Paralel'de Geçen Süre {end-start}")

# start = time.time()
# os.system(command2)
# end=time.time()
#
# print(f"Paralel'de Geçen Süre {end-start}")
