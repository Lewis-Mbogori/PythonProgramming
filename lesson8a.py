from flask import Flask, request

app = Flask(__name__)

# Define the main USSD handler
@app.route('/ussd', methods=['POST'])
def ussd_handler():
    session_id = request.form.get('sessionId')
    service_code = request.form.get('serviceCode')
    phone_number = request.form.get('phoneNumber')
    text = request.form.get('text')

    # Implement your USSD logic here
    response = handle_ussd(session_id, service_code, phone_number, text)

    return response


# Function to handle USSD logic
def handle_ussd(session_id, service_code, phone_number, text):
    # Splitting user input
    user_input = text.split('*')

    if text == '':
        # Initial USSD screen
        response_text = 'Welcome to My USSD Application!\n'
        response_text += '1. Option 1\n'
        response_text += '2. Option 2\n'
        response_text += '3. Option 3\n'
        response_text += 'Please enter your choice:'
    elif len(user_input) == 1:
        # Handling first level menu options
        choice = user_input[0]
        if choice == '1':
            response_text = 'You selected Option 1.\n'
            response_text += 'Enter something for Option 1:'
        elif choice == '2':
            response_text = 'You selected Option 2.\n'
            response_text += 'Enter something for Option 2:'
        elif choice == '3':
            response_text = 'You selected Option 3.\n'
            response_text += 'Enter something for Option 3:'
        else:
            response_text = 'Invalid choice. Please try again.'
    elif len(user_input) == 2:
        # Handling second level menu options
        choice = user_input[0]
        sub_choice = user_input[1]
        if choice == '1':
            response_text = f'You entered "{sub_choice}" for Option 1.\n'
            response_text += 'Thank you for using My USSD Application!'
        elif choice == '2':
            response_text = f'You entered "{sub_choice}" for Option 2.\n'
            response_text += 'Thank you for using My USSD Application!'
        elif choice == '3':
            response_text = f'You entered "{sub_choice}" for Option 3.\n'
            response_text += 'Thank you for using My USSD Application!'
        else:
            response_text = 'Invalid choice. Please try again.'
    else:
        response_text = 'Invalid input. Please try again.'

    # Construct the USSD response
    response = 'CON ' + response_text if not response_text.startswith('Invalid') else 'END ' + response_text

    return response


if __name__ == '__main__':
    app.run(debug=True)
