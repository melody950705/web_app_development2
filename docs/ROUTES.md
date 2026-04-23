# 路由設計文件 - 個人記帳簿系統

本文件基於 PRD、架構設計與資料庫設計，規劃系統內的所有 URL 路由、對應的 HTTP 方法以及所需要的 Jinja2 模板。

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| ---- | --------- | -------- | -------- | ---- |
| 首頁與明細列表 | GET | `/` | `templates/index.html` | 顯示目前總餘額與近期的收支紀錄 |
| 新增收支頁面 | GET | `/records/new` | `templates/records/form.html` | 顯示新增收支紀錄的表單 |
| 建立收支 | POST | `/records` | — | 接收表單存入 DB，完成後重導向至首頁 |
| 編輯收支頁面 | GET | `/records/<id>/edit` | `templates/records/form.html` | 顯示編輯表單（帶入原資料） |
| 更新收支 | POST | `/records/<id>/update` | — | 接收表單更新 DB，完成後重導向至首頁 |
| 刪除收支 | POST | `/records/<id>/delete` | — | 刪除後重導向至首頁 |
| 金錢流向統計頁 | GET | `/statistics` | `templates/statistics.html` | 顯示特定期間的收支統計數據 |
| 分類管理頁面 | GET | `/categories` | `templates/categories/index.html`| 顯示目前的分類列表 |
| 新增分類 | POST | `/categories` | — | 接收表單存入 DB，重導向至分類管理頁 |

## 2. 每個路由的詳細說明

### 首頁 (`GET /`)
- **輸入**：無
- **處理邏輯**：呼叫 `Record.get_balance_summary()` 與 `Record.get_all()`
- **輸出**：渲染 `index.html`
- **錯誤處理**：無特定錯誤

### 新增收支頁面 (`GET /records/new`)
- **輸入**：無
- **處理邏輯**：呼叫 `Category.get_all()` 提供分類選項
- **輸出**：渲染 `records/form.html`

### 建立收支 (`POST /records`)
- **輸入**：表單欄位 `date`, `amount`, `type`, `category_id`, `description`
- **處理邏輯**：驗證欄位是否為空，若通過則呼叫 `Record.create(...)`
- **輸出**：成功後重導向至 `/`；失敗則攜帶錯誤訊息重新渲染 `records/form.html`

### 編輯/更新/刪除收支
- 邏輯類似建立，需要額外取得 `id` 並呼叫 `Record.update()` 或 `Record.delete()`。
- 刪除與更新使用 POST 是因為採用純 HTML 表單。

### 金錢流向統計頁 (`GET /statistics`)
- **處理邏輯**：取得資料，可依賴 `Record.get_balance_summary()`
- **輸出**：渲染 `statistics.html`

### 分類管理頁面 (`GET /categories` & `POST /categories`)
- **GET**：呼叫 `Category.get_all()` 渲染 `categories/index.html`
- **POST**：接收 `name`, `type` 並呼叫 `Category.create()`，然後重導向至 `/categories`

## 3. Jinja2 模板清單

所有的模板都將繼承自 `base.html`，統一導覽列與外觀。

- `templates/base.html`：包含 `<head>`、導覽列 (Navbar) 與頁尾 (Footer)。
- `templates/index.html`：首頁儀表板與明細列表。
- `templates/records/form.html`：新增與編輯紀錄共用的表單頁面。
- `templates/statistics.html`：統計報表頁面。
- `templates/categories/index.html`：分類列表與新增分類的表單頁面。
