import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def gauss(A,b):
    n = len(b)
    pasos = []

    mtx_aum = np.hstack([A,b.reshape(-1,1)])
    pasos.append(("Matrix inicial" , mtx_aum.copy()))

    for i in range (n):
        if mtx_aum[i,i] == 0:
            for j in range(i+1,n):
                if mtx_aum[j,i] !=0:
                    mtx_aum[i,j] = mtx_aum[j,i]
                    pasos.append(("Intercambio de filas", mtx_aum.copy()))
        for j in range (i+1,n):
            pivot = mtx_aum[j,i] / mtx_aum[i,i]
            mtx_aum[j] = mtx_aum[j] - (pivot*mtx_aum[i])
            pasos.append(("Generar 0 en la parte inferior", mtx_aum.copy()))

    x2 = mtx_aum[1,-1]/ mtx_aum[1,1]
    x1 = (mtx_aum[0,-1]-(mtx_aum[0,1]*x2))/ mtx_aum[0,0] 

    v_sol = np.array([x1,x2]).reshape(-1,1)

    pasos.append(("Solución final", v_sol))
    return np.array([x1, x2]), pasos


st.title("Solucionador de Sistemas de Ecuaciones lineales 2D")

st.markdown("""Esta herrramienta le permitira solucionar sus Sistemas de Ecuaciones Lineales 2D ingresando los valores de los terminos correspondientes. **Ingrese los coeficientes de su ecuación recordando la estructura del SEL 2D :** """ )

with st.container(border=True):
    st.markdown("Estructura SEL 2D")
    st.latex(r"ax + ry = c \\ dw + ez = f")

clm1, clm2, clm3 = st.columns(3)

with clm1:
    a = st.number_input("Ingrese el valor del coeficiente ***a***", value=1.00)
    d = st.number_input("Ingrese el valor del coeficiente ***d***", value=2.00)

with clm2:
    r = st.number_input("Ingrese el valor del coeficiente ***r***", value=1.00)
    e = st.number_input("Ingrese el valor del coeficiente ***e***", value=1.00)

with clm3:
    c = st.number_input("Ingrese el valor del 1° resultado ***c***", value=1.00)
    f = st.number_input("Ingrese el valor del 2° resultado ***f***", value=1.00)

A = np.array([[a,r], [d,e]])
b = np.array([c,f])

if st.button("Resolver"):
    if np.linalg.det(A) == 0:
        st.error("El Sistema de Ecuaciones no tiene solución unica")
    else: 
        solucion, pasos = gauss(A,b)
        st.subheader("Pasos de la solución")
        for npasos, matrix in pasos:
            st.markdown(f"{npasos}")
            st.dataframe(pd.DataFrame(matrix))

        st.subheader("Solucion")
        st.markdown(f"x1 = {solucion[0]:.2f}, x2 = {solucion[1]:.2f}") 
        
        
        x = np.linspace(-10,10,400)
        if r == 0:
            x = c/a
            y1 = np.linspace(-10,10,400)
        else:
            y1 = (c-(a*x))/r

        if e == 0:
            x = f/d
            y2 = np.linspace(-10,10,400)
        else:
            y2 = (f - (d*x))/e

        fig,ax = plt.subplots()

        ax.plot(x, y1, label="Grafica 1")
        ax.plot(x,y2, label="Grafica 2")
        ax.grid()
        ax.scatter(solucion[0], solucion[1], color="red", label="Solución")
        ax.axhline(0, color='black', linewidth=0.7)  
        ax.axvline(0, color='black', linewidth=0.7)  
        ax.legend()  
        ax.set_title("Gráfica de las rectas y su solución")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        st.pyplot(fig)





