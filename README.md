# GPT Online Chat

一个基于 Next.js 和 OpenAI API 构建的在线聊天应用，支持流式输出和多种文档上下文检索。

## 功能特点

### 1. 智能对话
- 流式输出（打字机效果）
- 自动维护对话上下文（保留最近20条消息）
- 支持 Markdown 格式显示
- 多行输入支持（Ctrl+Enter换行）
- 优雅的错误处理机制

### 2. 文档上下文集成
#### 本地文档
- 使用 `@文档名` 语法加载本地文档
- 支持多文件合并查询
- 自动提取文档内容作为对话上下文

#### GitHub文件集成
- 使用 `@GitHub链接` 语法直接引用GitHub文件
- 自动转换为原始内容链接
- 支持任意公开仓库的文件访问

#### GitLab文件集成
- 支持 `@GitLab链接` 语法
- 支持标准GitLab文件路径
- 支持GitLab Wiki页面
- 同时支持公共和私有仓库（需配置token）

#### 容错机制
- 服务器端获取失败自动回退到客户端获取
- 多级错误处理和友好提示
- 支持不同格式的仓库链接

### 3. 服务控制
- `!open` - 开启服务
- `!close` - 关闭服务
- 实时服务状态反馈
- 优雅的状态切换

### 4. UI/UX设计
- 消息分类显示：
  - 用户消息：右对齐
  - AI回复：左对齐
  - 系统消息：居中显示
- 每条消息显示时间戳
- 响应式布局设计
- 流畅的动画效果

## 环境配置

1. 安装依赖：
```bash
npm install
```

2. 配置环境变量：
创建 `.env.local` 文件并添加：
```bash
OPENAI_API_KEY=你的OpenAI API密钥
```

3. 启动开发服务器：
```bash
npm run dev
```

4. 打开浏览器访问：
```
http://localhost:3000/chat
```

## 使用指南

### 基本对话
- 直接输入文字并发送
- Ctrl+Enter 输入多行文本

### 文档查询
```
@docs 请解释这段代码
@https://github.com/用户名/仓库名/blob/分支名/文件路径 请解析这个文件
```

### 服务控制
```
!open  // 开启服务
!close // 关闭服务
```

## 项目结构
```
/
├── app/
│   └── chat/           # 聊天页面
├── components/         # React组件
│   ├── ChatInput      # 输入组件
│   └── ChatMessage    # 消息显示组件
├── pages/
│   └── api/           # API路由
│       ├── chat.ts    # ChatGPT API
│       ├── control.ts # 服务控制
│       └── readDocs.ts# 文档读取
├── styles/            # 样式文件
├── utils/            # 工具函数
└── docs/             # 本地文档
```

## 技术栈
- Next.js 14
- React 18
- TypeScript
- OpenAI API
- CSS Modules
- Server-Sent Events (SSE)

## 开发说明

### API 限制
- 保留最近20条消息上下文
- 流式输出实时更新
- 支持服务状态控制

### 注意事项
- 确保 docs 目录下有对应文档
- GitHub 文件链接需要是公开仓库的文件
- API密钥请妥善保管
