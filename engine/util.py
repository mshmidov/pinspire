import operator

__author__ = 'mshmidov'


def most_popular(generator, count=10, runs=10000):
    stat = {}

    for _ in range(runs):
        item = generator()
        stat[item] = stat.setdefault(item, 0) + 1

    sorted_stats = sorted(stat.items(), key=operator.itemgetter(1), reverse=True)

    print("[INFO] {} unique items".format(len(stat.keys())))

    return sorted_stats[:count]
