# Lobster Word Analysis / Lobster 词频分析工具

一个用于从TXT文档中提取词汇并进行词频分析的Python工具。

A Python tool for extracting vocabulary from TXT documents and performing word frequency analysis.

## 功能特点 / Features

- ✅ 支持中文和英文文本分析 / Support for both Chinese and English text analysis
- ✅ 自动检测文本语言 / Automatic language detection
- ✅ 中文分词支持（使用jieba）/ Chinese word segmentation (using jieba)
- ✅ 可配置的最小词长过滤 / Configurable minimum word length filtering
- ✅ 停用词过滤 / Stop words filtering
- ✅ 高频词统计和排序 / High-frequency word statistics and ranking
- ✅ 命令行工具和Python API / Command-line tool and Python API
- ✅ 多种文件编码支持 / Multiple file encoding support

## 安装 / Installation

1. 克隆仓库 / Clone the repository:
```bash
git clone https://github.com/SickleD/Lobster_word_analysis.git
cd Lobster_word_analysis
```

2. 安装依赖 / Install dependencies:
```bash
pip install -r requirements.txt
```

## 使用方法 / Usage

### 命令行使用 / Command Line Usage

#### 基本用法 / Basic Usage

```bash
# 分析英文文件 / Analyze English file
python lobster_word_analysis.py examples/sample_english.txt

# 分析中文文件 / Analyze Chinese file
python lobster_word_analysis.py examples/sample_chinese.txt
```

#### 高级选项 / Advanced Options

```bash
# 显示前10个高频词 / Show top 10 frequent words
python lobster_word_analysis.py examples/sample_english.txt -n 10

# 设置最小词长为2 / Set minimum word length to 2
python lobster_word_analysis.py examples/sample_english.txt --min-length 2

# 使用停用词文件 / Use stop words file
python lobster_word_analysis.py examples/sample_english.txt -s stopwords.txt

# 强制指定语言模式 / Force language mode
python lobster_word_analysis.py myfile.txt --mode chinese
python lobster_word_analysis.py myfile.txt --mode english

# 指定文件编码 / Specify file encoding
python lobster_word_analysis.py myfile.txt -e gbk
```

#### 查看帮助 / View Help

```bash
python lobster_word_analysis.py --help
```

### Python API 使用 / Python API Usage

```python
from lobster_word_analysis import LobsterWordAnalyzer

# 创建分析器 / Create analyzer
analyzer = LobsterWordAnalyzer(min_word_length=2)

# 分析文本 / Analyze text
text = "Your text here"
words = analyzer.extract_words(text)
frequency = analyzer.analyze_frequency(words, top_n=10)

# 打印结果 / Print results
analyzer.print_analysis(frequency)

# 分析文件 / Analyze file
result = analyzer.analyze_file('myfile.txt', top_n=20)
analyzer.print_analysis(result)

# 使用停用词 / Use stop words
stop_words = {'the', 'is', 'a', 'an'}
analyzer = LobsterWordAnalyzer(min_word_length=2, stop_words=stop_words)
```

### 运行示例 / Run Demo

```bash
python demo.py
```

## 示例输出 / Example Output

```
============================================================
词频分析结果 / Word Frequency Analysis
============================================================
总词数 / Total words: 45
不同词数 / Unique words: 28

词汇 / Word                           频次 / Frequency
------------------------------------------------------------
intelligence                                          4
artificial                                            4
learning                                              3
machine                                               2
of                                                    2
computer                                              2
...
============================================================
```

## 文件结构 / File Structure

```
Lobster_word_analysis/
├── lobster_word_analysis.py  # 主程序 / Main program
├── demo.py                    # 演示脚本 / Demo script
├── requirements.txt           # 依赖包 / Dependencies
├── README.md                  # 说明文档 / Documentation
└── examples/                  # 示例文件 / Example files
    ├── sample_english.txt     # 英文示例 / English sample
    └── sample_chinese.txt     # 中文示例 / Chinese sample
```

## 依赖 / Dependencies

- Python 3.6+
- jieba (用于中文分词 / for Chinese word segmentation)

## 许可证 / License

MIT License

## 贡献 / Contributing

欢迎提交问题和拉取请求！/ Issues and pull requests are welcome!

## 作者 / Author

SickleD