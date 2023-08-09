import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies=('http': 'http://localhost:8080','https': 'https://localhost:8080')

def main():
      if len(sys.argv)!=2:
            print("(+) Usage: %s <url>"%sys.argv[0])
            print("(+) Example: %s www.example.com " % sys.argv[0])
            sys.exit(-1)
      url=sys.argv[1]
      print("(+) Finding admin panel...")
      delete_user(url)


if __name__ == '__main__':
      main()