# from fastapi import FastAPI, Form, File, UploadFile, Depends
# import os
# from email.message import EmailMessage
# from aiosmtplib import send
# from dotenv import load_dotenv
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
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import FAISS
# from langchain_huggingface import HuggingFaceEmbeddings
# import json

# load_dotenv()
# SMTP_HOST = os.getenv("SMTP_HOST")
# SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
# SMTP_USER = os.getenv("SMTP_USER")
# SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
# SMTP_RECEIVER = os.getenv("SMTP_RECEIVER")
# GIGACHAT_CLIENT_ID = os.getenv("GIGACHAT_CLIENT_ID")
# GIGACHAT_CLIENT_SECRET = os.getenv("GIGACHAT_CLIENT_SECRET")
# PORT = int(os.getenv("PORT", 8000))

# # Проверка SMTP-переменных
# if not all([SMTP_HOST, SMTP_USER, SMTP_PASSWORD, SMTP_RECEIVER]):
#     missing_vars = [var for var, value in [
#         ("SMTP_HOST", SMTP_HOST),
#         ("SMTP_USER", SMTP_USER),
#         ("SMTP_PASSWORD", SMTP_PASSWORD),
#         ("SMTP_RECEIVER", SMTP_RECEIVER)
#     ] if not value]
#     raise ValueError(f"Следующие SMTP-переменные не определены в .env: {missing_vars}")

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
# EMBEDDINGS_URL = "https://gigachat.devices.sberbank.ru/api/v1/embeddings"

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
# if os.path.exists("./frontend/dist"):
#     app.mount("/static", StaticFiles(directory="./frontend/dist", html=True), name="static")
#     print("Папка frontend/dist смонтирована как /static")
# else:
#     print("Предупреждение: папка './frontend/dist' не найдена, статика не будет смонтирована.")

# # Глобальные переменные
# token = None
# vectorstore = None

# def get_token():
#     """Получает токен доступа для GigaChat"""
#     global token
#     credentials = f"{GIGACHAT_CLIENT_ID}:{GIGACHAT_CLIENT_SECRET}"
#     b64_credentials = base64.b64encode(credentials.encode()).decode()
#     headers = {
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Accept": "application/json",
#         "Authorization": f"Basic {b64_credentials}",
#         "RqUID": str(uuid.uuid4()),
#         "User-Agent": "MyGigaChatApp/1.0"
#     }
#     data = {
#         "grant_type": "client_credentials",
#         "scope": "GIGACHAT_API_PERS"
#     }
#     resp = requests.post(TOKEN_URL, headers=headers, data=data, verify=False, timeout=10)
#     resp.raise_for_status()
#     js = resp.json()
#     token = js.get("access_token") or js.get("accessToken")
#     print(f"Token received: {token[:10]}...")
#     return token

# def get_embeddings(texts, token):
#     """Получает эмбеддинги для списка текстов"""
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Content-Type": "application/json",
#         "Accept": "application/json"
#     }
#     payload = {
#         "model": "Embeddings",
#         "input": texts
#     }
#     resp = requests.post(EMBEDDINGS_URL, headers=headers, json=payload, verify=False, timeout=10)
#     resp.raise_for_status()
#     js = resp.json()
#     return [embedding["embedding"] for embedding in js["data"]]

# # Подготовка данных и векторного хранилища при старте
# try:
#     token = get_token()
#     docs = []
#     if os.path.exists("context"):
#         from langchain_community.document_loaders import PyMuPDFLoader, Docx2txtLoader, TextLoader
#         for fname in os.listdir("context"):
#             path = os.path.join("context", fname)
#             if not os.path.isfile(path):
#                 continue
#             ext = fname.lower().split('.')[-1]
#             try:
#                 if ext == "pdf":
#                     loader = PyMuPDFLoader(path)
#                 elif ext == "docx":
#                     loader = Docx2txtLoader(path)
#                 elif ext == "txt":
#                     loader = TextLoader(path)
#                 else:
#                     continue
#                 loaded_docs = loader.load()
#                 docs.extend(loaded_docs)
#             except Exception as e:
#                 print(f"Ошибка при загрузке файла {fname}: {e}")
#     else:
#         print("Предупреждение: папка 'context' не найдена.")

#     if docs:
#         text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#         split_docs = text_splitter.split_documents(docs)
#         texts = [doc.page_content for doc in split_docs]
#         embeddings = get_embeddings(texts, token)
#         from langchain.schema import Document
#         docs_with_embeddings = [Document(page_content=text, metadata={"embedding": emb}) for text, emb in zip(texts, embeddings)]
#         vectorstore = FAISS.from_documents(docs_with_embeddings, HuggingFaceEmbeddings(model_name="ai-forever/sbert_large_nlu_ru"))
#         print(f"Создано векторное хранилище с {len(docs_with_embeddings)} документами.")
#     else:
#         print("Нет документов для создания векторного хранилища.")
# except Exception as e:
#     print(f"Ошибка при инициализации векторного хранилища: {e}")
#     raise

# @app.get("/")
# async def root():
#     index_path = os.path.join("./frontend/dist", "index.html")
#     if os.path.exists(index_path):
#         return FileResponse(index_path)
#     return JSONResponse({"error": "index.html не найден"}, status_code=404)

# @app.get("/favicon.ico")
# async def favicon():
#     path = os.path.join("./frontend/dist", "favicon.ico")
#     if os.path.exists(path):
#         return FileResponse(path)
#     return {}

# @app.post("/chat")

# async def chat(request: Request):
#     global token, vectorstore
#     try:
#         data = await request.json()
#         user_msg = data.get("message", "").strip()
#         if not user_msg:
#             return JSONResponse({"answer": "Пожалуйста, введите сообщение."}, status_code=400)

#         if vectorstore:
#             # Преобразуем запрос в эмбеддинг
#             query_embedding = get_embeddings([user_msg], token)[0]
#             # Поиск похожих документов
#             docs = vectorstore.similarity_search_by_vector(query_embedding, k=3)
#             context = "\n".join([doc.page_content for doc in docs])
#             # Обогащенный запрос
#             enriched_prompt = f"Контекст: {context}\n\nВопрос: {user_msg}"
#         else:
#             enriched_prompt = user_msg

#         # Запрос к GigaChat
#         headers = {
#             "Authorization": f"Bearer {token}",
#             "Content-Type": "application/json",
#             "Accept": "application/json"
#         }
#         payload = {
#             "model": "GigaChat",
#             "messages": [
#                 {"role": "system", "content": "Вы — помощник. Используйте предоставленный контекст для ответа."},
#                 {"role": "user", "content": enriched_prompt}
#             ],
#             "temperature": 0.7
#         }
#         resp = requests.post(CHAT_URL, headers=headers, json=payload, verify=False, timeout=10)
#         resp.raise_for_status()
#         js = resp.json()
#         ans = js["choices"][0]["message"]["content"]

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

# @app.post("/api/send-form")
# async def send_form(
#     name: str = Form(...),
#     phone: str = Form(...),
#     email: str = Form(None)
# ):
#     try:
#         msg = EmailMessage()
#         msg["Subject"] = "Новая заявка с сайта"
#         msg["From"] = SMTP_USER
#         msg["To"] = SMTP_RECEIVER

#         msg.set_content(f"""
#         📝 Новая заявка:

#         Имя: {name}
#         Телефон: {phone}
#         Email: {email or "не указан"}
#         """)

#         # Исправленный вызов send
#         await send(
#             msg,  # Позиционный аргумент
#             hostname=SMTP_HOST,
#             port=SMTP_PORT,
#             username=SMTP_USER,
#             password=SMTP_PASSWORD,
#             use_tls=True,
#         )

#         return {"success": True}
#     except Exception as e:
#         print(f"Ошибка при отправке письма: {e}")
#         return JSONResponse(
#             status_code=500,
#             content={"success": False, "error": "Ошибка отправки письма"},
#         )

# @app.get("/api/send-form")
# async def send_form_get():
#     return JSONResponse(
#         status_code=405,
#         content={"error": "Метод GET не поддерживается для /api/send-form. Используйте POST."}
#     )

import os
import base64
import uuid
import sqlite3
import requests
import urllib3
import json
from email.message import EmailMessage
from aiosmtplib import send
from fastapi import FastAPI, Form, File, UploadFile, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from functools import wraps

# Загружаем переменные окружения
load_dotenv()
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_RECEIVER = os.getenv("SMTP_RECEIVER")
GIGACHAT_CLIENT_ID = os.getenv("GIGACHAT_CLIENT_ID")
GIGACHAT_CLIENT_SECRET = os.getenv("GIGACHAT_CLIENT_SECRET")
# PORT = int(os.getenv("PORT", 8000))

# Проверка SMTP-переменных
if not all([SMTP_HOST, SMTP_USER, SMTP_PASSWORD, SMTP_RECEIVER]):
    missing_vars = [var for var, value in [
        ("SMTP_HOST", SMTP_HOST),
        ("SMTP_USER", SMTP_USER),
        ("SMTP_PASSWORD", SMTP_PASSWORD),
        ("SMTP_RECEIVER", SMTP_RECEIVER)
    ] if not value]
    raise ValueError(f"Следующие SMTP-переменные не определены в .env: {missing_vars}")

# Отключаем предупреждения о самоподписанных сертификатах
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
if os.path.exists("./frontend/dist"):
    app.mount("/static", StaticFiles(directory="./frontend/dist", html=True), name="static")
    print("Папка frontend/dist смонтирована как /static")
else:
    print("Предупреждение: папка './frontend/dist' не найдена, статика не будет смонтирована.")

# Глобальные переменные
token = None
vectorstore = None

def handle_token_refresh(max_retries=2):
    """Декоратор для обработки истечения токена и повторных попыток"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 401:
                        print("Токен истек, обновляем...")
                        get_token()  # Обновляем глобальный токен
                        retries += 1
                        continue
                    raise
            raise ValueError(f"Не удалось выполнить запрос после {max_retries} попыток")
        return wrapper
    return decorator

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

@handle_token_refresh()
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
    index_path = os.path.join("./frontend/dist", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return JSONResponse({"error": "index.html не найден"}, status_code=404)

@app.get("/favicon.ico")
async def favicon():
    path = os.path.join("./frontend/dist", "favicon.ico")
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
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        payload = {
            "model": "GigaChat",
            "messages": [
                {"role": "system", "content": "Вы — ИИ-помощник компании ООО СК ДИОНИС, размещённый на сайте компании и предназначенный для взаимодействия с клиентами. Ваша главная задача — вежливо и профессионально консультировать клиентов по вопросам, связанным с приёмкой квартир, используя предоставленный контекст о компании, её услугах и процессах. Общайтесь исключительно на русском языке, поддерживая доброжелательный тон, который отражает ценности компании и стремление к высокому уровню сервиса. При ответе на запросы клиентов опирайтесь на предоставленный контекст из RAG-системы, чтобы обеспечить точные и актуальные ответы. Если в контексте есть конкретные данные, например, о длительности проверки квартиры или стоимости услуг, используйте их для формирования ответа. Убедитесь, что ваши ответы чёткие, релевантны и не отклоняются от темы приёмки квартир. Не раскрывайте конфиденциальную информацию и не делайте обещания, которые не подтверждены контекстом. Если в контексте нет информации для ответа на запрос, сохраняйте позитивный тон и предложите клиенту альтернативу. Например, попросите переформулировать вопрос для большей ясности, дайте общие рекомендации по приёмке квартир (например, обратить внимание на окна, сантехнику или электрику) или предложите связаться с поддержкой компании, указав контактные данные, если они доступны. Ваша цель — убедиться, что клиент чувствует поддержку и остаётся удовлетворённым, даже если прямой ответ невозможен. Примеры ответов: на вопрос о длительности проверки квартиры вы можете ответить: Обычно проверка квартиры занимает от 2 до 4 часов, в зависимости от размера и состояния. Если нет данных о стоимости, скажите: Стоимость услуг зависит от ряда факторов, таких как размер квартиры. Для точной цены свяжитесь с нашей поддержкой. На вопрос о зонах обслуживания: Мы работаем в Москве и прилегающих районах. Для других регионов уточните возможности у нашей команды. Эти примеры помогут вам адаптироваться к различным ситуациям, сохраняя профессионализм и заботу о клиенте."},
                {"role": "user", "content": enriched_prompt}
            ],
            "temperature": 0.7
        }
        # Обработка истечения токена
        retries = 0
        max_retries = 2
        while retries < max_retries:
            try:
                resp = requests.post(CHAT_URL, headers=headers, json=payload, verify=False, timeout=10)
                resp.raise_for_status()
                break
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 401:
                    print("Токен истек, обновляем...")
                    get_token()  # Обновляем глобальный токен
                    headers["Authorization"] = f"Bearer {token}"
                    retries += 1
                    continue
                raise
        else:
            raise ValueError(f"Не удалось выполнить запрос после {max_retries} попыток")

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

@app.post("/api/send-form")
async def send_form(
    name: str = Form(...),
    phone: str = Form(...),
    email: str = Form(None)
):
    try:
        msg = EmailMessage()
        msg["Subject"] = "Новая заявка с сайта"
        msg["From"] = SMTP_USER
        msg["To"] = SMTP_RECEIVER

        msg.set_content(f"""
        📝 Новая заявка:

        Имя: {name}
        Телефон: {phone}
        Email: {email or "не указан"}
        """)

        await send(
            msg,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            username=SMTP_USER,
            password=SMTP_PASSWORD,
            use_tls=True,
        )

        return {"success": True}
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")
        return JSONResponse(
            status_code=500,
            content={"success": False, "error": "Ошибка отправки письма"},
        )

@app.get("/api/send-form")
async def send_form_get():
    return JSONResponse(
        status_code=405,
        content={"error": "Метод GET не поддерживается для /api/send-form. Используйте POST."}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)