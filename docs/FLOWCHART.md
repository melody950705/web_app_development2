# 流程圖文件 - 個人記帳簿系統

本文件基於 PRD 需求與架構設計，視覺化使用者的操作路徑與系統內的資料流向，確保各項功能與互動皆能正確銜接。

## 1. 使用者流程圖（User Flow）

此流程圖描述使用者進入網站後，可以進行的各項主要操作路徑。

```mermaid
flowchart LR
    A([使用者開啟系統]) --> B[首頁 - 儀表板與明細]
    B --> C{要執行什麼操作？}
    
    C -->|查看| D[檢視目前總餘額與近期收支明細]
    C -->|新增紀錄| E[點擊「新增收支」按鈕]
    C -->|查看統計| F[點擊「金錢流向統計」]
    C -->|分類管理| G[點擊「管理收支分類」]
    
    E --> H[填寫表單: 日期, 金額, 類型, 項目]
    H --> I{資料驗證}
    I -->|失敗| H
    I -->|成功| J[儲存資料]
    J --> B
    
    F --> K[檢視特定期間收支與圖表]
    K -->|返回| B
    
    G --> L[新增或修改自訂分類]
    L -->|返回| B
```

## 2. 系統序列圖（Sequence Diagram）

此序列圖以「新增一筆收支紀錄」為例，展示從使用者點擊送出到資料庫寫入的完整資料流向。

```mermaid
sequenceDiagram
    actor User as 使用者
    participant Browser as 瀏覽器 (HTML)
    participant Flask as Flask 路由 (Controller)
    participant Model as 模型 (Model)
    participant DB as SQLite (database.db)
    
    User->>Browser: 在表單填寫日期、金額與項目並送出
    Browser->>Flask: POST /records (包含表單資料)
    Flask->>Flask: 驗證必填欄位
    alt 驗證失敗
        Flask-->>Browser: 重新渲染表單頁並顯示錯誤訊息
        Browser-->>User: 看到錯誤提示並重新填寫
    else 驗證成功
        Flask->>Model: 呼叫新增紀錄的方法
        Model->>DB: INSERT INTO records (...)
        DB-->>Model: 寫入成功
        Model-->>Flask: 成功狀態
        Flask-->>Browser: 302 Redirect 重導向至首頁
        Browser->>Flask: GET / (請求首頁)
        Flask->>Model: 取得最新餘額與明細列表
        Model->>DB: SELECT 查詢
        DB-->>Model: 回傳資料
        Model-->>Flask: 回傳計算後的總餘額與近期紀錄
        Flask-->>Browser: 渲染 index.html
        Browser-->>User: 看到最新餘額與剛新增的記帳明細
    end
```

## 3. 功能清單對照表

以下為主要功能對應的預期 URL 路徑與 HTTP 方法。

| 功能名稱 | URL 路徑 | HTTP 方法 | 說明 |
| -------- | -------- | --------- | ---- |
| 首頁與明細列表 | `/` | GET | 顯示目前總餘額與近期的收支紀錄 |
| 顯示新增表單 | `/records/new` | GET | 顯示新增收支紀錄的 HTML 表單 |
| 送出新增紀錄 | `/records` | POST | 接收表單資料並寫入資料庫，完成後導向首頁 |
| 金錢流向統計頁 | `/statistics` | GET | 顯示特定期間的收支統計總和 |
| 分類管理頁面 | `/categories` | GET | 顯示目前的支出與收入分類列表 |
| 新增收支分類 | `/categories` | POST | 接收分類名稱並寫入資料庫 |
