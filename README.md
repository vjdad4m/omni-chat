# OmniChat 🌐💬

OmniChat is an all-in-one chat interface that connects various Large Language Models (LLMs) to provide a seamless user experience. It enables users to easily access and interact with multiple LLMs through a single, unified platform.

## 🌟 Features

* Unified interface for accessing multiple LLMs
* Easy to extend and integrate new LLMs
* Supports both web-based and command-line interfaces (CLI)
* Configurable settings and credentials management
* Modular architecture for easy maintenance and scalability

## 📁 File Structure

```text
omni-chat/
│
├── config/
│ └── credentials_template.py
│
├── core/
│ ├── __init__.py
│ ├── chat_engine.py
│ ├── llm_handler.py
│ └── utils.py
│
├── llm_adapters/
│ ├── __init__.py
│ ├── openai_gpt3.py
│ └── ...
│
├── ui/
│ └── web_app.py
│
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher
* Access to the APIs of the desired LLMs (API keys required)

### Installation

1. Clone the repository:

    ```text
    git clone https://vjdad4m/omni-chat.git
    ```

2. Install the required Python packages:

    ```text
    cd omni-chat
    pip install -r requirements.txt
    ```

3. Set up your API keys in `config/credentials_template.py` and rename the file to `credentials.py`.

### Usage

To run the CLI, execute the following command:

```text
python main.py
```

To run the web app, execute the following command:

```text
python ui/web_app.py
```

## ➕ Adding New LLMs

To add a new LLM, follow these steps:

Create an adapter in the `llm_adapters` folder that encapsulates the logic required to interact with the LLM's API.
Add the adapter to `__init__.py` so that it can be managed by the core engine.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
