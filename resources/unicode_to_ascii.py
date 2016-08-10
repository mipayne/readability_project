import os
import sys
import codecs
import re
from unidecode import unidecode


dir = 'StoryCorpus/'

print('dir (absolute) = ' + os.path.abspath(dir))

for root, subdirs, files in os.walk(dir):

    for filename in files:

        if filename.endswith('.txt'):

            file_path = os.path.join(root, filename)
            print('\t- file %s (full path: %s)' % (file, file_path))

            new_file = file_path.replace (" ", "_")
            new_file = re.sub(r"[?|!|,|'|:]", "", new_file)

            with codecs.open(file_path, 'r', 'utf-8') as infile, codecs.open("./converted/"+new_file, 'w+', 'ascii') as outfile:

                for line in infile:
                    new_line = unidecode(line.strip())
                    outfile.write(new_line)
                    #print new_line


