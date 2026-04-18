FROM python:3.11-slim
RUN pip install streamlit pandas matplotlib requests   
WORKDIR /app
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
