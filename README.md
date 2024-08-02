# OpenAI Chatbot with Streamlit

This repository contains a Streamlit-based chatbot application that leverages the OpenAI API to provide interactive conversational experiences.

## Features

- **Interactive Chat**: Engage in real-time conversations with the chatbot powered by OpenAI's language models.
- **Sentiment Analysis**: Utilize NLP techniques to analyze the sentiment of user inputs.
- **Data Handling**: Load and analyze data from various file formats to enhance chatbot responses.

## Requirements

- Python 3.7+
- Streamlit
- OpenAI Python Client

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/MohammedLike/OpenAI-Chat-bot-Streamlit.git
    cd OpenAI-Chat-bot-Streamlit
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your OpenAI API key:
    ```sh
    export OPENAI_API_KEY='your-api-key-here'  # On Windows use `set OPENAI_API_KEY=your-api-key-here`
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to interact with the chatbot.

## Configuration

The main configuration is located in the `app.py` file. Ensure you update the OpenAI API key with your own key. Adjust the model and other parameters as needed.

## Error Handling

- **APIRemovedInV1**: Ensure you are using the correct version of the OpenAI API. Use `openai migrate` to upgrade your codebase if necessary.
- **InvalidRequestError**: Check the availability and access permissions of the model you are trying to use.
- **RateLimitError**: Manage your API usage to stay within your quota. Implement retry logic with exponential backoff as shown in the provided example.

## Troubleshooting

If you encounter issues, refer to the [OpenAI API documentation](https://platform.openai.com/docs/guides) for more information on error codes and solutions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, please open an issue or contact the maintainer at [your-email@example.com].

---

### Sample Code Snippet

Here’s an example of how to integrate retry logic for rate limit errors:

```python
import openai
import time

# Ensure you have the correct API key
openai.api_key = 'your-api-key-here'

def get_chat_response(messages, model="gpt-3.5-turbo", max_retries=5):
    for attempt in range(max_retries):
        try:
            response = openai.Chat.create(
                model=model,
                messages=messages
            )
            return response.choices[0].message['content']
        except openai.error.RateLimitError:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                raise

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
]

try:
    response_content = get_chat_response(messages)
    print(response_content)
except openai.error.RateLimitError:
    print("Rate limit exceeded. Please try again later.")
