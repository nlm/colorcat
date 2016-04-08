import sys
from argparse import ArgumentParser

colors = {
    'black': 0,
    'red': 1,
    'green': 2,
    'yellow': 3,
    'blue': 4,
    'magenta': 5,
    'cyan': 6,
    'white': 7,
}

ccodes = {
    'reset': 0,
    'bold': 1,
    'underline': 4,
}

def cat(fd):
    while True:
        cnt = fd.readline()
        if cnt == '':
            break
        sys.stdout.write(cnt)

def parse_args(arguments):
    parser = ArgumentParser()
    parser.add_argument('filename', nargs='*', default='-')
    parser.add_argument('-c', '--foreground-color', choices=colors.keys())
    parser.add_argument('-C', '--background-color', choices=colors.keys())

    parser.add_argument('-b', '--bold', dest='ccodes',
                        action='append_const', const='bold')
    parser.add_argument('-u', '--underline', dest='ccodes',
                        action='append_const', const='underline')
    return parser.parse_args()

def main(arguments=None):

    args = parse_args(arguments)

    if args.foreground_color:
        sys.stdout.write('\033[3{0}m'.format(colors[args.foreground_color]))

    if args.background_color:
        sys.stdout.write('\033[3{0}m'.format(colors[args.background_color]))

    if args.ccodes is not None:
        for ccode in args.ccodes:
            sys.stdout.write('\033[{0}m'.format(ccodes[ccode]))

    for fname in args.filename:
        if fname == '-':
            cat(sys.stdin)
        else:
            with open(fname) as fd:
                cat(fd)

    sys.stdout.write('\033[{0}m'.format(ccodes['reset']))

if __name__ == '__main__':
    main()
