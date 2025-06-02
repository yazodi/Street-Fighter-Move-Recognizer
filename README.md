---
tags:
- deep-learning
- lstm
- game-ai
- sequence-classification
- streamlit-app
---

# 🎮 Street Fighter Move Recognizer

Bu proje, joystick kombinasyonlarını analiz ederek oyuncunun hangi **özel hareketi** yapmak istediğini tahmin eden bir makine öğrenimi modelini içermektedir. Veri simüle edilmiştir ve Street Fighter benzeri dövüş oyunlarından esinlenilmiştir.

## 🧠 Proje Hedefi

Joystick sekanslarından (`["DOWN", "RIGHT", "PUNCH"]` gibi) yola çıkarak hangi **move (hareket)** yapıldığını sınıflandıran bir sekans model geliştirmek. Bu, oyun AI sistemlerinin temel yapı taşlarından biridir.

---

## 📊 Kullanılan Veri

Veri seti manuel olarak oluşturulmuştur ve aşağıdaki gibi örnek joystick girişlerinden ve etiketli hareket isimlerinden oluşur:

| Joystick Sequence           | Move           |
|-----------------------------|----------------|
| DOWN,RIGHT,PUNCH            | Hadouken       |
| RIGHT,DOWN,RIGHT,KICK       | Shoryuken      |
| LEFT,LEFT,PUNCH             | Dash Punch     |
| DOWN,KICK                   | Low Kick       |
| LEFT,DOWN,RIGHT,PUNCH       | Combo Strike   |
| ...                         | ...            |

---

## 🔧 Kullanılan Teknolojiler

- **TensorFlow / Keras** – LSTM model ile sekans sınıflandırma
- **scikit-learn** – LabelEncoder
- **Streamlit** – Web arayüzü
- **Pickle** – Model nesnelerinin kaydedilmesi
- **Hugging Face Hub** – Model paylaşımı
- **GitHub** – Kod ve dokümantasyon paylaşımı

---

## 🏗️ Model Mimarisi

- `Tokenizer` ile joystick girişleri tokenize edildi
- `pad_sequences` ile sabit uzunlukta girişe dönüştürüldü
- `LSTM` tabanlı sekans modeli eğitildi
- `LabelEncoder` ile sınıf etiketleri dönüştürüldü
- Model `.keras`, `tokenizer.pkl`, `label_encoder.pkl` olarak kaydedildi

---

## 🚀 Streamlit Uygulaması

Kullanıcıdan joystick kombinasyonu alınır ve model ile eşleşen hareket tahmin edilir.

### Uygulamayı Başlatmak İçin:
```bash
streamlit run app.py


🔬 Örnek Tahmin
DOWN,RIGHT,PUNCH
Çıktı:
Tahmin Edilen Hareket: Hadouken



💡 Gelecekte Ne Yapılabilir?
Gerçek zamanlı joystick verisi entegrasyonu

Sesli komut tanıma ile komboları tetikleme

Mobil uyumlu arayüz

Daha fazla kombo ile veri setinin genişletilmesi


📚 Eğitim Amaçlıdır
Bu proje, oyun zekası ve sekans modellemeyi birleştiren bir örnek olarak eğitim amaçlı geliştirilmiştir.
