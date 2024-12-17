import os
import sys
import time

def send_sms(phone_number, message, count):
    for i in range(count):
        os.system(f'termux-sms-send -n {phone_number} {message}')
        time.sleep(1)  # Adjust the sleep time as needed

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python spam_sms.py <phone_number> <message> <count>")
        sys.exit(1)

    phone_number = sys.argv[1]
    message = sys.argv[2]
    count = int(sys.argv[3])

    send_sms(phone_number, message, count)