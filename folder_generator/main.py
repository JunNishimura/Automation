import os

def TailSlashChecker(path):
    """ add \ at tail of the path """
    if path[-1] != '\\':
        path += '\\'
    return path 

def NewLineChecker(sentence):
    if sentence[-1] == '\n':
        sentence = sentence.split('\n')[0]
    return sentence

def CreateClassesDirs(path, cnt):
    for i in range(1, cnt+1):
        path = TailSlashChecker(path)
        f_name = 'class' + str(i).zfill(2)
        os.makedirs(path+f_name, exist_ok=True)

def main():
    # enter the working directory full path
    dir_path = input('Working Directory (full path): ')
    dir_path = TailSlashChecker(dir_path)

    # enter the term name
    term_name = input('Term name: ')
    term_name = TailSlashChecker(term_name)

    # create parent directory
    os.makedirs(dir_path + term_name, exist_ok=True)

    # make files
    in_file   = input('Class file (full_path): ')
    class_cnt = int(input('How many classes: '))
    with open(in_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        p_dir = dir_path + term_name
        for line in lines:
            line = NewLineChecker(line)
            os.makedirs(p_dir + line, exist_ok=True)
            CreateClassesDirs(p_dir + line, class_cnt)

if __name__ == '__main__':
    main()