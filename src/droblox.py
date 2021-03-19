from requests_futures.sessions import FuturesSession

class HTTPError(Exception):
    pass

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
                raise HTTPError("HTTP " + str(id_result.status_code))

    
    def last_online_date(**kwargs):

        for name, value in kwargs.items():

            user_id = 1

            with FuturesSession() as session:
                if name == 'username':
                    user_id = Dget.id_from_username(value)

                    if user_id is None: # If user does not exist returns None
                        return None

                elif name == 'id':
                    user_id = str(value)
                else:
                    raise ValueError("Invalid argument(s): " + str(', '.join([x[0] for x in kwargs.items()])) )     
            
                last_online_request = session.get('http://api.roblox.com/users/' + user_id + '/onlinestatus/')
                last_online_result = last_online_request.result()

                if last_online_result.status_code == 200:
                    return last_online_result.json()['LastOnline']
                else:
                    raise HTTPError("HTTP " + str(last_online_result.status_code))


    def previous_usernames(**kwargs):

        for name, value in kwargs.items():

            user_id = 1

            with FuturesSession() as session:
                if name == 'username':
                    user_id = Dget.id_from_username(value)

                    if user_id is None: # If user does not exist returns None
                        return None
                elif name == 'id':
                    user_id = value
                else:
                    raise ValueError("Invalid argument(s): " + str(', '.join([x[0] for x in kwargs.items()])) )     

                user_data_request = session.get('https://users.roblox.com/v1/users/' + str(user_id) + '/username-history?limit=10&sortOrder=Asc')
                user_data_result = user_data_request.result()
                
                if user_data_result.status_code == 200:
                    if user_data_result.json()['data'] == []:
                        return None
                    else:
                        return [x['name'] for x in user_data_result.json()['data']]
                else:
                    raise HTTPError("HTTP " + str(user_data_result.status_code))


    def headshot(**kwargs):

        for name, value in kwargs.items():

            user_id = 1

            with FuturesSession() as session:
                if name == 'username':
                    user_id = Dget.id_from_username(value)

                    if user_id is None: # If user does not exist returns None
                        return None
                elif name == 'id':
                    user_id = value
                else:
                    raise ValueError("Invalid argument(s): " + str(', '.join([x[0] for x in kwargs.items()])) )     

                headshot_request = session.get('https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds=' + str(user_id) + '&size=352x352&format=Png&isCircular=true')
                headshot_result = headshot_request.result()
                
                if headshot_result.status_code == 200:
                    if headshot_result.json()[0]['state'] == 'Pending':
                        return None
                    else:
                        return headshot_result.json()[0]['imageUrl']
                else:
                    raise HTTPError("HTTP " + str(headshot_result.status_code))


    def user_info(**kwargs):

        for name, value in kwargs.items():

            user_id = 1

            with FuturesSession() as session:
                if name == 'username':
                    user_id = Dget.id_from_username(value)

                    if user_id is None: # If user does not exist returns None
                        return None
                elif name == 'id':
                    user_id = value
                else:
                    raise ValueError("Invalid argument(s): " + str(', '.join([x[0] for x in kwargs.items()])) )     

                previous_username_request = session.get('https://users.roblox.com/v1/users/' + str(user_id))
                previous_username_result = previous_username_request.result()
                
                if previous_username_result.status_code == 200:
                    return previous_username_result.json()['description']
                else:
                    raise HTTPError("HTTP " + str(previous_username_result.status_code))



class Multi:

    # Multi.apis(username="cool" or id=1123, id_from_username, previous_usernames, etc) returns List of json results 

    def apis(**kwargs):

        method_list = [method for method in dir(Dget) if method.startswith('__') is False]

        for name, value in kwargs.items():
            if name not in method_list:
                raise ValueError("Invalid method(s): " + str(', '.join([x[0] for x in kwargs.items()])) )

            




