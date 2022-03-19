FROM node:12-slim
WORKDIR /app
COPY . /app
RUN npm install && pwd && ls -la && chmod +x node_modules/.bin/*
CMD npm run dev
