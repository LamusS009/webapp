import streamlit as st

# Crear las paginas 

sel2d = st.Page("paginas/sel2d.py", title="Sistemas de Ecuaciones Lineales", default=True)
sol = st.Page("paginas/solsel.py", title="Solucionador SEL")
graphs = st.Page("paginas/graficas.py", title="graficas")
eval1 = st.Page("paginas/eval1.py", title="Evaluación")



# Navigation

pg = st.navigation([sel2d,sol,eval1,graphs])

# ejecutar

pg.run()