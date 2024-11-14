# 使用官方 Python 运行时作为父镜像
FROM python:3.10-slim
# 设置工作目录
WORKDIR /app
# 复制项目文件到工作目录
COPY . /app
# 安装项目依赖
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
# 设置环境变量
ENV PYTHONUNBUFFERED=1
# 暴露应用端口, 这是默认的gradio的端口
EXPOSE 7860
# 运行应用
CMD ["python", "src/main.py"]