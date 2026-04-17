import logging 
import os 
from datetime import datetime 

log_file = f"{datetime.now().strftime('%m-%d-%y-%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(),'logs')
os.makedirs(logs_path,exist_ok=True)
log_file_path = os.path.join(logs_path,log_file)

logging.basicConfig(
    level= logging.INFO,
    filename= log_file_path,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

