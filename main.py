import streamlit as st

# Crear las paginas 

sel2d = st.Page("paginas/sel2d.py", title="Sistemas de Ecuaciones Lineales", default=True)
sol = st.Page("paginas/solsel.py", title="Solucionador SEL")
pres = st.Page("paginas/pres.py", title="Presentación ")
eval1 = st.Page("paginas/eval1.py", title="Evaluación")



# Navigation

pg = st.navigation({"Inicio" : [sel2d,sol,eval1],"Sobre mi" : [pres]})

# ejecutar

pg.run()