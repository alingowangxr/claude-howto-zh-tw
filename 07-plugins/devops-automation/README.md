<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# DevOps Automation 外掛

這是一個把部署、回滾、狀態檢查和 incident 響應打包到一起的 DevOps plugin。

## Features

- 自動部署
- 回滾流程
- 系統健康檢查
- incident 響應
- Kubernetes 整合

## Installation

```bash
/plugin install devops-automation
```

## What's Included

### Commands

- `/deploy`
- `/rollback`
- `/status`
- `/incident`

### Agents

- `deployment-specialist`
- `incident-commander`
- `alert-analyzer`

## Requirements

- `kubectl`
- 已設定叢集訪問
- 必要時設定 `KUBECONFIG`

## 最小設定

```bash
export KUBECONFIG=~/.kube/config
kubectl get pods
```

在真正使用 plugin 前，最好先確認 `kubectl` 本身可用、目標叢集可連。

## 一個最小使用流程

### 1. 安裝 plugin

```text
/plugin install devops-automation
```

### 2. 先從只讀狀態檢查開始

```text
/status
```

### 3. 再嘗試更高風險操作

```text
/deploy staging
```

或：

```text
/rollback production
```

## 使用建議

- 先用 `/status` 驗證環境
- 再用 staging 做演練
- 最後才考慮 production 級命令

## 常見坑

### 1. 本機 `kubectl` 沒配好

外掛本身沒問題，但底層依賴沒通，就會顯得“命令無效”。

### 2. 直接在 production 場景試第一把

這不是一個適合“第一次就直接上線試”的 plugin。

### 3. 沒寫清團隊流程

如果團隊內部的部署規範、回滾條件、incident 流程不明確，plugin 也很難替你兜底。
