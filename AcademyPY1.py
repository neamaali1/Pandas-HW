
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


mydata1 = pd.read_csv("schools_complete1.csv")
mydata2= pd.read_csv("schools_complete2.csv")


# In[4]:


#District Summary


# In[5]:


def getDistrictSummary (csv1,csv2):
    summary={}
    summary["Total Schools"]=csv2['School_ID'].count()
    summary["Total Students"]=csv1['Student_ID'].count()
    summary["Total Budget"]=csv2["Budget"].sum()
    summary["Average Math Score"]=csv1["Math_Score"].mean()
    summary["Average Reading Score"]=csv1["Reading_score"].mean()
    summary["%Passing Math"]=csv1[csv1["Math_Score"]>=70].Math_Score.count()/summary["Total Students"]
    Percent_Passing_Reading = (csv1[csv1.Reading_score>=70])
    summary["%Passing Reading"]=Percent_Passing_Reading.Reading_score.count()/summary["Total Students"]
    summary["Total Percent Passing"]=summary["%Passing Math"]+summary["%Passing Reading"]/2
    return summary 


# In[6]:


District_Summary = getDistrictSummary(mydata1,mydata2)


# In[7]:


pd.DataFrame(District_Summary, index=[0])


# In[8]:


def getSchoolSummary (csv1,csv2):
    summary={}
    summary["School_Name"] = []
    summary["School_Type"] = []
    summary["School_Size"] = []
    summary["School_Budget"] = []
    summary["Per_Student_Budget"] = []
    summary["Average_Math_Score"] =[]
    summary["Average_Reading_Score"]=[]
    summary["Overall_Passing_Rate"]=[]
    
    for (i,row) in csv2.iterrows():
        summary["School_Name"].append(row.Name_of_School)
        summary["School_Type"].append(row.Type)
        summary["School_Size"].append (row.Size)
        summary["School_Budget"].append(row.Budget)
        summary["Per_Student_Budget"].append(row.Budget/row.Size)
        AMS=csv1[csv1.School==row.Name_of_School].Math_Score.mean()
        summary["Average_Math_Score"].append(AMS)
        ARS =csv1[csv1.School==row.Name_of_School].Reading_score.mean()
        summary["Average_Reading_Score"].append(ARS)
        summary["Overall_Passing_Rate"].append ((AMS+ARS)/2)
        
    return summary

    


# In[9]:


School_Summary = getSchoolSummary (mydata1,mydata2)


# In[10]:


pd.DataFrame(School_Summary)


# In[11]:


#Top Performing Schools 5 top schools


# In[12]:


Top_Performing_Schools = {
    "School_Name":["Pena_High_School","Wright_High_School", "Holden_High_School", 
                   "Wilson_High_School", "Thomas_High_School"],
    "School_Type":["Charter","Charter", "Charter", "Charter", "Charter"],
    "Total_School_Budet":[585858,1049400,248087,1319574,1043130],
    "Per_Student_Budget":[609,583,581,578,638],
    "Average_Reading_Score":[84.04,83.81,83.9,83.9,83.6],
    "Average_Math_Score":[83.83,83.68,83.80,83.27,83.41]
    
}

df = pd.DataFrame(Top_Performing_Schools)
df


# In[13]:


#Top Performing Schools 5 bottom Schools


# In[ ]:


Bottom_Performing_Schools ={
    "School_Name":["Ford_High_School","Rodriguez_High_School","Johnson_High_School","Bailey_High_School",
                   "Hernandez_High_School"],
    "School_Type":["District", "District", "Charter", "District", "District"],
    "Total_School_Budget":[1763916,2547363,3094650,3124928,3022020],
    "Per_Student_Budget":[644, 637,650,628,652],
    "Average_Reading_Score":[80.74, 80.74, 80.96, 79.04,80.93],
    "Average_Math_Score":[77.10,76.84,77.07,77.04,77.28]   
}
df = pd.DataFrame(Bottom_Performing_Schools)
df

