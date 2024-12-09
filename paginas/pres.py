import streamlit as st


st.title("Presentación Personal")

clm1, clm2 = st.columns([1,2], vertical_alignment="center")

with clm1:
    with st.container(border=True):
        st.image ("https://static.vecteezy.com/system/resources/previews/010/880/780/non_2x/smiling-kid-face-boy-avatar-child-with-skin-cartoon-head-portrait-school-character-icon-cute-little-person-teenager-flat-illustration-isolated-on-white-vector.jpg")

with clm2 :
    st.markdown("""
    Soy de Bucaramanga, actualmente soy estudiante en la UIS. Mi área de afinidad en las matemáticas es el Álgebra Lineal,que permite explorar y resolver problemas complejos de manera lógica y estructurada. Esta disciplina es clave para la carrera de matematicas y algunas experiencias más.
    Además de las matemáticas, me apasionan áreas como Programación, que me permiten aplicar mis conocimientos y desarrollar soluciones innovadoras. También disfruto de otros intereses como deportes, música, lectura, etc..""")


with st.container(border=True):
    st.subheader("¿Qué enseñanza me dejó la materia de Programación?")
    st.markdown("""
    La materia de Programación I me dejó valiosas lecciones sobre la importancia de lalógica. Aprendí a aplicar algunas cosas de la programación en la carrera y en distintas
    areas de manera estructurada, al final el manejo de algunas herramientas que nos permitan el manejo de datos y creación de paginas web, por ultimo y más importante las bases solidas para seguir aprendiendo y aplicandolo en la carrera de Matematicas.
    """)






