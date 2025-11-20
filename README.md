# Math-App
Author: Yomi Adamo

Hello, this was a test to see how to call LLMs in the backend, it is a very simple math problem solver.

## How To Use
1. Install Ollama Model
~~~bash
curl -fsSL https://ollama.com/install.sh | sh
~~~

2. Clone the directory
~~~bash
git clone https://github.com/yomi-adamo/Math-App.git

cd Math-App
~~~

3. Create virtual environment 
~~~bash
python3 -m venv venv
~~~

4. Activate the virtual environmet and install dependencies
~~~bash
source venv/bin/activate

pip install fastapi uvicorn requests
~~~

5. Run the code
~~~bash
uvicorn main:app --reload
~~~

6. Example
~~~bash
curl -X POST http://127.0.0.1:8000/solve -H "Content-Type: application/json" -d '{"problem": "5 + 7"}'
~~~
