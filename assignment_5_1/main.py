# This is a sample Python script.
import argparse
import json
import csv

def listToStringWithoutBrackets(output):
    return str(output).replace('[', ' ').replace(']', ' ').replace(',', '')


def Sum(args):
    print(f'Sum: {sum(args.sum)}')


def generate(args):
    output = [*range(args.start, args.stop, args.step)]
    print(f'Generated:{listToStringWithoutBrackets(output)}', end=' ')
    
def convert(args):
    with open (f'{args.input}') as json_file:
        root = json.load(json_file)

    with open(f'{args.output}','w') as csv_file:
        reader = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        reader.writerow(root[0].keys())
        for row in root:
            reader.writerow(row.values())


parser = argparse.ArgumentParser(description='Program that sums numbers given')

# Create object used to add subparsers
subparsers = parser.add_subparsers(help='sub-command sum')

# Add the sum subparse
SUM = subparsers.add_parser('sum', help='summes numbers')
SUM.add_argument('sum', type=int, nargs='*')

GENEREATE = subparsers.add_parser('generate', help='Generates a list of outputs')
GENEREATE.add_argument('--start', dest='start', type=int)
GENEREATE.add_argument('--stop', dest='stop', type=int)
GENEREATE.add_argument('--step', dest='step', type=int)

CONVERT = subparsers.add_parser('convert', help='Converts jason-file to csv-file')
CONVERT.add_argument('--input', dest='input', type=str)
CONVERT.add_argument('--output', dest='output', type=str)
# Add the function that handles the  subcommand
SUM.set_defaults(func=Sum)
GENEREATE.set_defaults(func=generate)
CONVERT.set_defaults(func=convert)

# Parse given arguments with the above configuration
args = parser.parse_args()
args.func(args)
