import argparse
import requests

BASE_URL = "http://127.0.0.1:8000/books"

API_KEY = "mysecretkey"

HEADERS = {
    "Access_key": API_KEY
}

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

# Add
add_parser = subparsers.add_parser("add")
add_parser.add_argument("title")
add_parser.add_argument("author")

# List
subparsers.add_parser("list")

# Delete
delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("id", type=int)

args = parser.parse_args()

if args.command == "add":
    response = requests.post(
        BASE_URL,
        json={
            "title": args.title,
            "author": args.author
        },
        headers=HEADERS
    )
    print(response.json())

elif args.command == "list":
    response = requests.get(
        BASE_URL,
        headers=HEADERS
    )
    print(response.json())

elif args.command == "delete":
    response = requests.delete(
        f"{BASE_URL}/{args.id}",
        headers=HEADERS
    )

    if response.status_code == 204:
        print("Book deleted successfully.")
    else:
        print(response.json())