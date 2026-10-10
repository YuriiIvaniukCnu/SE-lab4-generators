def get_bytes(line):
    return int(line.split('"')[2].split()[1])

def count_bytes(path):
    with open(path) as file:
        return sum(get_bytes(line) for line in file)

if __name__ == '__main__':
    print(count_bytes('2017_05_07_nginx.txt'))