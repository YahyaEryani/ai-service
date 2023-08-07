# AI Service Project

This repository contains the source code and relevant files for the AI Service Project which, given a question about the data from a data analyst, uses a database, metadata from documents in a blob store, and a JSON data model schema to generate insightful responses and visual representations.

## Table of Contents

- [AI Service Project](#ai-service-project)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Issues and Troubleshooting](#issues-and-troubleshooting)
  - [Contribution](#contribution)
  - [Acknowledgements](#acknowledgements)
  
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- pip
- Virtual Environment (optional but recommended)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/YahyaEryani/ai-service.git
    ```

2. Navigate to the project directory:
    ```bash
    cd ai-service
    ```

3. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure any environment variables or configurations are set up as described in any `.env` or configuration files.
2. Run the main script or application entry point:
    ```bash
    uvicorn app.main:app --reload
    ```

## Issues and Troubleshooting

If you encounter an error related to importing modules from the transformers library, ensure you have the latest version installed. Some model or tokenizer names may vary based on the version or might be custom implementations specific to this project.

## Contribution

Contributions are always welcome! Please read the contribution guidelines and code of conduct before making any changes.
