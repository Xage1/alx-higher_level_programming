#!/usr/bin/python3
"""script for testing status of web pages
"""
if __name__ == "__main__":
    import urllib.request

    url = "https://intranet.hbtn.io/status"

    # Add a User-Agent header to the request
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            bytes_content = response.read()
            content = bytes_content.decode('utf-8')
            print_str = '''Body response:
    \t- type: {}
    \t- content: {}
    \t- utf8 content: {}'''.format(type(bytes_content), bytes_content, content)
            print(print_str)
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
