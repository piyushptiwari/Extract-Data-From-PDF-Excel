import tabula
import regex as re
import csv
from datetime import datetime
import datefinder
from glob import glob
df = tabula.read_pdf('C:\\Users\\200743\Desktop\\txdot\\Project\\1.pdf', pages='all')
tabula.convert_into('C:\\Users\\200743\Desktop\\txdot\\Project\\1.pdf', "output.txt", output_format="csv", pages='all')
'''
# Read pdf into list of DataFrame


# Read remote pdf into list of DataFrame
#df2 = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")

# convert PDF into CSV file


# convert all PDFs in a directory

'''
path="C:\\Users\\200743\\Desktop\\txdot\\"
print('Reading files in Path: '+path)
try:
    tabula.convert_into_by_batch(path+'PO\\', output_format='text', pages='all')
except:
    pass

print('Data has been prepared to export')
g = glob(path + 'PO/*.csv')
print(g)
datafile = open('fullpos.csv','w',newline='')

fieldnames = ['PO_number','PO_LineItemNo','PO_Date','NIGP','General_des',
              'Item_des','Quantity','Unit_cost','Unit','Total_cost',
              'Promise_Date','Vendor_name','Vendor_Id',
              'Solicitation_Number','Total']              
writer = csv.DictWriter(datafile, fieldnames=fieldnames)
writer.writeheader()
print("Exporting...")
for z in range(0,len(g)):
    f=open(g[z],'r')
    #print(f)
    #g=f.read()
    pon=None
    sol=None
    pod=None
    tpa=None
    vid=None
    VNAME=None
    dupli=[]
    nigp=[]
    qnt=[]
    tot=[]
    unit=[]
    unit_pri=[]
    pd=[]
    gen_des=[]
    full_des=[]
    var=1
    count=1
    '''
    #count for POLs and file does not support 2 loops so use seek
    for j in f:
        if j.startswith(str(count)+' '):
            print(count)
            count=count+1
    f.seek(0)
    '''
    
    for i in f:
            
        if "P.O. No" in i:
            try:
                POn=re.findall('[0-9]+', i)
                pon=POn[0]
            except:
                pon="NaN"

        
            
        if "Solicitation Number" in i:
            try:
                SOL=re.findall(r'[\d\.\d]+', i)
                print(SOL[0])
                sol=SOL[0]
            except:
                sol="NaN"
                
        if "P.O. Date" in i:
            try:
                da=re.findall('P.O. Date:  (\d.*),',i)
                if pod ==None:
                    pod=da[0]
                    print(da)
                    
                
                else:
                    print(pod)
                    continue
            except:
                pod="NaN"
                   
            
        
            
        if "To:" in i:
            try:
                k=next(f)
                vname=re.findall('^(\S.*),60144',k)

                if VNAME ==None:
                    VNAME=vname[0]
                    print(VNAME)       
                else:
                    continue
            except:
                vname="NaN"
            

        if "VENDOR ID" in i:
            try:
                VID=re.findall('^VENDOR ID: (\S+-\S+),',i)
                vid=VID[0]
                print(vid)
            except:
                vid="NaN"

            
        
        if i.startswith(str(var)+' '):
            print(var)
            try:
                NIGP=re.findall('^'+str(var)+' '+'([0-9]+)',i)
                nigp.append(NIGP[0])
                print(nigp)
            except:
                nigp.append("NaN")
            try:
                QNT=re.findall('^'+str(var)+' '+str(NIGP[0])+','+'(\S+) ',i)
                qnt.append(QNT[0])
                print(qnt)
            except:
                qnt.append("NaN")
            try:
                UNIT=re.findall('^'+str(var)+' '+str(NIGP[0])+','+str(QNT[0])+' '+'([0-9|SVC|EA]+)',i)
                unit.append(UNIT[0])
                print(unit)
            except:
                unit.append("NaN")
            try:
                TOTAL=i.split('$')
                up=TOTAL[-2]
                unit_pri.append(up)
            except:
                unit_pri.append("NaN")
            try:
                total=TOTAL[-1].strip('\n')
                tot.append(total)
                print(tot)
            except:
                tot.append("NaN")
            gd=[]
            for j in range(0,5):
                k=next(f)
                try:
                    if "Promise Date:" in k:
                        
                        PD=re.findall('Promise Date: (\S.*)"',k)
                        pd.append(PD[0])
                        print(pd)
                        break
                    else:
                        try:
                            gd.append(k.rstrip('\n'))
                        except:
                            gd.append("NaN")
                except:
                    pd.append("NaN")
                    
                
                   
            
            gen_des.append(' '.join(gd))
            gd=[]
              
            n=var+1
            fd=[]
            for l in range(0,9):
                m=next(f)
                try:
                    if '^'+str(n)+' ' in m:
                        
                        break
                    elif '^The following comments' in m:
                        break
                    elif '"",,,' in m:
                        break
                    else:
                    
                        fd.append(m.rstrip('\n'))
                except:
                    fd.append("NaN")
            full_des.append(' '.join(fd))
            fd=[]
                    
                    
                   
            
            var += 1
            
        if "Total PO Amount" in i:
            try:
                TPA=i.split('$')
                tpa=TPA[-1]
                print(tpa)
            except:
                tpa="NaN"
        
            
    for i in range(0,var-1):
        try:
            writer.writerow({'PO_number':pon,'PO_LineItemNo':i+1,'PO_Date':pod,'NIGP':nigp[i],
                             'General_des':gen_des[i],'Item_des':full_des[i],'Quantity':qnt[i],'Unit_cost':unit_pri[i],
                             'Unit':unit[i],'Total_cost':tot[i],'Promise_Date':pd[i],
                             'Vendor_name':VNAME, 'Vendor_Id':vid,'Solicitation_Number':sol,'Total':tpa})
        except:
            pass
print("Completed!")
datafile.close()
                         
                           
                          
        
     
        
        
    
    
        
    

        
        
        
    

        

  
            
        
    
        


        
        

