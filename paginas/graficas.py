import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd


st.title("Graficas")

# creo los puntos
x = [0,1,2,3,5]
y = [2,3,3,2,1]


# Creo el canva
fig, ax = plt.subplots()


# Dibujo el canva
ax.plot(x,y)

# Configuraciones (opcional)
ax.grid()  #Genera la cuadricula del grafico

 

# Mostrar el streamlit
st.pyplot(fig)


st.divider()

## PARA GRAFICAR FUNCIONES 

x = np.linspace(-np.pi, np.pi, 50)
y = np.sin(x)


fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()

st.pyplot(fig)


#Graficas x al 2 - 5

clm1, clm2 = st.columns([1,2],vertical_alignment= "center")

with clm1 : 
    st.markdown("Para mostrar diferentes intervalos en la grafica de la funcion  $f(x) = x+5$ utilice el siguiente deslizador")
    xin, xfin = st.slider("intervalo", min_value=-10, max_value=10, value=[-2,2])

with clm2:
    x = np.linspace(-3,3, 50)
    y = x**2-5


fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()

st.pyplot(fig)


st.divider()

st.subheader("Graficando figuras")

puntos = pd.DataFrame({
    "x": [1,1,-1],
    "y": [1,-1,0.5],
})

pol = patches.Polygon(puntos, closed=True, fill=True, facecolor="skyblue", edgecolor="navy")

fig, axis = plt.subplots()
ax.add_patch(pol)

ax.set_xlim(puntos["x"].min()-1, puntos["x"].max()+1)
ax.set_ylim(puntos["y"].min()-1, puntos["y"].max()+1)

ax.set_aspect("equal")


st.pyplot(fig)

st.divider()

st.subheader("Graficando figuras")

c1,c2 = st.columns([1,2])

with c1 :
    puntos = pd.DataFrame({
    "x": [1,1,-1],
    "y": [1,-1,0.5],
    })

st.data_editor()

pol = patches.Polygon(puntos, closed=True, fill=True, facecolor="skyblue", edgecolor="navy")

fig, axis = plt.subplots()
ax.add_patch(pol)

ax.set_xlim(puntos["x"].min()-1, puntos["x"].max()+1)
ax.set_ylim(puntos["y"].min()-1, puntos["y"].max()+1)

ax.set_aspect("equal")


st.pyplot(fig)




