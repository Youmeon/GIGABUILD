# import os
# import time
# import base64
# import uuid
# import sqlite3
# import requests
# import urllib3
# from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import JSONResponse, FileResponse
# from fastapi.staticfiles import StaticFiles
# from dotenv import load_dotenv
# from sentence_transformers import SentenceTransformer
# import faiss
# import fitz
# from docx import Document

# # Отключаем предупреждения о самоподписанных сертификатах
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# # Загружаем переменные окружения
# load_dotenv()
# GIGACHAT_CLIENT_ID = os.getenv("GIGACHAT_CLIENT_ID")
# GIGACHAT_CLIENT_SECRET = os.getenv("GIGACHAT_CLIENT_SECRET")
# PORT = int(os.getenv("PORT", 8000))

# # URL-адреса API
# TOKEN_URL = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
# CHAT_URL = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

# # Инициализация FastAPI
# app = FastAPI()

# # Разрешаем CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Статика
# if os.path.exists("./frontend"):
#     app.mount("/static", StaticFiles(directory="./frontend", html=True), name="static")
# else:
#     print("Предупреждение: папка './frontend' не найдена, статика не будет смонтирована.")

# # Глобальные переменные
# token = None
# token_expiry = 0.0

# # Модель эмбеддингов
# embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# # Загрузка контекста
# docs = []
# if os.path.exists("context"):
#     for fname in os.listdir("context"):
#         path = os.path.join("context", fname)
#         if not os.path.isfile(path):
#             continue
#         ext = fname.lower().split('.')[-1]
#         text = ""
#         try:
#             if ext == "pdf":
#                 pdf = fitz.open(path)
#                 text = "\n".join(p.get_text() for p in pdf)
#                 pdf.close()
#             elif ext == "docx":
#                 docx = Document(path)
#                 text = "\n".join(p.text for p in docx.paragraphs)
#             elif ext == "txt":
#                 with open(path, "r", encoding="utf-8") as f:
#                     text = f.read()
#             if text.strip():
#                 docs.append(text)
#         except Exception as e:
#             print(f"Ошибка при обработке файла {fname}: {e}")
# else:
#     print("Предупреждение: папка 'context' не найдена.")

# # FAISS-индекс
# if docs:
#     embs = embed_model.encode(docs)
#     dim = embs.shape[1]
#     index = faiss.IndexFlatL2(dim)
#     index.add(embs)
# else:
#     dim = 384
#     index = faiss.IndexFlatL2(dim)

# def get_token():
#     """Получает токен доступа для GigaChat"""
#     global token, token_expiry
#     auth = f"{GIGACHAT_CLIENT_ID}:{GIGACHAT_CLIENT_SECRET}"
#     b64 = base64.b64encode(auth.encode()).decode()

#     headers = {
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Accept": "application/json",
#         "Authorization": f"Basic {b64}",
#         "RqUID": str(uuid.uuid4())
#     }
#     data = {"scope": "GIGACHAT_API_PERS"}

#     resp = requests.post(TOKEN_URL, headers=headers, data=data, verify=False)
#     resp.raise_for_status()
#     js = resp.json()

#     token = js.get("access_token") or js.get("accessToken")
#     expires = js.get("expires_in") or js.get("expiresInSec") or 1800
#     token_expiry = time.time() + expires - 60

# @app.get("/")
# async def root():
#     index_path = os.path.join("./frontend", "index.html")
#     if os.path.exists(index_path):
#         return FileResponse(index_path)
#     return JSONResponse({"error": "index.html не найден"}, status_code=404)

# @app.get("/favicon.ico")
# async def favicon():
#     path = os.path.join("./frontend", "favicon.ico")
#     if os.path.exists(path):
#         return FileResponse(path)
#     return {}

# @app.post("/chat")
# async def chat(request: Request):
#     global token, token_expiry
#     try:
#         data = await request.json()
#         user_msg = data.get("message", "").strip()
#         if not user_msg:
#             return JSONResponse({"answer": "Пожалуйста, введите сообщение."}, status_code=400)

#         # Получаем или обновляем токен
#         if time.time() >= token_expiry or not token:
#             get_token()

#         # Поиск релевантного контекста
#         q_emb = embed_model.encode([user_msg])
#         k = min(3, len(docs)) if docs else 0
#         context = ""
#         if k > 0:
#             _, I = index.search(q_emb, k)
#             context = "\n\n".join(docs[i] for i in I[0] if i >= 0)

#         headers = {
#             "Accept": "application/json",
#             "Authorization": f"Bearer {token}"
#         }
#         payload = {
#             "model": "GigaChat",
#             "messages": [
#                 {"role": "system", "content": "Вы — помощник, отвечающий строго на основе предоставленной информации."},
#                 {"role": "assistant", "content": f"Контекст:\n{context}" if context else "Контекст отсутствует."},
#                 {"role": "user", "content": user_msg}
#             ]
#         }

#         try:
#             resp = requests.post(CHAT_URL, headers=headers, json=payload, verify=False)
#             resp.raise_for_status()
#         except requests.exceptions.HTTPError as http_err:
#             print(f"\n--- GigaChat API ERROR ---")
#             print(f"Status code: {resp.status_code}")
#             print(f"Response body: {resp.text}")
#             print(f"Exception: {http_err}")
#             print(f"--------------------------\n")
#             raise

#         ans = resp.json()["choices"][0]["message"]["content"]

#         # Сохраняем в БД
#         conn = sqlite3.connect("history.db")
#         cur = conn.cursor()
#         cur.execute("""CREATE TABLE IF NOT EXISTS history 
#                        (id INTEGER PRIMARY KEY, user TEXT, bot TEXT, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
#         cur.execute("INSERT INTO history (user, bot) VALUES (?, ?)", (user_msg, ans))
#         conn.commit()
#         conn.close()

#         return {"answer": ans}

#     except Exception as e:
#         print(f"Ошибка в обработке /chat: {str(e)}")
#         return JSONResponse({"answer": f"Ошибка: {str(e)}"}, status_code=500)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=PORT)



# ----------------------------------------------------------------------
import os
import base64
import uuid
import sqlite3
import requests
import urllib3
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import json

# Отключаем предупреждения о самоподписанных сертификатах
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Загружаем переменные окружения
load_dotenv()
GIGACHAT_CLIENT_ID = os.getenv("GIGACHAT_CLIENT_ID")
GIGACHAT_CLIENT_SECRET = os.getenv("GIGACHAT_CLIENT_SECRET")
PORT = int(os.getenv("PORT", 8000))

# URL-адреса API
TOKEN_URL = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
CHAT_URL = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
EMBEDDINGS_URL = "https://gigachat.devices.sberbank.ru/api/v1/embeddings"

# Инициализация FastAPI
app = FastAPI()

# Разрешаем CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Статика
if os.path.exists("./frontend"):
    app.mount("/static", StaticFiles(directory="./frontend", html=True), name="static")
    print("Папка frontend смонтирована как /static")
else:
    print("Предупреждение: папка './frontend' не найдена, статика не будет смонтирована.")

# Глобальные переменные
token = None
vectorstore = None

def get_token():
    """Получает токен доступа для GigaChat"""
    global token
    credentials = f"{GIGACHAT_CLIENT_ID}:{GIGACHAT_CLIENT_SECRET}"
    b64_credentials = base64.b64encode(credentials.encode()).decode()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "Authorization": f"Basic {b64_credentials}",
        "RqUID": str(uuid.uuid4()),
        "User-Agent": "MyGigaChatApp/1.0"
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "GIGACHAT_API_PERS"
    }
    resp = requests.post(TOKEN_URL, headers=headers, data=data, verify=False, timeout=10)
    resp.raise_for_status()
    js = resp.json()
    token = js.get("access_token") or js.get("accessToken")
    print(f"Token received: {token[:10]}...")
    return token

def get_embeddings(texts, token):
    """Получает эмбеддинги для списка текстов"""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "model": "Embeddings",
        "input": texts
    }
    resp = requests.post(EMBEDDINGS_URL, headers=headers, json=payload, verify=False, timeout=10)
    resp.raise_for_status()
    js = resp.json()
    return [embedding["embedding"] for embedding in js["data"]]

# Подготовка данных и векторного хранилища при старте
try:
    token = get_token()
    docs = []
    if os.path.exists("context"):
        from langchain_community.document_loaders import PyMuPDFLoader, Docx2txtLoader, TextLoader
        for fname in os.listdir("context"):
            path = os.path.join("context", fname)
            if not os.path.isfile(path):
                continue
            ext = fname.lower().split('.')[-1]
            try:
                if ext == "pdf":
                    loader = PyMuPDFLoader(path)
                elif ext == "docx":
                    loader = Docx2txtLoader(path)
                elif ext == "txt":
                    loader = TextLoader(path)
                else:
                    continue
                loaded_docs = loader.load()
                docs.extend(loaded_docs)
            except Exception as e:
                print(f"Ошибка при загрузке файла {fname}: {e}")
    else:
        print("Предупреждение: папка 'context' не найдена.")

    if docs:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        split_docs = text_splitter.split_documents(docs)
        texts = [doc.page_content for doc in split_docs]
        embeddings = get_embeddings(texts, token)
        from langchain.schema import Document
        docs_with_embeddings = [Document(page_content=text, metadata={"embedding": emb}) for text, emb in zip(texts, embeddings)]
        vectorstore = FAISS.from_documents(docs_with_embeddings, HuggingFaceEmbeddings(model_name="ai-forever/sbert_large_nlu_ru"))
        print(f"Создано векторное хранилище с {len(docs_with_embeddings)} документами.")
    else:
        print("Нет документов для создания векторного хранилища.")
except Exception as e:
    print(f"Ошибка при инициализации векторного хранилища: {e}")
    raise

@app.get("/")
async def root():
    index_path = os.path.join("./frontend", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return JSONResponse({"error": "index.html не найден"}, status_code=404)

@app.get("/favicon.ico")
async def favicon():
    path = os.path.join("./frontend", "favicon.ico")
    if os.path.exists(path):
        return FileResponse(path)
    return {}

@app.post("/chat")
async def chat(request: Request):
    global token, vectorstore
    try:
        data = await request.json()
        user_msg = data.get("message", "").strip()
        if not user_msg:
            return JSONResponse({"answer": "Пожалуйста, введите сообщение."}, status_code=400)

        if vectorstore:
            # Преобразуем запрос в эмбеддинг
            query_embedding = get_embeddings([user_msg], token)[0]
            # Поиск похожих документов
            docs = vectorstore.similarity_search_by_vector(query_embedding, k=3)
            context = "\n".join([doc.page_content for doc in docs])
            # Обогащенный запрос
            enriched_prompt = f"Контекст: {context}\n\nВопрос: {user_msg}"
        else:
            enriched_prompt = user_msg

        # Запрос к GigaChat
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        payload = {
            "model": "GigaChat",
            "messages": [
                {"role": "system", "content": "Вы — помощник. Используйте предоставленный контекст для ответа."},
                {"role": "user", "content": enriched_prompt}
            ],
            "temperature": 0.7
        }
        resp = requests.post(CHAT_URL, headers=headers, json=payload, verify=False, timeout=10)
        resp.raise_for_status()
        js = resp.json()
        ans = js["choices"][0]["message"]["content"]

        # Сохраняем в БД
        conn = sqlite3.connect("history.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS history 
                       (id INTEGER PRIMARY KEY, user TEXT, bot TEXT, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
        cur.execute("INSERT INTO history (user, bot) VALUES (?, ?)", (user_msg, ans))
        conn.commit()
        conn.close()

        return {"answer": ans}

    except Exception as e:
        print(f"Ошибка в обработке /chat: {str(e)}")
        return JSONResponse({"answer": f"Ошибка: {str(e)}"}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)