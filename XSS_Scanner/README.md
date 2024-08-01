# Advanced XSS Scanner

## Overview
This tool is designed to scan a website for XSS vulnerabilities. It crawls the entire site, tests forms with XSS payloads, and reports any vulnerabilities found.

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/XSS_Scanner.git
    ```
2. **Navigate into the directory:**
    ```bash
    cd XSS_Scanner
    ```
3. **Install required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To run the XSS scanner:

### Basic Scan:
```bash
python xss_scanner.py --url "http://example.com"
