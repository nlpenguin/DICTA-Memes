#!/usr/bin/env python
import sys

clusterCentroids=[]
#clusters=[]

def getSim(data, cent):
  try:
    return len(set(data) & cent)/ ( ( float(len( set(data) )) + len(set(cent)) ) / 2 )
  except:
    return 0

def delStopwords(wordlist=[]):
  stopwords=set(["a","about","above","after","again","against","all","also","am","an","another","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours ","ourselves","already","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"] )

  stopcnt=0.0
  outwordlist=[]
  for word in wordlist:
    if word.isdigit():
      outwordlist.append("numeric")
    else:
      if word not in stopwords:
        outwordlist.append(word)
    
  return outwordlist



def updateCentroid(cent, data):
  for word in data:
    cent.add(word)
  return cent  

line_no=0
for line in sys.stdin:
  line_no+=1
  if line_no%1000==0:
    sys.stderr.write(str(line_no)+" "+str(len(clusterCentroids))+"\n")


  meme=line.strip()

  data=meme.replace("'", " ")
  data=data.split(" ")
  data=delStopwords(data)
  settled=0
  if len(clusterCentroids)==0:
    clusterCentroids.append(set(data))
    #clusters.append([meme])
    continue
  i=0
  clusterupdate_flag=False
  for cent in clusterCentroids:
    #print getSim(data, cent)
    if getSim(data, cent)>0.6:
      clusterCentroids[i]=updateCentroid(cent, data)
      #clusters[i].append(meme)
      clusterupdate_flag=True
      break
    i+=1
  
  if (clusterupdate_flag==False):
    clusterCentroids.append(set(data))
    #clusters.append([meme])

for c in clusterCentroids:
  print ",".join(c)

