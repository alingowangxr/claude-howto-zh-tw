---
name: blog-draft
description: 根據想法和資料起草部落格文章。Use when users want to draft a blog post, write an article from research, or turn notes/resources into a structured post.
---

# Blog Draft / 部落格草稿生成

## User Input

```text
$ARGUMENTS
```

使用者最好提供：

- 主題 / 想法
- 參考資料（URL、檔案、筆記）
- 目標讀者
- 語氣風格

如果使用者是在修改已有草稿，直接從“迭代草稿”階段開始。

## Execution Flow

### Step 1: 建立文章目錄

目錄格式：

```text
blog-posts/
└── YYYY-MM-DD-short-topic-name/
    └── resources/
```

### Step 2: 整理資料

對每個資料生成摘要檔案，至少包含：

- 關鍵觀點
- 可引用的資料或句子
- 與主題的關聯

### Step 3: 明確文章方向

整理並向使用者確認：

- 主要觀點
- 可選角度
- 核心論點
- 資訊缺口

### Step 4: 先產出大綱

生成 `OUTLINE.md`，包含：

- 目標讀者
- 語氣
- 目標篇幅
- 核心 takeaway
- 文章結構
- 計劃引用的資料

### Step 5: 寫草稿

按大綱生成 `draft-v0.1.md`，要求：

- 有吸引人的開頭
- 結構清晰
- 有證據和範例
- 重要事實帶引用
- 結尾有總結或行動建議

### Step 6: 迭代

如果使用者要求修改：

- 記錄回饋
- 遞增版本號
- 儲存為 `draft-v0.2.md`、`draft-v0.3.md`

## 輸出要求

- 先給結構，再寫全文
- 引用要清楚
- 表達可以中文化，但檔案和目錄命名保持可管理
