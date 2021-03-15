from requests_futures.sessions import FuturesSession

class Dget:

    def id_from_username(USERNAME):

        # Returns users ID from username
      
        with FuturesSession() as session:
            id_request = session.get('https://api.roblox.com/users/get-by-username?username=' + str(USERNAME))
            id_result = id_request.result()

            if id_result.status_code == 200:

                if 'Id' in id_result.json():
                    return id_result.json()['Id']

                else: # If user does not exist returns None
                    return None
            else:
                return 'error: ' + id_result.status_code
       

    def previous_usernames(**kwargs):

        for name, value in kwargs.items():
            with FuturesSession() as session:
                if name == 'username':
                    user_id = Dget.id_from_username(value)
                    if user_id is None: # If user does not exist returns None
                        return None
                    elif 'error' in str(user_id):
                        return 'error' # Returns 'error' if error
                    else:
                        previous_username_request = session.get('https://users.roblox.com/v1/users/' + str(user_id) + '/username-history?limit=10&sortOrder=Asc')
                        previous_username_result = previous_username_request.result()
                   
                        if previous_username_result.status_code == 200:
                            if previous_username_result.json()['data'] == []:
                                return None
                            else:
                                return [x['name'] for x in previous_username_result.json()['data']]
                        else:
                            return 'error: ' + previous_username_result.status_code
                elif name == 'id':
                    previous_username_request = session.get('https://users.roblox.com/v1/users/' + str(value) + '/username-history?limit=10&sortOrder=Asc')
                    previous_username_result = previous_username_request.result()
                
                    if previous_username_result.status_code == 200:
                        if previous_username_result.json()['data'] == []:
                            return None
                        else:
                            return [x['name'] for x in previous_username_result.json()['data']]
                    else:
                        return 'error: ' + str(previous_username_result.status_code)
            
                else:
                    raise Exception("You have not used 'id' or 'username' as an arguement")

class Multi:

    def apis(**kwargs):
        pass

            




