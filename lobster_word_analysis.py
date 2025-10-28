#!/usr/bin/env python3
"""
Lobster Word Analysis Tool
提取TXT文档中的词汇并进行词频分析
Extract vocabulary from TXT documents and perform word frequency analysis
"""

import re
from collections import Counter
from pathlib import Path
from typing import List, Dict, Optional, Set
import argparse


class LobsterWordAnalyzer:
    """词频分析器 / Word Frequency Analyzer"""
    
    def __init__(self, min_word_length: int = 1, stop_words: Optional[Set[str]] = None):
        """
        初始化分析器 / Initialize the analyzer
        
        Args:
            min_word_length: 最小词长 / Minimum word length
            stop_words: 停用词集合 / Set of stop words to exclude
        """
        self.min_word_length = min_word_length
        self.stop_words = stop_words or set()
        self.chinese_mode = False
        
    def read_txt_file(self, file_path: str, encoding: str = 'utf-8') -> str:
        """
        读取TXT文件 / Read TXT file
        
        Args:
            file_path: 文件路径 / File path
            encoding: 编码方式 / Encoding (default: utf-8)
            
        Returns:
            文件内容 / File content
        """
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            # Try alternative encodings
            for alt_encoding in ['gbk', 'gb2312', 'latin-1']:
                try:
                    with open(file_path, 'r', encoding=alt_encoding) as f:
                        return f.read()
                except UnicodeDecodeError:
                    continue
            raise ValueError(f"无法解码文件 / Cannot decode file: {file_path}")
    
    def detect_chinese(self, text: str) -> bool:
        """
        检测文本是否包含中文 / Detect if text contains Chinese characters
        
        Args:
            text: 输入文本 / Input text
            
        Returns:
            是否包含中文 / Whether contains Chinese
        """
        chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')
        return bool(chinese_pattern.search(text))
    
    def extract_words_english(self, text: str) -> List[str]:
        """
        提取英文单词 / Extract English words
        
        Args:
            text: 输入文本 / Input text
            
        Returns:
            单词列表 / List of words
        """
        # Extract words (letters and numbers)
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        
        # Filter by length and stop words
        filtered_words = [
            word for word in words 
            if len(word) >= self.min_word_length and word not in self.stop_words
        ]
        
        return filtered_words
    
    def extract_words_chinese(self, text: str) -> List[str]:
        """
        提取中文词汇 / Extract Chinese words
        
        Args:
            text: 输入文本 / Input text
            
        Returns:
            词汇列表 / List of words
        """
        try:
            import jieba
            # Use jieba for Chinese word segmentation
            words = jieba.lcut(text)
            
            # Filter out non-Chinese words, punctuation, and apply filters
            chinese_pattern = re.compile(r'^[\u4e00-\u9fff]+$')
            filtered_words = [
                word for word in words
                if chinese_pattern.match(word) 
                and len(word) >= self.min_word_length 
                and word not in self.stop_words
            ]
            
            return filtered_words
        except ImportError:
            # Fallback: extract individual Chinese characters
            print("警告: jieba未安装，使用字符级分析 / Warning: jieba not installed, using character-level analysis")
            chinese_chars = re.findall(r'[\u4e00-\u9fff]', text)
            return [char for char in chinese_chars if char not in self.stop_words]
    
    def extract_words(self, text: str, force_mode: Optional[str] = None) -> List[str]:
        """
        提取词汇（自动检测中英文）/ Extract words (auto-detect Chinese/English)
        
        Args:
            text: 输入文本 / Input text
            force_mode: 强制模式 'chinese' 或 'english' / Force mode 'chinese' or 'english'
            
        Returns:
            词汇列表 / List of words
        """
        if force_mode:
            if force_mode.lower() == 'chinese':
                return self.extract_words_chinese(text)
            elif force_mode.lower() == 'english':
                return self.extract_words_english(text)
        
        # Auto-detect
        if self.detect_chinese(text):
            return self.extract_words_chinese(text)
        else:
            return self.extract_words_english(text)
    
    def analyze_frequency(self, words: List[str], top_n: Optional[int] = None) -> Dict[str, int]:
        """
        分析词频 / Analyze word frequency
        
        Args:
            words: 词汇列表 / List of words
            top_n: 返回前N个高频词 / Return top N frequent words (None for all)
            
        Returns:
            词频字典 / Word frequency dictionary
        """
        counter = Counter(words)
        
        if top_n:
            return dict(counter.most_common(top_n))
        
        return dict(counter.most_common())
    
    def analyze_file(self, file_path: str, top_n: Optional[int] = None, 
                    force_mode: Optional[str] = None) -> Dict[str, int]:
        """
        分析文件词频 / Analyze word frequency in file
        
        Args:
            file_path: 文件路径 / File path
            top_n: 返回前N个高频词 / Return top N frequent words
            force_mode: 强制模式 / Force mode
            
        Returns:
            词频字典 / Word frequency dictionary
        """
        text = self.read_txt_file(file_path)
        words = self.extract_words(text, force_mode)
        return self.analyze_frequency(words, top_n)
    
    def print_analysis(self, frequency_dict: Dict[str, int], title: str = "词频分析结果 / Word Frequency Analysis"):
        """
        打印分析结果 / Print analysis results
        
        Args:
            frequency_dict: 词频字典 / Word frequency dictionary
            title: 标题 / Title
        """
        print(f"\n{'='*60}")
        print(f"{title}")
        print(f"{'='*60}")
        print(f"总词数 / Total words: {sum(frequency_dict.values())}")
        print(f"不同词数 / Unique words: {len(frequency_dict)}")
        print(f"\n{'词汇 / Word':<30} {'频次 / Frequency':>10}")
        print(f"{'-'*60}")
        
        for word, count in frequency_dict.items():
            print(f"{word:<30} {count:>10}")
        
        print(f"{'='*60}\n")


def main():
    """命令行接口 / Command line interface"""
    parser = argparse.ArgumentParser(
        description='Lobster Word Analysis - 词频分析工具'
    )
    parser.add_argument('file', help='TXT文件路径 / TXT file path')
    parser.add_argument('-n', '--top', type=int, default=20,
                       help='显示前N个高频词 / Show top N frequent words (default: 20)')
    parser.add_argument('-m', '--min-length', type=int, default=1,
                       help='最小词长 / Minimum word length (default: 1)')
    parser.add_argument('-s', '--stop-words', type=str,
                       help='停用词文件路径 / Stop words file path')
    parser.add_argument('--mode', choices=['chinese', 'english'],
                       help='强制指定模式 / Force mode (auto-detect by default)')
    parser.add_argument('-e', '--encoding', default='utf-8',
                       help='文件编码 / File encoding (default: utf-8)')
    
    args = parser.parse_args()
    
    # Load stop words if provided
    stop_words = set()
    if args.stop_words:
        try:
            with open(args.stop_words, 'r', encoding='utf-8') as f:
                stop_words = set(line.strip() for line in f if line.strip())
        except Exception as e:
            print(f"警告: 无法加载停用词文件 / Warning: Cannot load stop words file: {e}")
    
    # Create analyzer
    analyzer = LobsterWordAnalyzer(
        min_word_length=args.min_length,
        stop_words=stop_words
    )
    
    # Analyze file
    try:
        result = analyzer.analyze_file(args.file, top_n=args.top, force_mode=args.mode)
        analyzer.print_analysis(result)
    except Exception as e:
        print(f"错误 / Error: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
