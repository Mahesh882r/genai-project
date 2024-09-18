from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set up OpenAI API key for Generative AI
openai.api_key = 'your-openai-api-key'


# Home route
@app.route('/')
def home():
    return render_template('index.html')


# Route to accept user inputs for generating code
@app.route('/generate_code', methods=['POST'])
def generate_code():
    try:
        # Capture the product requirements from the frontend form
        product_requirements = request.form['requirements']

        # GenAI code generation based on requirements
        response = openai.Completion.create(
            model="text-davinci-003",  # Using a GPT model
            prompt=f"Generate Python code based on the following product requirements: {product_requirements}",
            max_tokens=300
        )

        # Extracting generated code from OpenAI response
        generated_code = response.choices[0].text.strip()

        # Return generated code to the frontend
        return jsonify({'code': generated_code})

    except Exception as e:
        # Catch any errors and return a message
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
