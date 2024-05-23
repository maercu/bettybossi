docker run --rm -v $(pwd):/$(basename `pwd`) -w "/$(basename `pwd`)" -it node:lts-alpine sh -c "yarn config set "strict-ssl" false && yarn create vuetify"
sudo chown -R maercu:maercu $1

tee $1/Dockerfile << EOF
# develop stage
FROM node:lts-alpine as develop-stage
WORKDIR /app
COPY package*.json ./
RUN yarn config set "strict-ssl" false && yarn install
COPY . .

# build stage
FROM develop-stage as build-stage
RUN yarn build

# production stage
FROM nginx:alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
EOF

tee $1/docker-compose.yml << EOF
# for local development
services:
  vuetifyfrontend:
    build:
      context: .
      target: develop-stage
    ports:
      - 8081:3000
    volumes:
    - .:/app
    command: /bin/sh -c "yarn dev --host"
EOF

