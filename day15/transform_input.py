import sys

input_filenames = list(filter(lambda x : not x.endswith("doubled.txt"), sys.argv[1:]))

for input_filename in input_filenames:
    output_filename = input_filename.replace(".txt", ".doubled.txt")
    input_file = open(input_filename, 'r')
    output_file = open(output_filename, 'w')

    for input_line in input_file.readlines():
        output_file.write(input_line.
                        replace('#', '##'). 
                        replace('O', '[]'). 
                        replace('.', '..'). 
                        replace('@', '@.'))
    output_file.close()

