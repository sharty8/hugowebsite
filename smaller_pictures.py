import os

DIRECTORY = __file__[::-1].split('/', 1)[1][::-1] + '/static/'
MAX_SIZE = 10**6
total_size = 0

def recursiv_apply_to_all_files(directory, function=None):
    for filename in os.listdir(directory):
        path = directory + "/" + filename
        if os.path.isfile(path):
            if function:
                function(path)
        elif os.path.isdir(path):
            recursiv_apply_to_all_files(path, function)


def show_tot_size(path):
    global total_size
    total_size += os.path.getsize(path)
    print('\r', total_size , '-', end='')


def make_smaller(path):
    i = 0
    while (os.path.getsize(path) > MAX_SIZE):
        old = path
        new = path + '.tmp'
        res = os.system(f'convert -resize 80% {old} {new}')
        if res == 0:
            os.system(f'mv {new} {old}')
        print(path.split('/')[-1], 'resized', end='\r')
        i += 1
    print()

if __name__ == '__main__':
    recursiv_apply_to_all_files(DIRECTORY, make_smaller)
    recursiv_apply_to_all_files(DIRECTORY, show_tot_size)  # 220Mb -> 150Mb -> 70Mb
