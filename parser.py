#import numpy as np
class Node:
    total_number_of_levels = 0
    def __init__(self, parent, is_child, key, level):
        self.parent = parent
        self.is_child = is_child
        self.key = key
        self.level = level
        if(level > Node.total_number_of_levels):
            Node.total_number_of_levels = level
class token:
  def __init__(self, value, types):
    self.value = value
    self.type = types
nodelist = list()
#len(nodelist)-1=0
n=0
def correction():
    for i in range(1, len(nodelist)):
        if nodelist[i].is_child==1:
            setattr(nodelist[i], 'level', nodelist[int(nodelist[i].parent)].level +1)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def getToken(tokens):
    global n
    n=n+1
    return n
def error():
    print('error')
    return
def match (expectedToken):

    if tokens[n].value == expectedToken or tokens[n].type == expectedToken:
        getToken(tokens)
    else:
        error()
    return
def term(parent_id,ischild,parent_level):
     #global len(nodelist)-1
     m=n
     op_id=-1
     while (tokens[m].type == 'IDENTIFIER' or tokens[m].type == 'NUMBER' or   tokens[m].value == '(' or tokens[m].value == ')' ) and m< len(tokens) :
         if tokens[m]=='(':
             while tokens[m+1]!=')':
                 m=m+1
         m=m+1
     if m< len(tokens) and (tokens[m].value== '*' or tokens[m].value== '/'):
         key = "op (" + tokens[m].value + ")"
         if len(nodelist)>0:
             level=nodelist[int(parent_id)].level
         else:
             level=parent_level
         if ischild==1 :
            level = level + 1
         nodelist.append(Node(parent_id,ischild,key,level))
         #len(nodelist)-1+=1
         op_id = len(nodelist)-1
         factor_level=level
         ischild=1
     if op_id<0:
        op_id=factor(parent_id,ischild,parent_level) #it will not enter the while loop so this is the highest node
     else:
         factor(op_id,ischild,factor_level) #we care about the operation id (it's the parent of factors)
     cnt=0
     while tokens[n].value== '*' or tokens[n].value== '/':
         match(tokens[n].value)
         if cnt>0:
             new_op_level=level 
             old_op_level=nodelist[int(op_id)].level+1 
             key=tokens[n-1].value #operator
             nodelist.append(Node(parent_id,ischild,key,new_op_level))
             setattr(nodelist[int(op_id)], 'level', old_op_level) #old operator becomes at low level 
             setattr(nodelist[int(op_id)], 'parent', len(nodelist)-1) #parent id is the parent of caller of this function
             
             op_new=len(nodelist)-1 #id of the new operator
         else:
             op_new=op_id   #in first loop id of operator is op_id
         factor(op_new,ischild,factor_level)   
         cnt+=1
         if cnt>0:
            op_id=op_new
     return  op_id
def comparison_op(): 
     return
def simple_exp(parent_id,ischild,parent_level):
     op_id=-1
     #global len(nodelist)-1
     m=n
     while (tokens[m].type == 'IDENTIFIER' or tokens[m].type == 'NUMBER' or tokens[m].value == '*' or tokens[m].value == '/' or tokens[m].value == '(' or tokens[m].value == ')' ) and m< len(tokens) :   
         if tokens[m]=='(':
             while tokens[m+1]!=')':
                 m=m+1
         m=m+1
     if m< len(tokens) and (tokens[m].value== '+' or tokens[m].value== '-'):
         key = "op (" + tokens[m].value + ")"
         if len(nodelist)>0:
             level=nodelist[int(parent_id)].level
         else:
             level=parent_level
         if ischild==1 :
            level = level + 1
         nodelist.append(Node(parent_id,ischild,key,level))
         #len(nodelist)-1+=1
         op_id = len(nodelist)-1
         term_level=level
         ischild=1
     
     if op_id<0:
        op_id=term(parent_id,ischild,parent_level)
     else:
         term(op_id,ischild,term_level)
     cnt=0
     while tokens[n].value== '+' or tokens[n].value== '-':
         match(tokens[n].value)
         if cnt>0:
             new_op_level=level 
             old_op_level=nodelist[int(op_id)].level+1 
             key=tokens[n-1].value
             nodelist.append(Node(parent_id,ischild,key,new_op_level))
             setattr(nodelist[int(op_id)], 'level', old_op_level) #old operator becomes at low level 
             setattr(nodelist[int(op_id)], 'parent', len(nodelist)-1) #parent id is the parent of caller of this function
             
             op_new=len(nodelist)-1 #id of the new operator
         ##len(nodelist)-1+=1
         else:
             op_new=op_id   #in first loop id of operator is op_id
         term(op_new,ischild,term_level)
         cnt+=1
         if cnt>0:
            op_id=op_new    
     return  op_id
def exp(parent_id,ischild,parent_level):
     op_id=-1
     #global len(nodelist)-1
     m=n
     while (tokens[m].type == 'IDENTIFIER' or tokens[m].type == 'NUMBER' or tokens[m].value == '+' or tokens[m].value == '-' or tokens[m].value == '*' or tokens[m].value == '/' or tokens[m].value == '(' or tokens[m].value == ')') and m< len(tokens) :   
         m=m+1
     if m< len(tokens) and (tokens[m].value== '<' or tokens[m].value== '='):
         key = "op (" + tokens[m].value + ")"
         if len(nodelist)>0:
             level=nodelist[int(parent_id)].level
         else:
             level=parent_level
         if ischild==1 :
            level = level + 1
         nodelist.append(Node(parent_id,ischild,key,level))
         #len(nodelist)-1+=1
         op_id = len(nodelist)-1
         exp_level=level
         ischild=1
     if op_id<0:
        op_id=simple_id_l=simple_exp(parent_id,ischild,parent_level)
     else:
         simple_id_l=simple_exp(op_id,ischild,exp_level)
     cnt=0
     while tokens[n].value== '<' or tokens[n].value== '=':
         match(tokens[n].value)
         if cnt>0:
             new_op_level=level 
             old_op_level=nodelist[int(op_id)].level+1 
             key=tokens[n-1].value
             nodelist.append(Node(parent_id,ischild,key,new_op_level))
             setattr(nodelist[int(op_id)], 'level', old_op_level) #old operator becomes at low level 
             setattr(nodelist[int(op_id)], 'parent', len(nodelist)-1) #parent id is the parent of caller of this function
             
             op_new=len(nodelist)-1 #id of the new operator
         ##len(nodelist)-1+=1
         else:
             op_new=op_id   #in first loop id of operator is op_id
         ##len(nodelist)-1+=1
         simple_id_r=simple_exp(op_new,ischild,exp_level)
         cnt+=1
         if cnt>0:
            op_id=op_new
     return op_id      
def factor (parent_id,ischild,parent_level):
    if tokens[n].value== "(" :
        match("(") 
        factor_id=exp(parent_id,ischild,parent_level)
        match(")")
    elif tokens[n].type=='NUMBER' :
        match(tokens[n].value)
        if len(nodelist)>0:
            level=nodelist[int(parent_id)].level+1
        key = 'Const (' + tokens[n-1].value + ')'
        nodelist.append(Node(parent_id,ischild,key,level))
        factor_id=len(nodelist)-1
    elif tokens[n].type=='IDENTIFIER' :
        match(tokens[n].value)
        if len(nodelist)>0:
            level=nodelist[int(parent_id)].level+1
        key = 'id (' + tokens[n-1].value + ')'
        nodelist.append(Node(parent_id,ischild,key,level))
        factor_id=len(nodelist)-1
    else : 
        error()
    return factor_id
def write_statement(parent_id,ischild,parent_level):
     #global len(nodelist)-1
     match('WRITE')
     key= tokens[n-1].value
     if len(nodelist)>0:
         level=nodelist[int(parent_id)].level
     else:
         level=parent_level
     if ischild==1 :
         level = level + 1
     nodelist.append(Node(parent_id,ischild,key,level))
     write_id=len(nodelist)-1
     #len(nodelist)-1+=1
     child=1
     exp(write_id,ischild,level)
     return write_id
def repeat_statement(parent_id,ischild,parent_level):
     #global len(nodelist)-1
     match('REPEAT')
     key= tokens[n-1].value
     if len(nodelist)>0:
         level=nodelist[int(parent_id)].level
     else:
         level=parent_level
     if ischild==1 :
         level = level + 1
     nodelist.append(Node(parent_id,ischild,key,level))
     repeat_id= len(nodelist)-1
     #len(nodelist)-1+=1
     child=1
     parent_id=stmt_sequence(repeat_id,child,level)
     match('UNTIL')
     exp(repeat_id,child,level)
     return repeat_id
def read_statement(parent_id,ischild,parent_level):
     #global len(nodelist)-1
     match('READ')
     match('IDENTIFIER')
     key= tokens[n-2].value + " (" + tokens[n-1].value + ")"
     if len(nodelist)>0:
         level=nodelist[int(parent_id)].level
     else:
         level=parent_level
     if ischild==1 :
         level = level + 1
     nodelist.append(Node(parent_id,ischild,key,level))
     #len(nodelist)-1+=1
     read_id= len(nodelist)-1
     return read_id  
def assign_statement(parent_id,ischild,parent_level):
     #global len(nodelist)-1
     match('IDENTIFIER')
     key= tokens[n-1].value
     match('ASSIGN')
     key = "assign" + " (" + key + ")"
     if len(nodelist)>0:
         level=nodelist[int(parent_id)].level
     else:
         level=parent_level
     if ischild==1 :
         level = level + 1
     nodelist.append(Node(parent_id,ischild,key,level))
     assign_id= len(nodelist)-1 #last node created is assign
     #len(nodelist)-1+=1
     child=1
     parent_id=exp(assign_id,child,level)
     return assign_id 
def if_statement(parent_id,ischild,parent_level):
     #global len(nodelist)-1
     match('IF')
     if len(nodelist)>0:
         level=nodelist[int(parent_id)].level    
     if ischild==1 :
         level = level + 1
     key= 'if'    
     nodelist.append(Node(parent_id,ischild,key,level))
     #len(nodelist)-1+=1
     if_id=len(nodelist)-1 #last node created is "if" so we make it parent
     child=1
     exp(if_id,child,level)
     match('THEN')
     parent_id= stmt_sequence(if_id,child,level) #the highest node will be returned
     if tokens[n].value== 'else':
         match('else')
         parent_id = stmt_sequence(if_id,child,level)
     match('END')    
     return if_id
def statement(parent_id,ischild,parent_level):
     if tokens[n].type=='IF' :
        parent_id= if_statement(parent_id,ischild,parent_level)
     elif tokens[n].type=='IDENTIFIER':
        parent_id= assign_statement(parent_id,ischild,parent_level)
     elif tokens[n].type=='READ':
        parent_id= read_statement(parent_id,ischild,parent_level)
     elif tokens[n].type=='WRITE':
        parent_id= write_statement(parent_id,ischild,parent_level)
     elif tokens[n].type=='REPEAT':
        parent_id= repeat_statement(parent_id,ischild,parent_level)    
     else:
         error()        
     return   parent_id 
def stmt_sequence(parent_id,ischild,parent_level):
     #global len(nodelist)-1
     parent_id=statement(parent_id,ischild,parent_level)
     while tokens[n].value== ';' :
         match(';')
         parent_id =statement(parent_id,0,parent_level)
         if n >= len(tokens):
             break
     return parent_id
tokens=[token('read','READ'),token ('x','IDENTIFIER'),token (';','SEMICOLON'),token('if','IF'),
token('0','NUMBER'),token('<','LESSTHAN'),token ('x','IDENTIFIER'),token('then','THEN'),token ('fact','IDENTIFIER')
,token (':=','ASSIGN'),token('1','NUMBER'),token (';','SEMICOLON'),token('repeat','REPEAT'),token ('fact','IDENTIFIER')
,token (':=','ASSIGN'),token ('fact','IDENTIFIER'),token ('+','PLUS'),token ('x','IDENTIFIER'),token ('*','MULT'),token ('y','IDENTIFIER'),token (';','SEMICOLON'),token ('x','IDENTIFIER'),token (':=','ASSIGN'),token ('x','IDENTIFIER'),token ('-','MINUS'),token('1','NUMBER')
,token('until','UNTIL'),token ('x','IDENTIFIER'),token ('=','EQUAL'),token('0','NUMBER'),token (';','SEMICOLON'),token('write','WRITE'),token ('fact','IDENTIFIER'),token ('end','END')]
stmt_sequence(-1,-1,0)
correction()
print(nodelist)
