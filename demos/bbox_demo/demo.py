import sys
sys.path.append('../../src');
from Element import Element
from TableRow import TableRow
from Table import Table
from TableWriter import TableWriter

t = Table()
srcpath = 'http://ladoga.graphics.cs.cmu.edu/xiaolonw/affordance_TBBT/pose_det_vis/' 
image_set_file = 'paths.txt'
with open(image_set_file) as f:
    image_index = [x.strip() for x in f.readlines()]

trajnum = len(image_index) 

for r in range(trajnum):
    idx = r
    if r == 0:
        r = TableRow(isHeader = True)
    else:
        r = TableRow()
    now_path = image_index[idx]
    now_path =  srcpath + now_path  
    e = Element()
    e.addTxt(image_index[idx])
    r.addElement(e)
    for e in range(30):
        idx2 = e * 5 + 1
        e = Element()
        tpath = now_path + '{0:07d}'.format(idx2) + '.jpg'  
        e.addImg(tpath)
        r.addElement(e)
    t.addRow(r)
tw = TableWriter(t, 'out')
tw.write()

