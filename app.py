from dotenv import dotenv_values
import schedule
import time
from get_curr import update_table

config = dotenv_values()

def main():

    schedule.every(5).hours.do(update_table)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
