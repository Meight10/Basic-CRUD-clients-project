import sys

clients = ['pablo', 'ricardo']

def create_client(client_name):
    global clients #permite ocupar la var global dentro del scope de la funcion
    
    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print(f'{idx}: {client}') 


def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        #clients = clients.replace(client_name + ',', updated_client_name + ',')
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        print('Client is not in clients list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        #clients = clients.replace(client_name + ',', '')
        clients.remove(client_name)
    else:
        print('Client is not in clients list')


def search_client(client_name):
    #client_list = clients.split(',')
    
    for client in clients:
        if(client != client_name):
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
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client(client_name, updated_client_name)
        list_clients()        
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the client list')
        else:
            print(f'The client {client_name} is not in the client\'s list')
    else:
        print('Invalid command')