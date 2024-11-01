# weakpass-check
This Python program interacts with the Weakpass API to manage password hashes. It allows users to search for hashes, retrieve hash-password pairs based on prefixes, and get a list of available wordlists.

## ⭐ Like this project?

If you find it helpful, please give it a star! ⭐️ It helps others discover this project and motivates me to keep improving it.

### 🌟 Current Stars: ![GitHub stars](https://img.shields.io/github/stars/ankvv/weakpass-check?style=social)

## Features

- **Search for a Hash**: Look up a specific hash or a list of hashes from a file.
- **Retrieve Hash Ranges**: Get a list of hash-password pairs based on a specific prefix.
- **List Available Wordlists**: Fetch a list of wordlists available in the Weakpass API.

## Prerequisites

- Python 3.x
- `requests` library (can be installed via `pip install requests`)

## Usage

You can run this program from the command line. Below are the available commands:

### 1. Search for a Hash

To search for a single hash:
```bash
python weakpass-check.py search <hash>
```
To search for hashes from a file (one hash per line):
```bash
python weakpass-check.py search --file <file_path>
```
### 2. Retrieve Hash Ranges

To retrieve hash-password pairs based on a prefix:
```bash
python weakpass-check.py range <prefix> [--filter {hash,pass}] [--type {md5,ntlm,sha1,sha256}]
```
### 3. List Available Wordlists

To get a list of available wordlists:
```bash
python weakpass-check.py wordlists
```
## Example

# Search for a specific hash
```bash
# Searching for a single hash
python weakpass-check.py search 5f4dcc3b5aa765d61d8327deb882cf99
```
# Search for hashes listed in a file
```bash
python weakpass-check.py search --file hashes.txt
```
# Retrieve hash-password pairs for a prefix
```bash
python weakpass-check.py range a1b2c3
```
# List available wordlists
```bash
python weakpass-check.py wordlists
```

## Error Handling

The program includes basic error handling for HTTP requests. It will return meaningful messages for common issues, such as:

404: No data found<br>
500: Server error<br>
General network errors

### 6. Contributions

Contributions are welcome! Please fork the repository and submit a pull request.
