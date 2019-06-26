import os
from datetime import datetime

#lista com os nomes dos bancos que se deseja realizar o backup
bases = ["dataset_1",
         "dataset_2",
         "dataset_3",
         "dataset_4"]

# comando = "/opt/lampp/bin/mysqldump -u root granja > %s-%s.sql"
comando = "mysqldump -u root %s > %s-%s.sql"
data_hj = datetime.today()
dt_string = data_hj.strftime("%d_%m_%Y_%H_%M_%S")
for base in bases:
    print(comando % (base, bases, dt_string))
    try:
        os.system(comando % (base, base, dt_string))
    except Exception as e:
        print(e)
