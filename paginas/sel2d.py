import streamlit as st

st.title("Sistemas de Ecuaciones 2D")
st.header("Que son y sus aplicaciones")

st.markdown("""Un sistema de ecuaciones lineales en dos dimensiones es un conjunto de dos "reglas" que relacionan dos variables, que solemos llamar x y ***y***. Estas reglas se pueden escribir como líneas rectas cuando las dibujamos en un plano. La idea es encontrar el punto donde esas dos líneas se cruzan, si es que se cruzan. A veces, las líneas no se cruzan porque son paralelas, y otras veces son la misma línea, por lo que tienen muchos puntos en común.

Estos sistemas son súper útiles en la vida diaria y en diferentes áreas. Por ejemplo, pueden ayudarte a resolver problemas como repartir dinero entre dos personas, calcular cuánto de algo comprar con un presupuesto o entender cómo se equilibran las fuerzas en un puente. También se usan para ver dónde dos rutas se encuentran o para predecir cosas simples como precios o cantidades en economía. Son una herramienta básica, pero muy poderosa, que ayuda a resolver problemas en muchos contextos.
""")

st.subheader("¿Es esto un Sistema de ecuaciones Lineales?")
st.markdown("A continuación se mostrarán varias ecuaciones. Debes decir si son sistemas de ecuaciones lineales o no.")

clm1, clm2 = st.columns(2)

with clm1:
    st.latex(r"3x + πy = 6 \\ -2w + 3z = 5")
    rpst1 = st.selectbox("¿Es un Sistema de ecuaciones lineales?", ["Si","No"], key=1)
    st.latex(r"sen(x) + 2y = 3.4 \\ sen(90)w + 3z = 4")
    
with clm2:
    st.latex(r"3x + 4y = 8 \\ -1/2w + 3z = 0")
    rpst2 = st.selectbox("¿Es un Sistema de ecuaciones lineales?", ["Si","No"], key=3)
    st.latex(r"x/2 + 9y = 0 \\ w^2 + 3z = 6")

st.header("Metodo de Gauss para solucion de Sistemas de Ecuaciones Lineas 2D")
st.subheader("(De donde proviene y metodo de uso)")

st.markdown("""Las soluciones de un sistema de ecuaciones 2D son los valores de xx y yy que hacen que las dos ecuaciones sean verdaderas al mismo tiempo. En otras palabras, es el punto donde las dos líneas que representan las ecuaciones se cruzan en el plano. Puede haber una única solución (un solo punto), ninguna solución (si las líneas son paralelas y nunca se cruzan) o infinitas soluciones (si las líneas son exactamente la misma).

El método de Gauss, o eliminación gaussiana, es una forma organizada de resolver sistemas de ecuaciones usando matrices. La idea principal es transformar el sistema en algo más sencillo, como una escalera de números, haciendo operaciones como sumar o restar filas y dividirlas por números. Al final, puedes resolver el sistema fácilmente "de abajo hacia arriba", empezando con la última ecuación. Es como limpiar un lío de ecuaciones hasta que todo queda claro y ordenado. Es un método útil, sobre todo cuando hay más de dos ecuaciones o más de dos variables.
""")

with st.container(border=True):
    st.subheader("**Explicación metodo de Gauss**")
    st.video("https://youtu.be/2yfkEAt2ew0")



st.subheader("¿Son matrices que estan en forma escalonada?")
st.markdown("A continuación se mostrarán varias matrices. Debes indicar si estan reducidas de manera escalonada correcta")

c1, c2 = st.columns(2)

with c1 :
    st.latex(r"\begin{bmatrix} 3 & 5 & 0\\2 & 8 & 6\\7 & 1 & 4\end{bmatrix} ")
    rpst1 = st.selectbox("¿Es una matriz escalonada reducida de manera correcta?", ["Si","No"], key=5)
    st.latex(r"\begin{bmatrix} 4 & 5 & 1\\0 & 1 & 2\\0 & 0 & 2\end{bmatrix} ")

with c2 :
    st.latex(r"\begin{bmatrix} 2 & 1 & 2\\0 & 3 & 6\\0 & 0 & 0\end{bmatrix} ")
    st.latex(r"\begin{bmatrix} 1 & 2 & 0\\4 & 5 & 6\\9 & 3 & 0\end{bmatrix} ")

