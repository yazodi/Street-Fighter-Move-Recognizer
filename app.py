import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Model ve yardımcı objeleri yükle
model = load_model("joystick_move_model.keras")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# Başlık
st.title("🎮 Street Fighter Combo Tahmin Edici")
st.write("Joystick sekansını girin (örn: DOWN,RIGHT,PUNCH)")

# Girdi
user_input = st.text_input("Joystick Kombinasyonu")

if st.button("Tahmin Et"):
    if user_input:
        seq = tokenizer.texts_to_sequences([user_input])
        pad = pad_sequences(seq, maxlen=model.input_shape[1], padding='post')
        prediction = model.predict(pad)
        predicted_move = label_encoder.inverse_transform([np.argmax(prediction)])
        st.success(f"🧠 Tahmin Edilen Hareket: **{predicted_move[0]}**")
    else:
        st.warning("Lütfen bir joystick sekansı girin.")
