# GPT Online Chat

一个基于 Next.js 和 OpenAI API 构建的在线聊天应用，支持流式输出和文档上下文检索。

## 功能特点

### 1. 智能对话
- 流式输出（打字机效果）
- Markdown 格式支持
- 保留最近20条对话历史
- 多行输入（Ctrl+Enter换行）
- 代码高亮显示

### 2. 文档查询
- 使用 `@文档名` 或 `@GitHub文件链接` 语法
- 自动加载本地文档或GitHub文件内容作为上下文
- 支持多文件合并查询
- 文档引用高亮显示

### 3. 服务控制
- `!open` - 开启服务
- `!close` - 关闭服务
- 实时服务状态反馈

### 4. UI/UX
- 响应式设计
- 独特的消息样式
  - 用户消息：蓝色右对齐
  - AI回复：灰色左对齐
  - 系统消息：红色居中
- 平滑的动画效果
- 优雅的错误处理

## 快速开始

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
