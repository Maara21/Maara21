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
