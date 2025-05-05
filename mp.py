import streamlit as st
import pandas as pd
izquierda,centro,derecha=st.columns(3)
st.title("clientes")
with izquierda:
    nombre=st.text_input("nombre:")
    apellidos=st.text_input("apellidos:")
    edad=st.number_input_input("edad:")
    if edad<18:
        menor=("menor de edad")
    else:
        menor=("mayor de edad")
with centro:
    correo=st.text_input("correo:")  
    telefono=st.text_input("telefono:")
    direccion=st.text_input("direccion:")
with derecha:
    identificacion=st.number_input_input("identificacion:")
    tipo=st.text_input("tipo de identificacion:")
if st.button("guardar"):
    st.success(f"nombre:{nombre}")
    st.success(f"apellidos:{apellidos}")
    st.success(f"edad:{edad}")
    st.success(f"menor o mayor:{menor}")
    st.success(f"correo:{correo}")
    st.success(f"telefono:{telefono}")
    st.success(f"direccion:{direccion}")
    st.success(f"identificacion:{identificacion}")
    st.success(f"tipo:{tipo}")







