import ijson
import time


def process_anthem_index(filepath='2024-01-01_anthem_index.json', outputpath=None):

    start_time = time.time()
    output = set()

    with open(filepath, 'r') as f:
        data = next(ijson.items(f, ''))

        for struct in data['reporting_structure']:
            for inf in struct['in_network_files']:
                if inf['location'] not in output:
                    if 'NEW YORK' in inf['description'].upper() and 'PPO' in inf['description'].upper():
                        output.add(inf['location'])

    with open('output.txt' if outputpath is None else outputpath, 'w') as o:
        for url in output:
            o.write(f'{url}\n')

    print('Runtime:', (time.time() - start_time))

    return output

if __name__ == "__main__":
    process_anthem_index()
