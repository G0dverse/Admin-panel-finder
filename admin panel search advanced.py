import requests
from urllib.parse import urljoin

# Function to load admin paths from admin.txt
def load_admin_paths(filename="admin.txt"):
    with open(filename, "r") as file:
        # Read all lines, strip whitespace, and filter out empty lines
        admin_paths = [line.strip() for line in file.readlines() if line.strip()]
    return admin_paths

def check_admin_panel(url, admin_paths):
    # Loop through each admin panel path
    for path in admin_paths:
        # Construct the full URL
        full_url = urljoin(url, path)
        try:
            # Send a GET request to the admin URL
            response = requests.get(full_url, timeout=5)
            
            # Check if the response status code is 200 (OK) or 403 (Forbidden)
            if response.status_code == 200:
                print(f"[+] Admin panel found at: {full_url} (Status: 200 OK)")
            elif response.status_code == 403:
                print(f"[+] Access denied to {full_url} (Status: 403 Forbidden) - Potential admin panel")
            else:
                print(f"[-] No admin panel found at: {full_url} (Status: {response.status_code})")
        except requests.exceptions.RequestException as e:
            # Handle exceptions (timeouts, connection issues, etc.)
            print(f"[-] Error accessing {full_url}: {str(e)}")

def main():
    # Ask for user input for the base URL
    base_url = input("Enter the base URL of the website (e.g., https://example.com): ").strip()
    
    # Ensure the URL starts with http or https
    if not base_url.startswith('http'):
        base_url = 'http://' + base_url

    # Load the admin panel paths from admin.txt
    admin_paths = load_admin_paths()

    # Check for admin panel URLs
    check_admin_panel(base_url, admin_paths)

if __name__ == "__main__":
    main()