import argparse
import operator

__author__ = 'mshmidov'


def most_popular(generator, count=10, runs=10000, verbose=False):
    stat = {}

    for _ in range(runs):
        item = generator()
        stat[item] = stat.setdefault(item, 0) + 1

    sorted_stats = sorted(stat.items(), key=operator.itemgetter(1), reverse=True)

    if verbose:
        print("[INFO] {} unique items".format(len(stat.keys())))

    return sorted_stats[:count]


def parse_arguments(generators: dict) -> (argparse.Namespace, callable):
    parser = argparse.ArgumentParser()

    parser.add_argument('--cycles', type=int, default=100000)
    parser.add_argument('-v', '--verbose', action='store_true', default=False)
    parser.add_argument('--top', action='store_true', dest='top', default=False)
    parser.add_argument('count', type=int)

    if len(generators) > 1:
        parser.add_argument('generator', choices=generators.keys())

    args = parser.parse_args()

    generator = generators[args.generator] if len(generators) > 1 else list(generators.values())[0]

    return args, generator


def name_generator_by_argparse(generators: dict):

    args, generator = parse_arguments(generators)

    if args.top:
        for name, count in most_popular(generator, count=args.count, runs=args.cycles, verbose = args.verbose):
            if args.verbose:
                print("{}: {}".format(name, count))
            else:
                print(name)
    else:
        for _ in range(args.count):
            print(generator())
