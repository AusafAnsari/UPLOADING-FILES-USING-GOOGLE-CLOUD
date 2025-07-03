ɪɴ ᴛʜɪꜱ ᴘʀᴏᴊᴇᴄᴛ ɪ ʜᴀᴠᴇ ᴜꜱᴇᴅ ɢᴏᴏɢʟᴇ ᴄʟᴏᴜᴅ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴀɴᴅ ꜱᴛᴏʀᴇ ᴀɴʏ ᴅᴀᴛᴀ ᴡɪᴛʜᴏᴜᴛ ᴏᴘᴇɴɪɴɢ ᴛʜᴇ ᴘʟᴀᴛꜰᴏʀᴍ



# ☁️ Uploading Files Using Google Cloud

A clean Python script with **Streamlit UI** that allows users to upload files directly to **Google Cloud Storage** (GCS) via a user-friendly interface. Ideal for quick file transfers and demo integrations!

---

## ✨ Features

- Upload single or multiple files through a browser interface  
- Progress feedback for file uploads  
- Configurable Google Cloud Storage bucket  
- Secure authentication via service account JSON  
- Simple, intuitive interface powered by Streamlit  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x  
- A Google Cloud project with a **Storage bucket** set up  
- Service account key JSON with write permissions to GCS  

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/AusafAnsari/UPLOADING-FILES-USING-GOOGLE-CLOUD.git
cd UPLOADING-FILES-USING-GOOGLE-CLOUD
```

2. **Install the required packages**

```bash
pip install streamlit google-cloud-storage
```

3. **Add your service account key**

Place your `service_account.json` file in the project root.

4. **Update bucket name**

Open the script (e.g., `app.py` or `upload_to_gcs.py`) and set your bucket:

```python
BUCKET_NAME = "your-gcs-bucket-name"
```

5. **Run the Streamlit app**

```bash
streamlit run app.py
```

---

## 🧠 How It Works

- Streamlit app provides file uploader in the browser  
- Reads each selected file and uploads to the specified GCS bucket  
- Displays upload status and success confirmation  

---

## 📁 Project Structure

```
UPLOADING-FILES-USING-GOOGLE-CLOUD/
├── app.py                   # Streamlit app with upload logic
├── requirements.txt         # Python dependencies
└── service_account.json     # GCS service account credentials
```

---

## 🔐 Security Tip

- Never commit `service_account.json` to a public repo  
- Use `.gitignore` to exclude it  
- Rotate credentials regularly for enhanced security  

---

## ✍️ Author

**Ausaf Ansari**  
[GitHub Profile](https://github.com/AusafAnsari)

---

## 📝 License

This project is licensed under the **MIT License**.

