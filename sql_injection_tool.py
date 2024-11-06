import argparse
from scanner import Scanner
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def print_header():
    print(Fore.CYAN + "PLL SEC")  # Print "PLL SEC" in cyan color

def main():
    print_header()  # Print the header when the scanner starts
    parser = argparse.ArgumentParser(description='SQL Injection Testing Tool')
    parser.add_argument('url', type=str, help='Target URL')
    parser.add_argument('parameter', type=str, help='Vulnerable parameter')
    parser.add_argument('--proxy', type=str, help='Proxy server (e.g., http://127.0.0.1:8080)')
    args = parser.parse_args()

    print("\nSelect the type of SQL injection scan:")
    print("1. Error-based SQL Injection")
    print("2. Time-based SQL Injection")
    print("3. Union-based SQL Injection")
    
    choice = input("Enter your choice (1/2/3): ")
    
    scanner = Scanner(args.url, args.parameter, args.proxy)
    if choice == '1':
        scanner.run_error_based()
    elif choice == '2':
        scanner.run_time_based()
    elif choice == '3':
        scanner.run_union_based()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()