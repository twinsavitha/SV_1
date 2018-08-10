import argparse
parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
parser.add_argument("-f", "--firmware_list", nargs="*", required=True, help="The older firmware files",default=[])
args = parser.parse_args()

print args.firmware_list

hi = "Savitha"
print hi
