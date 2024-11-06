# SQL_Parasite

## Overview

This tool is designed to test for SQL injection vulnerabilities in web applications. It supports error-based, time-based, and union-based SQL injection techniques.
 ## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pulkit6732/SQL_Parasite
   cd SQL_Parasite
   pip install -r requirements.txt
## USAGE 
python3 sql_injection_tool.py <url> <parameter> [--proxy <proxy>]

##NOTE 
Make sure to edit the payloads.py as per your usage i will make a repo for the payloads for every vulnnebirity detection  
You can edit the files if you having any error as per your system usage 

#Example 
python3 sql_injection_tool.py "http://example.com/page.php" "id" 


