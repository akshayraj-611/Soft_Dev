from datetime import datetime
import time

def time_until(target):
    now = datetime.now()
    return target - now

def main():
    Xmas_eve = datetime(2025, 12, 24)
    new_year = datetime(2026, 1, 1)
    easter = datetime(2026, 4, 5)   

    while True:
        print(f"Till Christmas eve: {time_until(Xmas_eve)}")
        print(f"Till new year:     {time_until(new_year)}")
        print(f"Till easter:       {time_until(easter)}")
        print("------------------------------")
        time.sleep(1)

if __name__ == "__main__":
    main()
