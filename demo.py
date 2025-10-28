#!/usr/bin/env python3
"""
演示脚本 / Demo Script
展示如何使用Lobster词频分析工具
Demonstrates how to use the Lobster Word Analysis tool
"""

from lobster_word_analysis import LobsterWordAnalyzer


def demo_basic_usage():
    """基本使用示例 / Basic usage example"""
    print("=" * 60)
    print("示例 1: 基本用法 / Example 1: Basic Usage")
    print("=" * 60)
    
    # Create analyzer
    analyzer = LobsterWordAnalyzer(min_word_length=2)
    
    # Example text
    text = "The quick brown fox jumps over the lazy dog. The dog was sleeping."
    
    # Extract words
    words = analyzer.extract_words(text)
    print(f"\n提取的单词 / Extracted words: {words}")
    
    # Analyze frequency
    freq = analyzer.analyze_frequency(words)
    print(f"\n词频统计 / Word frequency: {freq}")


def demo_chinese_text():
    """中文文本示例 / Chinese text example"""
    print("\n" + "=" * 60)
    print("示例 2: 中文文本分析 / Example 2: Chinese Text Analysis")
    print("=" * 60)
    
    analyzer = LobsterWordAnalyzer(min_word_length=2)
    
    text = "人工智能是计算机科学的重要分支。人工智能技术正在改变世界。机器学习和深度学习是人工智能的核心技术。"
    
    words = analyzer.extract_words(text)
    print(f"\n提取的词汇 / Extracted words: {words[:10]}...")  # Show first 10
    
    freq = analyzer.analyze_frequency(words, top_n=5)
    analyzer.print_analysis(freq, title="中文词频分析 / Chinese Word Frequency")


def demo_file_analysis():
    """文件分析示例 / File analysis example"""
    print("\n" + "=" * 60)
    print("示例 3: 文件分析 / Example 3: File Analysis")
    print("=" * 60)
    
    analyzer = LobsterWordAnalyzer(min_word_length=2)
    
    # Analyze English file
    try:
        result = analyzer.analyze_file('examples/sample_english.txt', top_n=10)
        analyzer.print_analysis(result, title="英文文件分析 / English File Analysis")
    except FileNotFoundError:
        print("示例文件未找到 / Sample file not found: examples/sample_english.txt")
    
    # Analyze Chinese file
    try:
        result = analyzer.analyze_file('examples/sample_chinese.txt', top_n=10)
        analyzer.print_analysis(result, title="中文文件分析 / Chinese File Analysis")
    except FileNotFoundError:
        print("示例文件未找到 / Sample file not found: examples/sample_chinese.txt")


def demo_with_stop_words():
    """使用停用词示例 / Example with stop words"""
    print("\n" + "=" * 60)
    print("示例 4: 使用停用词 / Example 4: Using Stop Words")
    print("=" * 60)
    
    # Common English stop words
    stop_words = {'the', 'is', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'of'}
    
    analyzer = LobsterWordAnalyzer(min_word_length=2, stop_words=stop_words)
    
    text = "The artificial intelligence is the future of technology. The technology is evolving rapidly."
    
    words = analyzer.extract_words(text)
    freq = analyzer.analyze_frequency(words, top_n=5)
    
    print(f"\n过滤停用词后的结果 / Results after filtering stop words:")
    analyzer.print_analysis(freq)


def main():
    """运行所有示例 / Run all examples"""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 10 + "Lobster 词频分析工具演示" + " " * 10 + "║")
    print("║" + " " * 8 + "Lobster Word Analysis Tool Demo" + " " * 8 + "║")
    print("╚" + "═" * 58 + "╝")
    
    demo_basic_usage()
    demo_chinese_text()
    demo_file_analysis()
    demo_with_stop_words()
    
    print("\n" + "=" * 60)
    print("演示完成! / Demo Complete!")
    print("=" * 60)
    print("\n使用命令行工具 / Use command line tool:")
    print("  python lobster_word_analysis.py examples/sample_english.txt")
    print("  python lobster_word_analysis.py examples/sample_chinese.txt -n 10")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    main()
