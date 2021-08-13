### Hi there 👋

<!--
**Maara21/Maara21** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
import module 

from tabulate import tabulate 

  
# assign data 

mydata = [{"kumar", "kalvi"},  

          {"Ravi", "Kompan"},  

          {"Pavi", "kutti"},  

          {"Maara", "theri"}] 

  
# create header 

head = ["Name", "movies"] 

  
# display table 

print(tabulate(mydata, headers=head, tablefmt="grid")) 
Output:
     Name movies
     Kumar ,kalvi
     Ravi  ,Kompan
     Pavi  ,kutti
     Maara ,theri
#Enter thé movie name 

#Enter actor name and director 

# year of passing 
# awards

  

import mysql.connector 

  

  

mydb = mysql.connector.connect( 

  Movies = "Kumar-kalvi,Ravi-Kompan,Pavi-kutti,Mar
aara-theri",


  Director = "attlee", 

  Year = "2021", 

  database = "database_name"
)  

  

mycursor = mydb.cursor()
sql = "INSERT INTO Movies (actor, director) VALUES (%s, %s)"

val = ("kumar-kalvi,attle,21,2)
      ("Ravi -kompan,attle ,21,2)
    



  
mycursor.execute(sql, val) 
mydb.commit() 

  

print(mycursor.rowcount, "details inserted") 

  
# disconnecting from server 
mydb.close() 
Output:
   Name director actor awared year 
   Kalvi  attlee  Kumar   2   2021
   Ravi   attlee  Kompan  2    2021
  

