import sys
import json

def main(filename, args):
    print('starting...')
    csv_to_json = CsvToJson(args[0])
    csv_to_json.toJsonFile()
    print('DONE!')

class CsvToJson():

    __file_location = None
    __json_file = None
    __headers = None

    def __init__(self, file_location):
        self.__file_location = file_location
        self.__json_file = open('out.json', 'w')
        self.__headers = []

    def toJsonFile(self):
        print('entering toJsonFile...')
        self.__readCsvAndWriteToJson()

    def __readCsvAndWriteToJson(self):
        print('entering readCsvAndWriteToJson...')
        with open(self.__file_location) as csv_file:
            for index, line in enumerate(csv_file):
                if index == 0:
                    self.__storeHeaders(line)
                else:
                    json_line = self.__convertCsvLineToJson(line)
                    self.__writeToJsonFile(json_line)

    def __convertCsvLineToJson(self, csv_line):
        line_dict = {}
        csv_values = csv_line.split(',')
        for index, header in enumerate(self.__headers):
            value = ""
            if index < len(csv_values):
                value = csv_values[index]
            line_dict[header] = self.__cleanText(value)
        json_line = json.dumps(line_dict, separators=(', ',': '), sort_keys=True)
        return json_line

    def __writeToJsonFile(self, json_line):
        self.__json_file.write("%s\n" % json_line)

    def __storeHeaders(self, line):
        print('entering storeHeaders...')
        raw_headers = line.split(',')
        for header in raw_headers:
            self.__headers.append(self.__cleanText(header))

    def __cleanText(self, text):
        return text.replace("\"", "").replace("\n", "")

if __name__ == '__main__':
    main(__file__, sys.argv[1:])
