import hashlib, json, sys, random,csv, ast,operator
from itertools import *
import random

def hashMe(msg=""):
    # For convenience, this is a helper function that wraps our hashing algorithm
    if type(msg)!=str:
        msg = json.dumps(msg,sort_keys=True)  # If we don't sort keys, we can't guarantee repeatability!
        
    if sys.version_info.major == 2:
        return unicode(hashlib.sha256(msg).hexdigest(),'utf-8')
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()
def shareprice(txns):
    t=int(random.randint(1,10))
    a=[]
    for c in txns:
        a.append(txns[c])
    return a[1]*t;
def getDetails1():
        p=[]
        chain=[]
        alternate=[]
        with open('A.csv', 'r') as csvfile:
                           csvreader2 = csv.reader(csvfile)
                           for col in csvreader2:
                              chain.append(col)
                              
        csvfile.close()
        #print(chain)
        del chain[1::2]
        for col in chain[:]:
                        alternate.append(col[-1])
        t=ast.literal_eval(alternate[-1])
        p.append(t['infor'])
        return p[0]
def validationComp(list1,company):
    t=company+'.csv'
    for c in list1:
        if c==t:
            return False
            break
    return True
def getPoint():
        p=[]
        chain=[]
        alternate=[]
        with open('A.csv', 'r') as csvfile:
                           csvreader2 = csv.reader(csvfile)
                           for col in csvreader2:
                              chain.append(col)
                              
        csvfile.close()
        #print(chain)
        del chain[1::2]
        for col in chain[:]:
                        alternate.append(col[-1])
        t=ast.literal_eval(alternate[-1])
        p.append(t['points'])
        return p[0]
def getBitcoin():
        p=[]
        chain=[]
        alternate=[]
        with open('A.csv', 'r') as csvfile:
                           csvreader2 = csv.reader(csvfile)
                           for col in csvreader2:
                              chain.append(col)
                              
        csvfile.close()
        #print(chain)
        del chain[1::2]
        for col in chain[:]:
                        alternate.append(col[-1])
        t=ast.literal_eval(alternate[-1])
        p.append(t['bitcoins'])
        return p[0]
def updateState(txn,state):
   
    state = state.copy() # As dictionaries are mutable, let's avoid any confusion by creating a working copy of the data.
    for key in txn:
        if key in state.keys():
            state[key] = str(int(state[key]) + txn[key])
        else:
            state[key] = str(txn[key])

    return state
def updateBitcoin(txn,state,value):
   
    state = state.copy()
    # As dictionaries are mutable, let's avoid any confusion by creating a working copy of the data.
    a=[]
    for i in txn:
        a.append(i)
    for c in state:
            if c==a[0]:
               state[c]=str(int(state[c])+value)
            elif c==a[1]:
                state[c]=str(int(state[c])-value)
            
    
    
    return state
def updatePoint(miner,state):
    
    state = state.copy() # As dictionaries are mutable, let's avoid any confusion by creating a working copy of the data.
    for key in state:
        if key==miner:
            state[key]=int(state[key])+1
            state[key]=str(state[key])
    #print(state)
    return state

def isValidTxn(txn,col):
    
    if sum(txn.values()) is not 0:
        return False
    
    # Check that the transaction does not cause an overdraft
   
    for key in txn.keys():
        if key in col.keys(): 
            acctBalance = col[key]
        else:
            return False
        if (int(acctBalance) + txn[key]) < 0:
            return False
    
    return True

def isValidTxnBitcoin(txn,col,value):
    
    a=[]
    for i in txn:
        a.append(i)
    for k in col:
        if k==a[1]:
            if(int(col[k])>=value):
                return True
                break
            else:
                print("No sufficient Bitcoins")
                return False
                break
    return True
    
def makeTransaction():
    
      company=[]


      print("Enter seller")
      values=input()
      company.append(values)
      print("Enter buyer")
      values=input()
      company.append(values)
    
      print("enter amount of shares")
      amount=[]
      values=int(input())
      amount.append(-values)
      amount.append(values)   
      return {company[0]:amount[0],company[1]:amount[1]}
def makeHash(filename,t):
    chain=[]
    alternate=[]
    with open(filename, 'r') as csvfile:
                       csvreader2 = csv.reader(csvfile)
                       for col in csvreader2:
                          chain.append(col)
                          
    csvfile.close()
    del chain[1::2]
    for col in chain[:]:
                    alternate.append(col[-2])
    msg=str(alternate[-1])+t
    if type(msg)!=str:
        msg = json.dumps(msg,sort_keys=True)  # If we don't sort keys, we can't guarantee repeatability!
        
    if sys.version_info.major == 2:
        return unicode(hashlib.sha256(msg).hexdigest(),'utf-8')
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()
def makeminerTrans(t,txns,p,points,bitcoins):
    chain=[]
    alternate=[]
    with open(t, 'r') as csvfile:
                       csvreader2 = csv.reader(csvfile)
                       for col in csvreader2:
                          chain.append(col)
                          
    csvfile.close()
    del chain[1::2]
    for col in chain[:]:
                    alternate.append(col[-2])
    
    parentHash  = alternate[-1]
    blockContents = {u'parentHash':parentHash,u'txns':txns,u'infor':p,u'bitcoins':bitcoins,u'points':points}
    blockHash = hashMe( blockContents )
    block = {u'hash_value':blockHash,u'contents':blockContents}
    chain.append(block)  
    with open(t, 'a') as csvfile:
                 csvwriter = csv.writer(csvfile)
                 csvwriter.writerow(block.values())
def makeTrans(filename1,filename2,txns,p,points,bitcoins):
    chain=[]
    chain1=[]
    alternate=[]
    with open(filename1, 'r') as csvfile:
                       csvreader2 = csv.reader(csvfile)
                       for col in csvreader2:
                          chain.append(col)

    csvfile.close()
    del chain[1::2]
    for col in chain[:]:
                    alternate.append(col[-2])
    
    parentHash  = alternate[-1]
    with open(filename2, 'r') as csvfile:
                       csvreader2 = csv.reader(csvfile)
                       for col in csvreader2:
                          chain1.append(col)
                          
    csvfile.close()
    blockContents = {u'parentHash':parentHash,u'txns':txns,u'infor':p,u'bitcoins':bitcoins,u'points':points}
    blockHash = hashMe( blockContents )
    block = {u'hash_value':blockHash,u'contents':blockContents}
    chain1.append(block)
    with open(filename2, 'a') as csvfile:
                 csvwriter = csv.writer(csvfile)
                 csvwriter.writerow(block.values())
def makeNewTrans(filename1,filename2,txns,p,points,bitcoins):
    chain=[]
    chain1=[]
    alternate=[]
    with open(filename1, 'r') as csvfile:
                       csvreader2 = csv.reader(csvfile)
                       for col in csvreader2:
                          chain.append(col)
                          
    csvfile.close()
    del chain[1::2]
    for col in chain[:]:
                    alternate.append(col[-2])
    
    parentHash  = alternate[-1]
    blockContents = {u'parentHash':parentHash,u'txns':txns,u'infor':p,u'bitcoins':bitcoins,u'points':points}
    blockHash = hashMe( blockContents )
    block = {u'hash_value':blockHash,u'contents':blockContents}
    chain1.append(block)
    with open(filename2, 'a') as csvfile:
                 csvwriter = csv.writer(csvfile)
                 csvwriter.writerow(block.values())

    
def addCompany():
    print("enter name of the company")
    com=[]
    for values in range(1):
        values=input()
        com.append(values)
    print("enter amount of shares of company")
    shares=[]
    for values1 in range(1):
        values1=input()
        shares.append(values1)
    print("enter bitcoins in wallet")
    bitcoin=[]
    for values1 in range(1):
        values1=input()
        bitcoin.append(values1)
    return {'company':com[0],'shares':shares[0],'bitcoins':bitcoin[0]}
        
def block1(filename1,filename2,p,points,bitcoins):
    
    chain=[]
    alternate=[]
    with open(filename1, 'r') as csvfile:
                       csvreader2 = csv.reader(csvfile)
                       for col in csvreader2:
                          chain.append(col)
                          
    csvfile.close()
    #print(chain)
    del chain[1::2]
    for col in chain[:]:
                    alternate.append(col[-2])
    chain1=[]
    #print(alternate)
    with open(filename2, 'r') as csvfile:
                       csvreader2 = csv.reader(csvfile)
                       for col in csvreader2:
                          chain.append(col)
                          
    csvfile.close()
    makeTrans(filename1,filename2,{},p,points,bitcoins)
def includingNewCompany(list2):
    t=addCompany()
    p={}
    bit=getBitcoin()
    bit[t['company']]=t['bitcoins']
    p[t['company']]=t['shares']
    x=validationComp(list2,t['company'])
    if x:
        details=getDetails1()
        for c in p:
            details[c]=p[c];
        f=t['company']+'.csv'
        list2.append(f)
        points=getPoint()
        for c in p:
            points[c]='0';
        
        first='A.csv'
        points1=getPoint()
        for c in p:
            points1[c]='0';
        #print(list2[:-1])
        miner=algo(list1[:-1],{})
        m=miner+'.csv'
        index_ofminer=list1.index(m);
            #print(index_ofminer)
        list2=[]
        list3=[]
        for c in list1[:index_ofminer]:
                list2.append(c)
        for c in list1[index_ofminer+1:]:
                list3.append(c)
        for c in list2:
                list3.append(c)    
            #print(list3)
        points=updatePoint(miner,points)
        makeminerTrans(m,{},details,points,bit)
        miner1=m;
        for c in list3:
            if c==f:
                makeNewTrans(miner1,c,{},details,points,bit)
            else:
                makeNewTrans(miner1,c,{},details,points,bit)
            miner1=c
        print("Company details added successfully")
    else:
        print("Company name already exsist")
    return    
def algo(list2,trans):   
    
    hashed={}
    details=getDetails1()
    point=getPoint()
    trans=str(trans)+str(details)+str(point)
    for c in list2:
        t=c[:-4]
        hashed[t]=makeHash(c,trans)
    #print(hashed)
        k={}
    for c in hashed:
        k[c]=abs(hash(hashed[c]) %(10**8))
    a=[]
    b=[]
    for c in k:
        a.append(k[c])
        b.append(c)
    m=max(a)
    i=a.index(m)
    return b[i]
with open('A.csv', 'r') as csvf:
                    csvr= csv.reader(csvf,delimiter=",")
                    data=list(csvr)
                    count1=len(data)
csvf.close()
def updatingLedger(list1,trans,details,points,bitcoins):
            t=algo(list1,trans)
            #print(t)
            m=t+'.csv'
            index_ofminer=list1.index(m);
            #print(index_ofminer)
            list2=[]
            list3=[]
            for c in list1[:index_ofminer]:
                list2.append(c)
            for c in list1[index_ofminer+1:]:
                list3.append(c)
            for c in list2:
                list3.append(c)    
            #print(list3)
            points=updatePoint(t,points)
            makeminerTrans(m,trans,details,points,bitcoins)
            miner=m;
            for c in list3:
                makeTrans(miner,c,trans,details,points,bitcoins)
                miner=c
            return list3
    
if count1==0:    
    list1=['A.csv','B.csv','C.csv','D.csv']
    information={'A':'50','B':'70','C':'80','D':'100'}
    bitcoins={'A':'100','B':'200','C':'300','D':'400'}
    points_initial={}
    for c in list1:
        t=c[:-4]
        points_initial[t]='0'
    #print(points_initial)
    genesisBlockInfo = information
    genesisBlockContents = {u'parentHash':None,u'txns':{},u'infor':genesisBlockInfo,u'bitcoins':bitcoins,u'points':points_initial}
    genesisHash = hashMe( genesisBlockContents )
    genesisBlock = {u'hash_value':genesisHash,u'contents':genesisBlockContents}
    filename1='A.csv'
    with open(filename1, 'a') as csvf1:
                        csvw = csv.writer(csvf1)
                        csvw.writerow(genesisBlock.values())
    csvf1.close()

    c=0;

    for i in list1:
        with open(i, 'r') as csvf:
                        csvr= csv.reader(csvf,delimiter=",")
                        data=list(csvr)
                        count1=len(data)
        csvf.close()
        if count1==0:
           #print(list1[c-1]);
           block1(list1[c-1],i,information,points_initial,bitcoins)
        c=c+1;
details=getDetails1()
list1=[]
for c in details:
    t=c+'.csv'
    list1.append(t)
print("Enter your choice : \n1.Add a company\n2.Make a Transaction\n3.Exit")
value=int(input())
while value<3 and value>0:
    if value==1:
          includingNewCompany(list1)
          
    elif value==2:
        col=getDetails1()
        for c in col:
            print(c," : ",col[c])
        trans=makeTransaction()
        
        #print(col)
        isValid=isValidTxn(trans,col)
        if isValid:
            list1=[]
            for c in col:
                t=c+'.csv'
                list1.append(t)
            #print(list1)
            #col=getDetails1()
            col=updateState(trans,col)
            points=getPoint()
            
            bitcoins=getBitcoin()
            value=shareprice(trans)
            validity=isValidTxnBitcoin(trans,bitcoins,value)
            if validity:
                bitcoins=updateBitcoin(trans,bitcoins,value)
                list3=updatingLedger(list1,trans,col,points,bitcoins)
                print("Transaction successful")
            else:
                print("Ignored Transaction")
                break;
        else:
            print("Ignored Transaction")
            break
    print("Enter your choice : \n1.Add a company\n2.Make a Transaction\n3.Exit")
    value=int(input())
    


