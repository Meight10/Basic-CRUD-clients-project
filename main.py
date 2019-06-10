import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardoo@facebook.com',
        'position': 'Data engineer'
    }
]

def create_client(client):
    global clients #permite ocupar la var global dentro del scope de la funcion
    
    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print(
            '{uid} | {name} | {company} | {email} | {position}'.format(
                uid = idx,
                name = client['name'],
                company = client['company'],
                email = client['email'],
                position = client['position']
            )
        ) 


def update_client(client, updated_client):
    global clients

    if client in clients:
        #clients = clients.replace(client_name + ',', updated_client_name + ',')
        index = clients.index(client)
        clients[index] = updated_client
    else:
        print('Client is not in clients list')


def delete_client(client):
    global clients

    if client in clients:
        #clients = clients.replace(client_name + ',', '')
        clients.remove(client)
    else:
        print('Client is not in clients list')


def search_client(client):
    #client_list = clients.split(',')
    
    for clientI in clients:
        if(clientI != client):
            continue
        else:
            return True


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

def _get_client_field(field_name):
    field = None

    while not field:
        field = input(f'What is the client {field_name}? ')
    return field

def _get_client():
    client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
    return client


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            sys.exit()
    
    return client_name


if __name__ == '__main__':
    pass
    _print_welcome()

    command = input()
    command = command.upper() #colocando el input en mayus para que en la evaluación no s evaya al else

    if command == 'C':

        client = _get_client()
        create_client(client)
        list_clients()

    elif command == 'D':

        client = _get_client()
        delete_client(client)
        list_clients()

    elif command == 'L':

        list_clients()

    elif command == 'U':

        client = _get_client()
        print('*' * 50)
        print('Insert updated client fields:')
        updated_client = _get_client()
        update_client(client, updated_client)
        list_clients()   

    elif command == 'S':

        client = _get_client()
        found = search_client(client)

        if found:
            print('The client is in the client list')
        else:
            print('The client {} is not in the client\'s list'.format(client['name']))

    else:
        print('Invalid command')