from requests_futures.sessions import FuturesSession

def id_from_username(USERNAME):

    # Returns users ID from username
    try:
        with FuturesSession() as session:
            id_request = session.get('https://api.roblox.com/users/get-by-username?username=' + str(USERNAME))
            id_result = id_request.result()

            if id_result.status_code == 200:

                if 'Id' in id_result.json():
                    return id_result.json()['Id']

                else: # If user does not exist returns None
                    return None
            else:
                return id_result.status_code
    except Exception as error:
        return error
        




