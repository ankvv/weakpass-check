import requests
import argparse

BASE_URL = "https://weakpass.com/api/v1"

def get_json_response(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError:
        if response.status_code == 404:
            return "No data found."
        elif response.status_code == 500:
            return "An error occurred: server error."
        else:
            return "An error occurred."

def get_range(prefix, filter_type=None, hash_type="md5"):
    url = f"{BASE_URL}/range/{prefix}"
    params = {"filter": filter_type, "type": hash_type}
    return get_json_response(url, params)

def search_hash(hash_value):
    url = f"{BASE_URL}/search/{hash_value}"
    result = get_json_response(url)
    return None if result == "No data found." else result

def list_wordlists():
    url = f"{BASE_URL}/wordlists"
    return get_json_response(url)

def search_hashes_from_file(file_path):
    found_hashes = {}
    with open(file_path, 'r') as file:
        for hash_value in file:
            hash_value = hash_value.strip()
            if hash_value:
                result = search_hash(hash_value)
                if result:
                    found_hashes[hash_value] = result
    return found_hashes

def main():
    parser = argparse.ArgumentParser(description="Interact with the Weakpass API to manage password hashes.")
    subparsers = parser.add_subparsers(dest='command')

    range_parser = subparsers.add_parser('range', help='Retrieve hash-password pairs based on prefix')
    range_parser.add_argument('prefix', help='Hash prefix (5-64 chars, hex only)')
    range_parser.add_argument('--filter', choices=['hash', 'pass'], help='Show only hash or password')
    range_parser.add_argument('--type', default='md5', choices=['md5', 'ntlm', 'sha1', 'sha256'], help='Hash type (default: md5)')

    search_parser = subparsers.add_parser('search', help='Search for a supplied hash or hashes in the database')
    group = search_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('hash', nargs='?', help='The hash to search for (32-64 chars, hex only)')
    group.add_argument('--file', type=str, help='File containing hashes (one per line)')

    wordlists_parser = subparsers.add_parser('wordlists', help='Get the list of available wordlists')

    args = parser.parse_args()

    if args.command == 'range':
        result = get_range(args.prefix, args.filter, args.type)
        print(result)

    elif args.command == 'search':
        if args.hash:
            result = search_hash(args.hash)
            print(result if result else "Hash not found.")
        elif args.file:
            found_hashes = search_hashes_from_file(args.file)
            if found_hashes:
                for hash_value, details in found_hashes.items():
                    print(f"{hash_value}: {details}")
            else:
                print("No hashes found.")

    elif args.command == 'wordlists':
        result = list_wordlists()
        print(result)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
