# name,code,country,lat,lon,elev,style,rwdir,rwlen,freq,desc,userdata,pics
#pylint: disable=C0103

import csv

#inputfile = csv.reader(open (sys.argv[1], 'r'))
#outputfile = sys.argv[1][:-4]+".kml"
with open("BGA TPs 2017 - Club frequencies.cup", newline='') as InputFile:
    with open("Frequency.csv", 'w', newline='') as OutputFile:
        cupreader = csv.reader(InputFile)
        writer = csv.writer(OutputFile)
        next(cupreader)
        for row in cupreader:
            if len(row) == 13: #just deal with the rows that are waypoints
                if len(row[9]) > 0:
                    outputrow = (row[1], row[9])
                    writer.writerow(outputrow)
