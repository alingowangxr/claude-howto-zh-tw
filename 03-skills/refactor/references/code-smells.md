# Code Smells Catalog / 程式碼異味清單

這是一個用於識別程式碼異味的簡明參考表。

## 常見 Code Smells

### Long Method

**Signs**

- 方法超過 30-50 行
- 多層巢狀
- 需要靠註釋區分段落

**Refactorings**

- Extract Method
- Replace Temp with Query
- Introduce Parameter Object

### Large Class

**Signs**

- 欄位過多
- 方法過多
- 職責明顯混雜

**Refactorings**

- Extract Class
- Extract Subclass

### Primitive Obsession

**Signs**

- 用基礎型別表示複雜領域概念
- 到處都是 magic strings / numbers

**Refactorings**

- Replace Primitive with Object
- Replace Type Code with Class

### Long Parameter List

**Signs**

- 引數 4 個以上
- 引數經常成組出現

**Refactorings**

- Introduce Parameter Object
- Preserve Whole Object

### Data Clumps

**Signs**

- 相同一組欄位總是一起出現

**Refactorings**

- Extract Class
- Introduce Parameter Object
