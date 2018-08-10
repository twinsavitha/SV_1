import argparse
parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
parser.add_argument("-f", "--firmware_list", nargs="*", required=True, help="The older firmware files",default=[])
args = parser.parse_args()

print "111111111111111111111111111111111111111111111"
print args.firmware_list
print "222222222222222222222222222222222222222222222"

hi = "Savitha"
print hi
