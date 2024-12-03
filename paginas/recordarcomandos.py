import streamlit as st
import numpy as np

st.title("Esta es la pagina de textos")

#titulos 
st.title("titulo de nivel 1")
st.header("titulo de nivel 2")
st.subheader("titulo de nivel 3")


#textos 

st.markdown("""
En una etiqueta se pueden poner textos en **negrilla**, en *italica* o en ***ambos*** 

esto es otra linea.

enumeraciones
1.Primer item
2.Segundo item
3.tercer item

Items
+Item 1 
+Item 2
+Item 3

Podemos dar color al texto por ejemplo :red[rojo], :blue[azul], :violet[violeta]""")


#Montar ecuaciones

st.latex("a^2 + b^2 = c^2")

#Para multimedia

st.image("https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSYSLAWBiJmsPd9Mx-bxBamGZJLGbVKV92Yof6lWfV6-E6l0Bw67JUE9_2o1XcZBQsK4A7lOaUij0fgDpQls0QkHA")

st.video("https://youtu.be/2yfkEAt2ew0")


#layout

# container
with st.container(border=True):
    st.markdown("Formula del estudiante")
    st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")

# columns
c1,c2 = st.columns(2,vertical_alignment = "center")
with c1:
    st.markdown("Debe estar en columna 1")
with c2:
    st.markdown("debe estar en la comuna 2")

st.divider()

# Todo de sliders and inputs 

st.title("pagina de inputs")

nombre = st.text_input("Digite nombre :")


# pedir numeros

edad = st.number_input("ingrese su edad :",min_value=0, max_value=120, value=18) 

# Es posible colocar if y realizar todo tipo de calculos con esas variables

rango = st.slider("digite un valor : ", min_value=10, max_value=100)

ini, final = st.slider("seleccione rango :", min_value=10, max_value=100, value=(2,4))

st.markdown(f"Valor de inicio: {ini}")
st.markdown(f"Valor final: {final}")

#seleccione 



#seleccione 

x = st.number_input("x", value=1)
y = st.number_input("y", value=1)


opc= st.selectbox("operacion", options=["suma", "resta", "multiplicación"])






st.title("Evaluación De Retroalimentación")
st.markdown("La evaluación tendra una duración aproximada de 10 minutos donde podrá poner a prueba algunos conceptos basicos adquiridos en el la lectura de la información de la pagina, el uso del solucionador y las graficas generadas")



import streamlit as st
import numpy as np

st.title("Solucionador de Sistemas de Ecuaciones lineales 2D")

st.markdown("""Esta herrramienta le permitira solucionar sus Sistemas de Ecuaciones Lineales 2D ingresando los valores de los terminos correspondientes. **Ingrese los coeficientes de su ecuación recordando la estructura del SEL 2D :** """ )

with st.container(border=True):
    st.markdown("Estructura SEL 2D")
    st.latex(r"ax + by = p \\ cw + dz = l")

c1,c2,c3,c4 = st.columns(4)

with c1:
    a = st.number_input("ingrese su coeficiente **a** :",min_value=-1000000, max_value=120, value=1)
with c2:
    b = st.number_input("ingrese su coeficiente **b** :",min_value=-1000000, max_value=120, value=3)
with c3:
    c = st.number_input("ingrese su coeficiente **c** :",min_value=-1000000, max_value=120, value=5)
with c4:
    d = st.number_input("ingrese su coeficiente **d** :",min_value=-1000000, max_value=120, value=7)



