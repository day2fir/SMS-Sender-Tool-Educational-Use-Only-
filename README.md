
# SMS Sender Tool (Educational Use Only)

This project provides a Python script to send SMS messages using Termux on an Android device. **Use responsibly and only for ethical purposes.**

---


## **Requirements**
- Android device with Termux installed.
- Python installed in Termux.
- Access to Termux SMS functionality.

---

## **Installation**

1. **Install Termux:**
   Download and install Termux from the [Google Play Store](https://play.google.com/) or [F-Droid](https://f-droid.org/).

2. **Install Required Packages:**
   Open Termux and run:
   ```bash
   pkg update && pkg upgrade
   pkg install python
   pkg install git
   ```

3. **Clone This Repository:**
   ```bash
   git clone https://github.com/day2fir/SMS-Sender-Tool-Educational-Use-Only-

4. **Navigate to the Repository Directory:**
   ```bash
   cd 
   ```

5. **Install Python Dependencies:**
   If there is a `requirements.txt`, run:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

1. **Create the Script:**
   Use the following code and save it as `spam_sms.py`:
   ```python
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
   ```

2. **Make the Script Executable:**
   ```bash
   chmod +x spam_sms.py
   ```

3. **Run the Script:**
   Use the following command to send SMS:
   ```bash
   python spam_sms.py <phone_number> <message> <count>
   ```
   Example:
   ```bash
   python spam_sms.py 1234567890 "Hello, this is a test!" 5
   ```

---

## **Disclaimer**
This tool is designed for educational and testing purposes only. Unauthorized or unethical use, including spamming, may violate laws and result in consequences. The author is not responsible for misuse.

