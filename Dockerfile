FROM python:3.8-slim
WORKDIR /home/app
RUN pip install requests bs4
COPY . .
CMD ["bash"]