# -*- coding: utf-8 -*-
"""
@author: Victor Resende
"""
import streamlit as st
import time
def amor():
    with st.spinner('Calculando...'):
        time.sleep(5)
        st.markdown("<p style='text-align: justify; color: #750202;'> A quantidade de amor é: 1000 de 1000</p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='text-align: justify; color: #750202;'> Acurácia: 100% (❤️) </p>",
                    unsafe_allow_html=True)

st.set_page_config(page_icon='❤️', page_title='Com amor', layout='wide')
st.markdown("<h1 style='text-align: center; color: #fc0345; font-size: 42px'> Uma carta de amor </h1>",
            unsafe_allow_html=True)
st.markdown("""
        <style>
            .stApp {
                background-color: white;
                background-size: cover;
            }
            .streamlit-expanderHeader {
                color: black !important;
            }
        </style>""",unsafe_allow_html=True)  
st.markdown("<p style='text-align: center; color: #fc0345;'> De Victor para Cecília </p>",
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #fc0345; font-size: 22px'> Atração é o primeiro estágio, onde nasce a curiosidade e atração. A paixão é intensa e avassaladora, marcada por emoções arrebatadoras. Já o amor é o ápice, uma conexão profunda, calma e duradoura, que transcende a paixão, revelando um sentimento sereno e verdadeiro. </p>",
            unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.write('')
with col2:
    expanderAbout = st.expander( 
    label="❤️ Do maior poeta para a minha poeta preferida: Quando ela fala, de Machado de Assis ❤️ (clique aqui)")
    expanderAbout.markdown(
        """<p style='text-align: center; color: #fc0345; font-size: 18px'>
            Quando ela fala, parece <br>
            Que a voz da brisa se cala; <br>
            Talvez um anjo emudece <br>
            Quando ela fala. <br><br>
            Meu coração dolorido <br>
            As suas mágoas exala, <br>
            E volta ao gozo perdido <br>
            Quando ela fala. <br><br>
            Pudesse eu eternamente, <br>
            Ao lado dela, escutá-la, <br>
            Ouvir sua alma inocente <br>
            Quando ela fala. <br><br>
            Minha alma, já semimorta, <br>
            Conseguira ao céu alçá-la <br>
            Porque o céu abre uma porta <br>
            Quando ela fala. <br><br>
            Quando ela fala, de Machado de Assis
        </p>""",
        unsafe_allow_html=True)
with col3:
    st.write('')
col4, col1, col2, col3, col5 = st.columns(5)
with col4:
    st.write('')
with col1:
   st.markdown("<h2 style='text-align: center; color: #fc0345;'> Atração </h2>",
               unsafe_allow_html=True)
   st.markdown("<p style='text-align: justify; color: #fc0345; font-size: 22px'> A atração é a semente que floresce em um relacionamento duradouro. Ele nos impulsiona a conhecer o outro, compreender suas nuances e cultivar uma conexão genuína. Lembro-me quando começamos a conversar no meu aniversário, realmente acredito que foi um presente de Deus, uma pessoa tão linda, engraçada, maravilhosa, disposta a sair, conhecer coisas novas ou até mesmo jogar, isso me conquistou de maneira tão profunda que já sentia-me viciado em sua companhia. Lembro do nosso primeiro encontro, da primeira vez que segurei sua bolsa, da primeira vez que te dei flores, da primeira vez que fui a sua casa, do nosso primeiro sorriso e do nosso primeiro beijo no CCBB, onde possívelmente brincamos quando crianças em passeios da escola. </p>",
               unsafe_allow_html=True)
   
with col2:
    st.markdown("<h2 style='text-align: center; color: #750202;'> Paixão </h2>",
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: #750202; font-size: 22px'> A paixão é a chama ardente que aquece os corações e revigora a conexão em um relacionamento duradouro. Ela mantém viva a intensidade dos sentimentos, reavivando a admiração e atração mútua. Com ela, os momentos a dois são como eternos instantes de êxtase, sustentando a solidez de um amor que transcende o tempo.  Desde que percebi estar apaixonado por você, não pude deixar de tentar demonstrar isso. Certamente em alguns momentos falhei, mas eu sempre apreciei nossos momentos, risadas e beijos, dos quais me faziam sentir uma realização imensurável. Você é especial para mim, ninguém nunca me fez sentir algo como sinto por ti, a cada beijo, toque ou risada, meu coração ficava em paz, quente e confortável.</p>",
                unsafe_allow_html=True)
   
with col3:
    st.markdown("<h2 style='text-align: center; color: #b50730;'> Amor </h2>",
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: #b50730; font-size: 22px'> O amor é a essência que nutre a cumplicidade, a compreensão e a vontade de fazer o outro feliz. Com o amor, cada momento se torna precioso e cada obstáculo se transforma em oportunidade para crescerem juntos, construindo uma história de amor eterno. Entretanto, nem tudo em um relacionamento se resume ao amor, existe o compromisso, companheirismo, dedicação e zelo. Entendi que realmente era amor quando a nossa relação de intimidade começou a crescer, quando conheci sua família e você a minha e quando sabia que podia contar com você em momentos delicados, assim como você tinha a mim. Eu acordava e deitava como a pessoa mais feliz e realizada do mundo, eu amo estar junto e desfrutar a vida com você. </p>",
                unsafe_allow_html=True)
   
with col5:
    st.write('')
st.markdown("""
    <link
        rel="icon"
        type="image/png"
        sizes="100%"
        href="https://cdn-icons-png.flaticon.com/512/9444/9444300.png"
        />
    <style>
    p {
    text-align: center;
    font-size: 32px;
    font-family: Georgia, serif;
    }
    img {
    display: block;
    margin: 0 auto;
    width: 23%;
    }
    </style>
    <img src="https://media.tenor.com/WQjlw86rlpsAAAAC/muah-kiss.gif">
    """,
    unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.write('')
with col2:
    if st.button('Clique para o modelo prever a quantidade de amor que sinto por você'):
        amor()
with col3:
    st.write('')
st.markdown("<p style='text-align: justify; color: #750202; font-size: 22px'> Você é uma pessoa maravilhosa, em todas as áreas da vida, tenho muito orgulho e me inspiro em suas atitudes, das quais me ensinaram bastante. Eu espero que possamos realizar nossos sonhos juntos, viver momentos inesquecíveis e que as coisas se ajeitem, afinal eu te amo e quero poder cuidar de você, confortar em momentos de dificuldade e comemorar os momentos de alegrias. </p>",
            unsafe_allow_html=True)
st.markdown("<p style='text-align: justify; color: #750202; font-size: 22px'> Não precisamos estressar por coisas bobas, no final o nosso amor é maior do que elas, do qual tenho certeza que éramos muito felizes juntos. Eu sempre estarei disposto e disponível a te escutar, diálogar, absorver e pronto a mudar caso necessário, afinal você é importante e especial pra mim, o amor da minha vida. </p>",
            unsafe_allow_html=True)
st.markdown("<p style='text-align: justify; color: #750202; font-size: 22px'> Quero poder me entregar ao nosso amor, te chamar de mozi, te levar para lugares incríveis, sentir seu beijo, sentir seu toque, dormir com você, fazer coisas do nada, quero poder te farejar, sentir-me e fazer-te feliz ao olhar no fundo dos seus lindos olhos.  </p>",
            unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #750202; font-size: 22px'> ❤️❤️ Te amo ❤️❤️ </h2>",
            unsafe_allow_html=True)
st.markdown("<h2 style='text-align: justify; color: #750202; font-size: 22px'> P.S: Leia a carta física também </h2>",
            unsafe_allow_html=True)
