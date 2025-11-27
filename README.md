# Math-App
Author: Yomi Adamo

Hello, this was a test to see how to call LLMs in the backend, it is a very simple math problem solver.

## How To Use
1. Install Ollama Model
~~~bash
curl -fsSL https://ollama.com/install.sh | sh
~~~

2. Pull OLMo 2 1B Model or OLMo 3 7B
~~~bash
ollama pull hf.co/allenai/OLMo-2-0425-1B-Instruct-GGUF:Q4_K_M
~~~

~~~bash
ollama pull hf.co/unsloth/Olmo-3-7B-Instruct-GGUF:Q4_K_M
~~~

3. Clone the directory
~~~bash
git clone https://github.com/yomi-adamo/Math-App.git

cd Math-App
~~~

4. Create virtual environment 
~~~bash
python3 -m venv venv
~~~

5. Activate the virtual environmet and install dependencies
~~~bash
source venv/bin/activate

pip install fastapi uvicorn requests
~~~

6. Run the code
~~~bash
uvicorn main:app --reload
~~~

7. Example
~~~bash
curl -X POST http://127.0.0.1:8000/solve -H "Content-Type: application/json" -d '{"problem": "5 + 7"}'
~~~
