import json as js
import sys

fname = sys.argv[1]
decoder = js.JSONDecoder()

with open(fname,"r") as f:
  version = f.readline()
  info = f.readline()
  (name, group_number) = info.strip().split(":")
  if not(name == 'Sleeping Groups'):
    print "Invalid format"
    exit(1)
  group_number = int(group_number)
  for x in range(group_number):
    json_data = f.readline()
    data=decoder.decode(json_data)
    print "<h2>%s</h2>" % data.get(u'name',"").encode('utf-8')
    try:
      for x in data[u'tabs']:
        tab_entry = decoder.decode(x)
        index = tab_entry.get(u'index',1)
        if(index>0):
          index -= 1
        print "    <a href=\"%s\">%s</a>" % (tab_entry[u'entries'][index].get(u'url',"").encode('utf-8'),tab_entry[u'entries'][index].get(u'title',"").encode('utf-8'))
    except Exception as e:
      print "XXXX: ",e
      pass
    

