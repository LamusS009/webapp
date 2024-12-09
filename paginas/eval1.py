import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.title("Evaluación De Retroalimentación")
st.markdown("La evaluación tendra una duración aproximada de 15 minutos y consistira de 3 modulos donde podrá poner a prueba algunos conceptos basicos adquiridos en el la lectura de la información de la pagina, el uso del solucionador y las graficas generadas")

st.header("Conceptos Basicos de SEL 2D")
st.subheader("***1. ¿Para que sirve el metodo de Gauss?***")
rs1 = st.selectbox("", ["Para sumar matrices de igual tamaño", "Para resolver SEL por medio de eliminación", "Para calcular raices cuadradas", "Para hallar la matrix adjunta"], key=1, index=None, placeholder="Seleccione una opción")

st.subheader("***2. ¿Cuales son las posibles soluciones en un SEL 2D?***")
rs2 = st.selectbox(" ", ["Unica, Infinita, sin solución", "Siempre tiene solucion", "Tiene todas las soluciones dependiendo del sistema", "Solo tiene solución cuando las variables son proporcionales"],key=2, index=None, placeholder="Seleccione una opción")

st.subheader("****3. ¿Que representa la unica solución de un SEL 2D***")
rs3 = st.selectbox("", ["El punto donde las rectas se intersecan", "La distancia que hay entre las rectas", "El punto que da solución a una de las ecuaciones", "La direccion que tiene  las rectas"],key=3, index=None, placeholder="Seleccione una opción")

st.header("Soluciones de SEL 2D")
st.subheader("***1. ¿Tiene este Sistema de Ecuaciones lineales solución?***")
st.latex(r"3x + 2y = 5 \\ x + y = 1 ")
rs4 = st.selectbox(" ", ["Si, es unica", "Si, tiene infinitas soluciones","No tiene soluciones", "No es un Sistema de Ecuaciones"], key=4, index=None, placeholder="Seleccione una opción")

st.subheader("***2. ¿Esta reducida a manera escalonada correctamente esta matrix?***")
st.latex(r"\begin{bmatrix} 4 & 5 & 1\\0 & 1 & 2\\0 & 0 & 2\end{bmatrix}")
rs5 = st.selectbox(" ", ["Si", "No, no es posible reducir esta matrix","No"], key=5, index=None, placeholder="Seleccione una opción")

st.subheader("""***3. ¿Cual es la solución del Sistema de Ecuaciones Lineales?***""")
st.latex(r"-3x + 4y = 4 \\ 4x + y = 1 ")
rs6 =st.selectbox("", ["( x = 0, y = 3)", "(x = 1, y = 0)", "(x = 0, y = 1)", "(x = -1, y = 0)"], key=6, index=None, placeholder="Seleccione una opción")






st.header("Graficas de SEL 2D")
st.subheader("***1. ¿Cual es la coordenada del punto solucion del SEL 2D***")

x = np.linspace(-7,7,50)
y1 = (2-x)/3
y2 = (1-(5*x))/6

fig, ax = plt.subplots()
ax.plot(x,y1)
ax.plot(x,y2)
ax.grid()
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
st.pyplot(fig)

rs7 = st.selectbox("", ["(X = 1, Y = 2)", "(X = -1, Y = 1)", "(X = 0 Y = 3)","(X = 1, Y = -1)"],key=7, index=None, placeholder="Seleccione una opción")

st.subheader("***1. ¿Cual es la coordenada del punto solucion del SEL 2D***")
x = np.linspace(-8,8,50)
y3 = (3+(2*x))/4
y4 = (3-(5*x))/(-3)

fig, ax = plt.subplots()
ax.plot(x,y3)
ax.plot(x,y4)
ax.grid()
ax.axhline(0,color="black",linewidth=1)
ax.axvline(0,color="black",linewidth=1)
st.pyplot(fig)

rs8 = st.selectbox("", ["y = (3 + 2x)  4", "y = (3 - 5x) / -3", "y = 12 + x" "y = (3 + 2x) / 2"], key=8, index=None, placeholder="Seleccione una opción")

respuesta = {
    "1" : "Para resolver SEL por medio de eliminación",
    "2" : "Unica, Infinita, sin solución",
    "3" :  "El punto donde las rectas se intersecan",
    "4" : "Si, es unica",
    "5" : "Si",
    "6" : "(x = 0, y = 1)",
    "7" : "(X = -1, Y = 1)",
    "8" : "y = (3 - 5x) / -3",
    "9" : ""
}
preg = [rs1,rs2,rs3,rs4,rs5,rs6,rs7,rs8]

cont = 0
if st.button("Revisar su puntuación"):
    for p, r in  zip(preg, respuesta.values()):
        if p == r:
            st.markdown("""La respuesta es correcta ¡Felicidades!""")
            cont +=1
        else:
            st.markdown(f"La respuesta es incorrecta. La respuesta es {r}")
            cont = cont
    if cont < 5:
        st.markdown(f"""Su puntacion fue {cont} ¡puedes hacerlo mejor!""")
    else:
        st.markdown(f"""Su puntacion fue {cont} ¡Felicidades!""")