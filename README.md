# AI大模型RAG智能体开发

> 本项目学习课程和编程来源自黑马程序员

## 项目简介

本项目是一个完整的 RAG（检索增强生成）智能体开发教程，涵盖了从 LangChain 基础到 RAG 系统实现的完整学习路径。项目包含三个主要模块：

- **LangChainRAG开发**：LangChain 框架基础教程
- **提示词优化**：提示词工程和优化技巧
- **RAG开发**：完整的 RAG 系统实现

## 目录结构

```
AI大模型RAG智能体开发/
├── LangChainRAG开发/          # LangChain 基础教程
│   ├── 01-15/                # LangChain 核心概念
│   ├── 16-17/                # 会话记忆管理
│   ├── 18-21/                # 文档加载器
│   ├── 22-25/                # 向量存储和检索
│   ├── data/                  # 示例数据
│   └── chroma_db/             # 向量数据库
├── 提示词优化/               # 提示词工程教程
│   ├── 01-04/                # OpenAI 基础使用
│   └── 05-08/                # 提示词优化案例
└── RAG开发/                   # RAG 系统实现
    ├── config_data.py           # 配置文件
    ├── knowledge_base.py        # 知识库服务
    ├── vector_stores.py        # 向量存储服务
    ├── file_history_store.py   # 文件历史存储
    ├── rag.py                 # RAG 核心服务
    ├── app_qa.py              # 问答应用
    ├── app_file_uploader.py     # 文件上传应用
    ├── data/                  # 业务数据
    ├── chroma_db/             # 向量数据库
    └── chat_history/          # 对话历史
```

## 学习路径

### 第一阶段：LangChain 基础（LangChainRAG开发）

#### 1. LangChain 核心概念（01-15）

**基础入门**
- `01LangChain访问阿里云.py` - LangChain 与阿里云模型集成
- `02LangChain的流式输出.py` - 实现流式输出功能
- `03LangChain调用语言模型.py` - 基础语言模型调用
- `04LangChain调用聊天模型.py` - 聊天模型使用

**提示词模板**
- `06通用提示词模板.py` - PromptTemplate 基础使用
- `07fewshot提示词通用模板.py` - FewShotPromptTemplate 示例学习
- `08模板的format和invoke方法.py` - 模板方法详解
- `09ChatPromptTemplate的使用.py` - 聊天提示词模板

**链式调用**
- `10Chain的基础使用.py` - 链的基本概念
- `11Python的or运算符的重写.py` - 理解链式调用原理
- `12Runnable源码接口查看.py` - Runnable 接口分析

**输出解析**
- `13StrOutputParser解析器.py` - 字符串输出解析
- `14JsonOutputPaser解释器.py` - JSON 输出解析
- `15RunnableLambda的基本使用.py` - 自定义函数链

#### 2. 会话记忆管理（16-17）

- `16临时会话记忆.py` - 内存会话记忆实现
- `17长期会话记忆.py` - 文件持久化会话记忆

#### 3. 文档加载与处理（18-21）

- `18CSVLoader.py` - CSV 文件加载
- `19JsonLoader.py` - JSON 文件加载
- `20TextLoader和文档分割器.py` - 文本加载和分割
- `21PDFLoader.py` - PDF 文档处理

#### 4. 向量存储与检索（22-25）

- `22内存向量存储.py` - 内存向量数据库
- `23外部向量持久化存储.py` - 持久化向量存储
- `24向量检索构建提示词.py` - 向量检索集成
- `25RunnablePassthrough的使用.py` - 数据传递机制

### 第二阶段：提示词优化（提示词优化）

#### 1. OpenAI 基础（01-04）

- `01测试apikey的使用.py` - API 密钥配置
- `02OPENAI库的基本使用.py` - OpenAI 库基础
- `03OPENAI库的流式输出.py` - 流式输出实现

#### 2. 提示词优化案例（05-08）

- `05提示词优化案例_金融文本分类.py` - 文本分类优化
- `06Json的基本使用.py` - JSON 结构化输出
- `07提示词优化案例_金融信息抽取.py` - 信息抽取优化
- `08提示词优化案例_金融文本匹配判断.py` - 文本匹配优化

### 第三阶段：RAG 系统实现（RAG开发）

#### 1. 核心服务模块

**配置管理**
- `config_data.py` - 系统配置文件
  - 嵌入模型配置
  - 聊天模型配置
  - 向量数据库配置
  - 文本分割配置

**知识库服务**
- `knowledge_base.py` - 知识库管理
  - MD5 校验和去重
  - 文本分割处理
  - 向量化和存储
  - 元数据管理

**向量存储服务**
- `vector_stores.py` - 向量数据库操作
  - Chroma 向量数据库集成
  - 相似度检索
  - 批量文档管理

**历史存储服务**
- `file_history_store.py` - 对话历史管理
  - 文件持久化存储
  - 会话隔离
  - 历史查询和清理

#### 2. RAG 核心服务

- `rag.py` - RAG 智能体核心
  - 向量检索集成
  - 提示词模板管理
  - 会话历史管理
  - 链式调用构建

#### 3. 应用层

**问答应用**
- `app_qa.py` - 智能问答系统
  - 用户交互界面
  - 实时问答响应
  - 历史记录管理

**文件上传应用**
- `app_file_uploader.py` - 知识库管理
  - 文件上传处理
  - 自动文档分割
  - 向量化存储

## 技术栈

### 核心框架
- **LangChain** - 大语言模型应用开发框架
- **LangChain Core** - LangChain 核心组件
- **LangChain Community** - 社区扩展组件

### 模型与嵌入
- **通义千问（ChatTongyi）** - 阿里云聊天模型
- **DashScope Embeddings** - 阿里云文本嵌入模型

### 向量数据库
- **Chroma** - 开源向量数据库
- **持久化存储** - 支持本地持久化

### 文档处理
- **CSVLoader** - CSV 文件加载
- **JSONLoader** - JSON 文件加载
- **TextLoader** - 文本文件加载
- **PyPDFLoader** - PDF 文档加载
- **RecursiveCharacterTextSplitter** - 递归文本分割

### 提示词工程
- **PromptTemplate** - 基础提示词模板
- **ChatPromptTemplate** - 聊天提示词模板
- **FewShotPromptTemplate** - 少样本学习模板
- **MessagesPlaceholder** - 消息占位符

### 输出解析
- **StrOutputParser** - 字符串输出解析
- **JsonOutputParser** - JSON 输出解析

### 会话管理
- **InMemoryChatMessageHistory** - 内存会话历史
- **FileChatMessageHistory** - 文件会话历史
- **RunnableWithMessageHistory** - 会话历史管理

## 核心功能

### 1. 知识库管理
- 文档上传和解析
- 自动文本分割
- 向量化存储
- MD5 去重机制
- 元数据管理

### 2. 智能检索
- 语义相似度检索
- 多文档检索
- 相关性排序
- 上下文聚合

### 3. 对话管理
- 会话历史存储
- 多用户会话隔离
- 上下文保持
- 历史记录查询

### 4. RAG 增强
- 检索增强生成
- 提示词模板优化
- 流式输出支持
- 错误处理机制

## 快速开始

### 环境配置

```bash
# 安装依赖
pip install langchain langchain-core langchain-community
pip install langchain-chroma langchain-text-splitters
pip install dashscope pypdf
```

### 配置 API 密钥

```python
# config_data.py
import os

# 阿里云 API 密钥
os.environ["DASHSCOPE_API_KEY"] = "your_api_key_here"

# 模型配置
embedding_model_name = "text-embedding-v4"
chat_model_name = "qwen3-max"

# 向量数据库配置
collections_name = "knowledge_base"
persist_directory = "./chroma_db"

# 文本分割配置
chunk_size = 500
chunk_overlap = 50
separators = ["\n\n", "\n", "。", "！", "？", "；", "，", " ", ""]
max_split_char_number = 1000

# MD5 配置
md5_path = "./md5.text"
```

### 运行示例

```python
# 1. 运行 LangChain 基础教程
python LangChainRAG开发/01LangChain访问阿里云.py

# 2. 运行提示词优化案例
python 提示词优化/05提示词优化案例_金融文本分类.py

# 3. 运行 RAG 系统
python RAG开发/rag.py
```

## 学习建议

### 初学者路径
1. 先学习 LangChain 基础概念（01-15）
2. 理解会话记忆机制（16-17）
3. 学习文档加载和处理（18-21）
4. 掌握向量存储和检索（22-25）

### 进阶学习路径
1. 深入学习提示词优化技巧
2. 理解 RAG 系统架构
3. 实践知识库管理
4. 构建完整的问答系统

### 实践项目
1. 构建个人知识库
2. 开发智能客服系统
3. 实现文档问答应用
4. 优化检索准确率

## 常见问题

### 1. API 调用失败
- 检查 API 密钥是否正确配置
- 确认网络连接正常
- 验证模型名称是否正确

### 2. 向量数据库错误
- 检查 Chroma 数据库路径
- 确认嵌入模型配置正确
- 验证文档格式是否正确

### 3. 会话历史丢失
- 检查历史存储路径
- 确认会话 ID 配置正确
- 验证文件权限设置

## 扩展功能

### 1. 多模态支持
- 图片文档处理
- 音频转录集成
- 视频内容提取

### 2. 高级检索
- 混合检索（稠密+稀疏）
- 重排序机制
- 查询扩展

### 3. 性能优化
- 缓存机制
- 批量处理
- 异步调用

## 参考资源

- [LangChain 官方文档](https://python.langchain.com/)
- [通义千问 API 文档](https://help.aliyun.com/zh/dashscope/)
- [Chroma 向量数据库](https://docs.trychroma.com/)
- [黑马程序员](https://www.itheima.com/)

## 许可证

本项目学习课程和编程来源自黑马程序员，仅供学习参考使用。

## 联系方式

如有问题或建议，欢迎交流学习。

---

**祝学习愉快！**
