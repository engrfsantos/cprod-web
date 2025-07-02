# Base da imagem Docker a ser utilizada
FROM python:3.11-slim


WORKDIR /web

VOLUME /web

#COPY ./app app
#COPY ./cprod cprod
COPY ./ /web

# copiar o arquivo de instalação dos requisitos do ambiente
#COPY ./requirements.txt ./requirements.txt
#COPY ./Dockerfile ./Dockerfile

EXPOSE 80

# Define o ambiente como não interativo para evitar prompts
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza os pacotes e habilita o repositório da comunidade do Alpine
#RUN apk update && apk add --no-cache \
#    nodejs npm \
#    && npm install -g corepack \
#    && corepack enable

# Verifica as versões instaladas
#RUN python --version && node --version && npm --version && pnpm --version || true



# Instala dependências essenciais
RUN apt-get update && apt-get install -y \
    curl \
    bash \
    git \
    build-essential \
    && curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash \
    && echo "source $HOME/.nvm/nvm.sh" >> ~/.bashrc \
    && /bin/bash -c "source $HOME/.nvm/nvm.sh && nvm install 18" \
    && /bin/bash -c "source $HOME/.nvm/nvm.sh && nvm use 18" \
    && /bin/bash -c "source $HOME/.nvm/nvm.sh && nvm alias default 18" \
    && /bin/bash -c "source $HOME/.nvm/nvm.sh && npm install -g corepack && corepack enable" \
    && rm -rf /var/lib/apt/lists/*

# Verifica as versões instaladas
RUN python --version && node --version && npm --version && pnpm --version || true


RUN apt update && apt install zsh nodejs -y

RUN chsh -s $(which zsh)

# Atualiza o pip e o setuptools para as versões mais recentes e instala o Cython
RUN pip3 install --upgrade pip

# Instala as dependências do Python listadas no requirements.txt
RUN pip install -r ./requirements.txt

# Define o comando padrão a ser executado quando o container iniciar

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# Adicionar o interpretador de comandos bash
# RUN apk update && apk add bash

RUN export PYTHONPATH=/web

# Comando para o container não parar após a leitura de todas as camadas
# ENTRYPOINT ["tail", "-f", "/dev/null"]