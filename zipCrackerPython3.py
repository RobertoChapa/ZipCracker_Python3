# Python 3
import argparse
import zipfile
from threading import Thread

def main():
    parser = argparse.ArgumentParser(description='-f <zipfile> -d <dictionary>')
    parser.add_argument('-f', dest='zname',help='specify zip file')
    parser.add_argument('-d', dest='dname',help='specify dictionary file')
    args = parser.parse_args()

    if (args.zname == None) | (args.dname == None):
        print(parser.usage)
        
        exit(0)
    else:
        zname = args.zname
        dname = args.dname
        
        #assigns zipfile and dictionary to variables
        zFile = zipfile.ZipFile(zname)	
        passFile = open(dname)

        #reads lines and extracts in file
        for line in passFile.readlines():
            password = line.strip('\n')
            t = Thread(target=extractFile, args=(zFile, password))
            t.start()


#function to extract zipfile and test password
def extractFile(zFile, password):
        try:
            zFile.extractall(pwd=bytes(password,'utf-8'))
            print('[+] Found password ' + password + '\n')
        except:
            pass
  

if __name__ == '__main__':
	main()
