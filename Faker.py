from flask  import Flask 
from faker import Faker
import requests
import json
import xmltodict

app = Flask(__name__)
fake = Faker()

# / root path <- health_check
@app.route('/get_random_person')
def get_random_person():
    return {
        'name': fake.name(),
        'email': fake.email(),
        'company': fake.company(),
        'address': fake.address()
    }


@app.route('/get_random_persons/<int:count>')
def get_random_persons(count):
    users = [
        {
            'name': fake.name(),
            'email': fake.email(),
            'company': fake.company(),
            'address': fake.address()
        }
        for _ in range(count)
    ]
    return {'users': users}

@app.route('/')
def health_check():
    return 'I am alive!'



def health_check_2():
    return 'I am alive from hc2!'


if __name__ == '__main__':
    app.run(debug=True)