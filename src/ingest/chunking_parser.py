import os
import re
import json
import csv
import logging
from pathlib import Path
from typing import List, Dict, Any, Callable

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

RAW_DATA_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
OUTPUT_CHUNKS_FILE = PROCESSED_DIR / "chunks.json"

def parse_markdown_or_text(file_path: Path) -> List[Dict[str, Any]]:
    text = file_path.read_text(encoding="utf-8", errors="ignore")
    page_split_pattern = re.compile(
        r"(?:<!--\s*PAGE\s*(\d+)\s*-->|\[\s*PAGE\s*(\d+)\s*\]|(?:\n|^)Page\s+(\d+))",
        re.IGNORECASE
    )
    
    chunks = []
    paragraphs = re.split(r"\n\s*\n", text)
    current_page = 1
    current_h1 = "Cyprus Grid Regulations"
    current_clause = "General"
    parent_clause_context = ""
    buffer_text = []

    for para in paragraphs:
        para_stripped = para.strip()
        if not para_stripped:
            continue
        
        # 1. 跟踪页码
        page_match = page_split_pattern.search(para_stripped)
        if page_match:
            groups = [g for g in page_match.groups() if g is not None]
            if groups:
                current_page = int(groups[0])

        # 2. 跟踪标题层级
        first_line = para_stripped.split("\n")[0].strip()
        if first_line.startswith("# "):
            current_h1 = first_line.lstrip("#").strip()
            current_clause = current_h1
        elif first_line.startswith("## ") or first_line.startswith("### "):
            current_clause = first_line.lstrip("#").strip()

        # 3. 捕捉具体条款编号与主干宣告 (如 T1.7.3.1.1 Generating Units must satisfy...)
        clause_match = re.search(r"\b(T\d+(?:\.\d+)+)\b", para_stripped)
        if clause_match:
            detected_clause = clause_match.group(1)
            current_clause = detected_clause
            # 记录规范的主干宣告句，作为子项切片的必须上下文
            if "must satisfy" in para_stripped.lower() or "specifications" in para_stripped.lower():
                parent_clause_context = para_stripped

        # 判断是否属于词汇表页面 (Page 5 到 Page 38 主要是词汇表)
        is_glossary = (5 <= current_page <= 38) and ("glossary" in file_path.name.lower() or "km version" in file_path.name.lower())

        # 遇到子项 (如 (δ), (a), (i) 等具体技术指标)
        is_subitem = bool(re.match(r"^[\(\[\*]*(?:[α-ωa-z\d]+|\δ)[\)\]\.]\s*", para_stripped, re.IGNORECASE))
        
        # 如果是正文技术条款的子项，且缓冲区有内容，刷出上一块
        if is_subitem and buffer_text:
            content_body = "\n\n".join(buffer_text)
            # 注入前置上下文：文件、页码、所属条款及主语
            header_prefix = f"[{file_path.name} | Page {current_page} | Clause {current_clause}]\n"
            if parent_clause_context and parent_clause_context not in content_body:
                header_prefix += f"Context: {parent_clause_context}\n"
            
            chunks.append({
                "content": header_prefix + content_body,
                "metadata": {
                    "source": file_path.name,
                    "page": current_page,
                    "section": current_clause,
                    "type": "glossary" if is_glossary else "technical_clause"
                }
            })
            buffer_text = []

        buffer_text.append(para_stripped)
        accumulated_len = sum(len(p) for p in buffer_text)

        # 控制切片大小在 350~550 字符左右
        if accumulated_len >= 400:
            content_body = "\n\n".join(buffer_text)
            header_prefix = f"[{file_path.name} | Page {current_page} | Clause {current_clause}]\n"
            if parent_clause_context and not is_glossary and parent_clause_context not in content_body:
                header_prefix += f"Context: {parent_clause_context}\n"
            
            chunks.append({
                "content": header_prefix + content_body,
                "metadata": {
                    "source": file_path.name,
                    "page": current_page,
                    "section": current_clause,
                    "type": "glossary" if is_glossary else "technical_clause"
                }
            })
            buffer_text = []

    if buffer_text:
        content_body = "\n\n".join(buffer_text)
        header_prefix = f"[{file_path.name} | Page {current_page} | Clause {current_clause}]\n"
        chunks.append({
            "content": header_prefix + content_body,
            "metadata": {
                "source": file_path.name,
                "page": current_page,
                "section": current_clause,
                "type": "glossary" if is_glossary else "technical_clause"
            }
        })
    return chunks

def parse_json(file_path: Path) -> List[Dict[str, Any]]:
    try:
        data = json.loads(file_path.read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        return []
    chunks = []
    if isinstance(data, list):
        for idx, item in enumerate(data):
            chunks.append({
                "content": json.dumps(item, ensure_ascii=False, indent=2),
                "metadata": {"source": file_path.name, "page": idx + 1, "section": f"Item_{idx}", "type": "application/json"}
            })
    return chunks

def parse_csv(file_path: Path) -> List[Dict[str, Any]]:
    chunks = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            reader = csv.reader(f)
            rows = list(reader)
            if not rows:
                return []
            header = rows[0]
            for i in range(1, len(rows), 10):
                batch = rows[i:i+10]
                lines = [", ".join(f"{h}: {val}" for h, val in zip(header, r)) for r in batch]
                chunks.append({
                    "content": "\n".join(lines),
                    "metadata": {"source": file_path.name, "page": (i // 10) + 1, "section": "Table Data", "type": "text/csv"}
                })
    except Exception:
        pass
    return chunks

class UniversalDocumentParser:
    def __init__(self):
        self.handlers: Dict[str, Callable[[Path], List[Dict[str, Any]]]] = {
            ".md": parse_markdown_or_text,
            ".markdown": parse_markdown_or_text,
            ".txt": parse_markdown_or_text,
            ".json": parse_json,
            ".csv": parse_csv,
        }

    def parse_file(self, file_path: Path) -> List[Dict[str, Any]]:
        ext = file_path.suffix.lower()
        if ext in self.handlers:
            return self.handlers[ext](file_path)
        return []

    def load_directory(self, raw_data_dir: Path) -> List[Dict[str, Any]]:
        all_chunks = []
        if not raw_data_dir.exists():
            return all_chunks
        valid_files = [f for f in raw_data_dir.iterdir() if f.is_file() and not f.name.startswith(".")]
        for f in valid_files:
            chunks = self.parse_file(f)
            all_chunks.extend(chunks)
        return all_chunks

def load_and_chunk_documents(data_dir: str = "data/raw") -> List[Dict[str, Any]]:
    parser = UniversalDocumentParser()
    chunks = parser.load_directory(Path(data_dir))
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_CHUNKS_FILE, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    logger.info(f"Persisted {len(chunks)} chunks to {OUTPUT_CHUNKS_FILE}")
    return chunks

if __name__ == "__main__":
    load_and_chunk_documents()