<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Checkpoints 與 Rewind 指南

checkpoints 是 Claude Code 新手最值得儘早掌握的安全機制之一。  
它的意義很簡單：**敢試，因為隨時能回退。**

---

## checkpoint 是什麼

可以把 checkpoint 理解成當前會話狀態的快照，通常包括：

- 對話訊息
- 檔案改動
- 工具使用歷史
- 會話上下文

當你需要回退時，就使用 `rewind` 返回到某個 checkpoint。

---

## 為什麼它重要

很多人不敢放手讓 Claude 改程式碼，不是因為能力不夠，而是因為怕改壞。checkpoints 解決的就是這個心理門檻。

適合這些場景：

- 大膽試不同方案
- 複雜重構
- 出現錯誤後回滾
- 比較兩個實現方向

---

## 怎麼開啟

### 鍵盤方式

按 `Esc` 兩次。

### 命令方式

```text
/rewind
```

`/checkpoint` 也可以作為別名使用。

---

## rewind 時你會看到什麼選項

常見有這些：

1. **Restore code and conversation**：程式碼和對話都回退
2. **Restore conversation**：只回退對話
3. **Restore code**：只回退程式碼
4. **Summarize from here**：從這一點開始壓縮總結
5. **Never mind**：取消

---

## checkpoints 預設就有

Claude Code 會自動建立 checkpoints，所以你不需要手動先“存檔”才能用。

這意味著你可以把它當作日常工作流的一部分，而不是緊急救火功能。

---

## 一個很實用的工作流

```text
先讓 Claude 改
→ 如果結果好，繼續
→ 如果不滿意，/rewind
→ 換一種實現路線
```

這在這些任務裡尤其好用：

- UI 重構
- API 重構
- auth / permission 變更
- 大批次檔案整理

---

## 新手最容易忽略的點

### 1. checkpoint 不只是“撤銷”

它不只是救錯，還可以幫助你探索多種實現方案。

### 2. rewind 不一定要連程式碼一起退

有時你只是想保留程式碼，但回退對話；或者相反。這個選擇很有用。

### 3. summarize from here 很適合長會話

當上下文太長時，你可以用 summary 代替完整歷史，減少上下文負擔。

---

## 常見使用場景

| 場景 | 建議做法 |
|------|----------|
| 試兩種不同實現 | 做一次改動後 `/rewind` 回去重試 |
| 大型重構 | 每走一段就確認 checkpoint |
| Claude 改壞了 | 回到上一個穩定狀態 |
| 會話太長 | 用 summary 壓縮後繼續 |

---

## 新手使用者特別注意

如果你在在地化或改寫範例檔案時做大範圍文字替換，checkpoints 也非常有用。  
因為這類修改很容易“看起來都對，實際把命令名或欄位名翻壞”，有 checkpoint 會安全很多。

---

## 推薦下一步

- 想學命令列和 print mode：看 [10-cli](../10-cli/)
- 想學更復雜的規劃與許可權控制：看 [09-advanced-features](../09-advanced-features/)
