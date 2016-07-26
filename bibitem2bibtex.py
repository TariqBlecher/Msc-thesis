import sys

inputfile = sys.argv[1]

f = open(inputfile)
text = f.readlines()
f.close()

for line in range(len(text)):
    if (len(text[line]) > 1):
        if (text[line].split()[0][0] == '@'):

            alias =  text[line + 1].split()[2][2:-2] +'_'+  text[line][9:13]
            print alias
            
            text[line] = '@ARTICLE{' + alias + ',\n'


out = open('thesis.bib','w')
out.writelines(text)
out.close()
