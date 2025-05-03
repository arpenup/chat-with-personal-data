# chat-with-personal-data

A demo implementation of a personal knowledge base system, developed in Python utilizing LangChain framework and LLM's API services.

<div align="center">

![logo.png](images/logo.png)

</div>

<div align="center">

[中文](./README.md) | English

</div>

<div align="center">

[![GitHub Code License](https://img.shields.io/github/license/arpenup/chat-with-personal-data)](LICENSE)
![VS Code IDE](https://camo.githubusercontent.com/bb2bae0d39817b50e98af57c9664fbb145426ee1a03b7d96a7c5c702097d994e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4944452d56697375616c25323053747564696f253230436f64652d626c75653f7374796c653d666c6174266c6f676f3d76697375616c2d73747564696f2d636f6465266c6f676f436f6c6f723d666666666666)
![Python](https://img.shields.io/badge/Python-3.13.3-red?logo=python)
![HTML](https://img.shields.io/badge/HTML-5-red?logo=html5)
![LangChain](https://img.shields.io/badge/LangChain-0.3.24-red?logo=langchain)
![LangChain-OpenAI](https://img.shields.io/badge/OpenAI-grey?style=flat&logo=openai)

</div>

## 📌 Project Overview

This project represents a demo implementation developed through my exploratory practice with LangChain and Large Language Models (LLMs), constructing an AI-powered personal knowledge base system capable of semantic retrieval and conversational interaction with private data assets.

**Feature Implementation Matrix：**

1. Supported Data Sources

    | Data Source Type | Supported |
    | ---------- | -------- |
    | Local Files(Markdown)   | <div align="center">✔️</div> |

2. Supported LLMs

    | LLM Type | Supported |
    | ---------- | -------- |
    | OpenAI   | <div align="center">✔️</div> |

## 📌 Quick Start

> [!IMPORTANT]
> A VPN connection might be necessary to access LLMs in certain network environments.

<details>
<summary>My Software/Hardware Environment Configuration (For Reference Only)</summary>

- Windows 10
- VS Code 1.99.3 (system setup)
- Node.js: 20.18.3
- Python 3.13.3
- [requirements.txt](./requirements.txt)

</details>

### ✏️ Step 1

```bash
git clone https://github.com/arpenup/chat-with-personal-data.git
```

### ✏️ Step 2

```bash
pip install -r requirements.txt
```

### ✏️ Step 3

Adjust the configuration file config.py to specify the local file path using LOACL_FILES in the configuration file. The default path is app/resources/file_md under the project root directory, and you can also customize the path location as needed. Modify the OpenAI model version to be used according to your requirements.

### ✏️ Step 4

Create the api_key.txt file in the project root directory and add your OpenAI API Key in the following format:

```Plain Text
OPENAI_API_KEY=your_api_key_here  

```

### ✏️ Step 5

Execute the run.py file to launch the project.

![home.png](images/home.png)
