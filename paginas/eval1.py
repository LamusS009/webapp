import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.title("Evaluación De Retroalimentación")
st.markdown("La evaluación tendra una duración aproximada de 15 minutos y consistira de 3 modulos donde podrá poner a prueba algunos conceptos basicos adquiridos en el la lectura de la información de la pagina, el uso del solucionador y las graficas generadas")

st.header("Conceptos Basicos de SEL 2D")
st.subheader("***1. ¿Para que sirve un sistema de ecuaciones lineales?***")

st.markdown("¿Para que sirve un sistema de ecuaciones lineales?")
st.subheader("***2. ¿Cuales son las posibles soluciones en un SEL 2D?***")

st.subheader("****3. ¿Que representa la unica solución de un SEL 2D***")


st.header("Soluciones de SEL 2D")
st.subheader("***1. ¿Tiene este Sistema de Ecuaciones lineales solución?***")
st.latex(r"3x + 2y = 5 \\ y = 2 ")
st.selectbox(" ", ["Seleccione una opcion", "Si, es unica", "Si, tiene infinitas soluciones","No tiene soluciones", "No es un Sistema de Ecuaciones"], key=4)
st.subheader("***2. ¿Esta reducida a manera escalonada correctamente esta matrix?***")
st.latex(r"\begin{bmatrix} 4 & 5 & 1\\0 & 1 & 2\\0 & 0 & 2\end{bmatrix}")
st.selectbox(" ", ["Seleccione una opcion", "Si", "No, no es posible reducir esta matrix","No"], key=5)






st.header("Graficas de SEL 2D")
st.subheader("***1. ¿Cual es la coordenada del punto solucion del SEL 2D")

x = np.linspace(-7,7,50)
y1 = (2-x)/3
y2 = (1-(5*x))/6

fig, ax = plt.subplots()
ax.plot(x,y1)
ax.plot(x,y2)
ax.grid()
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
sy.pyplot(fig)

st.selectbox("", ["Seleccione una opción", "(X = 1, Y = 2)", "(X = -1, Y = 1)", "(X = 0 Y = 3)","(X = 1, Y = -1)"]key=7)

st.subheader("***1. ¿Cual es la coordenada del punto solucion del SEL 2D")
x = np.linspace(-8,8,50)
y3 = (3+(2*x))/4
y4 = (3-(5*x))/(-3)

fig, ax = plt.subplots()
ax.plot(x,y3)
ax.plot(x,y4)
ax.grid()
ax.axhline(0,color="black",linewidth=1)
ax.axvline(0,color="black",linewidth=1)
sy.pyplot(fig)


