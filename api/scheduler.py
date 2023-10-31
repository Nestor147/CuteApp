import schedule
import time
from api.utils import generar_mensaje_diario


schedule.every().day.at("20:53").do(generar_mensaje_diario)

while True:
    schedule.run_pending()
    time.sleep(1) 