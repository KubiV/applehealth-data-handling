import sys
from datetime import datetime, timedelta

# python exporter.py export.xml YYYY-MM-DD YYYY-MM-DD [output.csv]
# python exporter.py export.xml 2024-02-20 2024-02-25 output.csv

def convertToCSV(file, start_date, end_date, outputFile=None, shouldPrint=None):
    file = open(file).read()
    lines = file.split('\n')
    filtered = []

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    if outputFile is not None:
        output = open(outputFile, 'w+')
        output.write("date,heartrate\n")

    for line in lines:
        if "HKQuantityTypeIdentifierHeartRate" not in line:
            continue
        if "HKQuantityTypeIdentifierHeartRateVariabilitySDNN" in line:
            continue

        split = line.replace("<Record ", "").replace(" Record>", "").split('" ')
        lastPart = split[len(split) - 1]
        endIndex = len(lastPart) - 2
        number = float(lastPart[7:endIndex])

        datetime_str = split[6]
        datetime_str = datetime_str[datetime_str.index("\"")+1:]
        data_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S %z")

        if start_date <= data_datetime.replace(tzinfo=None) <= end_date:
            filtered.append({"datetime": datetime_str, "quantity": number})
            if outputFile is not None:
                output.write(datetime_str + "," + str(number) + "\n")

    if outputFile is not None:
        output.close()
    else:
        if shouldPrint is not None and shouldPrint is True:
            print(filtered)

    return filtered

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print("Please specify an input file (export.xml), a start date (YYYY-MM-DD), an end date (YYYY-MM-DD), and optionally, an output file (output.csv).")
        return 0
    if len(args) == 2:
        convertToCSV(args[0], args[1], args[1], shouldPrint=True)  # Pokud je pouze jeden den, použije se jako start i end
    elif len(args) == 3:
        convertToCSV(args[0], args[1], args[2], shouldPrint=True)
    else:
        convertToCSV(args[0], args[1], args[2], outputFile=args[3], shouldPrint=True)

if __name__ == '__main__':
    main()
