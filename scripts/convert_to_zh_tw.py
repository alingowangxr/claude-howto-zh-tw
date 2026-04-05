#!/usr/bin/env python3
"""Convert Simplified Chinese Markdown files to Traditional Chinese (Taiwan).

This script:
1. Protects code blocks (while allowing comments to be translated)
2. Protects technical identifiers (paths, env vars, etc.)
3. Applies Taiwan-specific terminology mapping (Simplified -> Simplified/Traditional)
4. Converts Simplified to Traditional Chinese using OpenCC (s2twp)
5. Restores protected content
6. Fixes common artifacts (e.g., "演演算法", "一箇")
"""

import argparse
import os
import re
import sys
from pathlib import Path

import opencc

# Root of the repository
ROOT = Path(__file__).resolve().parent.parent

# Files to skip entirely
SKIP_FILES = {
    "LICENSE",
}

# Directories to skip
SKIP_DIRS = {
    ".venv",
    "__pycache__",
    ".git",
    "node_modules",
}

# Taiwan-specific terminology mapping (Simplified -> Taiwan Traditional equivalent)
# These will be applied BEFORE OpenCC conversion for maximum accuracy
TW_TERMS = {
    # Tech / Computing
    "网络": "網路",
    "互联网": "網際網路",
    "网站": "網站",
    "网页": "網頁",
    "链接": "連結",
    "云端": "雲端",
    "云计算": "雲端運算",
    "大数据": "大數據",
    "人工智能": "人工智慧",
    "机器学习": "機器學習",
    "深度学习": "深度學習",
    "神经网络": "神經網路",
    "算法": "演算法",
    "数据结构": "資料結構",
    "数据库": "資料庫",
    "文件系统": "檔案系統",
    "文件": "檔案",
    "文件夹": "資料夾",
    "目录": "目錄",
    "配置": "設定",
    "配置文件": "設定檔",
    "设置": "設定",
    "选项": "選項",
    "参数": "引數",
    "命令行": "命令列",
    "终端": "終端機",
    "控制台": "主控台",
    "界面": "介面",
    "用户界面": "使用者介面",
    "图形界面": "圖形介面",
    "用户": "使用者",
    "用户名": "使用者名稱",
    "账号": "帳號",
    "账户": "帳號",
    "登录": "登入",
    "登出": "登出",
    "注销": "登出",
    "注册": "註冊",
    "权限": "權限",
    "管理员": "管理員",
    "版本控制": "版本控制",
    "版本": "版本",
    "分支": "分支",
    "合并": "合併",
    "提交": "提交",
    "拉取": "拉取",
    "推送": "推送",
    "克隆": "複製",
    "仓库": "儲存庫",
    "源代码": "原始碼",
    "代码": "程式碼",
    "脚本": "腳本",
    "指令码": "腳本",
    "指令碼": "腳本",
    "程序": "程式",
    "应用程序": "應用程式",
    "软件": "軟體",
    "硬件": "硬體",
    "操作系统": "作業系統",
    "进程": "處理程序",
    "线程": "執行緒",
    "内存": "記憶體",
    "缓存": "快取",
    "磁盘": "磁碟",
    "硬盘": "硬碟",
    "固态硬盘": "固態硬碟",
    "接口": "介面",
    "插件": "外掛程式",
    "扩展": "擴充功能",
    "模块": "模組",
    "组件": "元件",
    "服务器": "伺服器",
    "客户端": "用戶端",
    "代理程序": "代理程式",
    "代理服务器": "代理伺服器",
    "网关": "閘道器",
    "防火墙": "防火牆",
    "令牌": "權杖",
    "密钥": "金鑰",
    "密码": "密碼",
    "哈希": "雜湊",
    "签名": "簽章",
    "验证": "驗證",
    "认证": "認證",
    "授权": "授權",
    "日志": "記錄檔",
    "监控": "監控",
    "告警": "警示",
    "邮件": "電子郵件",
    "邮箱": "信箱",
    "信息": "訊息",
    "消息": "訊息",
    "调试": "偵錯",
    "测试": "測試",
    "单元测试": "單元測試",
    "集成测试": "整合測試",
    "自动化测试": "自動化測試",
    "覆盖率": "涵蓋率",
    "文档": "文件",
    "注释": "註解",
    "教程": "教學",
    "范本": "範本",
    "模板": "範本",
    "示例": "範例",
    "最佳实践": "最佳實務",
    "实践": "實務",
    "常見問題": "常見問題",
    "故障排查": "疑難排解",
    "排错": "除錯",
    "解決方案": "解決方案",
    "依赖": "相依",
    "安装": "安裝",
    "卸载": "解除安裝",
    "更新": "更新",
    "升级": "升級",
    "下載": "下載",
    "上傳": "上傳",
    "同步": "同步",
    "备份": "備份",
    "恢復": "復原",
    "還原": "還原",
    "部署": "部署",
    "發布": "發布",
    "建置": "建置",
    "编译": "編譯",
    "运行": "執行",
    "启动": "啟動",
    "重启": "重新啟動",
    "初始化": "初始化",
    "載入": "載入",
    "匯入": "匯入",
    "匯出": "匯出",
    "輸出": "輸出",
    "輸入": "輸入",
    "列印": "列印",
    "顯示": "顯示",
    "隱藏": "隱藏",
    "開啟": "開啟",
    "關閉": "關閉",
    "儲存": "儲存",
    "預設": "預設",
    "自訂": "自訂",
    "進階": "進階",
    "優化": "最佳化",
    "效能": "效能",
    "性能": "效能",
    "在地化": "在地化",
    "解析度": "解析度",
    "品質": "品質",
    "質量": "品質",
    "搜尋": "搜尋",
    "取代": "取代",
    "選單": "選單",
    "快速鍵": "快速鍵",
    "副檔名": "副檔名",
    "檔名": "檔名",
    # Phrases
    "通过": "透過",
    "反饋": "回饋",
    "反馈": "回饋",
    "流水线": "管線",
    "中介層": "中介層",
    "中間件": "中介軟體",
    "部落格": "部落格",
    "博客": "部落格",
    "專案": "專案",
    "項目": "專案",
    "計畫": "計畫",
    "技術棧": "技術堆疊",
    "技術堆疊": "技術堆疊",
    "強健性": "強健性",
    "魯棒性": "強健性",
    "全局性": "全域",
    "全域性": "全域",
    "全局": "全域",
    "箇": "個",
}


def protect_code_blocks(text: str) -> tuple[str, list[str]]:
    """Extract code blocks and replace with placeholders to protect them,
    but keep comments for translation.
    """
    placeholders = []
    line_placeholders = []
    counter = [0]
    line_counter = [0]

    def replace_code(match: re.Match) -> str:
        code_content = match.group(0)
        
        # If it's a code block (fenced or indented), we want to translate comments
        if code_content.startswith("```") or code_content.startswith("    ") or code_content.startswith("\t"):
            lines = code_content.splitlines()
            new_lines = []
            for line in lines:
                stripped = line.lstrip()
                # Protect code but keep comments and blank lines for translation
                if stripped.startswith("#") or stripped.startswith("//") or stripped.startswith("<!--") or not stripped or stripped.startswith("```"):
                    new_lines.append(line)
                else:
                    line_placeholders.append(line)
                    new_lines.append(f"__CODE_LINE_{line_counter[0]}__")
                    line_counter[0] += 1
            return "\n".join(new_lines)
        else:
            # Inline code or small tags, protect entirely
            placeholders.append(code_content)
            placeholder = f"__CODE_BLOCK_{counter[0]}__"
            counter[0] += 1
            return placeholder

    # Match fenced code blocks
    text = re.sub(r"```[\s\S]*?```", replace_code, text)
    # Match indented code blocks
    text = re.sub(r"(?:^|\n)(?: {4}|\t)[^\n]+(?:\n(?: {4}|\t)[^\n]+)*", replace_code, text)
    # Match inline code
    text = re.sub(r"`[^`\n]+`", replace_code, text)
    # Match HTML tags
    text = re.sub(r"<[^>]+>", replace_code, text)

    return text, (placeholders, line_placeholders)


def restore_code_blocks(text: str, placeholders_tuple: tuple[list[str], list[str]]) -> str:
    """Restore code blocks from placeholders."""
    placeholders, line_placeholders = placeholders_tuple
    
    # Restore lines first (specific to general)
    for i, content in enumerate(line_placeholders):
        text = text.replace(f"__CODE_LINE_{i}__", content)
        
    # Restore full blocks
    for i, content in enumerate(placeholders):
        text = text.replace(f"__CODE_BLOCK_{i}__", content)
        
    return text


def protect_inline_patterns(text: str) -> tuple[str, list[str]]:
    """Protect inline patterns that should not be translated."""
    placeholders = []
    counter = [0]

    def replace_pattern(match: re.Match) -> str:
        placeholders.append(match.group(0))
        placeholder = f"__INLINE_{counter[0]}__"
        counter[0] += 1
        return placeholder

    # Protect file paths (e.g., scripts/build_epub.py)
    text = re.sub(r"[\w\-]+/[\w\-/.]+", replace_pattern, text)
    # Protect environment variables
    text = re.sub(r"\$[\w]+", replace_pattern, text)
    # Protect command flags
    text = re.sub(r"--[\w\-]+", replace_pattern, text)
    # Protect version numbers
    text = re.sub(r"\d+\.\d+(?:\.\d+)?", replace_pattern, text)

    return text, placeholders


def restore_inline_patterns(text: str, placeholders: list[str]) -> str:
    """Restore inline patterns from placeholders."""
    for i, original in enumerate(placeholders):
        text = text.replace(f"__INLINE_{i}__", original)
    return text


def apply_tw_terms(text: str) -> str:
    """Apply Taiwan-specific terminology replacements."""
    # Sort by length (longest first) to avoid partial replacements
    sorted_keys = sorted(TW_TERMS.keys(), key=len, reverse=True)
    for key in sorted_keys:
        text = text.replace(key, TW_TERMS[key])
    return text


def convert_text(text: str) -> str:
    """Convert Simplified Chinese to Traditional Chinese (Taiwan)."""
    # 1. Protect code blocks (keeping comments visible)
    text, code_placeholders = protect_code_blocks(text)

    # 2. Protect inline patterns
    text, inline_placeholders = protect_inline_patterns(text)

    # 3. Apply TW terminology BEFORE OpenCC (to match Simplified keys)
    text = apply_tw_terms(text)

    # 4. OpenCC conversion (s2twp)
    converter = opencc.OpenCC("s2twp")
    text = converter.convert(text)

    # 4.5 Apply TW terminology AFTER OpenCC (to match any Traditional keys missed/restored)
    text = apply_tw_terms(text)

    # 5. Restore
    text = restore_inline_patterns(text, inline_placeholders)
    text = restore_code_blocks(text, code_placeholders)
    
    # 6. Final cleanup for common artifacts
    # Use regex to fix repeated "演" in "演算法" (e.g., 演演算法, 演演演算法 -> 演算法)
    text = re.sub(r"演+算法", "演算法", text)
    text = text.replace("一箇", "一個")
    text = text.replace("佈署", "部署")
    text = text.replace("箇", "個")
    
    # Natural Taiwan phrasing improvements
    text = text.replace("這是一個", "這是一個") # Just to be safe
    
    return text


def process_file(file_path: Path, dry_run: bool = False) -> dict:
    """Process a single Markdown file."""
    result = {"file": str(file_path.relative_to(ROOT)), "changed": False, "error": None}
    try:
        content = file_path.read_text(encoding="utf-8")
        converted = convert_text(content)
        if converted != content:
            result["changed"] = True
            if not dry_run:
                file_path.write_text(converted, encoding="utf-8")
    except Exception as e:
        result["error"] = str(e)
    return result


def main():
    parser = argparse.ArgumentParser(description="Convert to Traditional Chinese (Taiwan)")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--file", type=str)
    args = parser.parse_args()

    if args.file:
        file_path = Path(args.file).resolve()
        result = process_file(file_path, args.dry_run)
        print(f"{result['file']}: {'CHANGED' if result['changed'] else 'unchanged'}")
        return

    md_files = []
    for root_dir, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith(".md") and f not in SKIP_FILES:
                md_files.append(Path(root_dir) / f)

    md_files.sort()
    changed = 0
    for file_path in md_files:
        result = process_file(file_path, args.dry_run)
        if result["changed"]:
            changed += 1
            print(f"  CONVERTED: {result['file']}")

    print(f"\nSummary: {changed} files changed.")


if __name__ == "__main__":
    main()
