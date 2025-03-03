#!/usr/bin/env python
import sys

"""
 Daily heart rate exporter
 Turns Apple Health app export for a given day into a simple csv file
 Params:
    input file - Input file (.xml format, by default after export is export.xml)
    date - YYYY-MM-DD format
    (optional) outputFile - CSV output file location
    (optional) debug - If true, will print to the console
Usage:
    python exporter.py export.xml date exported
"""

def convertToCSV(file, date, outputFile=None, shouldPrint=None):
    file = open(file).read()
    lines = file.split('\n')
    filtered = []

    if outputFile is not None:
        output = open(outputFile, 'w+')
        output.write("date,heartrate\n")

    for line in lines:
        if "HKQuantityTypeIdentifierHeartRate" not in line:
            continue
        if "HKQuantityTypeIdentifierHeartRateVariabilitySDNN" in line:
            continue
        if date not in line:
            continue
        split = line.replace("<Record ", "").replace(" Record>", "").split('" ')
        lastPart = split[len(split) - 1]
        endIndex = len(lastPart) - 2
        number = float(lastPart[7:endIndex])

        datetime = split[6]
        datetime = datetime[datetime.index("\"")+1:]
        filtered.append({"datetime": datetime, "quantity": number})

        if outputFile is not None:
            output.write(datetime + "," + str(number) + "\n")
    if outputFile is not None:
        output.close()
    else:
        if shouldPrint is not None and shouldPrint is True:
            print(filtered)

    return filtered

def main():
    args = sys.argv[1:]
    if len(args) == 0 or len(args) == 1:
        print("Please specify an input file (export.xml), a date (YYYY-MM-DD), and optionally, an output file (output.csv).")
        return 0
    if len(args) == 2:
        convertToCSV(args[0], args[1], shouldPrint=True)
    else:
        convertToCSV(args[0], args[1], outputFile=args[2], shouldPrint=True)

if __name__ == '__main__':
    main()