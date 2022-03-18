FROM cypress/base:14
WORKDIR /app

ENV CI=1
RUN npm ci
RUN npx cypress verify