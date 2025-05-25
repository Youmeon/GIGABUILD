Настройка окружения: 
~/miniconda3/bin/conda init - инициализация conda3
conda --version проверяем версию conda
conda env list - список доступных окружений
conda create -n gigachat-bot python=3.10 -y - создание окружения. 
conda activate gigachat-bot - активируем окружение.
deactivate - выходим из окружения.
conda install -c conda-forge -y     numpy     faiss-cpu     python-dotenv     uvicorn     python-multipart 
pip install --upgrade pip
pip list | grep -E "numpy|faiss"
conda install -c conda-forge faiss-cpu=1.7.4 -y
pip install numpy==1.24.3 faiss-cpu==1.7.4 fastapi uvicorn gigachat llama-index-embeddings-gigachat python-dotenv requests tenacity
uvicorn main:app --reload