# Использованные команды
```bash
cd back
docker-compose --file docker-compose.dev.services.yml up -d
NODE_ENV=development npx sequelize-cli db:migrate
npm run dev

cd ..

cd back-ws-vcs/
vim .env
git checkout develop
npm i
npm run dev

cd ..

cd back-web-socket/
npm i
npm run dev

cd ..
cd front
vim .env
npm install -g pnpm@8.14.1
pnpm install
pnpm dev
```

В `back-ws-vcs` и `back-web-socket` пришлось поменять названия таблиц с метриками графаны с `metrics` на `grafana-metrics` - кто-то накосячил, и из-за этого не запускалось приложение

`vim src/databases/schemas/metrics.schema.ts`