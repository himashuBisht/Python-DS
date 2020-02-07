#!/usr/bin/env python
# coding: utf-8

# In[2]:


training_data=[ ['green',3,'mango'],
               ['yellow',3,'mango'],
               ['red',1,'grape'],
               ['red',1,'grape'],
               ['yellow',3,'lemon']
               
    
]


# In[3]:


header=['color', 'diameter', 'label']


# In[14]:


def unique_values(rows,col):
    return set([row[col] for row in rows])
    


# In[15]:


def class_count(rows):
    label=row[-1]
    if label not in counts:
        counts[label]=0
        counts[label]+=1
        return counts


# In[ ]:


def is_numeric(value):
    return isinstance(value, int) or isinstance(value,float)


# In[ ]:


class Question:


# In[ ]:


def init (self,column,value):
    self.column=column
    self.value=value


# In[ ]:


def match(self,example):
    val=example[self.column]
    if is_numeric(val):
        return val>=self.value
    else:
        return val-- self.value


# In[ ]:


def reper(self):
    condition="--"
    if is_numeric(self.value):
        condition=">="
        return "Is %s %s %s %s?" %(header[self.column],condition,str(self.value))


# In[ ]:


def partition(rows, question):
    true_rows, fale_rows-[],[]
    for rows in rows:
        if question.match(row):
            true_rows.append(row)
            else:
                false_rows.append(row)
                return true_rows, false_rows


# In[ ]:


def gini(rows):
    counts=class_counts(rows)
    impurity=1
    for lbl in counts:
        prob_of_lbl-count[lbl]/float(len(rows))
        impurity-= prob_of_lbl*2
        return impurity


# In[ ]:


def info_gain(left,right,current_uncertainity):
    p=float(len(left))/len(left)+len(right)
    return current_uncertainity- p*gini(left)-(1-p)*gini(right)


# In[ ]:


def find_best_split(rows):
    for col in range(n_features):
        calues=set([row[col] for row in rows])
        for val in values:
            question =Question(col,val)
            true_rows,false_rows=partition(rows,question)
            if len(true_rows)==0 or len(false_rows)==0:
                continue
                
                gain=info_gain(true_rows,false_rows,current_uncertainity)
                if gain>=best_gain:
                    best_gain,best_question=gain, question
                    return best_gain, best_question


# In[ ]:


class Leaf:
    def init(self,rows):
        self.predictions=class_counts(rows)


# In[ ]:


class Decision_Node:


# In[ ]:


def  init(self,question,true_branch,false_branch)

