import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--firmware_list", nargs="*", required=True, help="The older firmware files",default=[])
args = parser.parse_args()

print "111111111111111111111111111111111111111111111"
print args.firmware_list
print len(args.firmware_list)
for i in range(len(args.firmware_list)):
    print args.firmware_list[i]
print "222222222222222222222222222222222222222222222"

hi = "Savitha"
print hi
