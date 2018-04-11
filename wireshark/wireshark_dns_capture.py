import sys
import re

def main(filename, args):
    print('starting...')
    capture = WiresharkDnsCapture(args[0])
    capture.find()
    print('DONE!')

class WiresharkDnsCapture():

    __dns_file_location = None
    __out_file = None
    __dns_domain = []

    def __init__(self, dns_file_location):
        self.__dns_file_location = dns_file_location
        out_file = "%s%s" % (dns_file_location, '.clean')
        self.__out_file = open(out_file, 'w')

    def find(self):
        print('entering find...')
        self.__createDnsList()
        self.__readDnsAndWriteToOut()

    def __createDnsList(self):
        print('entering __createDnsList...')
        with open(self.__dns_file_location) as file:
            for index, line in enumerate(file):
                domain_array = line.split("CNAME ")
                ip_array = re.findall( r'[0-9]{1,3}(?:\.[0-9]{1,3}){3}', line)
                if(len(domain_array) > 1 and len(ip_array) > 0):
                    domain = self.__cleanText(domain_array[1].split(" ")[0])
                    if(domain not in self.__dns_domain):
                        self.__dns_domain.append(domain)

    def __readDnsAndWriteToOut(self):
        print('entering __readDnsAndWriteToOut...')
        for domain in self.__dns_domain:
            self.__writeToOutFile(domain)

    def __writeToOutFile(self, line):
        self.__out_file.write("%s%s" % (line, "\n"))

    def __cleanText(self, text):
        return text.replace("\n", "")

if __name__ == '__main__':
    main(__file__, sys.argv[1:])
