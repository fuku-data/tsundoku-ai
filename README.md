# tsundoku-ai
AIによるPDFからのテキスト抽出と質問応答システム

```bash
export OPENAI_API_KEY=sk-ABC...
docker compose build
docker compose up -d
```

```txt
tsundoku-ai
├── Dockerfile
├── README.md
├── book
│   └── 本.pdf
├── compose.yml
├── requirements.txt
└── tsundoku-ai
    ├── src
    │   ├── 00_🏠_Home.py
    │   └── pages
    │       └── 01_🔧_Settings.py
    └── test
        └── テスト.py
```