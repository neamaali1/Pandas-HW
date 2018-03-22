

```python
import numpy as np
```


```python
import pandas as pd
```


```python
mydata1 = pd.read_csv("schools_complete1.csv")
mydata2= pd.read_csv("schools_complete2.csv")
```


```python
#District Summary
```


```python
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

```


```python
District_Summary = getDistrictSummary(mydata1,mydata2)
```


```python
pd.DataFrame(District_Summary, index=[0])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>%Passing Math</th>
      <th>%Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Total Budget</th>
      <th>Total Percent Passing</th>
      <th>Total Schools</th>
      <th>Total Students</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.749809</td>
      <td>0.858055</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>24649428</td>
      <td>1.178836</td>
      <td>15</td>
      <td>39170</td>
    </tr>
  </tbody>
</table>
</div>




```python
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

    
```


```python
School_Summary = getSchoolSummary (mydata1,mydata2)
```


```python
pd.DataFrame(School_Summary)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average_Math_Score</th>
      <th>Average_Reading_Score</th>
      <th>Overall_Passing_Rate</th>
      <th>Per_Student_Budget</th>
      <th>School_Budget</th>
      <th>School_Name</th>
      <th>School_Size</th>
      <th>School_Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>78.906068</td>
      <td>655.0</td>
      <td>1910635</td>
      <td>Huang High School</td>
      <td>2917</td>
      <td>District</td>
    </tr>
    <tr>
      <th>1</th>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>78.934893</td>
      <td>639.0</td>
      <td>1884411</td>
      <td>Figueroa High School</td>
      <td>2949</td>
      <td>District</td>
    </tr>
    <tr>
      <th>2</th>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>83.542589</td>
      <td>600.0</td>
      <td>1056600</td>
      <td>Shelton High School</td>
      <td>1761</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>3</th>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>79.112082</td>
      <td>652.0</td>
      <td>3022020</td>
      <td>Hernandez High School</td>
      <td>4635</td>
      <td>District</td>
    </tr>
    <tr>
      <th>4</th>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>83.584128</td>
      <td>625.0</td>
      <td>917500</td>
      <td>Griffin High School</td>
      <td>1468</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>5</th>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>83.631844</td>
      <td>578.0</td>
      <td>1319574</td>
      <td>Wilson High School</td>
      <td>2283</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>6</th>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>83.518837</td>
      <td>582.0</td>
      <td>1081356</td>
      <td>Cabrera High School</td>
      <td>1858</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>7</th>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>79.041198</td>
      <td>628.0</td>
      <td>3124928</td>
      <td>Bailey High School</td>
      <td>4976</td>
      <td>District</td>
    </tr>
    <tr>
      <th>8</th>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>83.809133</td>
      <td>581.0</td>
      <td>248087</td>
      <td>Holden High School</td>
      <td>427</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>9</th>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>83.942308</td>
      <td>609.0</td>
      <td>585858</td>
      <td>Pena High School</td>
      <td>962</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>10</th>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>83.818611</td>
      <td>583.0</td>
      <td>1049400</td>
      <td>Wright High School</td>
      <td>1800</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>11</th>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>78.793698</td>
      <td>637.0</td>
      <td>2547363</td>
      <td>Rodriguez High School</td>
      <td>3999</td>
      <td>District</td>
    </tr>
    <tr>
      <th>12</th>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>79.019429</td>
      <td>650.0</td>
      <td>3094650</td>
      <td>Johnson High School</td>
      <td>4761</td>
      <td>District</td>
    </tr>
    <tr>
      <th>13</th>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>78.924425</td>
      <td>644.0</td>
      <td>1763916</td>
      <td>Ford High School</td>
      <td>2739</td>
      <td>District</td>
    </tr>
    <tr>
      <th>14</th>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>83.633639</td>
      <td>638.0</td>
      <td>1043130</td>
      <td>Thomas High School</td>
      <td>1635</td>
      <td>Charter</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Top Performing Schools 5 top schools
```


```python
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
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average_Math_Score</th>
      <th>Average_Reading_Score</th>
      <th>Per_Student_Budget</th>
      <th>School_Name</th>
      <th>School_Type</th>
      <th>Total_School_Budet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>83.83</td>
      <td>84.04</td>
      <td>609</td>
      <td>Pena_High_School</td>
      <td>Charter</td>
      <td>585858</td>
    </tr>
    <tr>
      <th>1</th>
      <td>83.68</td>
      <td>83.81</td>
      <td>583</td>
      <td>Wright_High_School</td>
      <td>Charter</td>
      <td>1049400</td>
    </tr>
    <tr>
      <th>2</th>
      <td>83.80</td>
      <td>83.90</td>
      <td>581</td>
      <td>Holden_High_School</td>
      <td>Charter</td>
      <td>248087</td>
    </tr>
    <tr>
      <th>3</th>
      <td>83.27</td>
      <td>83.90</td>
      <td>578</td>
      <td>Wilson_High_School</td>
      <td>Charter</td>
      <td>1319574</td>
    </tr>
    <tr>
      <th>4</th>
      <td>83.41</td>
      <td>83.60</td>
      <td>638</td>
      <td>Thomas_High_School</td>
      <td>Charter</td>
      <td>1043130</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Top Performing Schools 5 bottom Schools
```


```python
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
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average_Math_Score</th>
      <th>Average_Reading_Score</th>
      <th>Per_Student_Budget</th>
      <th>School_Name</th>
      <th>School_Type</th>
      <th>Total_School_Budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>77.10</td>
      <td>80.74</td>
      <td>644</td>
      <td>Ford_High_School</td>
      <td>District</td>
      <td>1763916</td>
    </tr>
    <tr>
      <th>1</th>
      <td>76.84</td>
      <td>80.74</td>
      <td>637</td>
      <td>Rodriguez_High_School</td>
      <td>District</td>
      <td>2547363</td>
    </tr>
    <tr>
      <th>2</th>
      <td>77.07</td>
      <td>80.96</td>
      <td>650</td>
      <td>Johnson_High_School</td>
      <td>Charter</td>
      <td>3094650</td>
    </tr>
    <tr>
      <th>3</th>
      <td>77.04</td>
      <td>79.04</td>
      <td>628</td>
      <td>Bailey_High_School</td>
      <td>District</td>
      <td>3124928</td>
    </tr>
    <tr>
      <th>4</th>
      <td>77.28</td>
      <td>80.93</td>
      <td>652</td>
      <td>Hernandez_High_School</td>
      <td>District</td>
      <td>3022020</td>
    </tr>
  </tbody>
</table>
</div>


