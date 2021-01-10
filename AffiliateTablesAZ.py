filesource = 'donotchange/basedata.txt'


filepath = 'InputFiles/amazonurl.txt'
basedata=open(filesource).read()


with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:

       if cnt == 1:
          link="KinnLink"+"Ten"
       else:
          link="KinnLink"+str(cnt)
       
       line = line.rstrip('\n')
       basedata = basedata.replace(link,line,basedata.find(link))

       line = fp.readline()
       cnt += 1






filepath = 'InputFiles/pictureurl.txt'

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:

       

       if cnt == 10:
          imglink="Kinnimg"+"Ten"
       else:
          imglink="Kinnimg"+str(cnt)
       
       line = line.rstrip('\n')
       basedata = basedata.replace(imglink,line,basedata.find(imglink))


       line = fp.readline()
       cnt += 1




filepath = 'InputFiles/names.txt'

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:


       if cnt == 10:
          NamesList="KinnName"+"Ten"
       else:
          NamesList="KinnName"+str(cnt)

       line = line.rstrip('\n')
       basedata = basedata.replace(NamesList,line,basedata.find(NamesList))

       line = fp.readline()
       cnt += 1


filepath = 'InputFiles/jumplinks.txt'

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:

       

       if cnt == 10:
          jmplink="jumplink"+"Ten"

       else:	
          jmplink="jumplink"+str(cnt)
       

       line = line.rstrip('\n')
       basedata = basedata.replace(jmplink,line,basedata.find(jmplink))


       line = fp.readline()
       cnt += 1




f= open("output.txt","w+")
f.write(basedata)
f.close() 
