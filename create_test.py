import pickle

infile = open('final' ,'rb')
final = pickle.load(infile)
infile.close()
for x in final:
    # fname=x+'.pred'
    # f= open(fname,"w+")
    # f.write(final[x][0])
    print(x)
    print(final[x][0])