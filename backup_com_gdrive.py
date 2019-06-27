import os
from datetime import datetime

#lista com os nomes dos bancos que se deseja realizar o backup
bases = ["dataset_1",
         "dataset_2",
         "dataset_3",
         "dataset_4"]

save_folder = os.path.dirname(os.path.abspath(__file__))
# comando = "/opt/lampp/bin/mysqldump -u root granja > %s-%s.sql"
comando = "mysqldump -u root %s > %s/%s-%s.sql"
comando_upload_folder = "gdrive upload %s --recursive"
data_hj = datetime.today()
dt_string = data_hj.strftime("%d_%m_%Y_%H_%M_%S")
for base in bases:
    print(comando % (base,save_folder, base, dt_string))
    try:
        os.system(comando % (base,save_folder, base, dt_string))
    except Exception as e:
        print(e)
#faz o upload dos arquivos para o drive do google
os.system(comando_upload_folder % save_folder)
