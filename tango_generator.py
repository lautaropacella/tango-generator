
import streamlit as st
from aitextgen.TokenDataset import TokenDataset
from aitextgen.tokenizers import train_tokenizer
from aitextgen import aitextgen
from PIL import Image
ai = aitextgen(model_folder="trained_model",
                tokenizer_file="aitextgen.tokenizer.json")
st.beta_set_page_config(layout="wide")
image2 = Image.open('Tango2.jpg')

expli = st.sidebar.beta_expander("Temperature", expanded=False)
with expli:
    st.write('Mientras mayor la temperatura, más "loco" el texto (recomendado: 0.7)')
temp = st.sidebar.slider("", value=0.7, min_value=0.6, max_value=1.2, step=0.1,)

expli2 = st.sidebar.beta_expander("Top K", expanded=False)
with expli2:
    st.write('Límite de palabras utilizadas para la muestra en la generación de la letra (recomendado: 0)')
top_k = st.sidebar.slider("",value=0, min_value=0, max_value=40, step=1)

expli3 = st.sidebar.beta_expander("Top P", expanded=False)
with expli3:
    st.write('Probabilidad cumulativa del modelo para elegir las palabras de la letra (recomendado: 0.9)') 
top_p = st.sidebar.slider("",value=0.9, min_value=0.5, max_value=1.0, step=0.1)

    
st.title('Tango Cromado')
st.subheader('Generación de letras de tango utilizando la arquitectura del Modelo GPT-2')
st.write('Creado por Lautaro Pacella')
st.image(image2)
inicio = st.text_input('Podes empezar con una palabra o frase tuya o dejar que el modelo genere una letra completamente al azar')
propio = st.button("Generar")

if propio:
    col1,col2,col3 = st.beta_columns(3)
    with col2:
        if inicio:
            st.write(ai.generate_one(prompt=inicio, temperature = temp, top_k = top_k, top_p = top_p).replace('\r\n', '  \n'))
        else:
            st.write(ai.generate_one(temperature = temp, top_k = top_k, top_p = top_p).replace('\r\n', '  \n'))
        

