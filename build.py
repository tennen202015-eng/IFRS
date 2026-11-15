import glob,os,re
h=open('index.html').read()
files=sorted(glob.glob('data/*.js'))+sorted(glob.glob('data/deep/*.js'))
tags='\n'.join('<script src="%s"></script>'%f for f in files)
h=re.sub(r'<!--DATA-->.*?<!--/DATA-->|<!--DATA-->','<!--DATA-->\n'+tags+'\n<!--/DATA-->',h,flags=re.S)
open('index.html','w').write(h)
print(tags.count('<script'))
